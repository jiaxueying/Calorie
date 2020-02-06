<template>
  <view>
    <view class="title">
      <div class="text1">今日推荐</div>
    </view>    
  <dl>
  <scroll-view scroll-y="true" scroll-top="200">
    <dt  v-for="(item,index) in meals" :key="index" >
      <view class="block">
        <checkbox color="#59453D" :checked="item.checked" @click="weatherAll(index)"></checkbox>
        <image style="width:85px;height:85px;" :src="item.src"></image>
        <view class="data">
          <p>{{item.name}}</p>
          <p style="font-size:0.5em;color: #59453D;">{{item.cal}}</p>
        </view>
        <view class="calculate">
          <uni-number-box :min="0" :max="9"></uni-number-box>
        </view>
      </view>
    </dt>
 </scroll-view>
 <div style="height:100px">
   {{           }} 
 </div>
 </dl>
  <view class="foot">
      <Footer @chooseAll="all" :select="select"></Footer>
  </view>
  </view>
</template>

<script>
  import uniNumberBox from"@/components/uni-ui/uni-number-box/uni-number-box.vue"
  import Footer from '../../components/recommodation/footer.vue'
  export default {
    components:{
      uniNumberBox,
      Footer,
    },
    props: [],
    methods: {    
      all:function(select){
        console.log('hi');
        for(var i=0;i<this.meals.length;i++)
        {
          this.meals[i].checked=select;
        }
        this.select=select
      },
      weatherAll:function(index){
        var flag=0;
        this.meals[index].checked=true
        console.log(index)
        for(var i=0;i<this.meals.length;i++){
         if(this.meals[i].checked==true)
          flag++
        }
        if(flag==this.meals.length) this.select=true;
      }
    },
     data() {
       return {
         select:false,
         meals:[
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/shrimp.png', name:'meal2',cal:'300kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
           
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
