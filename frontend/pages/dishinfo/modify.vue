<!-- TODO:change img src -->

<template>
  <view>
    <!--访问权限问题-->
    <view class="list">
        <image :src="'../../static/' + food.pic" @click="changeimage"></image>
        <text class="hint">点击上方图片更换菜品图片</text>
        <view class="table">
            <text class="dishname">菜品名称：</text>
            <input :placeholder="food.name"
                   focus="true"
                   @input="changename"/>
        </view>
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
export default {
    components:{
    },
	data() {
		return {
			food: null,
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
          }
        })
        
      },
      changename:function(event){
        this.dishname=event.detail.value;
        console.log(this.dishname);
      },
      //待完善
      upload:function(){
        console.log("into upload");
         /* uni.uploadFile({
                    url: 'http://cal.hanlh.com:8000/', 
                    filePath: this.src,
                    name: '',
                    formData: {
                        
                    },
                    success: (uploadFileRes) => {
                        console.log(uploadFileRes.data);
                    }
                });*/
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
          uni.showModal({
              title: '提示',
              content: '确认删除',
              success: function (res) {
                  if (res.confirm) {
                    console.log('用户点击确定');
                    wx.navigateTo({
                      url: "../MealManagement/MealManagement",
                    })
                  } else if (res.cancel) {
                    console.log('用户点击取消');
                  }
              }
          });
      },
      
		},
    onLoad(options) {
      this.food = JSON.parse(options.foodDetail);
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
  .image{
    width: 250rpx;
    height: 250rpx;
   }
  .dishname{
    font-size: 50rpx;
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
