<template>
  <view>
  <popup  v-if="isfirst" style="background-color:rgba(0,0,0,0.7);position:fixed;width:100%;height:100%" >
      <view class="timelist" >
        <view class="logo">
         <text >粟</text>
        </view>
        <text class="timeitem" @tap="setRange('breakfast')">breakfast</text>          
        <text class="timeitem" @tap="setRange('brunch')">brunch</text>
        <text class="timeitem" @tap="setRange('lunch')">lunch</text>
        <text class="timeitem" @tap="setRange('afternoon tea')">afternoon tea</text>
        <text class="timeitem" @tap="setRange('dinner')">dinner</text>
      </view>
  </popup>
  
	<recrange v-if="isrange"></recrange>
	
  <view style="display: flex;flex-direction: column;align-items: center;">
      <view class="title">
          <navigator>首页</navigator>
          <text class="time">本餐是 : {{msg}}</text>
      </view>
      
      <view class="allbtn">
            <view class="btn">
              <navigator url="../search/search" hover-class="none">查询功能
              <text>\n戳这里了解今天摄入了多少卡路里</text>
              </navigator>
            </view>
            <view class="btn">
              <navigator url="../recommondation/list" hover-class="none">推荐功能
              <text>\n戳这里摇出今天吃什么</text>
              </navigator>
            </view>
            <view class="btn">
              <navigator url="../user/user" hover-class="none">用户中心
              <text>\n了解您的信息可以更好的为您推荐呦</text>
              </navigator>
            </view>
   </view>
   </view>
	</view>
</template>

<script>
  import recrange from '../../components/all/recommendrange.vue'
	export default {
    components:{
      recrange,
    },
		data() {
			return {
        isfirst:true,
				msg:'',
        isrange:false
			}
		},
		methods: {
      setRange:function(rec){
        this.isfirst=false
        this.msg=rec
        let weight
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile",
          method:"GET",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            
          },
          success: (res) => {
            console.log(res.data.data)
            weight=res.data.data.weight
            console.log(weight)
            uni.setStorageSync('userid',res.data.data.id)
            let userid=uni.getStorageSync('userid')
            console.log(userid)
            uni.setStorage({
              key:'range',
              data:[1300,1350]
            })
			this.isrange=!this.isrange
          }
        })
      }
			
		},
    onLoad() {
      uni.login({
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
      })
      uni.getStorage({
        key:'meal-list',
        success: (res) => {
          console.log(res)
        },
        fail: () => {
          uni.setStorage({
            key:'meal-list',
            data:[],
            success: () => {
              console.log('set meal-list')
            }
          })
        }
      })
	   
    }
	}
</script>

<style>
  popup{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .timelist{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 450rpx;
    font-size: 2em;
    width:80%;
    color:#000000;
    border:#C8C7CC 2rpx solid;
    border-radius: 25rpx;
    padding-top: 50rpx;
    padding-bottom: 50rpx;
    background-color:#E8E8E8;
  }
  .timeitem{
    border:4rpx solid #C8C7CC;
    border-radius: 25rpx;
    margin-top: 15rpx;
    width: 60%;
    text-align: center;
    line-height: 150%;
    font-weight: 300;
  }
  .logo{
    border: 5rpx solid #C8C7CC;
    border-radius: 50%;
    width:70rpx;
    height:70rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1em;
  }
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

.time{
  border:2rpx solid #59453D;
  border-radius: 25rpx;
  line-height: 120%;
  margin-top: 35rpx;
  font-size: 1em;
  color:#59453D;
  padding-right: 20rpx;
  padding-left: 20rpx;
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
}
text{
  font-size: 0.5em;
  font-weight: 400;
  line-height: 100%;
}

</style>
