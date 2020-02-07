<template>
	<view class="orders">
		<view>
			<image></image><!--添加和后端的通信-->
			<view>我的菜单</view>
			<view>{{Calories}}kcal</view>
		</view> 
		<view>推荐卡路里摄入范围</view>
		<view>1350kcal-1750kcal/day</view>
		<view v-for="food in Foods" :key="food.foodname">
			<food-in-order  :calories="food.calories" :foodname="food.foodname"></food-in-order>
		</view>
		<button @tap='Close()'>继续添加</button>
		<button>生成我的菜单</button><!--添加和后端的通信-->
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

<style>
	.orders {
		background-color: #FFFFFF;
		width:100%;
		display:inline-block;
	}
</style>
