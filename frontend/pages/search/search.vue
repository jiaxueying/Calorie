<template>
  <view class="all">
    <view class="nav">
      <navTab
        ref="navTab"
        :tab-title="tabTitle"
        :tab-chosen="0"
        @changeTab="changeTab"
      />
    </view>
    <Searchbar
      :show="false"
      :val="searchVal"
      @search="search($event, 1)"
      @showall="showall"
    />
    <scroll-view
      class="scroll"
      v-show="!HistoryShow"
      scroll-y="true"
      lower-threshold=50
      @scrolltolower="getAllFoods"
    >
      <view
        v-if="showedFoods.length"
        v-for="Food in showedFoods"
        :key="Food.dish"
      >
        <like
          :food="Food"
          :menu_id="foods.menu_id"
        />
      </view>
      <uni-load-more :status="status" :content-text="contentText"/>
      
    </scroll-view>
    <view
      class="orders"
      v-show="IsShow"
    >
      <Orders :foods="OrderedFood" />
    </view>
    <view
      class="searchbottom"
      v-show="!IsShow"
    >
      <image
        :src="'../../static/orders.png'"
        class="searchbutton"
        @click="ChangeIsShow"
      /></image>
    </view>
  </view>
</template>

<script>
import {
  backendUrl,
  request,
} from '@/common/helper.js';
import Like from '../../components/for-search/like.vue';
import SearchHistory from '../../components/for-search/search-history.vue';
import InputBox from '../../components/for-search/input-box.vue';
import Orders from '../../components/for-search/orders.vue';
import Searchbar from './searchbar.vue';
export default {
  components: {
    InputBox,
    Orders,
    SearchHistory,
    Like,
    Searchbar,
  },
  props: {

  },
  data() {
    return {
      status:'more',
      IsShow: false,
      contentText: {
      					contentdown: '查看更多',
      					contentrefresh: '加载中',
      					contentnomore: '没有更多'
      				},
      HistoryShow: false,
      foods: new Array(),
      showedFoods: [],
      allFoods: [],
      name1: '搜索历史',
      name2: '热门搜索',
      HistoryName: new Array(),
      PopularName: new Array(),
      OrderedFood: new Array(),
      searchVal: '',
      searchbarActive: true,
      currentTab: 0, // sweiper所在页
      tabTitle: ['菜品查询', '菜品推荐', '个人中心'], // 导航栏格式
      offset:0,
      limit:10,

    };
  },
  onLoad() {
    uni.setStorageSync('meal-list', []);

    uni.login({
      success: (res) => {
        console.log(res.code);
        uni.request({
          url: backendUrl+'/user/login/',
          data: {
            code: res.code,
            name: '123',
          },
          method: 'POST',
          success: (res) => {
            console.log('log successfully');
            console.log(res);
            uni.setStorage({
              key: 'token',
              data: res.data.token,
            });
          },
        });
      },
    });

    uni.getStorage({
      key: 'weightdate',
      success: (res) => {
        console.log(res);
      },
      fail: () => {
        uni.setStorage({
          key: 'weightdate',
          data: 60,
          success: () => {
            console.log('set weightdate');
          },
        });
      },
    });

    uni.getStorage({
      key: 'meal-list',
      success: (res) => {
        console.log(res);
      },
      fail: () => {
        uni.setStorage({
          key: 'meal-list',
          data: [],
          success: () => {
            console.log('set meal-list');
          },
        });
      },
    });

    uni.$on('showhistory', this.ShowHistory);
    uni.$on('showorders', this.ChangeIsShow);
    uni.$on('hidehistory', this.HideHistory);
    uni.$on('search_key', this.searchBykey);
    uni.$on('search_tag', this.searchBykey);
    uni.$on('addHistory', this.addHistoryBykey);
    uni.$on('refresh1', this.refresh);
    uni.$on('showall', this.showall);
    uni.$on('get_likes', this.get_likes);
    this.getAllFoods();
  },
  methods: {
    changeTab(index) {
      this.currentTab = index;
    },
    swiperTab: function(e) {
      var index = e.detail.current; // 获取索引
      this.$refs.navTab.longClick(index);
    },
    search(e, val) {
      this.searchBykey(e);
    },
    ChangeIsShow() {
      this.IsShow = !this.IsShow;
      console.log('IsShow changed: ' + this.IsShow);
      this.OrderedFood = uni.getStorageSync('meal-list');
    },
    getAllFoods: function() {
      uni.request({
        url: backendUrl+'/dish/key_query/',
        method: 'GET',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        data: {
          key_word: '',
          offset:this.offset,
          limit:this.limit,
        },
        success: (res) => {
          console.log(res.data.data)
          if(res.data.data.length === 0){
            this.status='noMore'
          }else{
            this.allFoods = this.allFoods.concat(res.data.data)
            this.showedFoods = this.allFoods;
            this.offset += this.limit
          }
          
        },
      });
    },
    ShowHistory() {
      this.HistoryShow = true;
      this.IsShow = false;
      console.log('HistoryShow changed: ' + this.HistoryShow);
      request('/searchitem/query/', 'GET', {}).then(res => {
        console.log(res);
        this.HistoryName = res[1].data.data.history_items;
        console.log(this.HistoryName);
        this.PopularName = res[1].data.data.popular_items;
        console.log(this.PopularName);
      });
    },
    HideHistory() {
      this.HistoryShow = false;
      console.log('HistoryShow changed: ' + this.HistoryShow);
    },
    searchBykey(key) {
      console.log('searchBykey');
      // this.$refs.input.setValue(key);
      this.searchVal = key;
      uni.pageScrollTo({
        scrollTop: 0,
        duration: 300,
      });
      this.showedFoods = [];
      this.showedFoods = this.searchBykey_t(key).concat(this.searchByTag(key));
    },
    refresh() {
      this.OrderedFood = uni.getStorageSync('meal-list');
      console.log(this.OrderedFood);
    },
    showall() {
      console.log('CLEAR');
      this.showedFoods = this.allFoods;
      this.searchVal = '';
    },
    searchBykey_t(key) {
      var results = [];
      for (var i = 0; i < this.allFoods.length; i++) {
        if (this.allFoods[i]['name'].indexOf(key) != -1) {
          results.push(this.allFoods[i]);
        }
      }
      return results;
    },
    searchByTag(tag_name) {
      console.log('search tag');
      var results = [];
      for (var i = 0; i < this.allFoods.length; i++) {
        for (var j = 0; j < this.allFoods[i].tag.length; j++) {
          if (this.allFoods[i].tag[j].name.indexOf(tag_name) != -1) {
            results.push(this.allFoods[i]);
          }
        }
      }
      return results;
    },
    get_likes(id) {
      uni.request({
        url: backendUrl+'/dish/detail/',
        method: 'GET',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        data: {
          dish_id: id,
        },
        success: (res) => {
          for (var i = 0; i < this.showedFoods.length; i++) {
            if (this.showedFoods[i].id == id) {
              this.showedFoods[i].like = res.data.data.dish.like;
              this.showedFoods[i].dislike = res.data.data.dish.dislike;
            }
          }
        },
      });
    },
  },
  mounted() {
    console.log(this.OrderedFood);
  },
};
</script>

<style>

   .nav {
     position: fixed;
     left: 0rpx;
     top: 0rpx;
     color: #C8A57E;
     width: 100vw;
     display: flex;
     flex-direction: column;
     align-items: flex-start;
     justify-content: flex-start;
     font-size: 24upx;
     background-color: #FFFFFF;
     z-index: 99999;
     margin-bottom: 50rpx;
     }

  .scroll {
    width: 100%;
    position: absolute;
    left: 0;
    top: 180rpx;
    height: 80%;
  }

  .History {
    width: 100%;
    position: absolute;
    left: 0;
    top: 80rpx;
  }

  .all {
    height: 100vh;
  }

  .orders {
    width: 100%;
    position: fixed;
    right: 0;
    bottom: 0;
  }

  .searchbottom {
    position: fixed;
    width: 15%;
    height: 30%;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    bottom: 10px;
    right: 0;
  }

  .searchbutton {
    width: 35px;
    height: 35px;
    margin: 10px;
  }
</style>
