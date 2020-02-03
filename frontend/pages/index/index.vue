<template>
  <view class="content">
    
    <view class="text-area">
      <view v-html="str1"></view>
      <MoreInformation></MoreInformation>
      <MinMax></MinMax>
  </view>
  </view>
</template>

<script>
 import MinMax from './min&max.vue'
 import MoreInformation from './more information.vue'
 export default {
   components: {
    MinMax,
    MoreInformation
  },
  data() {
    return {
      title: 'Hello',
      str1:'<span> 点击下方按钮</span><br><span>选择本餐摄入的卡路里数据范围</span><br>',

    };
  },
 
  onLoad() {
      
  },
  methods: {

  },
};
</script>

<style>
 
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: ;
 
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
  display: block;
  justify-content: center;
  position: absolute;
  left:15%;
  top:10%;
  color: '#59453d';
  text-align: left;
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
</style>
