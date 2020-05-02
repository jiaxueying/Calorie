<!-- TODO:change img src -->

<template>
  <view>
    <!--访问权限问题-->
    <view class="list">
        <image :src="src" @click="changeimage"></image>
        <text class="hint">点击上方图片更换菜品图片</text>
        <view class="table">
            <text class="mealname">套餐名称：</text>
            <input :placeholder="food.dish"
                   focus="true"
                   @input="changename"/>
        </view>
        
        <view v-for="(dishname,index) in dishnames">
        <view class="table">
            <text class="dishname">菜品名称{{index+1}}：</text>
            <input :placeholder="dishname"
                   @input="dishnamechange(index,$event)"
                   />
        </view>
        </view>
        
        <view style="height:150rpx"></view>
        <view class="bottom">
          <button plain="true" class="delete" @click="deletedish">
              <image class="icon" src="../../static/delete.jpg"></image>
              删除菜品
          </button>
            <button plain="true" @click="complete">完成</button>
        </view>
    </view><!--list-->
  </view>
</template>

<script>
import {request} from "../../common/helper.js"
export default {
    components:{
    },
	data() {
		return {
      src:"",
      changeimg:false,
			food:null,
      dishid:1,
      dishnames:[" "," "," "],
		}
	},
	methods: {
      
      changeimage:function(){
        var that=this;
        console.log("进入照片上传函数");
        uni.chooseImage({
          count:1,
          success:function(res){
            that.src=res.tempFilePaths[0];
            that.changeimg=true;
          }
        })
        
      },
      
      dishnamechange:function(index,event){
        console.log("in dishnameadd!"+index);
        console.log(event.detail.value);
        this.dishnames[index]=event.detail.value;
        console.log(this.dishnames[index]);
      },
      
      changename:function(event){
        this.food.dish=event.detail.value;
        console.log(this.food.dish);
      },
      //待完善
      upload:function(){
        console.log("into upload");
        let names = [];
        for(let i = 0; i < this.dishnames.length; i++) {
          names.push(this.dishnames[i]);
        }
        console.log(JSON.stringify(names))
        if(this.changeimg===true){
        uni.uploadFile({
                  url: 'http://cal.hanlh.com:8000/canteen/editdish/', 
                  filePath: this.src,
                  name: 'img',
                  header:{
                      Authorization:'Token '+uni.getStorageSync('token'),
                      'Content-Type': 'application/x-www-form-urlencoded',
                    },
                  formData: {
                       'dish_id':this.dishid,
                       'dish':this.food.dish,
                       'img':this.src,
                       'names':JSON.stringify(names)
                  },
                  success: (uploadFileRes) => {
                      console.log(uploadFileRes.data.dish);
                  }
              });}
        else request('/canteen/editdish/', 'POST', {
          'Content-Type': 'application/x-www-form-urlencoded',
          'dish_id':this.dishid,
          'dish':this.food.dish,
          'names':JSON.stringify(names)
         });
         wx.navigateBack({
           url: "../MealManagement/MealManagement",
         })
      },
      
      complete:function(){
          console.log("进入完成函数");
          var that=this;
          uni.showModal({
            title: '提示',
            content: '确认上传',
            success: function (res) {
                if (res.confirm) {
                    console.log('用户点击确定');
                    that.upload();
                } else if (res.cancel) {
                    console.log('用户点击取消');
                }
              }
          });
      },
      //待完善，删除菜品信息的api
      deletedish:function(){
          console.log("进入删除函数")
          var that=this;
          uni.showModal({
              title: '确认删除',
              content: '删除后将影响已发布菜单',
              success: function (res) {
                  if (res.confirm) {
                    console.log('用户点击确定');
                    uni.request({
                              url:'http://cal.hanlh.com:8000/canteen/deletedish/',
                              method:'POST',
                              header:{
                                Authorization:'Token '+uni.getStorageSync('token'),
                                'Content-Type': 'application/x-www-form-urlencoded',
                              },
                              data:{
                                dish_id:that.dishid,
                              },
                              success: (res) => {
                                console.log(res)
                                console.log("删了一个")
                                let pages = getCurrentPages();
                                let page = pages[pages.length - 1];
                                console.log(pages)
                                page.onShow();
                                wx.navigateBack({
                                url: "../MealManagement/MealManagement",
                                isRefresh: true,
                                })
                              }
                            });
                   
                  } else if (res.cancel) {
                    console.log('用户点击取消');
                  }
              }
          });
      },
      
		},
    onLoad(options) {
      this.food = JSON.parse(options.foodDetail);
      this.dishid=this.food.dish_id;
      this.src='http://cal.hanlh.com:8000' + this.food.img;
      uni.request({
                url:'http://cal.hanlh.com:8000/canteen/dishview/',
                method:'GET',
                header:{
                  Authorization:'Token '+uni.getStorageSync('token'),
                  'Content-Type': 'application/x-www-form-urlencoded',
                },
                data:{
                  dish_id:this.dishid,
                },
                success: (res) => {
                  console.log(res)
                  this.food=res.data
                  if(res.data.names.length!=0){
                  this.dishnames=res.data.names;
                  }
                }
              });
      // uni.getStorage({
      //   key:'meal-list',
      //   success: (res) => {
      //     console.log(res)
      //   },
      //   fail: () => {
      //     uni.setStorage({
      //       key:'meal-list',
      //       data:[],
      //       success: () => {
      //         console.log('set meal-list')
      //       }
      //     })
      //   }
      // })
	   
    }
	}  
</script>

<style>
  .hint{
    display: block;
    font-size: 30rpx;
    font-weight: 500;
    color: #808080;
    text-align: center;
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
  .mealname{
    font-size: 1.5em;
    font-weight: 600;
   }
   .dishname{
     font-size: 1.2em;
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
    height: 80rpx;
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
    justify-content: space-around;
    align-items: center;
    background-color: #FFFFFF;
    z-index:10;
    }
  .icon{
    width:40rpx;
    height:40rpx;
  }
  .delete{
    width:200rpx;
    height: 60rpx;
    line-height: 60rpx;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
</style>
