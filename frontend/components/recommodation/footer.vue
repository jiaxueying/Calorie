<template>
  <view class="footer">
    <checkbox @click="tap">全选</checkbox>
    <button plain=true size="mini" @click="">加入菜单</button>
  </view>
</template>

<script>
  export default {
    props: [],
    methods: {
      tap:function(){
        this.$emit('chooseAll');
        console.log('hello')
      }
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
  }
  checkbox{
    padding-left: 8%;
  }
  button{
    position: relative;
    left:17%
  }
</style>
