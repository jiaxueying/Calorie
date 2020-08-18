<!-- TODO:change navigator Function -->

<template>
  <view>
    
    <view style="display: flex;flex-direction: column;align-items: center;">
    
      <view class="title">
        <view class="navigator">食堂管理首页
            <image src="../../static/icon.png" style="width:50rpx;height:50rpx"></image>
        </view>
        <text style="font-size: 0.8em;color:#808080">@软件学院出品</text>
      </view>
    
      <view class="allbtn">
        <view class="btn" @tap="openDealQuery">
          <view ><text class="navigator">查询订单</text>
          <!-- <text>\n戳这里了解今天摄入了多少卡路里</text> -->
          </view>
        </view>
        <view class="btn" @tap="openMealManage">
          <view ><text class="navigator">菜品管理</text>
          <!-- <text>\n戳这里摇出今天吃什么</text> -->
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
      openMealManage:function() {
        console.log("菜品管理 button clicked");
        wx.navigateTo({
          url: "./indexOfMealManagment",
        })
      },
      openDealQuery:function() {
        console.log("查询订单 button clicked");
        wx.navigateTo({
          url:"../MealList/MealList?booleans=" +
          JSON.stringify({
           modifyable:false,
           countable:true
          })
        });
      },
          
		},
    onLoad() {
      /*uni.login({
        success: (res) => {
          uni.request({
            url:'http://cal.hanlh.com:8000/user/login/',
            data:{
              code:res.code,
              name:'123'
            },
            method:"POST",
            success: (res) => {
              //console.log(res)
              uni.setStorage({
                key:'token',
                data:res.data.token,
              })
            }
          })
        }
      })*/
      
      uni.getStorage({
        key:'meal-list',
        success: (res) => {console.log(res)},
        fail: () => {
          uni.setStorage({key:'meal-list',data:[],})
        }
      })
      
	   
    }
	}
</script>

<style>
.navigator{
  font-size: 50rpx;
  font-weight: 800;
  text-align: center;
  margin-right: 15rpx;
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
  justify-content: center;
  align-items: center;
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
