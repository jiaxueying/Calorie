<template>
  <view>
  <dl>
  <scroll-view scroll-y="true" scroll-top="200">
    <dt  v-for="(item,index) in meals" :key="index" >
      <view class="block">
        <checkbox color="#59453D" :checked="item.checked" @click="weatherAll(index)"></checkbox>
        <image style="width:85px;height:85px;" :src="'https://cal.liyangpu.com:8000'+item.picture"></image>
        <view class="data">
          <p>{{item.name}}</p>
          <p style="font-size:0.5em;color: #59453D;">{{item.calorie}}</p>
        </view>
        <view class="calculate">
          <uni-number-box :min="0" :max="9"  @change="addproperty($event,index)"></uni-number-box>
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
     <text >加入菜单</text>
   </button>
 </view>
 
 <popup style="z-index: 3;left: 0;top: 0;position: absolute;" v-if="isshow"></popup>
 </view>
</template>

<script>
  import recrange from "../../components/all/recommendrange.vue"
  import uniNumberBox from"@/components/uni-ui/uni-number-box/uni-number-box.vue"
  import popup from "./popup.vue"
  export default {
    created(){
        let value = uni.getStorageSync("minmax");//从缓存获取本餐卡路里推荐范围
        let userid= uni.getStorageSync("userid");//从缓存获取userid
        //向后端发送请求
        uni.request({
      	 url:"https://cal.liyangpu.com:8000/dish/calorie_query/",
    	   method:"GET",
    	   data:{
            user_id:this.userid,
    		    min_calorie:0,
    		    max_calorie:10000
    	        },
         header:{
              Authorization:'Token '+uni.getStorageSync("token")
              }, 
         //呈现从后端获取的推荐菜品
    	   success:(res)=>{
              var meallist=res.data.data
              this.meals=meallist
              for(let i=0;i<this.meals.length;i++)
               {
                this.meals[i].checked=false
                this.meals[i].sum=1
                this.meals[i].cal=this.meals[i].calorie
               }
    	       }
          })
        },
    components:{
      uniNumberBox,
      popup,
      recrange,
    },
    props: [],
    methods: {    
      //判断是否为全选
      weatherAll:function(index){
            this.meals[index].checked=!this.meals[index].checked
            if(this.meals[index].checked==true)
            {this.flag+=1}
            else{this.flag-=1}
            if(this.flag==this.meals.length)
        {
          this.select=true
        }
        else {this.select=false}
      },
      
      //记录某一菜品的已选份数
      addproperty:function(value,index){
        this.meals[index].sum=value
      },
      
      //将菜品添加到菜单
      add:function(){
        this.isshow=true
        for(let i=this.meals.length-1;i>=0;i--)
        {
          if(this.meals[i].checked==false)
          {
            this.meals.splice(i,1)
          }
        }
        
        //将已选菜品添加到缓存
        uni.setStorage({
            key: 'meal-list',
            data: this.meals,
            success: function () {
                console.log('success');
            }
        });
        //开发阶段用于验证是否已存入缓存
        /*uni.getStorage({
            key: 'meal-list',
            success: function (res) {
                console.log(res.data);
            }
        });*/
      },
      
      //表示选中某一菜品
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
         select:false,//表示某一菜品是否选中
         meals:[null],
         
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
