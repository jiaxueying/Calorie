<template>
  <view>
  <view class="content" :style="contentsize">
    <canvas canvas-id="canvas" :style="size">
    </canvas>
  </view>
   
   
    <view class="allbtn">
        
        <view class="btn" >
          <button type="default" plain style="border:none" @click="friendcircle">
               <image class="icon" src="../../static/friendcircle.jpg"></image>
               <text>分享至朋友圈</text>
          </button>
        </view>
        
      
      
      <view class="btn" >
          <button type="default" open-type="share" plain style="border:none">
            <image class="icon" src="../../static/friend.jpg" style=""></image>
            <text>发送给朋友</text>
          </button>
      </view>
        
        
        
      <view class="btn">
        <button type="default" plain style="border:none" @click="save">
          <image class="icon" src="../../static/download.jpg" ></image>
          <text>保存到手机</text>
        </button>
      </view>
        
    </view>
  </view>
</template>

<script>
  export default {
      onShareAppMessage(res) {
        if (res.from === 'button') {
          console.log(res.target)
        }
        return {
          title: '粟',
          path: '/pages/index/index?url='
        }
      },
    
    data(){
      return{
        msg:'300',
        date:'',
        size:"width:600rpx;",
        contentsize:"",
        meallist:[ null ]
       
      }
    },
      
      created: function (e) {
        console.log(this.meallist)
           uni.setStorageSync('meallist', [{ mysrc:"../../static/shrimp.png",mealname:"shrimp",cal:"100"},{ mysrc:"../../static/shrimp.png",mealname:"shrimp",cal:"100"}]);
         console.log(this.meallist)                        
          let that=this
          uni.getStorage({
              key: 'meallist',
              success: function (res) {
                  console.log(res.data);
                  that.meallist=res.data;
                  that.draw();
              }
          });   
          console.log(this.meallist)
      },
      methods: {
        draw:function(e){
            console.log(this.meallist.length)          
            var j=(this.meallist.length>=3)?(this.meallist.length-3):0
            var k=j*90+800
            
            console.log(j)
            this.size+="height:"+k+"rpx;"
            this.contentsize+="height:"+k+"rpx;"
            console.log(this.size)
                        
            let rp=1
            wx.getSystemInfo({
                  success(res) {
                    rp = res.windowWidth/375;
                    console.log(rp)
                   },
               })
                      
           
           var time=new Date();
           this.date=time.toLocaleDateString();
           console.log(this.date)
                     
          
           var ctx = uni.createCanvasContext('canvas')          
            console.log(ctx)
            ctx.setFillStyle("#FFFFFF")
            ctx.fillRect(0,0,300*rp,400*rp)
           
            ctx.setStrokeStyle("#59453D")
            ctx.moveTo(50*rp,50*rp)
            ctx.lineTo(250*rp,50*rp)
            ctx.moveTo(50*rp,300*rp+j*90*rp)
            ctx.lineTo(250*rp,300*rp+j*90*rp)
            ctx.moveTo(0*rp,370*rp+j*90*rp)
            ctx.lineTo(300*rp,370*rp+j*90*rp)
            ctx.stroke()
            
            ctx.font="15rpx Arial";
            ctx.setFillStyle('#59453D')
            ctx.setTextBaseline('middle')
            ctx.fillText("My List",130*rp,40*rp)
            ctx.fillText("本餐共摄入",180*rp,320*rp+j*90*rp)
            ctx.fillText(this.msg+"kcal",200*rp,340*rp+j*90*rp)
            ctx.fillText("#粟",3*rp,390*rp+j*90*rp)
            ctx.fillText(this.date,200*rp,390*rp+j*90*rp)
            
            for(var i=0;i<this.meallist.length;i++){
                          ctx.drawImage(this.meallist[i].mysrc,0, 0, 600*rp, 600*rp,70*rp, 57*rp+i*90*rp, 70*rp, 70*rp)
                          ctx.fillText(this.meallist[i].mealname,180*rp,71*rp+i*90*rp)
                          ctx.fillText(this.meallist[i].cal+"kcal",180*rp,96*rp+i*90*rp)
                        }
                        
            ctx.setStrokeStyle("#000000")
            ctx.setLineWidth(2)
            ctx.rect(0,0,300*rp,400*rp+j*90*rp)
            ctx.shadowBlur=7
            ctx.shadowColor="#808080"
            ctx.shadowOffsetY=5
            ctx.stroke()
            
            ctx.draw()
            console.log('wancheng')
            console.log(this.meallist)
            
        },
          canvasIdErrorCallback: function (e) {
              console.error(e.detail.errMsg)
          },
           
         friendcircle:function(){
           uni.canvasToTempFilePath({
           			canvasId:'canvas',
           			success: function(res){
           				console.log(res.tempFilePath)
           				uni.saveImageToPhotosAlbum({
           					filePath:res.tempFilePath,
           					
           				})
           			}
           		});
           uni.showModal({
               title: '小程序的锅',
               content: '图片已保存至本地，手动分享叭亲',
               success: function (res) {
                   if (res.confirm) {
                       console.log('用户点击确定');
                   } else if (res.cancel) {
                       console.log('用户点击取消');
                   }
               }
           });
           
         },
         
         save:function(){
           uni.showLoading({
           		title: '图片绘制中...',
           	})
            uni.canvasToTempFilePath({
            			canvasId:'canvas',
            			success: function(res){
            				uni.hideLoading()
            				console.log(res.tempFilePath)
            				uni.saveImageToPhotosAlbum({
            					filePath:res.tempFilePath,
            					success : function(res){
            						uni.showToast({title : '图片已保存'})
            					}
            				})
            			}
            		})
           
         }
          
          
      }
  }
</script>

<style>
  .content{
    margin-top: 80rpx;
    display: flex;
    justify-content: center;
  }
  canvas{
    
  }
  .allbtn{
    width: 750rpx;
    display:flex;
    justify-content: space-between;
    position:fixed;
    bottom:0rpx;
    background-color: #FFFFFF;
  }
  .btn{
    display: flex;
    flex-direction: column;
    align-items: center;
    color:#59453D;
  }
  text{
    font-size: 30rpx;
    font-weight: 400;
  }
  .icon{
    width:70rpx;
    height:70rpx;
    opacity: 0.8;
  }
  button{
    display:flex;
    flex-direction: column;
    align-items: center;
  }
  
</style>
