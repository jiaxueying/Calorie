<!-- TODO:meal-management search
     TODO:生成新菜单-->

<template>
	<view>
    <InputBox :show_button="false"></InputBox>
    <scroll-view class="scroll" scroll-y="true">
      <view v-for="Food in MealList" :key="Food.name">
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
        checkedMealList: [],
			}
		},
		methods: {
			search:function(key) {
        console.log("search in /pages/MealManagement/MealManagement.vue: " + key);
        console.log("need to complete");
        console.log("meal-management-search on completed!");
      },
      changeCheckedMealList:function(f) {
        console.log("change " + f.name + " from checkedMealList");
        let i = 0;
        let l = this.checkedMealList.length;
        for(; i < l; i++)
          if(this.checkedMealList[i].name == f.name)
            break;
        if(i >= l){
          this.checkedMealList.push(f);
          console.log("there is no meal named " + f.name + " in checkedMealList");
          return;
        }
        this.checkedMealList[i] = this.checkedMealList[l - 1];
        this.checkedMealList.pop();
        console.log("checkedMealList now is: " + this.checkedMealList);
      },
      addNewMealList: function() {
        console.log("生成新菜单 button clicked");
        wx.navigateTo({
          url:"../MealList/MealList?booleans=" +
          JSON.stringify({
           modifyable:true,
           countable:false
          })
        });
      },
      isChecked: function(f) {
        for(let i = 0; i < this.checkedMealList.length; i++)
          if(f.name == this.checkedMealList[i].name) {
            console.log(f.name + " checked");
            return true;
          }
        return false;
      }
		},
    onLoad(options) {
      uni.$on("meal-management-search", this.search);
      uni.$on("change-checked-meal-list", this.changeCheckedMealList);
      this.checkedMealList = JSON.parse(options.selectedFood);
      // 从后端获取MealList
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
