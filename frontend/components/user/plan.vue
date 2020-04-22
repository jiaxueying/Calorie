<template>
  <view class="content">
      <view class="plan">近期是否有减肥计划</view>
      <view class="buttons">
           <view :class="{chosen:choice,button:true}" @click="Switch(true)">有</view>
          <view :class="{chosen:!choice,button:true}" @click="Switch(false)">无</view>
      </view>
      <view class="input" v-if="choice">
          <view class="input1">
            <text>目标体重:</text><input 
                    :value="targetweight" 
                    type="number" 
                    :placeholder="targetweight" 
                    maxlength="3" 
                    @input="set"/><text>KG</text>
          </view>
          <view class="input2">
            <text>所用天数:</text><input
                    :value="day"
                    type="number"
                    maxlength="4"
                    :placeholder="day"
                    @input="calculation"/><text>Day</text>
          </view>
      </view>
      <view class="tip" v-if="!choice">恰如其分，就是最好的你</view>
  </view>
</template>

<script>
  export default{
    props:['targetweightrec','plan','weight'],//子组件
    data(){
          return{
          choice:true,
          targetweight:999,
          rate:0,
          day:60,
          string:"",
            }
          },
    methods:{
      
      Switch:function(choi){
          this.choice=choi
          if(choi==false){this.string="暂无计划"}
          else{this.string="有计划"}
          let data={
              targetweight:this.targetweight,
              string:this.string,
              rate:0
              }
          this.$emit('input',data)
      },
      
      //设置目标体重
      set:function(event){
          if(event.detail.value!=""){
              this.targetweight=event.detail.value
              let data={
                  targetweight:this.targetweight,
                  string:this.string,
                  rate:this.rate
                  }
              this.$emit('input',data)
          }
      },
      
      //计算减重速率
      calculation:function(event){
          if(event.detail.value!=""){
              this.rate=(this.targetweight-this.weight)/event.detail.value
              let data={
                  targetweight:this.targetweight,
                  string:this.string,
                  rate:this.rate
                  }
              this.$emit('input',data)  
        }
      },
      
      
    },
      
      //组件创建函数
    created:function(){
        this.targetweight=this.targetweightrec
        if(this.plan=="暂无计划"){this.choice=false}
        else{this.choice=true}
      }
  }
</script>

<style>
  .content{
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .plan{
    color: #505050;
    font-size:60rpx;
    margin-top: 120rpx;
  }
  .button{
    font-size: 40rpx;
    text-align: center;
    width: 250rpx;
    height: 80rpx;
    line-height: 80rpx;
    margin: 20rpx;
    border: 2px #D2A9A9 solid;
    color: #d2a9a9;
    border-radius: 12rpx;
	  background-color: #FFFFFF;
  }
  .chosen{
    color: #ffffff;
    background-color: #D2A9A9;
  }
  .input{
    color:#d2a9a9;
    font-size: 45rpx;
    margin-top: 10rpx;
    animation: pushup 1s;
  }
  .input1{
    display: block;
    margin-top: 10rpx;
    margin-bottom: 10rpx;
  }
  .input2{
    display: block;
  }
  .tip{
    font-size: 45rpx;
    color: #000000;
    margin-top: 10rpx;
    animation: pushup 1s;
  }
  @keyframes pushup{
    from{margin-top: 50rpx;opacity: 0;}
    to{margin-top: 10rpx;}
  }
  .buttons{
    display: flex;
  }
  input{
    width: 150rpx;
    margin-top: 8rpx;
    border-bottom: #C09C79 4rpx solid;
    display: inline-block;
  }
  text{
    display: inline-block;
  }
</style>
