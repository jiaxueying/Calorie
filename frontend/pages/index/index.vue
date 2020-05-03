<template>
  <view>
  <popup  v-if="isisfirst">
    <view  class="popupforfirst" >
          <view  class="popupinfo" >
            <view class="logo" style="font-size: 2em;">
                <text >粟</text>
            </view>
            <text class="popuptext">由于疫情期间，本团队无法进入学校进行卡路里测算,故暂时不开放与卡路里监测相关的功能。\n疫情结束后屏幕前的你也毕业了...\n那就——毕业快乐！</text>
            <view style="width:100%;display:flex;justify-content: center;border-top: #C0C0C0 1rpx solid;" >
                <text style="color:#59453D;font-weight: 600; font-size:30rpx;" @click="isisfirstchange">我知道啦
                </text>
            </view>
          </view>
    </view>
  </popup>
  <popup  v-if="isfirst" >
        
        <view  class="timelist" >
          <view class="logo">
           <text >粟</text>
          </view>
          <text class="timeitem" @tap="setRange('breakfast')">breakfast</text>          
          <text class="timeitem" @tap="setRange('lunch')">lunch</text>
          <text class="timeitem" @tap="setRange('dinner')">dinner</text>
        </view>
        
  </popup>
  
	<!--<recrange v-if="isrange"></recrange> -->
  
	
  <view style="display: flex;flex-direction: column;align-items: center;">
      <view class="title" style="display: inline-block;">
          <navigator >首页 <image src="../../static/twentyfour.png" style="width:115rpx;height:90rpx;position:relative;right:-380rpx;bottom:-40rpx"></image></navigator>
          <text style="font-size: 0.8em;color:#808080">@软件学院出品</text>
      </view>
      
      
     
      <DateChooser style="margin-top: 50rpx; width: 700rpx;" @click.native="choosedate"></DateChooser>
      <text class="time" @tap="setIsFirst">{{msg}}</text>
      
      <view class="allbtn">
            <view @click="ordermeal" class="btn">
              <view  class="navigator">订餐功能</view><!--url="../search/search" hover-class="none"-->
              <!--<text>\n戳这里（不）可以根据卡路里订餐呦。</text>-->
            </view>
            <!--<view   @click="recommend" class="btn">
              <view class="navigator">推荐功能</view>url="../recommondation/shake" hover-class="none"
              <text>\n不知道今天吃什么？戳这里！（真的完全随机哟。）</text>
            </view>-->
            <view class="btn">
              <navigator url="../user/user" hover-class="none" class="navigator">用户中心
              <!--<text>\n了解您的信息（其实也不）可以更好地为您推荐啦。</text>-->
              </navigator>
            </view>
   </view>
   </view>
	</view>
</template>

