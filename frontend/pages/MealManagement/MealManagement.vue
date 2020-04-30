<!-- TODO:meal-management search -->

<template>
	<view>
		<InputBox :show_button="true"></InputBox>
		<scroll-view class="scroll" scroll-y="true">
		  <view v-for="Food in ShowedMealList" :key="Food.name">
        <Food :food="Food" :show_radio_button="false" :ischecked="false"></Food>
		  </view>
		</scroll-view>
	</view>
</template>

<script>
  import InputBox from "../../components/for-meal-management/input-box.vue"
  import Food from "../../components/for-meal-management/food.vue"
  import {request, backendurl} from "../../common/helper.js"
	export default {
    components: {
      InputBox,
      Food
    },
		data() {
			return {
				MealList: [ ],
        ShowedMealList: [ ],
			}
		},
    onShow() {
      this.refresh()
    },
		methods: {
			search:function(key) {
        console.log("search in /pages/MealManagement/MealManagement.vue: " + key);
        if(key.replace(" ", "") === "") {
          this.ShowedMealList = this.MealList;
          return;
        }
        this.ShowedMealList = [];
        for(let i = 0, l = this.MealList.length; i < l; i++) {
          if(this.MealList[i].dish.indexOf(key) != -1) {
            this.ShowedMealList.push(this.MealList[i]);
          }
        }
        console.log("meal-management-search on completed!");
      },
      refresh:function() {
        console.log("refreshing!");
        request('/canteen/dishesview/', 'GET', {
          }).then(res => {
          console.log(res);
          console.log('meals returned:\n');
          console.log(res[1].data.dishes);
          this.MealList = res[1].data.dishes;
          this.ShowedMealList = res[1].data.dishes;
        })
      }
		},
    onLoad() {
      uni.$on("meal-management-search", this.search);
      request('/canteen/dishesview/', 'GET', {
        }).then(res => {
        console.log(res);
        console.log('meals returned:\n');
        console.log(res[1].data.dishes);
        this.MealList = res[1].data.dishes;
        this.ShowedMealList = res[1].data.dishes;
      })
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
