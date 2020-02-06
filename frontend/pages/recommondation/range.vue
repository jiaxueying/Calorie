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
    <button class="skip" plain=true @click="skip">确定</button>
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
    },
    skip:function(){
      if((this.MAX-this.MIN)<1)
      {uni.showModal({
        title:"请重新选择范围",
        content:"范围的最大值必须大于最小值",
        showCancel:false
      })}
      else if(this.MAX=="MAX")
      {uni.showModal({
        title:"请重新选择范围",
        content:"请点击按钮选择范围",
        showCancel:false
      })}
      else{uni.navigateTo({
        url:"./shake"
      })}
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
.skip{
  border: 1px solid #333333;
  border-radius: 25px;
  margin: 20px;
  height: 30px;
  line-height: 30px;
}

</style>
