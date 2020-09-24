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
              <scroll-view scroll-y="true" class="scrollview">
                <view style="height:5rpx;"></view>
                <view v-for="(srcitem,i) in path">
                  <image :src="srcitem" ref="conf0" @load="onload"></image>
                  <view class="mealinfor">
                    <text>\n{{meallist[i].name}}\n\n</text>
                    <text> {{meallist[i].sum}} 份</text>
                  </view>
                </view>
              </scroll-view>
              <!--菜单下方文本部分-->
              <view style="height:100rpx;">
                <text :class="{'ordertime':isorder,'inorder':!isorder}">订餐时间：{{time}}\n订单号：01</text>

              </view>
            </view>
            <!--scroll-->
          </view>
          <!--content-->
          <!--最下方文本-->
          <view class="listBottomText">
            <text>#粟 </text>
            <text class="date">{{date}}</text>
          </view>
          <canvas canvas-id="canvas" :style="size" :width="width" :height="height"></canvas>
        </view>
        <!--list-->
      </view>
      <!--all-->
    </scroll-view>


    <view class="allbtn">

      <button style="display: none;">
        <image class="icon" src="../../static/friend.jpg" style="opacity: 0.7;"></image>
        <picker style="z-index:999" mode="time" :value="time" start="09:01" end="21:01" @change="bindTimeChange">
          <text>食堂订餐</text>
        </picker>
      </button>

      <button open-type="share" class="button">
        <image class="icon" src="../../static/friend.jpg" style=""></image>
        <view><text>发送给朋友</text></view>
      </button>

      <button @click="save" class="button">
        <image class="icon" src="../../static/download.jpg"></image>
        <view><text>保存到手机</text></view>
      </button>

    </view>

  </view>
</template>

