<template>
  <view calss="content">
    <view class="historyMenu">
      <text style="position: relative;right:35rpx;font-size: 30rpx;">历史菜单</text>
    </view>
    <dl>
    <dt class="historyList" v-for="(item,index) in list" :key="index">
      <view class="mealimg">
        <image style="width: 100rpx;height: 100rpx;" :src="item.src"></image>
      </view>
      <view class="historyInfo">
        <text>{{item.date}}\n</text>
        <text style="font-size: 0.6em;font-weight: 100;color:#505050;line-height: 50rpx;">{{item.cal}}kcal</text>
      </view>
      <image src="../../static/timg.jpg" class="deleteIcon" @click="deleteItem(index,list)"></image>
    </dt>
    </dl>
  </view>
</template>

<script>
  export default{
    data(){
      return{
        list:[
          {src:'../../static/shrimp.png',cal:'100',date:'date1'},
          {src:'../../static/shrimp.png',cal:'100',date:'date2'},
          {src:'../../static/shrimp.png',cal:'100',date:'date3'},
          {src:'../../static/shrimp.png',cal:'100',date:'date4'},
          {src:'../../static/shrimp.png',cal:'100',date:'date5'},
          {src:'../../static/shrimp.png',cal:'100',date:'date6'},
          {src:'../../static/shrimp.png',cal:'100',date:'date7'},
          {src:'../../static/shrimp.png',cal:'100',date:'date8'},
          {src:'../../static/shrimp.png',cal:'100',date:'date9'},
          
        ],
        replacelist:{src:'../../static/default.jpg',cal:'这里会记录你每餐的就餐卡路里数据,例如100',date:'这里会记录你的就餐时间'},
      }
    },
    methods:{
      deleteItem:function(index,list){
        list.splice(index,1);
        uni.showToast({
          title:'删除成功',
          duration:2000
        })
        if(this.list.length==0){
          this.list[0]=this.replacelist
          console.log('default')
        }
      }
     },
     created:function(){
       if(this.list.length==0)
       {this.list[0]=this.replacelist}
      }
  }

</script>

<style>
  .content{
    display: flex;
    align-items: center;
  }
 
  .mealimg{
    width:100rpx;
    height:100rpx
  }
  .historyMenu{
    border-top:2px #E8E8E8 solid;
    border-bottom:2px #E8E8E8 solid;
    color:#59453D;
    height: 80rpx;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    font-size: 0.8em;
    font-weight: 100;
    margin-bottom: 25rpx;
    margin-top: 50rpx;
  }
  .historyList{
    display: flex;
  }
  dl{
    margin-top: 15rpx;
  }
  dt{
    border: #E8E8E8 solid 1px;
  }
  .historyInfo{
    display: flex;
    flex-direction: column;
    position: relative;
    left: 50rpx;
  }
  .deleteIcon{
    width:40rpx;
    height: 40rpx;
    position:relative;
    left:500rpx;
    top:25rpx;
    opacity:0.4
  }
  
</style>
