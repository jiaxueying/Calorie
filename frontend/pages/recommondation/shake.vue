<template>
	<view class="content">
		<image src="../../static/shake.png" class="img"></image>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		onLoad(){
			uni.onAccelerometerChange(function(a){
			  let b=a.x*a.y*a.z
			  console.log(b)
			  if(b>0.5||b<-0.5)
			  {
			    console.log("success")
          uni.stopAccelerometer()
			    uni.redirectTo({url:"./list"})
			  }
			})
		},
    onUnload() {
      uni.stopAccelerometer()
    },
		methods: {
			
		}
	}
</script>

<style>
.content{
  display: flex;
  margin-top: 40%;
  height: 268px;
}
.img{
   width: 320px;
   height: 268px;
   margin: 0 auto;
}
</style>
