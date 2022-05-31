<template>
  <view>
    <scroll-view scroll-y="true" style="height:1260rpx">
      <view class="all">
        <!--my list 的菜单部分-->
        <view class="list">
          <text class="title">我的菜单</text>
          <view class="content">
            <view class="scroll">
              <!--菜单可滚动部分-->
              <scroll-view scroll-y="true" class="scrollview">
                <view style="height:5rpx; margin-top: 10px;"></view>
                <view v-for="(srcitem,i) in path">
                  <image :src="srcitem" ref="conf0" @load="onload" mode="aspectFill"></image>
                  <view class="mealinfor">
                    <text> {{meallist[i].name}}\n</text>
                    <text> {{meallist[i].sum}} 份\n</text>
                    <text> {{meallist[i].calorie}} kcal</text>
                  </view>
                </view>
              </scroll-view>
              <!--菜单下方文本部分-->
              <view class="energy">
                <text>本餐共摄入{{msg}}kcal</text>
              </view>
              <view class="energy">
                <text style="color:#ababab;">{{date}}</text>
              </view>
            </view>
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
        <image class="icon" src="../../static/friend.png" style=""></image><br>
        <view style="color: #909090; font-size: 20rpx;width: 200rpx;"><text>发送给朋友</text></view>
      </button>
      <button @click="save" class="button">
        <image class="icon" src="../../static/download.png"></image><br>
        <view style="color: #909090; font-size: 20rpx;width: 200rpx;"><text>保存到手机</text></view>
      </button>
    </view>
  </view>
</template>

