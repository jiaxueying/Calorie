<template>
  <view>
    <view class="all">
      <view class="userimg">
        <open-data type="userAvatarUrl"></open-data>
      </view>
      <view class="userinfor">
        <view style="display: flex;">
        <open-data type="userNickName" style="font-size: 2em;height:85rpx;"></open-data>
        <view class="button" @click="set">编辑模式</view>
        <switch color="#DD524D" style="transform: scale(0.6);position: relative;right: 100rpx;top: 10rpx;" :checked="Switch" @click="set"></switch>
        </view>
        <image src="../../static/edit.png" class="edit" v-if="Switch" @click="changeweight"></image>
        <view>
          <text style="font-size: 1.2em;margin-top: 6rpx;margin-bottom: 6rpx;">体重：{{weight}}KG\n目标体重：{{targetweightshow}}\n</text>
        </view>
        <text style="font-size: 0.7em;">本日推荐摄入卡路里范围：\n{{minCalForDay}}kcal-{{maxCalForDay}}kcal</text>
      </view>
    </view>
    <view v-if="!Switch" style="animation: pushright 1s;"><historylist></historylist></view>
    <view style="display: flex;justify-content: center;animation: pushleft 500ms;" v-if="Switch">
      <plan @input="changetarget" :plan="targetweightshow" :targetweightrec="targetweight"></plan>
    </view>
    <view class="popcontent" v-if="pop">
      <view class="popup">
        <view class="text">请输入您当前体重</view>
        <view style="display: flex;" class="popinput">
        <input :value="weight" type="number" maxlength="3" :placeholder="weight" @input="refresh"/>KG
        </view>
        <view class="bottom">
          <view class="popbutton" style="border-right: #000000 1px solid;color: #8F8F94;" @click="cancel">取消</view>
          <view class="popbutton" style="border-left: #000000 1px solid;color: #00aa00;" @click="confirm">确认</view>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
  import plan from "../../components/user/plan.vue"
  import historylist from "../../components/user/history.vue"
	export default {
    components:{
      plan,
      historylist
    },
		data() {
			return {
        weight:'100',
        minCalForDay:'1000',
        maxCalForDay:'1500',
        Switch:false,
        targetweight:600,
        pop:false,
        tempweight:1,
        targetweightshow:'999KG',
        plan:true
			}
		},
		methods: {
			set:function(){
        this.Switch=!this.Switch
      },
      changetarget:function(a){
        if(a!="暂无计划")
        {
        this.targetweight=a
        this.targetweightshow=a+'KG'
        this.plan=true
        
        }
        else
        {
        this.targetweightshow=a
        this.plan=false
        }
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile/",
          method:"POST",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            user_id:uni.getStorageSync('userid'),
            plan:this.plan,
            weight:this.weight,
            target_weight:this.targetweight
          }
        })
        
      },
      changeweight:function(){
        this.tempweight=this.weight
        this.pop=true
      },
      cancel:function(){
        this.pop=false
      },
      confirm:function(){
        this.weight=this.tempweight
        this.pop=false
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile/",
          method:"POST",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            user_id:uni.getStorageSync('userid'),
            weight:this.weight,
            plan:this.plan,
            target_weight:this.targetweight
          }
        })
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile",
          method:"GET",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          success: (res) => {
            console.log(res.data.data)
          }
        })
      },
      refresh:function(event){
        this.tempweight=event.detail.value
      }
		},
    onLoad() {
		uni.request({
			url:"http://cal.hanlh.com:8000/user/profile",
			method:"GET",
			header:{
				Authorization:'Token '+uni.getStorageSync('token')
			},
			success: (res) => {
				this.weight=res.data.data.weight
				this.targetweight=res.data.data.target_weight
        this.minCalForDay=res.data.data.min_calorie
        this.maxCalForDay=res.data.data.max_calorie
        this.plan=res.data.data.plan
        if(this.plan)
        {
          this.targetweightshow=this.targetweight+'KG'
        }
        else
        {
          this.targetweightshow='暂无计划'
        }
			}
		})
    
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
    height: 60rpx;
    line-height: 60rpx;
    width: 190rpx;
    border-radius: 15rpx;
    margin-top: 18rpx;
    margin-left: 20rpx;
    border-left: 5px #e8e8e8 solid;
  }
  @keyframes pushleft{
    from{margin-left: 750rpx;opacity: 0;}
    to{}
  }
  @keyframes pushright{
    from{margin-right: 750rpx;opacity: 0;}
    to{}
  }
  .edit{
    position: absolute;
    top:95rpx;
    left: 240rpx;
    height: 35rpx;
    width: 35rpx;
  }
  .popcontent{
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    justify-content: center;
    background-color: rgba(0,0,0,.50);
    width: 100%;
    height: 100%;
    z-index: 99;
  }
  .popup{
    background-color: #ffffff;
    width: 600rpx;
    height: 320rpx;
    margin-top: 40%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    border: #000000 1px solid;
    border-radius: 15rpx;
    overflow: hidden;
  }
  .text{
    font-size: 40rpx;
    margin-bottom: 40rpx;
  }
  .popinput{
    border-bottom: #000000 1px solid;
    width: 120rpx;
    margin-bottom: 40rpx;
  }
  .bottom{
    display: flex;
    width: 600rpx;
    background-color: #ffffff;
  }
  .popbutton{
    border-top: #000000 2rpx solid;
    text-align: center;
    line-height: 90rpx;
    height: 90rpx;
    width: 300rpx;
  }
</style>
