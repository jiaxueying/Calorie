<template>
	<view class="orders">
		<view class="orderHead">
			<view class="head_one">
        <image class="image_head"></image><!--添加和后端的通信-->
        <view class="name_head">我的菜单</view>
        <view class="cont_head">{{Calories}}kcal</view>
      </view>
      <view class="cancel_head"><button>清空</button></view>
		</view>
    <view class="orderMid">
     <view class="midOne">推荐卡路里摄入范围</view>
     <view class="midTwo">1350kcal-1750kcal/day</view>
    </view>
		
		<view class="order_list" v-for="food in Foods" :key="food.foodname">
			<food-in-order  :calories="food.calories" :foodname="food.foodname"></food-in-order>
		</view>
		<view class="order_bottom">
      <button @tap='Close()'>继续添加</button>
      <button>生成我的菜单</button><!--添加和后端的通信-->
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
			OrderedFood: {
				type: Array,
				default: () => [],
			},
		},
		data() {
			return {
				Foods: this.OrderedFood,
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
				uni.$emit("showorders");
			},
			caloriesChange(v) {
				console.log(v);
				this.Calories += v;
			},
			delName(v) {
				console.log("DelName activated");
				var i = 0;
				for(; i < this.Foods.length; i++) 
					if(this.Foods[i].foodname == v)break;
				this.Foods.splice(i,1);
				for(i = 0; i < this.Foods.length; i++)
					console.log(this.Foods[i]);
			},
		},
		watch: {
			Foods(newV, oldV) {
				if(oldV.length < newV.length) {
					this.Calories += this.Foods[this.Foods.length - 1].calories;
				}
			}
		}
	}
</script>

<style lang="less">
	.orders {
		background-color: #FFFFFF;
		width:100%;
		display:inline-block;    
    .orderHead {
      background-color:rgba(219, 207, 202, 1);
      // overflow: hidden;
      
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
          background-color: rgba(89, 69, 61, 1);
          font-size: 26rpx;
          line-height: 50rpx;
          text-align: center;
        }
      }
      
      .cancel_head {
        text-align: right;
        button {
          text-align: right;
          background-color: rgba(0,0,0,0);
          font-size: 24rpx;
          color: rgba(80, 80, 80, 1);
          border: none;
          display: inline-block;
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
