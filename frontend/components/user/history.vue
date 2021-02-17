<template>
  <view calss="content">
    <!--    <view class="historyMenu">
      <text style="position: relative;right:35rpx;font-size: 30rpx;">历史菜单</text>
    </view> -->
    <dl v-show="isShow">
      <dt
        class="historyList"
        v-for="(item,index) in list"
        :key="index"
      >
        <view
          class="mealimg"
          @click="showhistorymenu(index)"
        >
          <image
            style="width: 100rpx;height: 100rpx;"
            :src="item.picture"
            mode="aspectFill"
          /></image>
        </view>
        <view
          class="historyInfo"
          @click="showhistorymenu(index)"
        >
          <text style="font-size: 40rpx;font-weight:250;color:#000000;line-height: 40rpx;">{{ item.name }}</text>
          <view style="display: flex; flex-direction: row;justify-content: space-between;">
            <text style="font-size: 25rpx;font-weight: 100;color:#505050;line-height: 40rpx;">{{ item.calorie }}kcal</text>
            <text style="font-size: 25rpx;font-weight: 100;color:#505050;line-height: 40rpx;">{{ item.date }}</text>

          </view>
        </view>
        <image
          src="https://nkucalorie.top:8000/media/static/timg.jpg"
          class="deleteIcon"
          @click="deleteItem(item.id,index)"
          v-if="isdelete"
        /></image></image></image>
      </dt>
    </dl>
    <view
      v-show="!isShow"
      style="font-size: 30rpx;font-weight: 100;color:#505050;text-align: center;margin-top: 20px;"
    >你还没有历史用餐记录哦~</view>
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
        id: -1,
      },
      isdelete: true,
      date: '',
      isShow: false,
    };
  },
  methods: {
    showhistorymenu: function(index) {
      if (this.list[index].id == -1) return;
      uni.request({
        url: 'https://nkucalorie.top:8000/menu/detail/',
        method: 'GET',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        data: {
          menu_id: this.list[index].id,
        },
        success: (res) => {
          console.log(res.data);
          var tempdate = new Date(new Date(this.list[index].date).getTime(this.list[index].date) + 8 * 3600 * 1000);
          this.date = tempdate.toISOString().substr(0, 19);
          this.date = this.date.replace('T', ' ');
          console.log(this.date);
          var data = {
            detail: res.data.data.dishes,
            date: this.date,
          };
          console.log(data);
          uni.setStorage({
            key: 'historymsg',
            data: data,
          });
          uni.navigateTo({
            url: '../../pages/others/mylist',
          });
        },
      });
    },

    deleteItem: function(id, index) {
      console.log(id);
      uni.request({
        url: 'https://nkucalorie.top:8000/menu/delete/',
        method: 'POST',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        data: {
          menu_id: id,
        },
      });
      this.list.splice(index, 1);
      uni.showToast({
        title: '删除成功',
        duration: 2000,
      });
      if (this.list.length == 0) {
        this.isShow = false;
        console.log('default');
      }
    },
  },

  created: function() {
    uni.request({
      url: 'https://nkucalorie.top:8000/menu/query/',
      method: 'GET',
      header: {
        Authorization: 'Token ' + uni.getStorageSync('token'),
      },
      success: (res) => {
        console.log(res.data.data.user_menus);
        this.list = res.data.data.user_menus;
        if (this.list.length == 0) {
          this.isShow = false;
          this.isdelete = false;
        } else {
          this.isShow = true;
          for (let i = 0; i < this.list.length; i++) {
            this.list[i].picture = 'https://nkucalorie.top:8000/media/' + this.list[i].picture;
            console.log(this.list[i].date);
            var str = this.list[i].date.substr(0, 19);
            str = str.replace('T', ' ');
            this.date = str;
            this.list[i].date = str;
            console.log(this.list[i].date);
          }
        }
        console.log(this.list);
      },
      fail: (res) => {
        console.log('history quary fail');
        console.log(res);
      },
    });
  },

};
</script>

<style>
  .content {
    display: flex;
    align-items: center;
  }

  .mealimg {
    width: 100rpx;
    height: 100rpx;
  }

  .historyList {
    display: flex;
    border-radius: 10px;
    margin: 10px;
    overflow: hidden;
  }

  dl {
    margin-top: 10px;
  }

  dt {
    border: #d5c2c6 solid 1rpx;
  }

  .historyInfo {
    display: flex;
    flex-direction: column;
    position: relative;
    width: 550rpx;
    margin-top: 5px;
    margin-left: 10px;
    margin-right: 10px;
    justify-content: space-between;
    /* margin-left: 30rpx; */
  }

  .deleteIcon {
    width: 40rpx;
    height: 40rpx;
    position: relative;
    top: 25rpx;
    opacity: 0.4
  }
</style>
