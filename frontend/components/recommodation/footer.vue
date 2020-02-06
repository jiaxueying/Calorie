<template>
  <view>
  <view class="footer">
    <checkbox @click="tap">全选</checkbox>
    <button plain=true size="mini" @click="add">加入菜单</button>
  </view>
  <popup style="position: absolute;left: 0;top: 0;z-index: 3;" v-if="isshow"></popup>
  </view>
</template>

<script>
  import popup from "./popup.vue"
  export default {
    components:{
      popup
    },
    data(){
      return{
        isshow:false
      }
    },
    props: [],
    methods: {
      tap:function(){
        this.$emit('chooseAll');
        console.log('hello')
      },
	  add:function(){
		  this.isshow=true
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
    z-index: 2;
  }
  checkbox{
    padding-left: 8%;
  }
  button{
    position: relative;
    left:17%
  }
</style>
