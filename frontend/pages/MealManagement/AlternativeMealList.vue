<!-- TODO:meal-management search
     TODO:生成新菜单-->

<template>
	<view>
    <InputBox :show_button="false"></InputBox>
    <scroll-view class="scroll" scroll-y="true">
      <view v-for="Food in ShowedMealList" :key="Food.dish">
        <Food :food="Food" :show_radio_button="true" :ischecked="isChecked(Food)"></Food>
      </view>
    </scroll-view>
    <view class="bottom">
        <button class="add" @tap="addNewMealList">生成新菜单</button>
    </view>
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
				MealList: [],
        checkedMealList: [],
        ShowedMealList: [],
        time: ""
			}
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
      changeCheckedMealList:function(f) {
        console.log("change " + f.dish + " from checkedMealList");
        let i = 0;
        let l = this.checkedMealList.length;
        for(; i < l; i++)
          if(this.checkedMealList[i].dish == f.dish)
            break;
        if(i >= l){
          this.checkedMealList.push(f);
          console.log("there is no meal named " + f.dish + " in checkedMealList");
          return;
        }
        this.checkedMealList[i] = this.checkedMealList[l - 1];
        this.checkedMealList.pop();
        console.log("checkedMealList now is: " + this.checkedMealList);
      },
      addNewMealList: function() {
        console.log("生成新菜单 button clicked");
        uni.$emit("changeMealList", {time:this.time, list:this.checkedMealList});
        wx.navigateBack({
          url:"../MealList/MealList?booleans=" +
          JSON.stringify({
           modifyable:true,
           countable:false
          })
        });
      },
      isChecked: function(f) {
        for(let i = 0; i < this.checkedMealList.length; i++)
          if(f.dish == this.checkedMealList[i].dish) {
            console.log(f.dish + " checked");
            return true;
          }
        return false;
      }
		},
    onLoad(options) {
      uni.$on("meal-management-search", this.search);
      uni.$on("change-checked-meal-list", this.changeCheckedMealList);
      this.checkedMealList = JSON.parse(options.selectedFood);
      this.time = options.time;
      console.log(this.time);
      // 从后端获取MealList
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
    bottom: 120rpx;
  }
  .add {
    z-index: 2;
    height: 80rpx;
		width:250rpx;
    margin:auto;
		border: 1rpx solid #C8C7CC;
		border-radius: 10rpx;
    font-size: 30rpx;
    font-weight: 500;
    color:#59453D;
  }
  .bottom{
    z-index: 1;
    position: fixed;
    height:120rpx;
    bottom:0rpx;
    background-color: #FAFAFA;
    width:100%;
    display: flex;
    justify-content: center;
    align-items: center;
    border-top: #C0C0C0 2rpx solid;
  }
</style>
