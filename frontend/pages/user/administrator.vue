<template>
  <view>
    <view>后台管理人员登陆</view>
    <view>
      <p>账号</p>
      <input type="text" v-model="form.user">
      <p>密码</p>
      <input type="password" v-model="form.password"/>
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
              console.log("administrator login successfully!"),
              console.log(res)
              uni.setStorageSync('adtoken',res.data.data.token)
              var adtoken=uni.getStorageSync('adtoken')
              console.log("set storage success!"+adtoken)
              uni.navigateTo({
                url:'../index/index'
              })
            },
            fail:()=>{
              console.log("login fail!")
            }
        
      })//
      },
    },
  }
</script>

<style>
</style>
