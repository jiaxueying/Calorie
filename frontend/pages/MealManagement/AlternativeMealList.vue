<!-- TODO:meal-management search -->

<template>
	<view>
    <InputBox :show_button="false"></InputBox>
    <scroll-view class="scroll" scroll-y="true">
      <view v-for="Food in MealList" :key="Food.name">
        <Food :food="Food" :show_radio_button="true"></Food>
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
        checkedMealList: [],
			}
		},
		methods: {
			search:function(key) {
        console.log("search in /pages/MealManagement/MealManagement.vue: " + key);
        console.log("need to complete");
        console.log("meal-management-search on completed!");
      },
      addCheckedMealList:function(f) {
        console.log("add " + f.name + " into checkedMealList");
        this.checkedMealList.push(f);
        console.log("checkedMealList now is: " + this.checkedMealList);
      },
      removeCheckedMealList:function(f) {
        console.log("remove " + f.name + " from checkedMealList");
        let i = 0;
        let l = this.checkedMealList.length;
        for(; i < l; i++)
          if(this.checkedMealList[i].name == f.name)
            break;
        if(i >= l){
          console.log("there is no meal named " + f.name + " in checkedMealList");
          return;
        }
        this.checkedMealList[i] = this.checkedMealList[l - 1];
        this.checkedMealList.pop();
        console.log("checkedMealList now is: " + this.checkedMealList);
      }
		},
    onLoad() {
      uni.$on("meal-management-search", this.search);
      uni.$on("add-checked-meal-list", this.addCheckedMealList);
      uni.$on("remove-checked-meal-list", this.removeCheckedMealList);
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
