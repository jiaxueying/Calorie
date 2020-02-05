<template>
  <view class="content">
    <view class="text-area">
        <text>点击下方按钮\n</text>
        <text>选择本餐摄入的卡路里数据范围</text>
    </view>
    <MoreInformation class="more"></MoreInformation>
	  <calPicker @refresh="change">
		<MinMax :MIN="MIN" :MAX="MAX"></MinMax>
	  </calPicker>
  </view>
</template>

<script>
 import MinMax from '../../components/recommodation/min&max.vue'
 import MoreInformation from '../../components/recommodation/moreInformation.vue'
 import calPicker from '../../components/recommodation/calPicker.vue'
 export default {
   components: {
    MinMax,
    MoreInformation,
    calPicker
  },
  data() {
    return {
	  MIN:'MIN',
	  MAX:'MAX'
    };
  },
 
  onLoad() {
      
  },
  methods: {
    change:function(cal,index){
      this.MIN=cal[0][index[0]];
      this.MAX=cal[1][index[1]];
    }
  },
};
</script>

<style>
 
.content {
  display:flex;
  flex-direction: column;
  align-items: center;
  justify-content: baseline;
}

.text-area {
  padding-top:15%;
  color: '#59453d';
}

.title {
  font-size: 36rpx;
  color: #8f8f94;
}
text{
  font-size: 1.2em;
  font-weight: 400;
}
.more{
}


</style>
