<!-- TODO:meal-management search -->

<template>
	<view>
    <InputBox :show_button="true"></InputBox>
    <scroll-view class="scroll" scroll-y="true">
      <view v-for="Food in MealList" :key="Food.name">
        <Food :food="Food"></Food>
      </view>
    </scroll-view>
	</view>
</template>

<script>
  import InputBox from "../../components/for-meal-management/input-box.vue"
  import Food from "../../components/for-meal-management/food.vue"
	export default {
    components: {
      InputBox,
      Food
    },
		data() {
			return {
				MealList: [
          {"name":"菜品1", "pic":"logo.png"},
          {"name":"菜品2", "pic":"logo.png"},
        ],
			}
		},
		methods: {
			search:function(key) {
        console.log("search in /pages/MealManagement/MealManagement.vue: " + key);
        console.log("need to complete");
        console.log("meal-management-search on completed!");
      }
		},
    onLoad() {
      uni.$on("meal-management-search", this.search);
    }
	}
</script>

<style>
  .scroll {
    width:100%;
    position:absolute;
    left:0;
    top:80rpx;
  }
</style>
