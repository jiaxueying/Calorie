<template>
  <view style="margin: 10px; display: flex;flex-direction: column;justify-content: center; align-items: center;">
    <view style="width:90%; display:flex; align-items:flex-end;justify-content: space-between; margin-bottom: 10px;">
      <view class='title'>食材表</view>
      <view class="add" @click="IngredientAdd">添加食材</view>
    </view>
    <view v-for="(ingredient , index) in ingredients" :key='index' class="row">
      <p class="ingredient" @click='ShowDetails(ingredient.id)'>{{ingredient.name}}</p>
      <view class="red-button" @click="DeleteIngredient(ingredient.id)">删除</view>
    </view>
  </view>
</template>

<script>
  export default {
    data() {
      return {
        ingredients: []
      }
    },
    created: function() {
      this.GetAllIngredients()
    },
    methods: {
      GetAllIngredients: function() {
        uni.request({
          url: 'https://calorie.liyangpu.com:8003/administrate/ingredient/all/',
          method: 'GET',
          header: {
            'administrator-token': uni.getStorageSync('adtoken'),
            Authorization: "Token " + uni.getStorageSync("token")
          },
          success: (res) => {
            if (res.data.error == "Auth time out!") {
              uni.reLaunch({
                url: "../user/administrator"
              })
              return
            }
            this.ingredients = res.data.data
          }
        })
      },
      ShowDetails: function(id) {
        uni.request({
          url: 'https://calorie.liyangpu.com:8003/administrate/ingredient/get/',
          method: 'GET',
          header: {
            'administrator-token': uni.getStorageSync('adtoken'),
            Authorization: "Token " + uni.getStorageSync("token")
          },
          data: {
            'id': id
          },
          success: (res) => {
            if (res.data.error == "Auth time out!") {
              uni.reLaunch({
                url: "../user/administrator"
              })
              return
            }
            console.log(res)
            uni.showModal({
              title: res.data.data.name,
              confirmText: "编辑",
              content: '能量:' + res.data.data.calorie + '千卡' + ',' + res.data.data.energy + '千焦' + "\n" +
                '蛋白质:' + res.data.data.protein + 'g\n' +
                '脂肪:' + res.data.data.fat + 'g\n' +
                '碳水化合物:' + res.data.data.carbohydrates + 'g\n' +
                '膳食纤维:' + res.data.data.dietary_fiber + 'g\n' +
                '维生素C:' + res.data.data.vitaminC + 'mg\n' +
                '钙:' + res.data.data.calcium + 'mg\n' +
                '钠:' + res.data.data.sodium + 'mg',
              success: (r) => {
                if (r.confirm) {
                  uni.redirectTo({
                    url: "./IngredientEdit?edit=true" +
                      "&name=" + res.data.data.name +
                      "&calorie=" + res.data.data.calorie +
                      "&energy=" + res.data.data.energy +
                      "&protein=" + res.data.data.protein +
                      "&fat=" + res.data.data.fat +
                      "&carbohydrates=" + res.data.data.carbohydrates +
                      "&dietary_fiber=" + res.data.data.dietary_fiber +
                      "&vitaminC=" + res.data.data.vitaminC +
                      "&calcium=" + res.data.data.calcium +
                      "&sodium=" + res.data.data.sodium +
                      "&id=" + res.data.data.id
                  })
                }
              }
            })
          }
        })
      },
      DeleteIngredient: function(id) {
        uni.showModal({
          title: '确定要删除这一条数据吗',
          success: (res) => {
            if (res.confirm) {
              uni.request({
                url: 'https://calorie.liyangpu.com:8003/administrate/ingredient/delete/',
                method: 'GET',
                header: {
                  'administrator-token': uni.getStorageSync('adtoken'),
                  Authorization: "Token " + uni.getStorageSync("token")
                },
                data: {
                  'id': id
                },
                success: (res) => {
                  if (res.data.error == "Auth time out!") {
                    uni.reLaunch({
                      url: "../user/administrator"
                    })
                    return
                  }
                  uni.redirectTo({
                    url: './IngredientManage'
                  })
                }
              })
            }
          }
        })
      },
      IngredientAdd: function() {
        uni.redirectTo({
          url: "./IngredientEdit"
        })
      }
    }
  }
</script>

<style>
  .title {
    font-size: 1.5em;
    /* width: 750rpx; */
    text-align: left;
    display: inline-block;
    vertical-align: bottom;
  }

  .row {
    display: flex;
    justify-content: space-around;
    width: 90%;
    margin-top: 5rpx;
    padding: 5px 0;
    border-bottom: rgb(217, 207, 202) solid 1px;
    /* background-color: #d9cfca; */
    /* border-radius: 5px; */
  }

  .ingredient {
    width: 550rpx;
  }

  .red-button {
    border: 1px solid red;
    color: red;
    text-align: center;
    padding: 1px 2px;
    border-radius: 2px;
    font-size: 12px;
  }

  uni-modal .uni-modal__bd {
    white-space: pre-wrap;
  }

  .add {
    border: green 1px solid;
    border-radius: 2px;
    color: green;
    padding: 1px 2px;
    display: inline-block;
    vertical-align: bottom;
    margin-right: 0;
  }
</style>
