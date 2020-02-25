<template>
  <view class="content">
    <view class="head">
      <text>本餐推荐的卡路里范围为{{min}}-{{max}}cal</text>
    </view>
    
    <view style="height: 50rpx;width: 750rpx;">
      
    </view>
    
    <view class="imgarea" @touchstart="start" @touchend="end" @touchmove="move">
      <image :src="'http://cal.hanlh.com:8000'+food.picture" class="img" v-if="isimg"></image>
      <view class="tab" v-if="!isimg">
        <tab>
          <ttr align="left">
            <tth style="width: 200rpx;">项目</tth>
            <tth style="width: 200rpx;">每100克(g)</tth>
            <tth style="width: 200rpx;">NRV%</tth>
          </ttr>
          <ttr v-for="(content,index) in nutrition" :key="index" align="left">
            <ttd style="width: 200rpx;">{{content.item}}</ttd>
            <ttd style="width: 200rpx;">{{content.value}}</ttd>
            <ttd style="width: 200rpx;">{{content.percent}}</ttd>
          </ttr>
        </tab>
      </view>
      <view style="display: flex;margin-top: 20rpx;">
        <view :class="{blackspot:isimg,whitespot:!isimg}" style="margin-right: 10rpx;"></view><view :class="{whitespot:isimg,blackspot:!isimg}" style="margin-left: 10rpx;"></view>
      </view>
    </view>
    
    <view class="detail">
      <view class="name">{{name}}</view>
      <view class="cal">{{cal}}</view>
    </view>
    
    <view class="opinion">
      <image src="../../static/happy.png" class="countimg" @click="like"></image>
      <view class="count" @click="like">{{like_count}}</view>
      <image src="../../static/sad.png" class="countimg" @click="dislike"></image>
      <view class="count" @click="dislike">{{dislike_count}}</view>
    </view>
    
    <view style="margin-top: 50rpx;">
    <view style="width: 550rpx;display: flex;height: 30rpx;margin-top: 10rpx;">
      <view style="height: 20rpx;width: 20rpx;border-radius: 10rpx;margin-right: 10rpx;background-color: #000000;margin-top: 5rpx;"></view>
      <view style="margin-left: 10rpx;font-size: 30rpx;line-height: 30rpx;font-weight: 500;">关键词</view>
    </view>
    
    <view class="tags">
      <view v-for="(tag,index) in tags" class="tag" :key="index" @click="taptag(index)">{{tag.name}}</view>
    </view>
    </view>
    
    <view style="background-color: #FFFFFF;width: 750rpx;height: 100rpx;">
      
    </view>
    
    <view class="bottom">
      <image src="../../static/tableware.jpg" style="height: 70rpx;width: 70rpx;margin-left: 60rpx;border: #B0B0B0 1rpx solid;border-radius: 15rpx;padding: 5rpx;" @click="mylist"></image>
      <view class="buttun" @click="add">Add to List</view>
    </view>
  </view>
</template>