<script>
  import recrange from '../../components/all/recommendrange.vue'
  import DateChooser from "../../components/all/date-chooser.vue"
  import { backendUrl, request } from '@/common/helper.js';
  
	export default {
    components:{
      recrange,
      DateChooser
    },
		data() {
			return {
        isisfirst:true,
        isfirst:false,
				msg:'点击此处选择餐品时间段',
        isrange:false,
        date:"",
        isdate:false,
			}
		},
		methods: {
        
      ordermeal:function(){
        console.log(this.isdate)
        if(this.isdate==true){
          var length=0;
          request('/canteen/menuview/', 'GET', {
                date: this.date,
                }).then(res =>{
                  console.log(res)
                        if(res[1].statusCode==404){
                                    uni.showModal({
                                    content:"当日当前时段的菜单还未生成哦",
                                    })
                                    }
                         else{
                                    uni.navigateTo({
                                    url:"../search/search"
                                    })
                                    var menuid;
                                    switch(this.msg) {
                                    case "breakfast": menuid= res[1].data.bre.menu_id;break;
                                    case "lunch":menuid = res[1].data.lun.menu_id;break;
                                    case "dinner":menuid = res[1].data.din.menu_id;break;
                                    }
                                    uni.setStorage({
                                      key:'menuid',
                                      data:menuid
                                    })
                                    }
                         })
               
        }
        else{
            uni.showModal({
                title: '提示',
                content: '请先选择日期',
                success: function (res) {
                          if (res.confirm) {
                          console.log('用户点击确定');
                          } else if (res.cancel) {
                          console.log('用户点击取消');
                          }
                          }
                });
            }
      },
      
      choosedate:function(){
        console.log("in choosedate")
        var that=this
        uni.$on('date change', function(){
            that.isdate=true;
            console.log(that.isdate)
            });
      },
      
      recommend:function(){
        console.log(this.isdate)
        if(this.isdate==true){
             var length=0;
             request('/canteen/menuview/', 'GET', {
                   date: this.date,
                   }).then(res =>{
                     console.log(res)
                           if(res[1].statusCode==404){
                                       uni.showModal({
                                       content:"当日当前时段的菜单还未生成哦",
                                       })
                                       }
                            else{
                                       uni.navigateTo({
                                       url:"../recommondation/shake"
                                       })
                                       }
                            })
        }
        else{
            uni.showModal({
                title: '提示',
                content: '请先选择日期',
                success: function (res) {
                          if (res.confirm) {
                          console.log('用户点击确定');
                          } else if (res.cancel) {
                          console.log('用户点击取消');
                          }
                          }
                });
            }
      },
      
      isisfirstchange:function(){
            this.isisfirst=false;
            uni.setStorage({
            key:'isisfirst',
            data:false,
            })
      },
     
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
                success: (res) => {
                let a=uni.getStorageSync('token')
                weight=res.data.data.weight
                uni.setStorageSync('userid',res.data.data.id)
                let userid=uni.getStorageSync('userid')
                    uni.setStorage({
                    key:'range',
                    data:[1000,1500]
                    })
                this.isrange=!this.isrange
                }
            })
      },
      
      setDate(d) {
        this.date = d;
      },
        
      setIsFirst() {
        this.isfirst = true;
      },
      
      getDate() {
        return this.date;
      },
      
      getMsg() {
        return this.msg;
      }
			
		},
    
    onLoad() {
      uni.setStorageSync('meal-list', []);
      uni.getStorage({
       key:'isisfirst',
       success: (res) => {
         console.log(res.data)
         this.isisfirst=res.data
       },
       fail:()=> {
         uni.setStorage({
           key:'isisfirst',
           data:true,
           success() {
             this.isisfirst=true,
             console.log("isisfirst set"+this.isisfirst)
           }
         })
       }
      })
      const date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      month = month > 9 ? month : '0' + month;;
      day = day > 9 ? day : '0' + day;
      this.date =  `${year}-${month}-${day}`;
      uni.$on('date change', this.setDate);
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
                  uni.setStorage({
                  key:'token',
                  data:res.data.token,
                  })
                  }
              })
        }
      })
      
      
      uni.getStorage({
        key:'weightdate',
        success: (res) => {
          console.log(res)
        },
        fail: () => {
          uni.setStorage({
            key:'weightdate',
            data:60,
            success: () => {
              console.log('set weightdate')
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
    background-color:rgba(0,0,0,0.7);
    position:fixed;width:100%;
    height:100%;
    display: flex;
    justify-content: center;
  }
  .popupforfirst{
    margin-top:0rpx;
    width:500rpx;
    border:#C8C7CC 2rpx solid;
    border-radius:40rpx;
    background-color:#E8E8E8;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .popupinfo{
    width:500rpx;
    border:#C8C7CC 2rpx solid;
    border-radius:40rpx;
    background-color:#E8E8E8;
    z-index: 10;
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .popuptext{
    color:#59453D;
    font-weight: 500; 
    font-size:30rpx;
    margin-left: 20rpx;
    margin-right: 20rpx;
  }
  .timelist{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-top: 0rpx;
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
.navigator{
  font-size: 1.5em;
  font-weight: 800;
  color:#59453D;
  text-align: center;
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
  line-height: 120%;
  margin-top: 35rpx;
  font-size: 1em;
  color:#59453D;
  padding-right: 20rpx;
  padding-left: 20rpx;
  border:#59453D 7rpx solid;
  border-radius: 40rpx;
  width:650rpx;
  text-align: center;
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
