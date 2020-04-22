<template>
  <view>
    <text class="hint">请输入以下信息,点击图标上传菜品图片</text>
    <!--访问权限问题-->
    <view class="list">
        <image :src="src" @click="chooseimage"></image>
        <view class="table">
            <text class="meal">套餐名称：</text>
            <input placeholder="  输入内容"
                   focus="true"
                   @input="addname"
                   />
        </view>
        <view v-for="(dishname,index) in dishnames">
        <view class="table">
            <text class="dishname">菜品名称{{index+1}}：</text>
            <input placeholder="  输入套餐内菜品名称"
                   @input="dishnameadd(index,$event)"
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
export default {
    components:{
    },
		data() {
			return {
        src:"../../static/upload.jpg",
        mealname:"",//预留给套餐名称
        dishnames:[
          {name:"dish1"},
          {name:"dish2"},
          {name:"dish3"}
        ],
			}
		},
		methods: {
      
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
       this.dishnames[index].name=event.detail.value;
       console.log(this.dishnames[index].name);
     },
     //所有的上传在此处完成
     complete:function(){
       var that=this
         console.log("进入完成函数")
         uni.showModal({
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
         /*uni.uploadFile({
                   url: 'http://cal.hanlh.com:8000/', 
                   filePath: this.src,
                   name: '',
                   formData: {
                       
                   },
                   success: (uploadFileRes) => {
                       console.log(uploadFileRes.data);
                   }
               });*/
     },
     
     
		},
    onLoad() {
      
      uni.getStorage({
        key:'meal-list',
        success: (res) => {
          console.log(res)
        },
        fail: () => {
          uni.setStorage({
            key:'meal-list',
            data:[],
            success: () => {
              console.log('set meal-list')
            }
          })
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
    height: 500rpx;
   }
  .meal{
    font-size: 50rpx;
    font-weight: 600;
   }
   .dishname{
     font-size: 45rpx;
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
   }
  button{
    font-size: 20rpx;
    font-weight: 300;
    width:100rpx;
    height: 60rpx;
    line-height: 60rpx;
    border: #D0DEE5 3rpx solid;
    border-radius: 10rpx;
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
