<template>
  <view class="meal_classifier">
    <view class="title">
      <text>{{name}}</text>
      <button v-if="modifyable" @tap="openAlternativeMealList" class="buttona">编辑</button>
    </view>
    <scroll-view scroll-y="true" :class="fold ? 'fold' : 'unfold'">
      <view v-for="Food in MealList" :key="Food.name" >
        <Food :food="Food" :show_radio_button="false" :ischecked="false" :show_count="countable"></Food>
      </view>
    </scroll-view>
    <button @tap="changeFold" class="buttona">{{button_name}}</button>
  </view>
</template>

<script>
  import Food from "../for-meal-management/food.vue"
  export default {
    props: ['name', 'meallist', 'modifyable', 'countable'],
    components: {
      Food
    },
    data() {
      return {
        MealList: this.meallist,
        button_name: "展开",
        fold: true,
      }
    },
    methods: {
      changeFold:function() {
        console.log(this.button_name + " button clicked");
        this.fold = !this.fold;
        if(this.fold)this.button_name = "展开";
        else this.button_name = "收起";
      },
      openAlternativeMealList:function() {
        console.log("编辑 button clicked");
        wx.navigateTo({
          url: "../../pages/MealManagement/AlternativeMealList?selectedFood=" + JSON.stringify(this.MealList)
        })
      }
    }
  }
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
    border: 1rpx #FFFFFF;
    border-radius: 30rpx;
    font-size: 30rpx;
  }
  .meal_classifier {
    padding: 10rpx;
    border: 5rpx #59453D solid;
    margin: 20rpx;
    border-radius: 30rpx;
  }
</style>
