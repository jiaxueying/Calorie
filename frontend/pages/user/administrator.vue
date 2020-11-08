<template>
  <view class="page">
    <view class="title">后台管理人员登陆</view>
    <view class="form">
      <p>账号</p>
      <input type="text" v-model="form.user" class="input">
      <p>密码</p>
      <input type="password" v-model="form.password" class="input">
    </view>
      <button type="default" @click="submit">提交</button>
  </view>
</template>

<script>
	export default {
		data() {
			return {
        form:{
          user:'nkucalorie',
          password:'nkucalorie123456',
        }
			}
		},
		methods: {
      submit:function(){
        uni.request({
            url:"https://nkucalorie.top:8000/administrate/login/",
            method:"POST",
            header:{
              Authorization:"Token "+uni.getStorageSync("token")
            },
            data:{
              account:this.form.user,
              password:this.form.password,
            },
            success: (res) => {
              if(res.statusCode==200)
              {
                console.log("administrator login successfully!"),
                console.log(res)
                uni.setStorageSync('adtoken',res.data.data.token)
                var adtoken=uni.getStorageSync('adtoken')
                console.log("set storage success!"+adtoken)
                uni.redirectTo({
                  url:'../index/index'
                })
              }
              else
              {
                uni.showToast({
                  title:'账号或密码错误',
                  icon:'none'
                })
              }
            }
      })//
      },
    },
  }
</script>

<style>
  .title {
    font-weight: 800;
    font-size:40rpx;
    text-align: center;
    padding-left: 20rpx;
    padding-right: 20rpx;
  }
  .input {
    border: solid 1px #D3D3D3;
    border-radius: 5px;
    margin: 30rpx 10rpx;
    padding: 2px 1px;
  }
  .page{
    padding-top: 20%;
  }
  .form{
    margin-top: 20rpx;
    margin-left: 20rpx;
    margin-right: 20rpx;
    border-top: 2px solid #000000;
    border-bottom: 2px solid #000000;
  }
  button{
    position: fixed;
    bottom: 0;
    width: 100%;
  }
</style>
