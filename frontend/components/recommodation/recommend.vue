<template>
  <view>
    <dl>
      <scroll-view
        scroll-y="true"
        scroll-top="200"
      >
        <dt
          v-for="(item,index) in meals"
          :key="index"
        >
          <view class="block">
            <checkbox
              style="transform:scale(0.7)"
              color="#3a2d27"
              :checked="item.checked"
              @click="weatherAll(index)"
            />
            <image
              :src="'https://calorie.liyangpu.com:8003'+item.picture"
            /></image>
            <view class="data">
              <p>{{ item.name }}</p>
              <p>{{ item.calorie }} Kcal</p>
            </view>
            <view class="calculate">
              <uni-number-box
                :min="0"
                :max="9"
                @change="addproperty($event,index)"
              />
            </view>
          </view>
        </dt>
      </scroll-view>
    </dl>

    <!--底部多选栏-->
    <view class="footer">
      <view
        class="checkbox"
        @click="tap"
        color="#59453D"
      >
        <text v-show="!selectAll">全选</text>
        <text v-show="selectAll">取消全选</text>
      </view>
      <view
        class="button"
        plain="true"
        size="default"
        @click="add"
        v-show="!selectNone"
      >
        <text>加入菜单</text>
      </view>
      <view
        class="button"
        plain="true"
        size="default"
        @click="getmeals"
        v-show="selectNone"
      >
        <text>重新推荐</text>
      </view>
    </view>

    <popup
      style="z-index: 3;left: 0;top: 0;position: absolute;"
      v-if="isshow"
    />

  </view>
</template>

<script>
import recrange from '../../components/all/recommendrange.vue';
import uniNumberBox from '@/components/uni-ui/uni-number-box/uni-number-box.vue';
import popup from './popup.vue';
export default {
  data() {
    return {
      isshow: false,
      flag: 0,
      selectAll: false, // 是否全选
      meals: [], // checked，picture
      selectNone: true,
    };
  },

  created() {
    let value = uni.getStorageSync('minmax'); // 从缓存获取本餐卡路里推荐范围
    let userid = uni.getStorageSync('userid'); // 从缓存获取userid
    this.getmeals();
  },
  components: {
    uniNumberBox,
    popup,
    recrange,
  },
  props: [],
  methods: {
    // 判断是否为全选
    weatherAll: function(index) {
      this.meals[index].checked = !this.meals[index].checked;
      if (this.meals[index].checked == true) {
        this.flag += 1;
      } else {
        this.flag -= 1;
      }

      if (this.flag == this.meals.length) this.selectAll = true;
      else this.selectAll = false;
      if (this.flag == 0) this.selectNone = true;
      else this.selectNone = false;
    },

    // 记录某一菜品的已选份数
    addproperty: function(value, index) {
      this.meals[index].sum = value;
    },

    // 将菜品添加到菜单
    add: function() {
      this.isshow = true;
      for (let i = this.meals.length - 1; i >= 0; i--) {
        if (this.meals[i].checked == false) {
          this.meals.splice(i, 1);
          continue;
        }
        this.meals[i].cal = this.meals[i].calorie;
      }

      // 将已选菜品添加到缓存
      var OrderedFood = uni.getStorageSync('meal-list');
      for (var j = 0; j < this.meals.length; j++) {
        for (let i = 0; i < OrderedFood.length; i++) {
          if (OrderedFood[i].name === this.meals[j].name) {
            OrderedFood[i].sum += this.meals[j].sum;
            continue;
          }
        }
        OrderedFood.push({
          name: this.meals[j].name,
          cal: this.meals[j].calorie,
          sum: this.meals[j].sum,
          picture: this.meals[j].picture,
          id: this.meals[j].id,
        });
      }

      uni.setStorageSync('meal-list', OrderedFood);
    },

    // 全选
    tap: function() {
      this.selectAll = !this.selectAll;
      for (let i = 0; i < this.meals.length; i++) {
        this.meals[i].checked = this.selectAll;
      }

      if (this.selectAll == true) {
        this.flag = this.meals.length;
        this.selectNone = false;
      } else {
        this.flag = 0;
        this.selectNone = true;
      }
    },

    getmeals() {
      uni.request({
        url: 'https://calorie.liyangpu.com:8003/dish/recommend/',
        method: 'GET',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        success: (res) => {
          this.meals = res.data.data.dishes;
          for (var i = 0; i < this.meals.length; i++) { this.meals[i].checked = false; }
        },
      });
    },

    gotoshake() {
      uni.redirectTo({
        url: '../../pages/recommondation/shake',
      });
    },
  },

};
</script>

<style>
  .block {
    display: grid;
    grid-template-columns: 1fr 3fr 3fr 3fr;
    grid-template-rows: 225rpx;
    margin-bottom: 10px;
    justify-content: center;
    align-items: center;
  }

  .data {
    font-weight: 800;
    font-size: 28rpx;
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
    width: 100%;
    height: 120rpx;
    bottom: 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #FFFFFF;
    box-shadow:0 0 20px #d0d0d0;
  }

  .checkbox {
    margin-left: 17.5rpx;
  }

  .button {
    margin-right: 25rpx;
  }

  text {
    font-weight:bolder;
    font-size: 28rpx;
    color: #59453D;
    font-family: "Microsoft YaHei";
  }
  image{
    height:80%;
    width:90%;
    border-radius: 30%;
  }
</style>
