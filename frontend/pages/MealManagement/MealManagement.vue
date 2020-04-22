<!-- TODO:meal-management search -->

<template>
	<view>
		<InputBox :show_button="true"></InputBox>
		<scroll-view class="scroll" scroll-y="true">
		  <view v-for="Food in MealList" :key="Food.name">
			<Food :food="Food" :show_radio_button="false" :ischecked="false"></Food>
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
          {"name":"菜品1", "pic":"logo.png", "count":10},
          {"name":"菜品2", "pic":"logo.png", "count":10},
          {"name":"菜品3", "pic":"logo.png", "count":10},
          {"name":"菜品4", "pic":"logo.png", "count":10},
          {"name":"菜品5", "pic":"logo.png", "count":10},
          {"name":"菜品6", "pic":"logo.png", "count":10},
          {"name":"菜品7", "pic":"logo.png", "count":10},
          {"name":"菜品8", "pic":"logo.png", "count":10},
          {"name":"菜品9", "pic":"logo.png", "count":10},
          {"name":"菜品10", "pic":"logo.png", "count":10},
          {"name":"菜品11", "pic":"logo.png", "count":10},
          {"name":"菜品12", "pic":"logo.png", "count":10},
          {"name":"菜品13", "pic":"logo.png", "count":10},
          {"name":"菜品14", "pic":"logo.png", "count":10},
          {"name":"菜品15", "pic":"logo.png", "count":10},
          {"name":"菜品16", "pic":"logo.png", "count":10},
          {"name":"菜品17", "pic":"logo.png", "count":10},
          {"name":"菜品18", "pic":"logo.png", "count":10},
          {"name":"菜品19", "pic":"logo.png", "count":10},
          {"name":"菜品20", "pic":"logo.png", "count":10},
          {"name":"菜品21", "pic":"logo.png", "count":10},
          {"name":"菜品22", "pic":"logo.png", "count":10},
          {"name":"菜品23", "pic":"logo.png", "count":10},
          {"name":"菜品24", "pic":"logo.png", "count":10},
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
