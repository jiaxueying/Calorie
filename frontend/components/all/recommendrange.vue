<template>
  <view class="content">
    <text>本日推荐的卡路里范围为{{min}}-{{max}}cal</text>
  </view>
</template>

<script>
  export default {
    props:[],//子组件
    	data() {
   		return {
         min:'',
         max:''
   		}
   	},
     methods:{
      
     },
     created() {
       uni.getStorage({
         key:'range',
         success: (res) => {
           this.min=res.data[0]
           this.max=res.data[1]
         }
       })
     }
   }
</script>

<style>
  .content{
    display: flex;
    border:#000000 1rpx solid;
    justify-content: center;
    font-size: 50rpx;
    font-weight: 400;
    }
    text{
      line-height: 200%;
      color:#505050;
    }
</style>
