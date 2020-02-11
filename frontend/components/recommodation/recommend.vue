<template>
  <view>
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
 <div style="height:100px"></div>
 </dl>
 <view class="footer">
   <checkbox @click="tap" :checked="select" color="#59453D" class="checkbox">
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
  import recrange from '../../components/all/recommendrange.vue'
  import uniNumberBox from"@/components/uni-ui/uni-number-box/uni-number-box.vue"
  import popup from "./popup.vue"
  export default {
    components:{
      uniNumberBox,
      popup,
      recrange,
    },
    props: [],
    methods: {    
      
      weatherAll:function(index){
        this.meals[index].checked=!this.meals[index].checked
        console.log(index)
         if(this.meals[index].checked==true)
         {this.flag+=1}
         else{this.flag-=1}
        if(this.flag==this.meals.length)
        {
          this.select=true
        }
        else {this.select=false}
      },
      add:function(){
        this.isshow=true
        
        
        
        
      },
      tap:function(){
        this.select=!this.select
        for(let i=0;i<this.meals.length;i++)
        {this.meals[i].checked=this.select}
        if(this.select==true)
        {this.flag=this.meals.length}
        else{this.flag=0}
      }
      
    },
     data() {
       return {
         isshow:false,
         flag:0,
         select:false,
         meals:[
           {src:'../../static/shrimp.png', name:'meal2',cal:'300kcal',quantity:'0',checked:false},
           {src:'../../static/chocolate.png', name:'meal1',cal:'200kcal',quantity:'0',checked:false},
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
  .checkbox{
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
