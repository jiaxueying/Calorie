<template>
  <view class="content">
    <view class="more" @click="more"> #点击此处获取更多关于卡路里的信息 </view>
  </view>
</template>

<script>
  export default {
    props: [],
    methods: {
      more() {
        uni.showModal({
          title: '提示',
          content: 'go to baidu' ,
        }).then(data => {
          let [error, res] = data
          if (res.confirm) {
            console.log('用户点击确定');
          } else if (res.cancel) {
            console.log('用户点击取消');
          }
        });
      }
    }
  }
</script>

<style>
  .more{
    font-size: 0.8em;
    color: '#59453d';
    position: relative;
    padding-bottom: 5%;
	  display:flex;
	  justify-content: flex-end;
  }
  
</style>
