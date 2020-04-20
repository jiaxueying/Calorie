<template>
  <view>
    <scroll-view scroll-y="true" style="height:1260rpx">
    <view class="all">
    <!--my list 的菜单部分-->
    <view class="list">
      <text class="title">My list</text>
      <view class="content">
      <view class="scroll">
        <!--菜单可滚动部分-->
        <scroll-view  scroll-y="true" class="scrollview" style="height:660rpx;">
            <view v-for="(srcitem,i) in path">
                <image :src="srcitem"></image>
                <view class="mealinfor">
                    <text>\n{{meallist[i].name}}\n\n</text>
                    <text> {{meallist[i].cal}} kcal</text>
                </view>
            </view>
        </scroll-view>
        <!--菜单下方文本部分-->
        <view>
           <text class="intakeinfor">本餐共摄入\n</text>
           <text class="intakeinfor">{{msg}}kcal\n</text>
        </view>
      </view><!--scroll-->
      </view><!--content-->
      <!--最下方文本-->
      <view class="listBottomText">
          <text >#粟 </text>
          <text class="date">{{date}}</text>
      </view>    
      <canvas canvas-id="canvas" :style="size" :width="width" :height="height"></canvas>
    </view><!--list-->
    </view><!--all-->
    </scroll-view>
    
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
    //发送给朋友图标
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
        width:"",//确定类型
        height:"",//确定类型
        meallist:[ null ],
        path: [],//图片的路径
        size:"width:600rpx;",
      }
    },
      //created用于组件加载，onload用于页面加载
    created: async function (e) {
      //异步函数
      this.meallist = uni.getStorageSync('meal-list');   
      this.msg = 0;
      for(var i = 0; i < this.meallist.length; i++) {
        this.msg += this.meallist[i].cal;
        await this.get(i);
        }
      this.draw();
      this.post();
    },
    
    methods: {
      
      get(i) {
        return new Promise((resolve, reject) => {
              uni.getImageInfo({
              src:'http://cal.hanlh.com:8000'+this.meallist[i].picture,
              success: (res) => {
                this.path.push(res.path);//push是什么
                resolve('success');//这句的作用
                },
              fail: () => {
                reject('error');//这句的作用
                }
              })
        });
      },
      draw:function(e){
        var j=(this.meallist.length>=3)?(this.meallist.length-3):0
        var k=j*220+800
        
        let rp=1
        wx.getSystemInfo({
          success(res) {
            rp = res.windowWidth/375;
            },
          })
        
        var widthNum=600*rp; 
        this.width=widthNum.toString();
        var heightNum=k*rp;
        this.height=heightNum.toString();
        var p=k+100*rp;
        this.size+="height:"+k+"rpx;"
                 
        var time=new Date();
        this.date=time.toLocaleDateString();
        
        var ctx = uni.createCanvasContext('canvas') 
        ctx.setFillStyle("#FFFFFF")
        ctx.fillRect(0,0,300*rp,j*90+400*rp)//在画布上填充背景，未设置颜色默认为黑色
         
        ctx.setStrokeStyle("#59453D")
        ctx.moveTo(50*rp,50*rp)
        ctx.lineTo(250*rp,50*rp)//mylist 下面的线
        ctx.moveTo(50*rp,320*rp+j*90*rp)
        ctx.lineTo(250*rp,320*rp+j*90*rp)//本餐共摄入之上的线
        ctx.moveTo(0*rp,370*rp+j*90*rp)
        ctx.lineTo(300*rp,370*rp+j*90*rp)//日期之上的线
        ctx.stroke()
          
        ctx.font="15rpx Arial";
        ctx.setFillStyle('#59453D')//设置绘图的背景颜色
        ctx.setTextBaseline('middle')
        ctx.fillText("My List",130*rp,40*rp)
        ctx.fillText("本餐共摄入",180*rp,340*rp+j*90*rp)
        ctx.fillText(this.msg+"kcal",200*rp,360*rp+j*90*rp)
        ctx.fillText("#粟",3*rp,390*rp+j*90*rp)
        ctx.fillText(this.date,200*rp,390*rp+j*90*rp)
          
        for(var i=0;i<this.meallist.length;i++){
          ctx.drawImage(this.path[i],70*rp, 57*rp+i*90*rp, 70*rp, 70*rp)
          ctx.fillText(this.meallist[i].name,180*rp,71*rp+i*90*rp)
          ctx.fillText(this.meallist[i].cal+"kcal",180*rp,96*rp+i*90*rp)
        }
                    
        ctx.setStrokeStyle("#000000")
        ctx.setLineWidth(2)
        ctx.rect(0,0,300*rp,400*rp+j*90*rp)//绘制一个矩形
        ctx.shadowBlur=7
        ctx.shadowColor="#808080"
        ctx.shadowOffsetY=5
        ctx.stroke()//无其他颜色设置，默认用黑色笔画线
        
        ctx.draw();
      },
      canvasIdErrorCallback: function (e) {
        console.error(e.detail.errMsg)
      },
         
      //分享到朋友圈
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
              } 
            else if (res.cancel) {
              console.log('用户点击取消');
              }
            }
          });
      },
       
      //保存到本地
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
      }, 
      
      
      post:function(){
        var menulist=new Array(this.meallist.length)
        for(let i=0;i<menulist.length;i++)
        {
          let templist={}
          templist.dish_id=this.meallist[i].id
          templist.mass=this.meallist[i].sum
          menulist[i]=templist
        }
        console.log(menulist)
        uni.request({
          url:'http://cal.hanlh.com:8000/menu/order/',
          method:'POST',
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            dishes:menulist
          },
          success: (res) => {
            console.log(res)
          }
        })
        uni.setStorage({
          key:'meal-list',
          data:[]
        })
      }
    }
  }
</script>

<style>
  .all{
    display: flex;
    align-content: center;  
    justify-content: center;
  }
  .list{
    width:90%;
    margin-top: 5%;
    margin-bottom: 5%;
    border:#333333 solid 5rpx;
    background-color: #F5F5F5;
  }
  .content{
    display: flex;
    align-content: center;
    justify-content: center;
    margin-bottom: 5%;
  }
  .scroll{
    width:80%;
  }
  .allbtn{
    width:100%;
    display:flex;
    justify-content: space-between;
    position:fixed;
    bottom:0rpx;
    background-color: #FFFFFF;
  }
  text{
    font-size: 30rpx;
    font-weight: 500;
    color:"#59453D";
  }
  button{
   display: flex;
   flex-direction: column;
   align-items: center;  
  }
  .icon{
    width:70rpx;
    height:70rpx;
    opacity: 0.8;
    position: relative;
        top:5rpx;
        left:-25rpx;
  }
  image{
    width:180rpx;
    height:180rpx;
    margin-top: 20rpx;
    margin-left: 40rpx;
    padding-bottom: 20rpx;
    display: inline-block;
  }
  .title{
    font-size: 40rpx;
    font-weight: 1500;
    text-align: center;
    display: block;
    margin-top: 80rpx;
  }
  .mealinfor{
    display: inline-block;
    position: absolute;
    right:120rpx;
    //使用inline-block的时候所有的justify和align布局都失效
  }
  .intakeinfor{
    margin-left: 390rpx;
  }
  canvas{
    position:fixed;
    left:-10000rpx;
  }
  .scrollview{
    border-top: #333333 inset 5rpx; 
    border-bottom: #333333 outset 5rpx;
  }
  .listBottomText{
    border-top: #333333 groove 5rpx;
  }
  .date{
    position: absolute; 
    right:50rpx;
  }
</style>
