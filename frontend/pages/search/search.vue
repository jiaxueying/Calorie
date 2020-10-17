<template>
  <view class="all">
    <input-box ref="input" class="input"/>
    <scroll-view
      class="scroll"
      scroll-y="true"
      v-show="!HistoryShow"
    >
      <view v-if="showedFoods.length" v-for="Food in showedFoods" :key="Food.dish">
        <like :food="Food" :menu_id="foods.menu_id"/>
      </view>
    </scroll-view>
    <view
      v-show="IsShow"
      class="orders"
    >
      <Orders :Foods="OrderedFood" />
    </view>
  </view>
</template>

<script>
import { backendUrl, request } from '@/common/helper.js';
import Like from '../../components/for-search/like.vue';
import SearchHistory from '../../components/for-search/search-history.vue';
import InputBox from '../../components/for-search/input-box.vue';
import Orders from '../../components/for-search/orders.vue';
export default {
  components: {
    InputBox,
    Orders,
    SearchHistory,
    Like,
  },
  props: {

  },
  data() {
    return {
      IsShow: false,
      HistoryShow: false,
      foods: new Array(),
      showedFoods:[],
      allFoods:[],
      name1: '搜索历史',
      name2: '热门搜索',
      HistoryName: new Array(),
      PopularName: new Array(),
      OrderedFood: new Array(),
    };
  },
  onLoad() {
    uni.$on('showhistory', this.ShowHistory);
    uni.$on('showorders', this.ChangeIsShow);
    uni.$on('hidehistory', this.HideHistory);
    uni.$on('search_key',this.searchBykey);
    uni.$on('search_tag',this.searchBykey);
    uni.$on('addHistory',this.addHistoryBykey);
    uni.$on('refresh1',this.refresh);
    uni.$on('get_likes',this.get_likes);
    this.getAllFoods();
  },
  methods: {
    ChangeIsShow() {
      this.IsShow = !this.IsShow;
      console.log('IsShow changed: ' + this.IsShow);
      this.OrderedFood = uni.getStorageSync("meal-list");
    },
    getAllFoods:function(){
      uni.request({
        url:'https://nkucalorie.top:8000/dish/key_query/',
        method:'GET',
        header:{
          Authorization:"Token "+uni.getStorageSync("token")
        },
        data:{
          key_word:""
        },
        success:(res)=> {
          this.allFoods=res.data.data
          this.showedFoods=this.allFoods
        }
      })
    },
    ShowHistory() {
      this.HistoryShow = true;
      this.IsShow = false;
      console.log('HistoryShow changed: ' + this.HistoryShow);
      request('/searchitem/query/', 'GET', { }).then(res => {
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
      console.log("searchBykey");
      this.$refs.input.setValue(key);
      this.showedFoods=[]
      this.showedFoods=this.searchBykey_t(key).concat(this.searchByTag(key))
    },
    refresh() {
      this.OrderedFood = uni.getStorageSync('meal-list');
      console.log(this.OrderedFood);
    },
    searchBykey_t(key){
      var results=[]
      for(var i=0;i<this.allFoods.length;i++)
      {
        if(this.allFoods[i]["name"].indexOf(key)!=-1)
        {
          results.push(this.allFoods[i])
        }
      }
      return results
    },
    searchByTag(tag_name) {
      console.log('search tag')
      var results=[]
      for(var i=0;i<this.allFoods.length;i++)
      {
        for(var j=0;j<this.allFoods[i].tag.length;j++)
        {
          if(this.allFoods[i].tag[j].name.indexOf(tag_name)!=-1)
          {
            results.push(this.allFoods[i])
          }
        }
      }
      return results
    },
    get_likes(id) {
      uni.request({
        url:"https://nkucalorie.top:8000/dish/detail/",
        method:"GET",
        header:{
          Authorization: "Token " + uni.getStorageSync("token")
        },
        data: {
          dish_id: id
        },
        success: (res) => {
          for(var i=0;i<this.showedFoods.length;i++)
          {
            if(this.showedFoods[i].id==id)
            {
              this.showedFoods[i].like=res.data.data.dish.like
              this.showedFoods[i].dislike=res.data.data.dish.dislike
            }
          }
        }
      })
    }
  },
  mounted() {
    console.log(this.OrderedFood);
  },
};
</script>

<style>
  .scroll {
    width:100%;
    position:absolute;
    left:0;
    top:80rpx;
  }
  .History{
    width:100%;
    position:absolute;
    left:0;
    top:80rpx;
  }
  .all {
    height:100vh;
  }
  .orders {
    width:100%;
    position:fixed;
    right: 0;
    bottom: 0;
  }
</style>
