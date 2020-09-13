<template>
	<view>
		<view style="position: relative;">
      <p class="title">菜品表</p>
      <view class="add" @click="DishAdd">添加</view>
    </view>
    
    <view v-for="(dish,index) in dishes" :key="index" class="row" @click="showDetails(index)">
      <image :src="dish.picture" class="img" mode="aspectFit"></image>
      <view class="label">{{dish.name}}</view>
      <view class="red-button" @click.stop="deleteDish(index)">删除</view>
    </view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				dishes:[]
			}
		},
    onLoad:function(){
        uni.request({
          url:'https://nkucalorie.top:8000/dish/key_query/',
          method:'GET',
          header:{
            Authorization:"Token "+uni.getStorageSync("token")
          },
          data:{
            key_word:""
          },
          success:(res)=> {
            console.log(res)
            this.dishes=res.data.data
            for(var i=0;i<this.dishes.length;i++)
            {
              this.dishes[i]['picture']="https://nkucalorie.top:8000"+this.dishes[i]['picture']
            }
          }
        })
    },
		methods: {
			DishAdd:function(){
        uni.redirectTo({
          url:"./DishEdit"
        })
      },
      deleteDish:function(index){
        uni.showModal({
          title:"确认要删除这个菜吗",
          success: (res) => {
            if(res.confirm)
            {
              uni.request({
                url:'https://nkucalorie.top:8000/administrate/dish/delete/',
                method:'GET',
                header:{
                  'administrator-token':uni.getStorageSync('adtoken'),
                  Authorization:"Token "+uni.getStorageSync("token")
                },
                data:{
                  id:this.dishes[index].id
                },
                success:(res)=> {
                  if(res.data.error=="Auth time out!")
                  {
                    uni.reLaunch({
                      url:"../user/administrator"
                    })
                    return
                  }
                  uni.redirectTo({
                    url:"./DishManage"
                  })
                }
              })
            }
          }
        })
      },
      showDetails:function(index){
        uni.request({
          url:'https://nkucalorie.top:8000/dish/detail/',
          method:'GET',
          header:{
            Authorization:"Token "+uni.getStorageSync("token")
          },
          data:{
            dish_id:this.dishes[index].id
          },
          success:(res)=> {
            console.log(res)
            uni.showModal({
              title:res.data.data.dish.name,
              confirmText:"编辑",
              content:'能量:'+res.data.data.dish.calorie+'千卡'+','+res.data.data.dish.energy+'千焦'+"\n"+
                      '蛋白质:'+res.data.data.dish.protein+'g\n'+
                      '脂肪:'+res.data.data.dish.fat+'g\n'+
                      '碳水化合物:'+res.data.data.dish.carbohydrates+'g\n'+
                      '膳食纤维:'+res.data.data.dish.dietary_fiber+'g\n'+
                      '维生素C:'+res.data.data.dish.vitaminC+'mg\n'+
                      '钙:'+res.data.data.dish.calcium+'mg\n'+
                      '钠:'+res.data.data.dish.sodium+'mg',
              success: (r) => {
                if(r.confirm){
                  uni.redirectTo({
                    url:"./DishEdit?edit=true"+
                        "&name="+res.data.data.dish.name+
                        "&picture="+res.data.data.dish.picture+
                        "&id="+res.data.data.dish.id
                  })
                }
              }
            })
          }
        })
      }
		}
	}
</script>

<style>
  .add {
    position: absolute;
    right: 20rpx;
    top: 10rpx;
    border: green 1px solid;
    border-radius: 2px;
    color: green;
    padding: 1px 2px;
  }
  .title {
    font-size: 2em;
    width: 750rpx;
    text-align: center;
  }
  .row {
    display: flex;
    width: 710rpx;
    margin: 10rpx 20rpx;
    padding: 5px 0;
    background-color: #d9cfca;
    position: relative;
  }
  .img {
    width: 200rpx;
    height: 200rpx;
  }
  .label {
    margin: 10px 20px;
  }
  .red-button {
    border: 1px solid red;
    color: red;
    text-align: center;
    padding: 1px 2px;
    border-radius: 2px;
    font-size: 12px;
    position: absolute;
    top: 10px;
    right: 10px;
  }
</style>
