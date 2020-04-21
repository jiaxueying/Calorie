<!-- TODO:change navigate Function -->

<template>
  <view>
	
  <view style="display: flex;flex-direction: column;align-items: center;">
    
    <view class="title">
      <navigator>菜品管理</navigator>
    </view>
    
    <view class="allbtn">
      <view class="btn" @tap="openRealeaseNewMealList">
        <navigator hover-class="none">发布新菜单
        <!-- <text>\n戳这里了解今天摄入了多少卡路里</text> -->
        </navigator>
      </view>
      <view class="btn" @tap="openCheckMealList">
        <navigator hover-class="none">查看已发布菜单
        <!-- <text>\n戳这里摇出今天吃什么</text> -->
        </navigator>
      </view>
      <view class="btn" @tap="openMealListManage">
        <navigator hover-class="none">菜品信息管理
        <!-- <text>\n</text> -->
        </navigator>
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
          url:"../MealManagement/AlternativeMealList"
        });
      },
      openRealeaseNewMealList:function() {
        console.log("发布新菜单 button clicked");
        wx.navigateTo({
          url:"../dishinfo/add"
        });
      }
		},
    onLoad() {
	   
    }
	}
</script>

<style>
navigator{
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
