<template>
  <view
    v-if="weight"
    class="FoodInOrder"
  >
    <view class="FoodName">{{ foodname }}</view>
    <view
      style="color:#000000;"
      class="Calories"
    >{{ calorie }}kcal</view>
    <view class="numarea">
      <button
        class="ButtonInOrder"
        @tap="MinusWeight"
      >-</button>
      <view class="Weight">{{ weight }}</view>
      <button
        class="ButtonInOrder"
        @tap="AddWeight"
      >+</button>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    foodname: {
      type: String,
      default: 'None',
    },
    calorie: {
      type: Number,
      default: 0,
    },
    weight: {
      type: Number,
      default: 0,
    },
  },
  data() {
    return {};
  },
  methods: {
    MinusWeight() {
      var orderedFood = uni.getStorageSync('meal-list');
      for (var i = 0; i < orderedFood.length; i++) {
        var f = orderedFood[i];
        if (f.name === this.foodname) {
          // f.cal -= f.cal / f.sum * 50;
          if (f.sum > 0) {
            f.sum -= 1;
            uni.setStorageSync('meal-list', orderedFood);
            uni.$emit('refresh1');
            uni.$emit('refresh2');
          }
          return;
        }
      }
      uni.$emit('refresh');
    },
    AddWeight() {
      var orderedFood = uni.getStorageSync('meal-list');
      console.log('ordered_food:');
      console.log(orderedFood);
      for (var i = 0; i < orderedFood.length; i++) {
        var f = orderedFood[i];
        if (f.name === this.foodname) {
          // f.cal += f.cal / f.sum * 50;
          f.sum += 1;
          orderedFood[i] = f;
          console.log('orderedFood:');
          console.log(orderedFood);
          uni.setStorageSync('meal-list', orderedFood);
          uni.$emit('refresh1');
          uni.$emit('refresh2');
          return;
        }
      }
    },
  },
};
</script>

<style>
  .FoodInOrder {
    position: relative;
    width: 100%;
    font-size: 30rpx;
    display: flex;
    flex-direction: row;
  }

  .FoodName {
    text-align: center;
    width: 33%;
    display: inline-block;
  }

  .Calories {
    text-align: center;
    width: 33%;
    display: inline-block;
  }

  .ButtonInOrder {
    font-size: 35rpx;
    height: 45rpx;
    width: 45rpx;
    border-radius: 50%;
    display: inline-block;
    color: #fff;
    background-color: rgba(89, 69, 61, 1);
    line-height: 45rpx;
    padding: 0;
    margin: 0;
  }

  .numarea {
    width: 33%;
    align-items: center;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
  }

  .Weight {
    text-align: center;
    width: 10%;
    display: inline-block;
    vertical-align: top;
  }
</style>
