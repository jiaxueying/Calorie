<template>
  <view class="page">
    <image :src="'../../static/cook.png'" style="width: 100px;height: 100px; text-align: center;"></image>
    <view class="title">后台管理人员登陆</view>
    <view class="form">
      <view style="display: flex; flex-direction: row; justify-content: space-around; margin-top: 20px;">
        <label style="vertical-align: middle">账号</label>
        <input type="text" v-model="form.user" class="input">
      </view>
      <view style="display: flex; flex-direction: row; justify-content: space-around; margin-top: 20px;">
        <label style="vertical-align: middle">密码</label>
        <input type="password" v-model="form.password" class="input">
      </view>
      <button @click="submit" class="button">提交</button>
    </view>
    
  </view>
</template>

<script>
  export default {
    data() {
      return {
        form: {
          user: 'nkucalorie',
          password: 'nkucalorie123456',
        }
      }
    },
    methods: {
      submit: function() {
        uni.request({
          url: "https://calorie.liyangpu.com:8003/administrate/login/",
          method: "POST",
          header: {
            Authorization: "Token " + uni.getStorageSync("token")
          },
          data: {
            account: this.form.user,
            password: this.form.password,
          },
          success: (res) => {
            if (res.statusCode == 200) {
              console.log("administrator login successfully!"),
                console.log(res)
              uni.setStorageSync('adtoken', res.data.data.token)
              var adtoken = uni.getStorageSync('adtoken')
              console.log("set storage success!" + adtoken)
              uni.redirectTo({
                url: '../index/index'
              })
            } else {
              uni.showToast({
                title: '账号或密码错误',
                icon: 'none'
              })
            }
          }
        }) //
      },
    },
  }
</script>

<style>
  .title {
    font-weight: 800;
    font-size: 40rpx;
    text-align: center;
    padding-left: 20rpx;
    padding-right: 20rpx;
  }

  .input {
    border: solid 1px #D3D3D3;
    border-radius: 5px;
    /* margin: 30rpx 10rpx; */
    /* padding: 2px 1px; */
    vertical-align: middle;
    margin-left: 10px;
    text-align: center;
  }

  .page {
    padding-top: 20%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  .form {
    margin: 20px;
    /* border: 1px solid #ceaea1; */
    display: flex;
    flex-direction: column;
    justify-content: left;
  }

 .button {
    width: 30%;
    /* height: 30px; */

    background-color: #d1b0a3; 
    border-radius: 10px;
    font-size: 13px;
    text-align: center;
    align-items: center;
    vertical-align: middle;
    padding: 0;
    margin-right: 0;
    margin-top: 10px;
  }
</style>
