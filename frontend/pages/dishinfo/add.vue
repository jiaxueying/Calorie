<template>
  <view>
    <text class="hint">请输入以下信息,点击图标上传菜品图片</text>
    <view class="list">
        <image :src="src" @click="chooseimage"></image>
        <view class="table">
            <text class="meal">菜品名称：</text>
            <input placeholder="  输入内容"
                   focus="true"
                   @input="addname"
                   />
        </view>
        <view>
            <text>所用食材</text><button class="btn1" size="mini" @click="ifshow">+</button>
        </view>
        <view>
            <lv-select
            @handleSearch="handleSearch"
            placeholder="点击此处选择菜品所含食材"
            :infoList="infoList"
            :uniShadow="true"
            v-model="searchValue"
            :loading="loading"
            type="primary"
            >
            </lv-select>
        </view>
        <view v-for="(dishname,index) in dishnames" :key="index" v-show="isshow">
        <view class="table">
            <text class="dishname">食材名{{index+1}}：</text>
            <input placeholder="  点击选择食材"
                   @input="dishnameadd(index,$event)"
                   />
            <input placeholder=" 填写所需克数"
                   @input=""
                   />
        </view>
        </view>
        <view style="height:150rpx"></view>
        <view class="bottom">
            <button plain="true" @click="complete">完成</button>
        </view>
    </view><!--list-->
  </view>
</template>

<script>
import {request, backendurl} from "../../common/helper.js"
import lvSelect from "../../components/lv-select/lv-select.vue"  
export default {
    components:{lvSelect},
		data() {
			return {
        src:"../../static/upload.jpg",
        mealname:"",//预留给套餐名称
        dishnames:[" 未填写"," 未填写"," 未填写"],
        ingredients:[],
        isshow:false,
        infoList:[],
        infoLists:[],
        loading:false,
        searchValue:""
			}
		},
		methods: {
        
    handleSearch(){
        this.loading=true
        this.infoList=[]
        for(var i=0;i<this.infoLists.length;i++){
           if(this.infoLists[i].name.search(this.searchValue)!=-1){
              this.infoList.push({id:this.infoLists[i].id, name:this.infoLists[i].name});
              console.log("push!")
              continue;
          }
        }
          
        setTimeout(()=>{
          this.loading=false
          if(this.infoList.length==0){
            this.infoList=[{name:"未找到您所需食材，请添加食材后返回本页面"}]
          }
        },2000)
      },
      
      
    change(val){
      console.log(val)
    },  
      
     chooseimage:function(){
       var that=this;
       console.log("进入照片上传函数")
       uni.chooseImage({
         count:1,
         success:function(res){
           console.log(res.tempFilePaths)
           that.src=res.tempFilePaths[0];
           
         }
       })
       
     },
     
     addname:function(event){
       console.log(event.detail);
       this.mealname=event.detail.value;
       console.log(this.mealname);
     },
     
     dishnameadd:function(index,event){
       console.log("in dishnameadd!"+index);
       console.log(event.detail.value);
       this.dishnames[index]=event.detail.value;
       console.log(this.dishnames[index]);
     },
     ifshow:function(){
       this.isshow=true;
     },
     
     //所有的上传在此处完成
     complete:async function(){
       var that=this
         console.log("进入完成函数")
         await uni.showModal({
           title: '提示',
           content: '确认上传',
           success: function (res) {
               if (res.confirm) {
                   console.log('用户点击确定');
                   console.log(that.src);
                   that.upload();
                   
               } else if (res.cancel) {
                   console.log('用户点击取消');
               }
             }
         });
         
     },
     //此处完善上传图片文件和菜品名称的api
     upload:function(){
         console.log("into upload");
         let names = [];
         for(let i = 0; i < this.dishnames.length; i++) {
           names.push(this.dishnames[i]);
         }
         console.log(JSON.stringify(names))
         uni.uploadFile({
                   url: 'http://cal.hanlh.com:8000/canteen/adddish/', 
                   filePath: this.src,
                   name: 'img',
                   header:{
                       Authorization:'Token '+uni.getStorageSync('token'),
                       'Content-Type': 'application/x-www-form-urlencoded',
                     },
                   formData: {
                        'dish':this.mealname,
                        'img':this.src,
                        'names':JSON.stringify(names)
                   },
                   success: (uploadFileRes) => {
                       console.log(uploadFileRes);
                       wx.navigateBack({
                       url: "../MealManagement/MealManagement",
                       })
                   }
               });
               
     },
     
     
		},
    onLoad() {
      
      uni.request({
            url:"https://calorie.liyangpu.com:8003/administrate/ingredient/all/",
            method:"GET",
            header:{
              Authorization:"Token "+uni.getStorageSync("token"),
              'administrator-token':uni.getStorageSync("adtoken")
            },
            success:(res)=>{
              console.log("success")
              console.log(res)
              this.infoLists=res.data.data
              console.log(this.infoLists)
            },
            fail:(res)=>{
              console.log(res.date)
            }
      }) 
      
      
    }
	}  
</script>

<style>
  .hint{
    display: block;
    border-top: 5rpx solid #808080;
    border-bottom: 5rpx solid #808080;
    font-size: 30rpx;
    font-weight: 500;
    color: #808080;
    text-align: center;
    margin-bottom: 100rpx;
    }
  .list{
    width:100%;
    display:flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    }
  image{
    width: 550rpx;
    height: 450rpx;
   }
  .meal{
    font-size: 1em;
    font-weight: 600;
   }
   .dishname{
     font-size:1.2em;
     font-weight: 600;
   }
  .table{
    margin-top: 100rpx;
    display: flex;
    flex-direction: row;
   }
  input{
    border: #808080 2rpx solid;
    border-radius: 10rpx;
    outline: none;
    height: 80rpx;;
    width:60%;
   }
  button{
    font-size: 1em;
    font-weight: 300;
    width:100rpx;
    height: 60rpx;
    line-height: 60rpx;
    border: #D0DEE5 3rpx solid;
    border-radius: 10rpx;
     }
  .btn1{
    width:60rpx;
    height:60rpx;
    padding: 0;
    border-radius: 50%;
    font-size: 1em;
  }
  .bottom{
    position: fixed;
    bottom: 0rpx;
    height:100rpx;
    border-top: #C8C7CC 5rpx solid;
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    z-index:10;
    background-color: #FFFFFF;
    }
</style>
