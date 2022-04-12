<template>
	<view>
    <input v-model="name" placeholder="菜名" class="input">
    <image :src="img" class="img" mode="aspectFit"></image>
		<view class="button" @click="chooseimage">选择图片</view>
    <view v-for="(ingredient , index) in ingredients" :key="index" class="row">
      食材:{{ingredient.name}}<br>
      重量:{{ingredient.weight}}g
      <view class="red-button" @click="deleteIngredient(index)">删除</view>
    </view>
    <view class="button" @click="addIngredient">添加一项食材</view>
    <button style="margin-top: 30px;" @click="submit">提交</button>
    
    
    
    <view class="popup" v-show="isAddIngredient">
      <p class="title">{{ingredientName}}</p>
      <view class="small-button" @click="chooseIngredient">选择食材</view>
      <p>重量(g):</p>
      <input v-model="weight" class="input">
      <button size="mini" style="text-align: center;width: 60%;margin-left: 20%;" @click="comfirmIngredient">确认</button>
    </view>
    
    <view class="popup" v-show="isChooseIngredient" style="top: 100rpx;overflow: scroll;height: 750rpx;">
      <input v-model="keywords" class="input" @input="searchIngredient" placeholder="搜索">
      <view v-for="(item , index) in shownIngredients" :key="index" @click="tapIngredient(index)" class="ingredient">
        {{item.name}}
      </view>
    </view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				img:"",
        name:"",
        id:"",
        ingredients:[],
        weight:"",
        isAddIngredient:false,
        ingredientName:"",
        isChooseIngredient:false,
        keywords:"",
        allIngredient:[],
        shownIngredients:[],
        edit:false,
        pictureChange:false,
        dish_id:""
			}
		},
    onLoad:function(res){
        uni.request({
          url:'https://comi.hi.cn:8000/administrate/ingredient/all/',
          method:'GET',
          header:{
            'administrator-token':uni.getStorageSync('adtoken'),
            Authorization:"Token "+uni.getStorageSync("token")
          },
          success:(res)=> {
            if(res.data.error=="Auth time out!")
            {
              uni.reLaunch({
                url:"../user/administrator"
              })
              return
            }
            this.allIngredient=res.data.data
          }
        })
        if(res.edit=="true")
        {
          this.edit=true
          this.name=res.name
          this.img="https://comi.hi.cn:8000"+res.picture
          this.dish_id=res.id
        }
    },
		methods: {
			chooseimage:function(){
        uni.chooseImage({
          count:1,
          success: (res) => {
            this.img=res.tempFilePaths[0]
          }
        })
        this.pictureChange=true
      },
      addIngredient:function(){
        this.ingredientName=""
        this.id=""
        this.weight=""
        this.isAddIngredient=true
      },
      comfirmIngredient:function(){
        if(this.ingredientName=="")
        {
          uni.showToast({
            icon:"none",
            title:"请选择食材"
          })
          return
        }
        if(this.weight=="")
        {
          uni.showToast({
            icon:"none",
            title:"请输入重量"
          })
          return
        }
        if(!/^[0-9]+.?[0-9]*$/.test(this.weight))
        {
          uni.showToast({
            icon:"none",
            title:"请输入数字"
          })
          return
        }
        this.ingredients.push({
          id:this.id,
          name:this.ingredientName,
          weight:this.weight
        })
        this.isAddIngredient=false
      },
      chooseIngredient:function(){
        this.isChooseIngredient=true
        this.shownIngredients=this.allIngredient
      },
      tapIngredient:function(index){
        this.ingredientName=this.shownIngredients[index].name
        this.id=this.shownIngredients[index].id
        this.isChooseIngredient=false
      },
      searchIngredient:function(){
        var arr=[]
        for(var i=0;i<this.allIngredient.length;i++)
        {
          if(this.allIngredient[i].name.search(this.keywords)!=-1)
          {
            arr.push(this.allIngredient[i])
          }
        }
        this.shownIngredients=arr
      },
      deleteIngredient:function(index){
        this.ingredients.splice(index,1)
      },
      submit:function() {
        if(this.name=="")
        {
          uni.showToast({
            icon:"none",
            title:"请输入菜名"
          })
          return
        }
        if(this.img=="")
        {
          uni.showToast({
            icon:"none",
            title:"请选择图片"
          })
          return
        }
        if(this.ingredients.length==0)
        {
          uni.showToast({
            icon:"none",
            title:"请选择至少一种食材"
          })
          return
        }
        if(this.edit)
        {
          this.DishEdit()
        }
        else
        {
          this.DishAdd()
        }
      },
      DishAdd:function(){
        uni.uploadFile({
          url:'https://comi.hi.cn:8000/administrate/dish/add/',
          header:{
            'administrator-token':uni.getStorageSync('adtoken'),
            Authorization:"Token "+uni.getStorageSync("token")
          },
          formData:{
            name:this.name,
            ingredient:JSON.stringify(this.ingredients)
          },
          filePath:this.img,
          name:"picture",
          success:function(res){
            console.log(res)
            uni.redirectTo({
              url:"./DishManage"
            })
          }
        })
      },
      DishEdit:function(){
        if(this.pictureChange)
        {
          uni.uploadFile({
            url:'https://comi.hi.cn:8000/administrate/dish/edit/',
            header:{
              'administrator-token':uni.getStorageSync('adtoken'),
              Authorization:"Token "+uni.getStorageSync("token")
            },
            formData:{
              id:this.dish_id,
              name:this.name,
              ingredient:JSON.stringify(this.ingredients)
            },
            filePath:this.img,
            name:"picture",
            success:function(res){
              console.log(res)
              uni.redirectTo({
                url:"./DishManage"
              })
            }
          })
        }
        else
        {
          uni.request({
            url:'https://comi.hi.cn:8000/administrate/dish/edit/',
            method:"post",
            header:{
              'administrator-token':uni.getStorageSync('adtoken'),
              Authorization:"Token "+uni.getStorageSync("token")
            },
            data:{
              id:this.dish_id,
              name:this.name,
              ingredient:JSON.stringify(this.ingredients)
            },
            success:function(res){
              console.log(res)
              uni.redirectTo({
                url:"./DishManage"
              })
            }
          })
        }
      }
		}
	}
