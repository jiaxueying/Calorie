<template>
  <view class="meal_classifier">
    <view class="title">
      <text>{{ name }}</text>
      <view
        v-if="modifyable"
        @click="openAlternativeMealList"
        class="{buttona:true;buttonb:true}"
      >编辑</view>
    </view>
    <scroll-view
      scroll-y="true"
      :class="fold ? 'fold' : 'unfold'"
    >
      <view
        v-for="Food in meallist"
        :key="Food.dish"
      >
        <Food
          :food="Food"
          :show_radio_button="false"
          :ischecked="false"
          :show_count="countable"
        />
      </view>
    </scroll-view>
    <button
      @tap="changeFold"
      class="buttona"
      plain="true"
    >{{ button_name }}</button>
  </view>
</template>

<script>
import Food from '../for-meal-management/food.vue';
export default {
  props: ['name', 'meallist', 'modifyable', 'countable'],
  components: {
    Food,
  },
  data() {
    return {
      button_name: '展开',
      fold: true,
    };
  },
  methods: {
    changeFold: function() {
      console.log(this.button_name + ' button clicked');
      this.fold = !this.fold;
      if (this.fold) this.button_name = '展开';
      else this.button_name = '收起';
    },
    openAlternativeMealList: function() {
      console.log('编辑 button clicked');
      wx.navigateTo({
        url: '../../pages/MealManagement/AlternativeMealList?selectedFood=' + JSON.stringify(this.meallist) +
          '&time=' + JSON.stringify(this.name),
      });
    },
  },
};
</script>

<style>
  .title {
    display: flex;
    margin: 20rpx 40rpx 0 40rpx;
    padding: 0 20rpx 10rpx 20rpx;
    border-bottom: 1rpx #59453D solid;
  }
  .title text {
    margin:auto;
    font-size: 40rpx;
    flex: 1;
  }
  .fold {
    height: 200rpx;
    overflow: hidden;
  }
  .unfold {
    height: auto;
  }
  .buttona {
    height: 70rpx;
    width: 200rpx;
    margin:auto;
    font-size: 30rpx;
    line-height: 70rpx;
  }
  .buttonb{
    width: auto;
    margin-left: 50rpx;
    color:#555555;
  }
  .meal_classifier {
    padding: 10rpx;
    border: 5rpx #59453D solid;
    margin: 20rpx;
    border-radius: 30rpx;
  }
</style>
