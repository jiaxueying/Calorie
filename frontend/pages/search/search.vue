<template>
  <view class="all">
    <input-box />
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
        <like :food="Food" @tap="detail(Food)"/>
      </view>
      <view v-if="!foods.length">对不起！没有您想查询的菜品</view>
    </scroll-view>
    <view
      v-show="HistoryShow"
      class="History"
    >
      <search-history :viewname="name1" :Names="HistoryName" />
      <search-history :viewname="name2" />
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
      OrderedFood: new Array(),
    };
  },
  onLoad() {
    uni.$on('showhistory', this.ShowHistory);
    uni.$on('showorders', this.ChangeIsShow);
    uni.$on('hidehistory', this.HideHistory);
    uni.$on('search_key',this.searchBykey);
    uni.$on('addHistory',this.addHistoryBykey);
    uni.$on('aWeight',this.addWeight);
    uni.$on('mWeight',this.minusWeight);
    uni.$on("clear_all",this.clrAll);
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
    },
    HideHistory() {
      this.HistoryShow = false;
      console.log('HistoryShow changed: ' + this.HistoryShow);
    },
    MealListRefresh(key) {
      console.log("meallist fresh");
      request('/dish/key_query/', 'GET', {
        key_word: key,
      }).then(res => {
        this.foods = res[1].data.data.dishes;
        console.log(this.foods);
      });
    },
    searchBykey(key) {
      console.log("searchBykey");
      this.MealListRefresh(key);
    },
    addHistoryBykey(key) {
      if(key.match(/^[ ]*$/)) return;
      var i = 0;
      for(; i < this.HistoryName.length; i++) {
        if(this.HistoryName[i] === key) {
          var arr1 = this.HistoryName.slice(0, i);
          var arr2 = this.HistoryName.slice(i + 1);
          this.HistoryName = arr1.concat(arr2);
          break;
        }
      }
      this.HistoryName.unshift(key);
      if(this.HistoryName.length > 10)this.HistoryName.pop();
      console.log("history added " + key);
    },
    addWeight(name) {
      console.log("addWeight in search.vue");
      for(var i = 0; i < this.OrderedFood.length; i++) {
        var f = this.OrderedFood[i];
        console.log(f);
        if(f.name === name) {
          f.cal += f.cal / f.sum * 50;
          f.sum += 50;
          uni.setStorageSync("meal-list", this.OrderedFood);
          return;
        }
      }
    },
    minusWeight(name) {
      console.log("addWeight in search.vue");
      for(var i = 0; i < this.OrderedFood.length; i++) {
        var f = this.OrderedFood[i];
        console.log(f);
        if(f.name === name) {
          f.cal -= f.cal / f.sum * 50;
          f.sum -= 50;
          if(f.sum <= 0) {
            var a = this.OrderedFood.slice(0, i);
            var b = this.OrderedFood.slice(i + 1);
            this.OrderedFood = a.concat(b);
          }
          uni.setStorageSync("meal-list", this.OrderedFood);
          return;
        }
      }
    },
    clrAll() {
      console.log("clear all");
      while(this.OrderedFood.length)this.OrderedFood.pop();
      uni.setStorageSync("meal-list", this.OrderedFood);
    },
    detail(e) {
      console.log(e);
      this.IsShow = false;
      wx.navigateTo({
        url:'../others/detail?foodDetail='+JSON.stringify(e),
      });
    },
  },
  mounted() {
    this.MealListRefresh('');
    request('/searchitem/query/', 'GET', { }).then(res => {
      console.log(res);
    });
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
