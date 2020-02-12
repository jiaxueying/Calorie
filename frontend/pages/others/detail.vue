<template>
  <view class="content">
    <view class="head">
      <text>本餐推荐的卡路里范围为{{min}}-{{max}}cal</text>
    </view>
    
    <view class="imgarea" @touchstart="start" @touchend="end" @touchmove="move">
      <image :src="src" class="img" v-if="isimg"></image>
      <rich-text class="tab" v-if="!isimg" :nodes="tab"></rich-text>
    </view>
  </view>
</template>

<script>
  export default{
    components:{
      
    },
    data(){
      return{
        X:Number,
        tempX:Number,
        min:'',
        max:'',
        src:'../../static/chocolate.png',
        isimg:true,
        tab:"<h2>ahahahahaha</h2>"
      }
    },
    methods:{
      start:function(event){
        this.X=event.touches[0].pageX
        console.log(this.X)
      },
      end:function(event){
        if(this.tempX>50)
        {this.isimg=true}
        if(this.tempX<-50)
        {this.isimg=false}
        console.log(this.isimg)
      },
      move:function(event){
        this.tempX=event.touches[0].pageX-this.X
        console.log(this.tempX)
      }
    },
    
  }
</script>

<style>
  .content{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .head{
    display: flex;
    border:#000000 1rpx solid;
    justify-content: center;
    font-size: 30rpx;
    font-weight: 400;
    line-height: 200%;
    color:#505050;
    width: 750rpx;
    }
    .imgarea{
      margin-top: 20rpx;
      height: 400rpx;
      display: flex;
    }
    .img{
      position: relative;
      width: 400rpx;
      height: 400rpx;
      animation: showimg 0.5s;
    }
    .tab{
      position: relative;
      width: 550rpx;
      height: 400rpx;
      background-color: #007AFF;
      animation: showtab 0.5s;
    }
    @keyframes showimg{
      from{right: 600rpx;}
      to{right: 0;}
    }
    @keyframes showtab{
      from{left: 600rpx;}
      to{left: 0;}
    }
</style>
