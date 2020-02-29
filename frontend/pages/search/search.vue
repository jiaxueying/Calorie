<template>
  <view class="all">
    <input-box ref="input" />
    <scroll-view
      class="scroll"
      scroll-y="true"
      v-show="!HistoryShow"
    >
      <view
        v-if="foods.length"
        v-for="Food in foods"
        :key="Food.name"
      >
        <like :food="Food" />
      </view>
      <view v-if="!foods.length">对不起！没有您想查询的菜品</view>
    </scroll-view>
    <view
      v-show="HistoryShow"
      class="History"
    >
      <search-history :viewname="name1" :Names="HistoryName" />
      <search-history :viewname="name2" :Names="PopularName" />
    </view>
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
    uni.$on('search_tag',this.searchByTag);
    uni.$on('addHistory',this.addHistoryBykey);
    uni.$on('refresh1',this.refresh);
  },
  methods: {
    ChangeIsShow() {
      this.IsShow = !this.IsShow;
      console.log('IsShow changed: ' + this.IsShow);
      this.OrderedFood = uni.getStorageSync("meal-list");
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
    MealListRefresh(key) {
      console.log("meallist fresh:" + key);
      request('/dish/key_query/', 'GET', {
        key_word: key,
      }).then(res => {
        this.foods = res[1].data.data;
        console.log(res);
      });
    },
    searchBykey(key) {
      console.log("searchBykey");
      this.$refs.input.setValue(key);
      this.MealListRefresh(key);
    },
    searchByTag(tag) {
      console.log("searchBytag");
      this.$refs.input.setValue(tag.name);
      request('/dish/tag_query', 'GET', {
        tag_id: tag.id,
      }).then(res => {
        this.foods = res[1].data.data.dishes;
        console.log(this.foods);
      });
    },
    refresh() {
      this.OrderedFood = uni.getStorageSync('meal-list');
    },
  },
  mounted() {
    this.MealListRefresh('');
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
