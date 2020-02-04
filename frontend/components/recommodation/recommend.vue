<template>
  <view>
    <view class="title">
    <div class="text" style="opacity: 0.4;">今日推荐</div>
    </view>
    <div class="text1">今日推荐</div>
  <ul>
    <li style="list-style-type: none;" v-for="(item,index) in meals" :key="index">
      <view class="block">
        <checkbox color="#59453D" style="position:relative;top:23px;right:10px"></checkbox>
        <image style="width:80px;height:80px" :src="item.src"></image>
        <view class="data">
          <p>{{item.name}}</p>
          <p style="font-size:0.5em;color: #59453D;">{{item.cal}}</p>
        </view>
        <view class="calculate">
         <p @click="item.quantity--" v-model="item.quantity" >-</p> 
         {{item.quantity}}份
         <p @click="item.quantity++" v-model="item.quantity">+</p>
        </view>
      </view>

    </li>
  </ul>
  <view class="foot">
    
  </view>
  </view>
</template>

<script>
  export default {
    props: [],
    methods: {          },
     data() {
       return {
         str1:'<input id="input" type="checkbox">',
         meals:[
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0'},
           {src:'../../static/shrimp.png', name:'meal2',cal:'300kcal',quantity:'0'}
         ],
       };
     },
     
     }
  
  
</script>

<style>
  .title{
    background-color:#dbd0ca;
    color:#59453d;
    display: flex;
    flex:2; 
    line-height: 50px;
    opacity: 0.5;
  }
  .text{
    font-weight:800;
    position:relative;
    left: 40%;
  }
  .block{
    display:flex;
    margin-top: 10px;
    
  }
  .calculate{
    margin-left: 25px;
    display: flex;
    vertical-align: middle;
    position:relative;
    top:20px;
    font-size: 1em;
    border: #59453D;
    border-radius: 25px;
  }
  .data{
    margin-top: 5px;
    margin-left: 16px;
    font-weight: 800;
    font-size:1.5em;
    color: #59453D;
  }
  lable{
    position:relative;
    top:15px
  }
  .text1{
    font-weight:800;
    position:absolute;
    left: 40%;
    top:12px;
    color:#59453d;
  }
</style>
