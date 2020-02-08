<template>
  <view class="content">
    <view class="text">近期是否有减肥计划？</view>
    <view style="display: flex;">
      <view :class="{chosen:choice,button:true}" @click="Switch(true)">有</view>
      <view :class="{chosen:!choice,button:true}" @click="Switch(false)">无</view>
    </view>
    <view class="input" v-if="choice">
      目标体重:<input 
               :value="targetweight" 
               type="number" 
               :placeholder="targetweight" 
               maxlength="3" 
               style="width: 150rpx;margin-top: 8rpx;border-bottom: #C09C79 4rpx solid;"
               @blur="set"/>KG
    </view>
    <view class="tip" v-if="!choice">记得及时制定体重控制计划哟~</view>
  </view>
</template>

<script>
  export default{
    data(){
      return{
        choice:true,
        targetweight:999
      }
    },
    methods:{
      Switch:function(choi){
        this.choice=choi
      },
      set:function(event){
        if(event.detail.value!="")
        {this.targetweight=event.detail.value}
        this.$emit('input',this.targetweight)
      }
    }
  }
</script>

<style>
  .content{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .text{
    color: #505050;
    font-size: 60rpx;
  }
  .button{
    font-size: 40rpx;
    text-align: center;
    width: 300rpx;
    height: 80rpx;
    line-height: 80rpx;
    margin: 20rpx;
    border: 2px #D2A9A9 solid;
    color: #d2a9a9;
    border-radius: 12rpx;
  }
  .chosen{
    color: #ffffff;
    background-color: #D2A9A9;
  }
  .input{
    color: #c09c79;
    font-size: 45rpx;
    margin-top: 10rpx;
    animation: pushup 1s;
    display: flex;
  }
  .tip{
    font-size: 45rpx;
    color: #a5b4ac;
    margin-top: 10rpx;
    animation: pushup 1s;
  }
  @keyframes pushup{
    from{margin-top: 50rpx;opacity: 0;}
    to{margin-top: 10rpx;}
  }
</style>
