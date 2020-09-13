<template>
  <view>
    <view class="title">后台管理人员登陆</view>
    <view>
      <p>账号</p>
      <input type="text" v-model="form.user" class="input">
      <p>密码</p>
      <input type="password" v-model="form.password" class="input">
      <button type="primary" @click="submit">提交</button>
    </view>
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
                uni.navigateTo({
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
    width: 750rpx;
    text-align: center;
  }
  .input {
    border: solid 1px black;
    border-radius: 2px;
    margin: 30rpx 10rpx;
    padding: 2px 1px;
  }
</style>
