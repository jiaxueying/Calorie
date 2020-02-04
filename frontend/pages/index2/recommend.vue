<template>
  <ul>
    <li style="list-style-type: none;" v-for="(item,index) in meals" :key="index">
      <view class="block">
        <div v-html="str1" style="width: 30px;" ></div>
        <image style="width:80px;height:80px" src="../../static/logo.png"></image>
        <view class="data" style="margin-left: 16px;font-size:1.5em;color: #59453D;">
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
</template>

<script>
  export default {
    props: [],
    methods: {          },
     data() {
       return {
         str1:'<input id="input" type="checkbox">',
         meals:[
           {name:'meal1',cal:'200kcal',quantity:'0'},
           {name:'meal2',cal:'300kcal',quantity:'0'}
         ]
       };
     },
     
     }
  
  
</script>

<style>
  .block{
    display:flex;
    margin-top: 10px;
  }
  .calculate{
    margin-left: 25px;
    display: flex;
    vertical-align: middle;
    position: relative;
    top:20px;
    font-size: 1em;
    border: #59453D;
    border-radius: 25px;
  }
  .data{
    margin-top: 5px;
  }
  lable{
    position:relative;
    top:15px
  }
</style>