</script>

<style>
  .img {
    width: 500rpx;
    height: 500rpx;
    margin-left: 125rpx;
    background-color: #d9cfca;
    margin-top: 10px;
  }
  .button {
    border: 1px solid black;
    text-align: center;
    padding: 1px 0;
    border-radius: 2px;
    font-size: 12px;
    width: 500rpx;
    margin-left: 125rpx;
    margin-top: 10px;
  }
  .small-button {
    border: 1px solid black;
    text-align: center;
    padding: 1px 0;
    border-radius: 2px;
    font-size: 12px;
    width: 350rpx;
    margin-left: 125rpx;
    margin-top: 10px;
  }
  .row {
    width: 670rpx;
    margin: 10rpx 20rpx;
    padding: 5px 20rpx;
    background-color: #d9cfca;
    position: relative;
  }
  .input {
    border: solid 1px black;
    border-radius: 2px;
    margin: 30rpx 10rpx;
    padding: 2px 1px;
  }
  .popup {
    position: fixed;
    left: 75rpx;
    top: 200rpx;
    width: 600rpx;
    background-color: #d9cfca;
  }
  .title {
    font-size: 2em;
    width: 600rpx;
    text-align: center;
  }
  .ingredient {
    margin: 2px 2px;
    background-color: white;
    border-radius: 2px;
  }
  .red-button {
    border: 1px solid red;
    color: red;
    text-align: center;
    padding: 1px 2px;
    border-radius: 2px;
    font-size: 12px;
    position: absolute;
    right: 20rpx;
    top: 5px;
  }
</style>