<script>
  export default {

    //发送给朋友的图标
    onShareAppMessage(res) {
      if (res.from === 'button') {
        console.log(res.target)
      }
      return {
        title: '粟',
        path: '/pages/index/index?url='
      }
    },

    data() {
      return {
        menuid: "",
        msg: '300',
        date: '',
        width: "", //确定类型
        height: "", //确定类型
        meallist: [],
        path: [], //图片的路径*/
        paths: [],
        size: "width:600rpx;",
        ispost: true, //是否上传，区分来自于查看历史菜单详情还是生成新菜单
        onloadtime: 0,
        time: "食堂订餐",
        isorder: false
      }
    },

    //created用于组件加载，onload用于页面加载
    created: async function(e) {
      await this.show();
      for (var j = 0; j < this.meallist.length; j++) {
        await this.get(j);
      }

    },

    onload: function() {
      console.log("in onload!")
      this.onloadtime++
      if (this.onloadtime == this.meallist.length) {
        setTimeout(this.draw, 500);
        console.log("to draw !")
        // 旧 post 的位置
        // if (this.ispost) this.post();
      }
    },
    methods: {

      show() {
        return new Promise((resolve, reject) => {
          uni.getStorage({
            key: 'historymsg',
            success: () => {
              var data = uni.getStorageSync('historymsg')
              console.log(data)
              this.date = data.date;
              console.log(data.date)
              for (var i = 0; i < data.detail.dishes.length; i++) {
                this.meallist[i].picture = data.detail.dishes[i].img
                this.path.push('https://nkucalorie.top:8000' + data.detail.dishes[i].img)
                this.getinfo(i)
                this.meallist[i].name = data.detail.dishes[i].dish
                this.meallist[i].sum = 1 //确定是1？
                console.log(this.meallist[i])
              }
              this.ispost = false
              console.log("from history list~");
              uni.removeStorageSync('historymsg');
              resolve('success');
            },
            fail: () => { //未获取到历史菜单，从购物车进入
              reject('error in show');
              var time = new Date();
              this.date = time.toLocaleDateString();
              console.log(this.date)
              this.menuid = uni.getStorageSync('menuid');
              var tempmeallist = uni.getStorageSync('meal-list');
              console.log(tempmeallist);
              for (var i = 0, j = 0; i < tempmeallist.length; i++) {
                if (tempmeallist[i].sum != 0) {
                  this.meallist[j] = tempmeallist[i];
                  this.path.push('https://nkucalorie.top:8000' + this.meallist[j].picture);
                  this.getinfo(j);
                  j++;
                }
              }
              // 新 post 的位置
              if (this.ispost) this.post();

            }, //fail的结束
          })
        })
      },



      getinfo: function(i) {
        uni.getImageInfo({
          src: 'https://nkucalorie.top:8000' + this.meallist[i].picture,
          success: (res) => {
            this.paths.push(res.path)
            console.log("get one picture!")
          }
        })
      },

      get(i) {
        return new Promise((resolve, reject) => {
          uni.getImageInfo({
            src: 'https://nkucalorie.top:8000' + this.meallist[i].picture,
            success: (res) => {
              this.paths.push(res.path);
              console.log(this.paths);
              resolve('success');
            },
            fail: () => {
              reject('error');
            }
          })
        });
      },

      draw: function(e) {
        this.meallist = uni.getStorageSync('meal-list')
        console.log(this.meallist)
        var j = (this.meallist.length >= 3) ? (this.meallist.length - 3) : 0
        var k = j * 220 + 800

        let rp;
        wx.getSystemInfo({
          success(res) {
            rp = res.windowWidth / 375;
          },
        })

        this.size += "height:" + k + "rpx;"

        var ctx = uni.createCanvasContext('canvas')
        ctx.setFillStyle("#FFFFFF")
        ctx.fillRect(0, 0, 300 * rp, j * 90 + 400 * rp) //在画布上填充背景，未设置颜色默认为黑色

        ctx.setStrokeStyle("#59453D")
        ctx.moveTo(50 * rp, 50 * rp)
        ctx.lineTo(250 * rp, 50 * rp) //mylist 下面的线
        ctx.moveTo(50 * rp, 320 * rp + j * 90 * rp)
        ctx.lineTo(250 * rp, 320 * rp + j * 90 * rp) //本餐共摄入之上的线
        ctx.moveTo(0 * rp, 370 * rp + j * 90 * rp)
        ctx.lineTo(300 * rp, 370 * rp + j * 90 * rp) //日期之上的线
        ctx.stroke()

        ctx.font = "15rpx Arial";
        ctx.setFillStyle('#59453D') //设置绘图的背景颜色
        ctx.setTextBaseline('middle')
        ctx.fillText("My List", 130 * rp, 40 * rp)
        //ctx.fillText("本餐共摄入",180*rp,340*rp+j*90*rp)
        //ctx.fillText(this.msg+"kcal",200*rp,360*rp+j*90*rp)
        ctx.fillText("#粟", 3 * rp, 390 * rp + j * 90 * rp)
        ctx.fillText(this.time, 270 * rp, 350 * rp + j * 90 * rp)
        const metrics = ctx.measureText(this.date).width
        console.log(metrics)
        ctx.fillText(this.date, 300 * rp - metrics, 390 * rp + j * 90 * rp)

        for (var i = 0; i < this.meallist.length; i++) {
          ctx.drawImage("https://nkucalorie.top:8000" + this.meallist[i].picture, 70 * rp, 57 * rp + i * 90 * rp, 70 *
            rp, 70 * rp)
          ctx.fillText(this.meallist[i].name, 180 * rp, 71 * rp + i * 90 * rp)
          ctx.fillText(this.meallist[i].sum + "份", 180 * rp, 96 * rp + i * 90 * rp)
          //ctx.fillText(this.meallist[i].cal+"kcal",180*rp,96*rp+i*90*rp)
        }

        /*for(var i=0;i<this.meallist.length;i++){
                   let img = this.$refs.conf0;
                   img.onload=() =>{
                      console.log(this.path[i])
                      console.log(img.src)
                           ctx.drawImage(img, 70*rp, 57*rp+i*90*rp, 70*rp, 70*rp);
                       }
                   console.log(this.paths[i])
                   ctx.drawImage(this.paths[i],70*rp, 57*rp+i*90*rp, 70*rp, 70*rp)
                   ctx.fillText(this.meallist[i].name,180*rp,71*rp+i*90*rp)
                   ctx.fillText(this.meallist[i].sum+"份",180*rp,96*rp+i*90*rp)
               console.log("wait")
             },*/

        ctx.setStrokeStyle("#000000")
        ctx.setLineWidth(2)
        ctx.rect(0, 0, 300 * rp, 400 * rp + j * 90 * rp) //绘制一个矩形
        ctx.shadowBlur = 7
        ctx.shadowColor = "#808080"
        ctx.shadowOffsetY = 5
        ctx.stroke() //无其他颜色设置，默认用黑色笔画线

        ctx.draw();
      },


      canvasIdErrorCallback: function(e) {
        console.error(e.detail.errMsg)
      },

      //食堂订餐
      bindTimeChange: function(e) {
        this.time = e.target.value
        this.isorder = true
        uni.showModal({
          title: '请您确认',
          content: "取餐时间为" + this.time,
          success: function(res) {
            if (res.confirm) {
              console.log('用户点击确定');
              uni.showToast({
                title: '下单成功',
                duration: 2000
              });
            } else if (res.cancel) {
              console.log('用户点击取消');
            }
          }
        });

      },





      //保存到本地

      save: function() {
        uni.showLoading({
          title: '图片绘制中...',
        })
        var that = this
        uni.canvasToTempFilePath({
          canvasId: 'canvas',
          success: function(res) {
            setTimeout(that.wait, 300);
            uni.hideLoading()
            console.log(res.tempFilePath)
            uni.saveImageToPhotosAlbum({
              filePath: res.tempFilePath,
              success: function(res) {
                uni.showToast({
                  title: '图片已保存'
                })
              }
            })
          }
        })
      },


      wait: function(e) {
        console.log("wait")
      },

      post: function() {
        var menulist = new Array(this.meallist.length)
        for (let i = 0; i < menulist.length; i++) {
          let templist = {
            dish_id: 0,
            mass: 0
            // menu_id: 0
          }
          templist.dish_id = this.meallist[i].id
          // templist.menu_id = this.menuid
          templist.mass = this.meallist[i].sum
          menulist[i] = templist
        }
        console.log(menulist)
        uni.request({
          url: 'https://nkucalorie.top:8000/menu/order/',
          method: 'POST',
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
            'Content-Type': 'application/x-www-form-urlencoded'
          },
          data: {
            // TODO: 问题出在这里？？
            dishes: JSON.stringify(menulist)

          },
          success: (res) => {
            console.log("success ins post: ")
            console.log(res)
          },
          fail: (res) => {
            console.log("fail ins post: ")
            console.log(res)
          },
        })
        uni.setStorage({
          key: 'meal-list',
          data: []
        })
      }

    }
  }
