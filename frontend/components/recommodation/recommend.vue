<template>
  <view>
    <dl>
      <scroll-view scroll-y="true" scroll-top="200">
        <dt v-for="(item,index) in meals" :key="index">
          <view class="block">
            <checkbox color="#59453D" :checked="item.checked" @click="weatherAll(index)"></checkbox>
            <image style="height: 100%;width: 100%;" :src="'https://nkucalorie.top:8000'+item.picture"></image>
            <view class="data">
              <p>{{item.name}}</p>
              <p style="font-size:0.5em;color: #59453D;">{{item.calorie}} Kcal</p>
            </view>
            <view class="calculate">
              <uni-number-box :min="0" :max="9" @change="addproperty($event,index)"></uni-number-box>
            </view>
          </view>
        </dt>
      </scroll-view>
      <div style="height:100px"></div>
    </dl>

    <!--底部多选栏-->
    <view class="footer">
      <checkbox @click="tap" :checked="selectAll" color="#59453D" class="checkbox">
        <text>全选</text>
      </checkbox>
      <button plain=true size="default" @click="add" v-show="!selectNone">
        <text>加入菜单</text>
      </button>
      <button plain=true size="default" @click="getmeals" v-show="selectNone">
        <text>重新推荐</text>
      </button>
    </view>

    <popup style="z-index: 3;left: 0;top: 0;position: absolute;" v-if="isshow"></popup>


  </view>
</template>

<script>
  import recrange from "../../components/all/recommendrange.vue"
  import uniNumberBox from "@/components/uni-ui/uni-number-box/uni-number-box.vue"
  import popup from "./popup.vue"
  export default {
    data() {
      return {
        isshow: false,
        flag: 0,
        selectAll: false, //是否全选
        meals: [], //checked，picture
        selectNone: true
      };
    },

    created() {
      let value = uni.getStorageSync("minmax"); //从缓存获取本餐卡路里推荐范围
      let userid = uni.getStorageSync("userid"); //从缓存获取userid
      this.getmeals()
    },
    components: {
      uniNumberBox,
      popup,
      recrange,
    },
    props: [],
    methods: {
      //判断是否为全选
      weatherAll: function(index) {
        this.meals[index].checked = !this.meals[index].checked
        if (this.meals[index].checked == true) {
          this.flag += 1
        } else {
          this.flag -= 1
        }

        if (this.flag == this.meals.length) this.selectAll = true
        else this.selectAll = false
        if (this.flag == 0) this.selectNone = true
        else this.selectNone = false
      },



      //记录某一菜品的已选份数
      addproperty: function(value, index) {
        this.meals[index].sum = value
      },

      //将菜品添加到菜单
      add: function() {
        this.isshow = true
        for (let i = this.meals.length - 1; i >= 0; i--) {
          if (this.meals[i].checked == false) {
            this.meals.splice(i, 1)
            continue
          }
          this.meals[i].cal = this.meals[i].calorie
        }

        //将已选菜品添加到缓存
        var OrderedFood = uni.getStorageSync("meal-list");
        for (var j = 0; j < this.meals.length; j++) {
          for (let i = 0; i < OrderedFood.length; i++) {
            if (OrderedFood[i].name === this.meals[j].name) {
              OrderedFood[i].sum += this.meals[j].sum
              continue
            }
          }
          OrderedFood.push({
            name: this.meals[j].name,
            cal: this.meals[j].calorie,
            sum: this.meals[j].sum,
            picture: this.meals[j].picture,
            id: this.meals[j].id
          });
        }

        uni.setStorageSync("meal-list", OrderedFood);


      },

      //全选
      tap: function() {
        this.selectAll = !this.selectAll
        for (let i = 0; i < this.meals.length; i++) {
          this.meals[i].checked = this.selectAll
        }

        if (this.selectAll == true) {
          this.flag = this.meals.length
          this.selectNone = false
        } else {
          this.flag = 0
          this.selectNone = true
        }
      },

      getmeals() {
        uni.request({
          url: 'https://nkucalorie.top:8000/dish/recommend/',
          method: 'GET',
          header: {
            Authorization: "Token " + uni.getStorageSync("token")
          },
          success: (res) => {
            this.meals = res.data.data.dishes
            for (var i = 0; i < this.meals.length; i++)
              this.meals[i].checked = false
          }
        })
      },

      gotoshake() {
        uni.redirectTo({
          url: "../../pages/recommondation/shake"
        })
      }
    },

  }
</script>

<style>
  .block {
    display: grid;
    grid-template-columns: 1fr 3fr 3fr 3fr;
    grid-template-rows: 225rpx;
    align-items: center;
    justify-content: center;
    margin-bottom: 10px;
  }

  .calculate {
    overflow: hidden;
    font-size: 1em;
    border: #59453D;
  }

  .data {
    font-weight: 800;
    font-size: 50rpx;
    color: #59453D;
  }

  lable {
    position: relative;
    top: 15px
  }

  .text1 {
    font-weight: 800;
    color: #59453d;
  }

  .footer {
    position: fixed;
    height: 8%;
    width: 752rpx;
    bottom: 0px;
    display: flex;
    justify-content: flex-end;
    align-items: center;
    background-color: #FFFFFF;
    border-top: 1rpx solid #59453D;
    z-index: 2;
  }

  .checkbox {
    margin-left: 17.5rpx;
  }

  button {
    margin-right: 25rpx;
  }

  text {
    font-weight: 600;
    font-size: 1em;
    color: #59453D;
  }
</style>
