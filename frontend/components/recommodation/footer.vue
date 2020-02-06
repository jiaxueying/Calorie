<template>
  <view>
  <view class="footer">
    <checkbox @click="tap" :checked="select" color="#59453D">
      <text>全选</text>
    </checkbox>
    <button plain=true size="default" @click="add">
      <text>加入菜单</text>
    </button>
  </view>
  <popup style="z-index: 3;left: 0;top: 0;position: absolute;" v-if="isshow"></popup>
  </view>
</template>

<script>
  import popup from "./popup.vue"
  export default {
    components:{
      popup
    },
    props: ['select'],
    data() {
      return{
        isshow:false
      }
    },
    
    methods: {
      tap:function(){
        this.select=!this.select;
        if(this.select==true)
        {this.$emit('chooseAll',true)}
        else
        {this.$emit('chooseAll',false)}
        console.log('hello')
      },
      add:function(){
        this.$emit('sub')
        this.isshow=true
      }
        
    }
  }
</script>

<style>
  .footer{
    position: fixed;
    height:8%;
    width:752rpx;
    bottom:0px;
    display:flex;
    justify-content:flex-end;
    align-items:center;
    background-color: #FFFFFF;
    border-top: 1rpx solid #59453D;
    z-index:2;
  }
  checkbox{
    margin-left: 17.5rpx;
  }
  button{
    margin-right:25rpx;
  }
  text{
    font-weight: 600;
    font-size:1em;
    color: #59453D;
  }
</style>
