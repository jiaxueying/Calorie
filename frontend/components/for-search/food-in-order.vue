<template>
	<view class="FoodInOrder">
		<view class="FoodName">{{foodname}}</view>
		<view class="Calories">{{cal}}kcal</view>
		<button class="ButtonInOrder" @tap="MinusWeight">-</button>
		<view class="Weight">{{weight}}g</view>
		<button class="ButtonInOrder" @tap="AddWeight">+</button>
	</view>
</template>

<script>
	export default {
		props: {
			foodname: {
				type: String,
				default: "None",
			},
			calories: {
				type: Number, 
				default: 0,
			}
		},
		data() {
			return {
				weight: 100,
				cal: this.calories,
			}
		},
		methods: {
			MinusWeight() {
				if(this.weight > 50) {
					this.cal -= this.cal/this.weight*50;
					this.weight -= 50;
					this.$parent.caloriesChange(-this.cal/this.weight*50);
				}
				else {
					console.log("delname actived"); 
					this.$parent.delName(this.foodname);
				}
			},
			AddWeight() {
				this.cal += this.cal/this.weight*50;
				this.weight += 50;
				this.$parent.caloriesChange(this.cal/this.weight*50);
			}
		},
	}
</script>

<style>
	.FoodInOrder {
		position: relative;
		width: 100%;
		font-size: 30rpx;
	}
	.FoodName {
		text-align: left;
		width: 40%;
		display: inline-block;
	}
	.Calories {
		text-align: left;
		width: 20%;
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
    margin:0 5rpx;
	}
	.Weight {
		text-align: center;
		width: 10%;
		display: inline-block;
    vertical-align:top;
	}
</style>
