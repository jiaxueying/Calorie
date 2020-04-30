<template>
  <view>
    <text class="hint">请输入以下信息,点击图标上传菜品图片</text>
    <view class="list">
        <image :src="src" @click="chooseimage"></image>
        <view class="table">
            <text class="meal">套餐名称：</text>
            <input placeholder="  输入内容"
                   focus="true"
                   @input="addname"
                   />
        </view>
        <view v-for="(dishname,index) in dishnames" :key="index">
        <view class="table">
            <text class="dishname">菜品名称{{index+1}}：</text>
            <input placeholder="  输入套餐内菜品名称"
                   @input="dishnameadd(index,$event)"
                   />
        </view>
        </view>
        <view style="height:150rpx"></view>
        <view class="bottom">
            <button plain="true" @click="complete">完成</button>
        </view>
    </view><!--list-->
  </view>
</template>

<script>
import {request, backendurl} from "../../common/helper.js"
export default {
    components:{
    },
		data() {
			return {
        src:"../../static/upload.jpg",
        mealname:"",//预留给套餐名称
        dishnames:["  输入套餐内菜品名称","  输入套餐内菜品名称","  输入套餐内菜品名称"],
			}
		},
		methods: {
      
     chooseimage:function(){
       var that=this;
       console.log("进入照片上传函数")
       uni.chooseImage({
         count:1,
         success:function(res){
           console.log(res.tempFilePaths)
           that.src=res.tempFilePaths[0];
           
         }
       })
       
     },
     
     addname:function(event){
       console.log(event.detail);
       this.mealname=event.detail.value;
       console.log(this.mealname);
     },
     
     dishnameadd:function(index,event){
       console.log("in dishnameadd!"+index);
       console.log(event.detail.value);
       this.dishnames[index]=event.detail.value;
       console.log(this.dishnames[index]);
     },
     //所有的上传在此处完成
     complete:async function(){
       var that=this
         console.log("进入完成函数")
         await uni.showModal({
           title: '提示',
           content: '确认上传',
           success: function (res) {
               if (res.confirm) {
                   console.log('用户点击确定');
                   console.log(that.src);
                   that.upload();
                   
               } else if (res.cancel) {
                   console.log('用户点击取消');
               }
             }
         });
         
     },
     //此处完善上传图片文件和菜品名称的api
     upload:function(){
         console.log("into upload");
         let names = [];
         for(let i = 0; i < this.dishnames.length; i++) {
           names.push(this.dishnames[i]);
         }
         console.log(JSON.stringify(names))
         uni.uploadFile({
                   url: 'http://cal.hanlh.com:8000/canteen/adddish/', 
                   filePath: this.src,
                   name: 'img',
                   header:{
                       Authorization:'Token '+uni.getStorageSync('token'),
                       'Content-Type': 'application/x-www-form-urlencoded',
                     },
                   formData: {
                        'dish':this.mealname,
                        'img':this.src,
                        'names':JSON.stringify(names)
                   },
                   success: (uploadFileRes) => {
                       console.log(uploadFileRes.data.dish);
                   }
               });
               wx.redirectTo({
                 url: "../MealManagement/MealManagement",
               })
     },
     
     
		},
    onLoad() {
    }
	}  
</script>

<style>
  .hint{
    display: block;
    border-top: 5rpx solid #808080;
    border-bottom: 5rpx solid #808080;
    font-size: 30rpx;
    font-weight: 500;
    color: #808080;
    text-align: center;
    margin-bottom: 100rpx;
    }
  .list{
    width:100%;
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    }
  image{
    width: 550rpx;
    height: 450rpx;
   }
  .meal{
    font-size: 1.5em;
    font-weight: 600;
   }
   .dishname{
     font-size:1.2em;
     font-weight: 600;
   }
  .table{
    margin-top: 100rpx;
    display: flex;
    flex-direction: row;
   }
  input{
    border: #808080 2rpx solid;
    border-radius: 10rpx;
    outline: none;
    height: 80rpx;;
    width:60%;
   }
  button{
    font-size: 20rpx;
    font-weight: 300;
    width:100rpx;
    height: 60rpx;
    line-height: 60rpx;
    border: #D0DEE5 3rpx solid;
    border-radius: 10rpx;
     }
  .bottom{
    position: fixed;
    bottom: 0rpx;
    height:100rpx;
    border-top: #C8C7CC 5rpx solid;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index:10;
    background-color: #FFFFFF;
    }
</style>
