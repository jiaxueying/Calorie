<template>
  <view calss="content">
    <view class="historyMenu">
      <text style="position: relative;right:35rpx;font-size: 30rpx;">历史菜单</text>
    </view>
    <dl>
    <dt class="historyList" v-for="(item,index) in list" :key="index">
      <view class="mealimg">
        <image style="width: 100rpx;height: 100rpx;" :src="item.picture"></image>
      </view>
      <view class="historyInfo">
        <text>{{item.date}}\n</text>
        <text style="font-size: 0.6em;font-weight: 100;color:#505050;line-height: 50rpx;">{{item.calorie}}kcal</text>
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
          {picture:'../../static/shrimp.png',calorie:'100',date:'date1'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date2'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date3'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date4'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date5'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date6'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date7'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date8'},
          {picture:'../../static/shrimp.png',calorie:'100',date:'date9'},
          
        ],
        replacelist:{picture:'../../static/default.jpg',calorie:'这里会记录你每餐的就餐卡路里数据,例如100',date:'这里会记录你的就餐时间'},
      }
    },
    methods:{
      deleteItem:function(index,list){
        uni.request({
          url:"http://cal.hanlh.com:8000/menu/delete",
          method:"POST",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            user_id:uni.getStorageSync('userid'),
            menu_id:this.list[index].id
          }
        })
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
       uni.request({
         url:"http://cal.hanlh.com:8000/menu/query",
         method:"GET",
         header:{
           Authorization:'Token '+uni.getStorageSync('token')
         },
         data:{
           user_id:uni.getStorageSync('userid')
         },
         success: (res) => {
           this.list=res.data.data.user_menus
           if(this.list.length==0)
           {this.list[0]=this.replacelist}
         }
       })
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
