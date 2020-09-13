<template>
  <view class="content">
      <!--上方文本-->
      <view class="text-area">
          <text>点击下方按钮\n</text>
          <text>选择本餐摄入的卡路里数据范围</text>
          <view  class="more">
              <text @click="more"> #点击此处获取更多关于卡路里的信息</text>
          </view>
      </view>
	  <!--min max按键-->
      <calPicker @refresh="change">
          <view class="minmax"  :MIN="MIN" :MAX="MAX">
                <button size="mini" style="background-color: #59453D;color: #FFFFFF;">{{MIN}}</button>
                <text class="and">&</text>
                <button size="mini">{{MAX}}</button>
         </view>
      </calPicker>
      <button class="skip" plain=true @click="skip">确定</button>
  </view>
</template>

<script>
 import calPicker from '../../components/recommodation/calPicker.vue'
 export default {
   components: {
    calPicker
  },
  data() {
    return {
	  MIN:"MIN",
	  MAX:"MAX"
    };
  },
 
  onLoad() {
      
  },
  methods: {
	//获取更多
    more:function() {
        uni.showModal({
          title: "当然是关注公众号啦",
          content: "'粟的工具人'欢迎您来" ,
        }).then(data => {
          let [error, res] = data
          if (res.confirm) {
            console.log('用户点击确定');
          } else if (res.cancel) {
            console.log('用户点击取消');
          }
        });
      },
      change:function(cal,index){
        this.MIN=cal[0][index[0]];
        this.MAX=cal[1][index[1]];
        let that=this
		//把min和max的值存到缓存中
        uni.setStorage({
            key: 'minmax',
            data: [this.MIN,this.MAX],
            success: function () {
                console.log('success');
            }
        });
		/*
        uni.getStorage({
            key: 'minmax',
            success: function (res) {
                console.log(res.data);
            }
        });*/
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
        else{uni.redirectTo({
          url:"./shake"
        })}
      }
    },
  };
</script>

<style>
 
.content {
  position: absolute;
  top:0px;
  bottom:0px;
  left:0px;
  right:0px;
  display:flex;
  flex-direction:column;
  align-items: center;
}

.text-area {
  padding-top:35%;
  font-weight:800;
  font-size: 1.4em;
  color: #59453D;
}

.more{
  font-size: 0.6em;
  font-weight: 300;
  display: flex;
  justify-content: flex-end;
  color: '#59453d';
}
 .minmax{
    margin-bottom: 15%;
    margin-top: 40%;
    border:1px solid #59453d;
    border-radius: 15px;
    width:200px;
    display:inline-flex;
    font-weight: 400;
    font-size: 18px;
    
  }
  button{
    line-height: 30px;
    margin-top: 5px;
    margin-bottom: 5px;
    width:70px;
  }
  .and{
    margin-top: 5px;
    margin-bottom: 5px;
  }
.skip{
  border: 1px solid #333333;
  border-radius: 25px;
  margin:  20px;
  height: 30px;
  line-height: 30px;
  font-size: 0.7em;
  width:80px;
}
</style>