<script>
  import {backendUrl} from '@/common/helper.js'
  
  export default {

    //发送给朋友的图标
    onShareAppMessage(res) {
      if (res.from === 'button') {
        console.log(res.target)
      }
      return {
        title: '粟',
        path: '/pages/index/newindex?url='
      }
    },

    data() {
      return {
        menuid: "",
        msg: 0,
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

    methods: {
      onload: function() {
        
        this.onloadtime++
        if (this.onloadtime == this.meallist.length) {
          setTimeout(this.draw, 500);
          console.log("to draw !")
          // 旧 post 的位置
          // if (this.ispost) this.post();
        }
      },
      
      show() {
        return new Promise((resolve, reject) => {
          uni.getStorage({
            key: 'historymsg',
            success: () => {
              var data = uni.getStorageSync('historymsg')
              console.log(data)
              this.date = data.date;
              console.log(data.date)
              console.log(data.detail[0].picture)
              for (var i = 0; i < data.detail.length; i++) {
                this.meallist[i] = {}
                this.meallist[i].picture = data.detail[i].picture
                this.meallist[i].calorie = data.detail[i].calorie
                this.msg += this.meallist[i].calorie
                console.log('backendUrl')
                console.log(backendUrl)
                this.path.push(backendUrl + data.detail[i].picture)
                this.getinfo(i)
                this.meallist[i].name = data.detail[i].name
                this.meallist[i].sum = data.detail[i].mass
                console.log(this.meallist[i])
              }
              this.ispost = false
              console.log("from history list~");
              uni.removeStorageSync('historymsg');
              resolve('success');
            },
            fail: () => { //未获取到历史菜单，从购物车进入
              reject('error in show');
              var time = new Date(new Date().getTime() + 8 * 3600 * 1000);
              this.date = time.toISOString().substr(0, 19)
              this.date = this.date.replace('T', ' ')
              console.log(this.date)
              this.menuid = uni.getStorageSync('menuid');
              var tempmeallist = uni.getStorageSync('meal-list');
              console.log(tempmeallist);

              
              for (var i = 0, j = 0; i < tempmeallist.length; i++) {
                if (tempmeallist[i].sum != 0) {
                  this.meallist[j] = tempmeallist[i];
                  this.meallist[j].calorie = this.meallist[i].cal * this.meallist[i].sum
                  this.msg += this.meallist[j].calorie
                  this.path.push(backendUrl + this.meallist[j].picture);
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
          src: backendUrl + this.meallist[i].picture,
          success: (res) => {
            this.paths.push(res.path)
            console.log("get one picture!")
          }
        })
      },

      get(i) {
        return new Promise((resolve, reject) => {
          uni.getImageInfo({
            src: backendUrl+ this.meallist[i].picture,
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
        //this.meallist = uni.getStorageSync('meal-list')
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
        ctx.fillText("本餐共摄入", 180 * rp, 340 * rp + j * 90 * rp)
        var w = ctx.measureText(this.msg + "kcal").width
        ctx.fillText(this.msg + "kcal", 200 * rp + 35 - w, 360 * rp + j * 90 * rp)
        ctx.fillText("#粟", 3 * rp, 390 * rp + j * 90 * rp)
        var metrics = ctx.measureText(this.date).width
        console.log(metrics)
        ctx.fillText(this.date, 300 * rp - metrics * 1.5, 390 * rp + j * 90 * rp)

        for (var i = 0; i < this.meallist.length; i++) {
          ctx.drawImage(this.paths[i], 70 * rp, 57 * rp + i * 90 * rp, 70 * rp, 70 * rp)
          ctx.fillText(this.meallist[i].name, 180 * rp, 71 * rp + i * 90 * rp)
          ctx.fillText(this.meallist[i].sum + "份", 180 * rp, 94 * rp + i * 90 * rp)
          ctx.fillText(this.meallist[i].calorie + "kcal", 180 * rp, 117 * rp + i * 90 * rp)
        }

        // for (var i = 0; i < this.meallist.length; i++) {
        //   console.log("refs: ")
        //   console.log(this.$refs)
        //   let img = this.$refs.conf0;
        //   img.onload = () => {
        //     console.log(this.path[i])
        //     console.log(img.src)
        //     ctx.drawImage(img, 70 * rp, 57 * rp + i * 90 * rp, 70 * rp, 70 * rp);
        //   }
        //   console.log(this.paths[i])
        //   ctx.drawImage(this.paths[i], 70 * rp, 57 * rp + i * 90 * rp, 70 * rp, 70 * rp)
        //   ctx.fillText(this.meallist[i].name, 180 * rp, 71 * rp + i * 90 * rp)
        //   ctx.fillText(this.meallist[i].sum + "份", 180 * rp, 96 * rp + i * 90 * rp)
        //   console.log("wait")
        // }

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
        this.draw()
        uni.showLoading({
          title: '图片绘制中...',
        })
        var that = this
        let tmpTimeout = setTimeout(() => {
          uni.canvasToTempFilePath({
            canvasId: 'canvas',
            success: function(res) {
              // this.setTimeout(that.wait, Z900);
              console.log(res.tempFilePath)
              uni.saveImageToPhotosAlbum({
                filePath: res.tempFilePath,
                success: function(res) {
                  uni.hideLoading()
                  uni.showToast({
                    title: '图片已保存'
                  })
                },
                fail: function(err) {
                  console.log(err)
                  uni.showToast({
                    title: '图片保存失败'
                  })
                }
              })
            }
          })
          clearTimeout(tmpTimeout)
        }, 1000)
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
          url: backendUrl+'/menu/order/',
          method: 'POST',
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
          },
          data: {
            dishes: JSON.stringify(menulist)
          },
          success: (res) => {
            console.log("success in post: ")
            console.log(res)
          },
          fail: (res) => {
            console.log("fail in post: ")
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
    width: 80%;
    margin-top: 10%;
    margin-bottom: 10%;
    /* padding-top: 10px; */
    border: #333333 solid 2rpx;
    border-radius: 10px;
    background-color: #FFFFFF;
  }

  .content {
    display: flex;
    align-content: center;
    justify-content: center;
    margin-bottom: 5%;
    padding-top: 10px;
  }

  .scroll {
    width: 80%;
  }

  .allbtn {
    width: 100%;
    display: flex;
    justify-content: space-around;
    position: fixed;
    bottom: 0rpx;
    background-color: #ffffff;
    /* border-top: #000000 solid 1px; */
    padding-top: 20rpx;
    /* box-shadow: #a7a7a7 0 -1px 1rpx; */
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
    width: 200rpx;
    padding: 0px;
    background-color: rgb(255, 255, 255, 1);
  }

  button::after {
    border: none;
  }

  .button {}

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
    border-radius: 15rpx;
  }

  .title {
    font-size: 40rpx;
    font-weight: 1500;
    text-align: center;
    display: block;
    margin-top: 30rpx;
    margin-bottom: 10rpx;
  }

  .mealinfor {
    display: inline-block;
    position: absolute;
    left: 330rpx;
    /* line-height: 50rpx; */
    margin-top: 15px;
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
    border-top: #a5a5a5 dashed 1rpx;
    border-bottom: #a5a5a5 dashed 1rpx;
    height: 660rpx;
  }

  .listBottomText {
    border: #333333 solid 2rpx;

  }

  .date {
    position: relative;
    margin-right: 5rpx;
    /* right: 50rpx; */

  }

  .ordertime {
    display: inline;
  }

  .inorder {
    display: none;
  }

  .energy {
    text-align: right;
    width: 100%;
  }
</style>
