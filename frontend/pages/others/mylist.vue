<template>
  <view>
  <view class="content">
    <canvas canvas-id="canvas"  :height="trueheight"  style="width:600rpx;">
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
          title: '自定义分享标题',
          path: '/pages/index/index.vue'
        }
      },
    
    data(){
      return{
        msg:'300',
        data:'2020/02/12',
        trueheight:800,
        meallist:[
          { mysrc:"../../static/shrimp.png",mealname:'shrimp',cal:'100'},
          { mysrc:"../../static/shrimp.png",mealname:'shrimp',cal:'100'},
          { mysrc:"../../static/shrimp.png",mealname:'shrimp',cal:'100'},
          { mysrc:"../../static/shrimp.png",mealname:'shrimp',cal:'100'},
          
        ]
       
      }
    },
      
      created: function (e) {
          let rp=1
          wx.getSystemInfo({
                success(res) {
                  rp = res.windowWidth/375;
                  console.log(rp)
                 },
             })
          
         var ctx = uni.createCanvasContext('canvas')          
          
         ctx.setFillStyle("#FFFFFF")
         ctx.fillRect(0,0,300*rp,400*rp)
         ctx.stroke()
         
          ctx.setStrokeStyle("#59453D")
          ctx.moveTo(50*rp,50*rp)//firstline
          ctx.lineTo(250*rp,50*rp)
          ctx.moveTo(50*rp,300*rp)
          ctx.lineTo(250*rp,300*rp)
          ctx.moveTo(0*rp,370*rp)
          ctx.lineTo(300*rp,370*rp)
          ctx.stroke()
          
          ctx.font="15rpx Arial";
          ctx.setFillStyle('#59453D')
          ctx.setTextBaseline('middle')
          ctx.fillText("My List",130*rp,40*rp)
          ctx.fillText("本餐共摄入",180*rp,320*rp)
          ctx.fillText(this.msg+"kcal",200*rp,340*rp)
          ctx.fillText("#粟",3*rp,390*rp)
          ctx.fillText(this.data,200*rp,390*rp)
          ctx.stroke()
          
          for(var i=0;i<this.meallist.length;i++){
            ctx.drawImage(this.meallist[i].mysrc,0, 0, 600*rp, 600*rp,70*rp, 57*rp+i*90*rp, 70*rp, 70*rp)
            ctx.fillText(this.meallist[i].mealname,180*rp,71*rp+i*90*rp)
            ctx.fillText(this.meallist[i].cal+"kcal",180*rp,96*rp+i*90*rp)
            ctx.stroke()
          }
          
          ctx.setStrokeStyle("#59453D")
          ctx.setLineWidth(2)
          ctx.rect(0,0,300*rp,400*rp)
          ctx.shadowBlur=7
          ctx.shadowColor="#808080"
          ctx.shadowOffsetY=5
          ctx.stroke()
          
          ctx.draw()
          
      },
      methods: {
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
    display: flex;
    flex-direction: column;
    align-items: center;
    height:1000rpx;
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
