<template>
  <view calss="content">
    <view class="historyMenu">
      <text style="position: relative;right:35rpx;font-size: 30rpx;">历史菜单</text>
    </view>
    <dl>
      <dt class="historyList" v-for="(item,index) in list" :key="index">
        <view class="mealimg" @click="showhistorymenu(index)">
          <image style="width: 100rpx;height: 100rpx;" :src='item.picture'></image>
        </view>
        <view class="historyInfo" @click="showhistorymenu(index)">
          <text>{{item.date}}\n</text>
          <!--<text style="font-size: 0.6em;font-weight: 100;color:#505050;line-height: 50rpx;">{{item.calorie}}kcal</text>-->
        </view>
        <image src="https://nkucalorie.top:8000/media/static/timg.jpg" class="deleteIcon" @click="deleteItem(item.id,index)"
          v-if="isdelete"></image>
      </dt>
    </dl>
  </view>
</template>

<script>
  export default {
    data() {
      return {
        list: [],
        replacelist: {
          picture: 'https://nkucalorie.top:8000/media/static/default.jpg',
          calorie: '这里会记录你每餐的就餐卡路里数据,例如100',
          date: '这里会记录你的就餐时间',
          id:-1
        },
        isdelete: true,
        date: "",
      }
    },
    methods: {
      showhistorymenu: function(index) {
        if(this.list[index].id==-1) return
        uni.request({
          url: "https://nkucalorie.top:8000/menu/detail/",
          method: "GET",
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
          },
          data:{
            menu_id:this.list[index].id
          },
          success: (res) => {
            console.log(res.data)
            var tempdate = new Date(this.list[index].date);
            this.date = tempdate.toLocaleDateString();;
            console.log(tempdate)
            var data = {
              detail: res.data.data.dishes,
              date: this.date
            }
            console.log(data)
            uni.setStorage({
              key: 'historymsg',
              data: data,
            })
            uni.navigateTo({
              url: "../../pages/others/mylist"
            });
          }
        })
      },

      deleteItem: function(id, index) {
        console.log(id)
        uni.request({
          url: "https://nkucalorie.top:8000/menu/delete/",
          method: "POST",
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
          },
          data: {
            menu_id: id
          }
        })
        this.list.splice(index, 1);
        uni.showToast({
          title: '删除成功',
          duration: 2000
        })
        if (this.list.length == 0) {
          this.list[0] = this.replacelist
          this.isdelete = false
          console.log('default')
        }
      }
    },

    created: function() {
      uni.request({
        url: "https://nkucalorie.top:8000/menu/query/",
        method: "GET",
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        success: (res) => {
          console.log(res.data.data.user_menus)
          this.list = res.data.data.user_menus
          if (this.list.length == 0) {
            this.list[0] = this.replacelist
            this.isdelete = false
          } else {
            for (let i = 0; i < this.list.length; i++) {
              this.list[i].picture = 'https://nkucalorie.top:8000/media/' + this.list[i].picture
              var str = "";
              for (let j = 0; j < 10; j++) {
                str += this.list[i].date[j];
              }
              this.date = str;
              this.list[i].date = str;
              console.log(this.list[i].date);
            }
          }
          console.log(this.list)
        },
        fail: (res) => {
          console.log("history quary fail")
          console.log(res)
        }
      })
    },


  }
</script>

<style>
  .content {
    display: flex;
    align-items: center;
  }

  .mealimg {
    width: 100rpx;
    height: 100rpx
  }

  .historyMenu {
    border-top: 2px #E8E8E8 solid;
    border-bottom: 2px #E8E8E8 solid;
    color: #59453D;
    height: 80rpx;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    font-size: 0.8em;
    font-weight: 100;
    margin-bottom: 25rpx;
    margin-top: 50rpx;
  }

  .historyList {
    display: flex;
  }

  dl {
    margin-top: 15rpx;
  }

  dt {
    border: #E8E8E8 solid 1px;
  }

  .historyInfo {
    display: flex;
    flex-direction: column;
    position: relative;
    left: 50rpx;
  }

  .deleteIcon {
    width: 40rpx;
    height: 40rpx;
    position: relative;
    left: 400rpx;
    top: 25rpx;
    opacity: 0.4
  }
</style>