<script>
  import { like, dislike } from '@/common/helper.js';
  import { backendUrl, request } from '@/common/helper.js';
  import tab from "../../components/t-table/t-table.vue";
  import ttr from "../../components/t-table/t-tr.vue";
  import tth from "../../components/t-table/t-th.vue";
  import ttd from "../../components/t-table/t-td.vue";
  export default{
    components:{
      tab,
      ttr,
      tth,
      ttd
    },
    data(){
      return{
        food: null,
        like_count:666,
        liked: 0,
        disliked: 0,
        dislike_count:666,
        X:Number,
        tempX:Number,
        min:'',
        max:'',
        isimg:true,
        name:"菜品名称",
        cal:"100KCAL/100g",
        tags:[
          {id:1,name:'理科食堂'},
          {id:2,name:'二楼'},
          {id:3,name:'低卡'},
          {id:1,name:'五号窗口'},
        ],
        nutrition:[
          {item:'能量',value:'2012KJ',percent:'24%'},
          {item:'蛋白质',value:'10.0g',percent:'17%'},
          {item:'脂肪',value:'21.0g',percent:'35%'},
          {item:'碳水化合物',value:'62.5g',percent:'21%'},
          {item:'钠',value:'663mg',percent:'33%'},
          {item:'钙',value:'280mg',percent:'35%'}
        ],
      }
    },
    onLoad: function(options) {
      this.food = JSON.parse(options.foodDetail);
      console.log(this.food);
      this.like_count = this.food.like;
      this.dislike_count = this.food.dislike;
      this.name = this.food.name;
      this.cal = this.food.calorie + "KCAL/100g";
      this.tags = this.food.tag;
      this.nutrition[1].value = this.food.protein+'g';
      this.nutrition[2].value = this.food.fat+'g';
      this.nutrition[3].value = this.food.carbohydrate+'g';
      this.nutrition[4].value = this.food.sodium+'mg';
      console.log(this.nutrition);
      uni.getStorage({
        key:'range',
        success: (rec) => {
          this.min=rec.data[0]
          this.max=rec.data[1]
        }
      })
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
      },
      like:function(){
        console.log("like")
        like(this.food.id);
        request('/dish/key_query/', 'GET', {
          key_word: this.food.name,
        }).then(res => {
          this.like_count = res[1].data.data[0].like;
          this.dislike_count = res[1].data.data[0].dislike;
          console.log(res);
        });
      },
      dislike:function(){
        console.log("dislike")
        dislike(this.food.id);
        request('/dish/key_query/', 'GET', {
          key_word: this.food.name,
        }).then(res => {
          this.like_count = res[1].data.data[0].like;
          this.dislike_count = res[1].data.data[0].dislike;
          console.log(res);
        });
      },
      taptag:function(index){
        console.log(this.tags[index]);
        uni.$emit("search_tag", this.tags[index]);
        wx.navigateBack();
      },
      mylist:function(){
        console.log("mylist");
      },
      add:function(){
        console.log("add")
        var OrderedFood = uni.getStorageSync("meal-list");
        for(var i = 0; i < OrderedFood.length; i++) {
          if(OrderedFood[i].name === this.food.name) return;
        }
        OrderedFood.push({
          name: this.food.name,
          cal: this.food.calorie,
          sum: 100,
        });
        uni.setStorageSync("meal-list", OrderedFood);
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
    font-size: 26rpx;
    font-weight: 400;
    line-height: 200%;
    color:#505050;
    width: 750rpx;
    position: fixed;
    background-color: #FFFFFF;
    z-index: 3;
    }
    .imgarea{
      margin-top: 40rpx;
      height: 600rpx;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    .img{
      position: relative;
      width: 600rpx;
      height: 600rpx;
      animation: showimg 0.5s;
    }
    .tab{
      position: relative;
      width: 600rpx;
      height: 600rpx;
      animation: showtab 0.5s;
      overflow: hidden;
    }
    @keyframes showimg{
      from{right: 600rpx;}
      to{right: 0;}
    }
    @keyframes showtab{
      from{left: 600rpx;}
      to{left: 0;}
    }
    .blackspot{
      background-color: #000000;
      width: 20rpx;
      height: 20rpx;
      border-radius: 10rpx;
    }
    .whitespot{
      width: 20rpx;
      height: 20rpx;
      border-radius: 10rpx;
      background-color: #b0b0b0;
    }
    .detail{
      display: flex;
      align-items: flex-end;
      margin-top: 30rpx;
    }
    .name{
      font-size: 70rpx;
      margin-right: 30rpx;
      font-weight: 800;
      color: #505050;
      line-height: 80rpx;
    }
    .cal{
      font-size: 40rpx;
      font-weight: 800;
      color: #505050;
      line-height: 50rpx;
    }
    .opinion{
      align-self: flex-end;
      display: flex;
      height: 50rpx;
      margin-right: 50rpx;
      margin-top: 30rpx;
    }
    .countimg{
      width: 50rpx;
      height: 50rpx;
      margin-left: 50rpx;
      margin-right: 10rpx;
    }
    .count{
      line-height: 50rpx;
      font-size: 40rpx;
    }
    .tags{
      display: flex;
      width: 550rpx;
      margin-top: 30rpx;
      flex-wrap: wrap;
    }
    .tag{
      background-color:#FFFFFF;
      height: 50rpx;
      border-radius: 30rpx;
      margin-right: 30rpx;
      font-size: 30rpx;
      line-height: 50rpx;
      padding-left: 30rpx;
      padding-right: 30rpx;
      border: #B0B0B0 1rpx solid;
      margin-bottom: 20rpx;
    }
    .bottom{
      position: fixed;
      bottom: 0;
      width: 750rpx;
      border-top-color: #b0b0b0;
      border-top-width: 3rpx;
      border-top-style: solid;
      height: 100rpx;
      background-color: #FFFFFF;
      z-index: 1;
      display: flex;
      align-items: center;
    }
    .buttun{
      border: #B0B0B0 1rpx solid;
      font-size: 30rpx;
      height: 80rpx;
      line-height: 80rpx;
      padding-left: 20rpx;
      padding-right: 20rpx;
      position: absolute;
      left: 520rpx;
      border-radius: 15rpx;
    }
</style>