</script>

<style>
  .all {
    display: flex;
    align-content: center;
    justify-content: center;
  }

  .list {
    width: 90%;
    margin-top: 5%;
    margin-bottom: 5%;
    border: #333333 solid 5rpx;
    background-color: #FFFFFF;
  }

  .content {
    display: flex;
    align-content: center;
    justify-content: center;
    margin-bottom: 5%;
  }

  .scroll {
    width: 80%;
  }

  .allbtn {
    width: 100%;
    display: flex;
    justify-content: space-evenly;
    position: fixed;
    bottom: 0rpx;
    background-color: #FFFFFF;
  }

  text {
    font-size: 30rpx;
    font-weight: 500;
    color: "#59453D";
  }

  button {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 72px;
    padding: 0px;
    background-color: rgb(255, 255, 255, 1);
  }

  button::after {
    border: none;
  }

  .button {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .icon {
    width: 70rpx;
    height: 70rpx;
    opacity: 0.8;
  }

  .scrollview>image {
    z-index: -1;
  }

  image {
    width: 180rpx;
    height: 180rpx;
  }

  .title {
    font-size: 40rpx;
    font-weight: 1500;
    text-align: center;
    display: block;
    margin-top: 80rpx;
  }

  .mealinfor {
    display: inline-block;
    position: absolute;
    left: 330rpx;
    line-height: 30rpx;
    //使用inline-block的时候所有的justify和align布局都失效
  }

  .intakeinfor {
    margin-left: 390rpx;
  }

  canvas {
    position: fixed;
    left: -10000rpx;
  }

  .scrollview {
    border-top: #333333 inset 5rpx;
    border-bottom: #333333 outset 5rpx;
    height: 660rpx;
  }

  .listBottomText {
    border-top: #333333 groove 5rpx;
  }

  .date {
    position: absolute;
    right: 50rpx;
  }

  .ordertime {
    display: inline;
  }

  .inorder {
    display: none;
  }
</style>
