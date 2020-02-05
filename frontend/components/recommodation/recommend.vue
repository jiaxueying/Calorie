<template>
  <view>
    <view class="title">
      <div class="text1">今日推荐</div>
    </view>    

  <dl>
    <dt  v-for="(item,index) in meals" :key="index">
      <view class="block">
        <checkbox color="#59453D"></checkbox>
        <image style="width:85px;height:85px;" :src="item.src"></image>
        <view class="data">
          <p>{{item.name}}</p>
          <p style="font-size:0.5em;color: #59453D;">{{item.cal}}</p>
        </view>
        <view class="calculate">
          <uni-number-box :min="0" :max="9"  @change="quantityChange"></uni-number-box>
        </view>
      </view>

    </dt>
  </dl>
  <view class="foot">
    
  </view>
  </view>
</template>

<script>
  import uniNumberBox from"@/components/uni-ui/uni-number-box/uni-number-box.vue"
  
  export default {
    components:{
      uniNumberBox
    },
    props: [],
    methods: {    
      quantityChange(){
      }
    },
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
    background: rgba(219,207,202,.3); 
    height:50px;
    color:#59453d;
    display: flex;
    flex:2; 
    justify-content: center;
    align-items: center;
  }
 
  .block{
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    justify-content: space-evenly;
    align-items: center;
    
  }
  .calculate{
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 1em;
    border: #59453D;
  }
  .data{
    font-weight: 800;
    font-size:1.8em;
    color: #59453D;
  }
  lable{
    position:relative;
    top:15px
  }
  .text1{
    font-weight:800;
    color:#59453d;
  }
</style>
