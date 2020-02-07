<template>
  <view class="content">
    <image
      class="logo"
      src="/static/logo.png"
    />
    <view class="text-area">
      <text class="title">
        {{ title }}
      </text>
    </view>
    <button
      type="primary"
      open-type="getUserInfo"
      @getuserinfo="onGetUserInfo"
    >
      授权
    </button>
    <button
      type="primary"
      open-type="openSetting"
    >
      权限设置
    </button>
    <button
      type="primary"
      @click="test"
    >
      test
    </button>
    <button
      type="primary"
      @click="openSearch"
    >
      search
    </button>
  </view>
</template>

<script>
import { backendUrl, request } from '@/common/helper.js';
export default {
  data() {
    return {
      title: 'Hello',
      emmm: 123,
    };
  },
  onLoad() {

  },
  methods: {
    onGetUserInfo(userInfo) {
      const nickName = userInfo.detail.userInfo.nickName;
      uni.login({
        provider: 'weixin',
      }).then(loginRes => {
        const [loginError, loginData] = loginRes;
        console.assert(loginError === null);
        const loginCode = loginData.code;
        uni.request({
          url: backendUrl + '/user/login/',
          data: {
            code: loginCode,
            name: nickName,
          },
          method: 'POST',
        }).then(backendRes => {
          const [backendError, backendData] = backendRes;
          console.assert(backendError === null);
          const token = backendData.data.token;
          uni.setStorageSync('token', token);
          console.log('token: ', token);
        });
      });
    },
    test() {
      request('/dish/key_query/', 'GET', {
        key_word: '菜',
      }).then(res => {
        console.log(res);
      });
    },
    openSearch() {
      wx.navigateTo({
        url: '../search/search',
      });
    },
  },
};
</script>

<style>
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.logo {
  height: 200rpx;
  width: 200rpx;
  margin-top: 200rpx;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 50rpx;
}

.text-area {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
</style>
