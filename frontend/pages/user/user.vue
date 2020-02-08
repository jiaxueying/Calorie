<template>
  <view>
    <view class="all">
      <view class="userimg">
        <open-data type="userAvatarUrl"></open-data>
      </view>
      <view class="userinfor">
        <open-data type="userNickName" style="font-size: 2em;height:85rpx;"></open-data>
        <view style="display: flex">
          <text style="font-size: 1.2em;margin-top: 6rpx;margin-bottom: 6rpx;">体重：{{weight}}kg\n目标体重：{{targetweight}}kg\n</text>
          <view class="button" @click="set">编辑</view>
        </view>
        <text style="font-size: 0.7em;">本日推荐摄入卡路里范围：\n{{minCalForDay}}kcal-{{maxCalForDay}}kcal</text>
      </view>
    </view>
    <view style="display: flex;justify-content: center;">
      <plan v-if="!Switch" style="animation: pushleft 500ms;"></plan>
    </view>
  </view>
</template>

<script>
  import plan from "../../components/user/plan.vue"
	export default {
    components:{
      plan
    },
		data() {
			return {
        weight:'100',
        minCalForDay:'1000',
        maxCalForDay:'1500',
        Switch:true
			}
		},
		methods: {
			set:function(){
        this.Switch=!this.Switch
      }
		}
	}
</script>

<style>
  .all{
    display: flex;
  }
	.userimg{
    margin-top: 15%;
		width:200rpx;
		height:200rpx;
		border-radius:50%;
    overflow: hidden;
    position:relative;
    left:55rpx;
	}
  .userinfor{
    color: #505050;
    margin-top: 15%;
    display: flex;
    flex-direction: column;
    position:relative;
    left:100rpx
  }
  .button{
    font-size: 25rpx;
    background-color: #e8e8e8;
    height: 40rpx;
    line-height: 40rpx;
    width: 80rpx;
    text-align: center;
    border-radius: 15rpx;
    margin-left: 15rpx;
    margin-top: 20rpx;
  }
  @keyframes pushleft{
    from{margin-left: 750rpx;opacity: 0;}
    to{}
  }
</style>
