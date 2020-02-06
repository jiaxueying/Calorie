<template>
  <view class="footer">
    <checkbox @click="tap" :checked="select" color="#59453D">全选</checkbox>
    <button plain=true size="mini" @click="">加入菜单</button>
  </view>
</template>

<script>
  export default {
    props: ['select'],
    data() {
      return{
      }
    },
    
    methods: {
      tap:function(){
        this.select=!this.select;
        if(this.select==true)
        this.$emit('chooseAll',true);
        else
        this.$emit('chooseAll',false);
        console.log('hello')
      },
        
        
    }
  }
</script>

<style>
  .footer{
    position: fixed;
    width: 100%;
    height:8%;
    bottom:0px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    font-weight: 500;
    color: #59453D;
    background-color: #FFFFFF;
    border-top: 1px solid #59453D;
    z-index:99;
  }
  checkbox{
    padding-left: 8%;
  }
  button{
    position: relative;
    left:17%
  }
</style>
