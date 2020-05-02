<!-- TODO:change navigate Function -->

<template>
  <view>
	
  <view style="display: flex;flex-direction: column;align-items: center;">
    
    <view class="title">
      <view class="navigator">菜品管理</view>
    </view>
    
    <view class="allbtn">
      <view class="btn" @tap="openRealeaseNewMealList">
        <view class="navigator">发布新菜单
        </view>
      </view>
      <view class="btn" @tap="openCheckMealList">
        <view class="navigator">查看已发布菜单
        </view>
      </view>
      <view class="btn" @tap="openMealListManage">
        <view class="navigator">菜品信息管理
        </view>
      </view>
    </view>
   </view>
	</view>
</template>

<script>
	export default {
    components:{
    },
		data() {
			return {
			}
		},
		methods: {
      openMealListManage:function() {
        console.log("菜品信息管理 button clicked");
        wx.navigateTo({
          url:"../MealManagement/MealManagement"
        });
      },
      openCheckMealList:function() {
        console.log("查看已发布菜单 button clicked");
        wx.navigateTo({
          url:"../MealList/MealList?booleans=" +
          JSON.stringify({
           modifyable:false,
           countable:true,
          })
        });
      },
      openRealeaseNewMealList:function() {
        console.log("发布新菜单 button clicked");
        wx.navigateTo({
          url:"../MealList/MealList?booleans=" +
          JSON.stringify({
           modifyable:true,
           countable:false
          })
        });
      }
		},
    onLoad() {
	   
    }
	}
</script>

<style>
.navigator{
  font-size: 1.5em;
  font-weight: 800;
  color:#59453D;
}
.title{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width:100%;
  margin-top: 100rpx;
  margin-left: 100rpx;
}

.allbtn{
  margin-top: 50rpx;;
}
.btn{
  display: flex;
  flex-direction: column;
  justify-content: center;
  border:#59453D 7rpx solid;
  border-radius: 40rpx;
  width:650rpx;
  height:200rpx;
  margin-bottom: 50rpx;
  padding-left: 40rpx;
  text-align: center;
}
text{
  font-size: 0.5em;
  font-weight: 400;
  line-height: 100%;
}

</style>
