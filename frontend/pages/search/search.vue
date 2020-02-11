<template>
  <view class="all">
    <input-box />
    <scroll-view
      class="scroll"
      scroll-y="true"
      v-show="!HistoryShow"
    >
      <view
        v-for="food in foods"
        :key="food.foodname"
      >
        <like />
      </view>
    </scroll-view>
    <view
      v-show="HistoryShow"
      class="History"
    >
      <search-history :viewname="name1" />
      <search-history :viewname="name2" />
    </view>
    <view
      v-show="IsShow"
      class="orders"
    >
      <Orders :OrderedFood="foods" />
    </view>
  </view>
</template>

<script>
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
      foods: [{foodname: '0', calories: 100},
        {foodname: '1', calories: 200},
        {foodname: '2', calories: 300},
        {foodname: '3', calories: 400},
        {foodname: '4', calories: 400},
        {foodname: '5', calories: 400},
        {foodname: '6', calories: 400},
        {foodname: '7', calories: 400}],
      name1: '搜索历史',
      name2: '热门搜索',
    };
  },
  onLoad() {
    uni.$on('showhistory', this.ShowHistory);
    uni.$on('showorders', this.ChangeIsShow);
    uni.$on('hidehistory', this.HideHistory);
  },
  methods: {
    ChangeIsShow() {
      this.IsShow = !this.IsShow;
      console.log('IsShow changed: ' + this.IsShow);
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
