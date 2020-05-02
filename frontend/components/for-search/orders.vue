<template>
	<view class="orders">
		<view class="orderHead">
			<view class="head_one">
        <view class="image_head">
          <open-data type="userAvatarUrl"></open-data>
        </view>
        <view class="name_head">我的菜单</view>
        <view class="cont_head">{{Calories}}kcal</view>
      </view>
      <view class="cancel_head"><view class="button" @click="clrAll">清空</view></view>
		</view>
    <view class="orderMid">
     <view class="midOne">西米提醒您</view><!--推荐卡路里摄入范围-->
     <view class="midTwo">合理搭配饮食哈，健康最重要</view><!--1350kcal-1750kcal/day-->
    </view>
		
		<view class="order_list" v-for="food in Foods" :key="food.name">
			<food-in-order :foodname="food.name" :weight="food.sum" :calorie="food.cal"></food-in-order>
		</view>
		<view class="order_bottom">
      <button @tap='Close()'>继续添加</button>
      <button @tap='mylist'>生成我的菜单</button><!--添加和后端的通信-->
    </view>
	</view>
</template>

<script>
	import FoodInOrder from "./food-in-order.vue"
	export default {
		components: {
			FoodInOrder,
		},
		props: {
			Foods: {
				type: Array,
				default: () => [],
			},
		},
		data() {
			return {
				Calories: 0,
       }
		},
		onLoad() {
			uni.$on("CalChange", this.caloriesChange);
			uni.$on("delname", this.delName);
		},
		methods: {
			Close() {
				console.log("add button clicked");
				this.$parent.IsShow = false;
			},
			caloriesChange(v) {
				console.log(v);
				this.Calories += v;
			},
			delName(v) {
				console.log("DelName activated");
				var i = 0;
				for(; i < this.Foods.length; i++) 
				if(this.Foods[i].name == v)break;
					this.Foods.splice(i,1);
					for(i = 0; i < this.Foods.length; i++)
						console.log(this.Foods[i]);
			},
      clrAll() {
        uni.setStorageSync('meal-list', []);
        uni.$emit("refresh1");
        uni.$emit("refresh2");
      },
      mylist() {
        console.log("mylist clicked");
        if(this.Foods.length === 0) {
          uni.showModal({
            title: '提示',
            content: '您的购物车中还没有菜品哦~',
          });
          return;
        }
				uni.$emit("showorders");
        wx.navigateTo({
          url: '../others/mylist',
        });
      }
		},
    watch: {
      Foods(newV) {
        console.log("Foods changed");
        this.Calories = 0;
        for(var i = 0; i < newV.length; i++) {
          this.Calories += newV[i].cal;
        }
      }
    },
	}
</script>

<style lang="less">
	.orders {
		background-color: #FFFFFF;
		width:100%;
		display:inline-block;    
    .orderHead {
      background-color:rgba(219, 207, 202, 1);
      height: 110rpx;
      .head_one {
        height:50rpx;
        .image_head {
          width: 86rpx;
          height: 86rpx;
          position: relative;
          top:-20rpx;
          left: 10rpx;
          background-color: #ccc;
          float: left;
        }
        .name_head {
          // position: relative;
          float: left;
          margin-left: 20rpx;
          line-height:50rpx;
        }
        .cont_head {
          float: right;
          width: 113rpx;
          height: 50rpx;        
          color: rgba(255, 255, 255, 1);
          color: rgba(219, 207, 202, 1);
          background-color: rgba(89, 69, 61, 1);
          background-color:  rgba(219, 207, 202, 1);
          font-size: 26rpx;
          line-height: 50rpx;
          text-align: center;
        }
      }
      
      .cancel_head {
        text-align: right;
        .button {
          background-color: rgba(0,0,0,0);
          font-size: 24rpx;
          color: rgba(80, 80, 80, 1);
          display: inline-block;
          margin-right: 20rpx;
        }
      }
    }
    .orderMid {
      font-size: 20rpx;
      padding:10rpx 20rpx;
      .midOne{
          width: 89px;
         	color: rgba(80, 80, 80, 1);
         	box-shadow: rgba(204, 204, 204, 1) solid 1px;
         	// border-radius: 9px;
         	font-size: 18rpx;
         	line-height: 150%;
         	text-align: center;
          display: inline-block;
          border:1px solid #ccc;
          border-radius: 18rpx;
      }
      .midTwo {
        	color: rgba(153, 153, 153, 1);
        	font-size: 20rpx;
        	line-height: 150%;
        	text-align: left;
          display: inline-block;
          margin-left: 39rpx;
      }
    }
    .order_list {
      padding:10rpx 20rpx;
    }
    .order_bottom {
      button {
        box-sizing: border-box;
        width:50%;
        font-size: 24rpx;
        display: inline-block;
        background-color: rgba(219, 207, 202, 1);
        color: rgba(80, 80, 80, 1);
      }
    }
	}
</style>
