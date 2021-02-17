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
          <view class="dishitem">
            <checkbox
              color="#59453D"
              :checked="item.checked"
              @click="weatherAll(index)"
            />
            <image :src="item.picture"/></image>

            <view class="data">
              <p>{{ item.name }}</p>
              <p>{{ item.calorie }}</p>
            </view>

            <view class="calculate"><!--份数-->
              <uni-number-box
                :min="0"
                :max="9"
                @change="addproperty($event,index)"
              />
            </view>

          </view>
        </dt>

      </scroll-view>
      <div style="height:100px"/>
    </dl>

    <!--底部多选栏-->
    <view class="footer">
      <checkbox
        @click="tap"
        :checked="selectAll"
        color="#59453D"
        class="checkbox"
      >
        <text>全选</text>
      </checkbox>
      <button
        plain
        size="default"
        @click="add"
      >
        <text >加入菜单</text>
      </button>
    </view>

    <popup
      style="z-index: 3;left: 0;top: 0;position: absolute;"
      v-if="isshow"
    />

  </view>
</template>

<script>
import recrange from '.../../../components/all/recommendrange.vue';
import uniNumberBox from '@/components/uni-ui/uni-number-box/uni-number-box.vue';
import popup from '../popup.vue';
export default
{
  data() {
    return {
      isshow: false,
      flag: 4, // 列表元素个数
      selectAll: true,
      meals: [
        {checked: 'true', picture: 'https://cal.liyangpu.com:8000/media/static/tomato&egg.png', name: '番茄炒蛋', calorie: '81kcal'},
        {checked: 'true', picture: 'https://cal.liyangpu.com:8000/media/static/rice.png', name: '米饭', calorie: '116kcal'},
        {checked: 'true', picture: 'https://cal.liyangpu.com:8000/media/static/corn.png', name: '糯玉米', calorie: '102kcal'},
        {checked: 'true', picture: 'https://cal.liyangpu.com:8000/media/static/gruel.png', name: '小米粥', calorie: '46kcal'},
      ], // checked，picture,name,calorie
    };
  },

  created() {
    let value = uni.getStorageSync('minmax');// 从缓存获取本餐卡路里推荐范围
    let userid = uni.getStorageSync('userid');// 从缓存获取userid
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
      console.log(this.flag);

      if (this.flag == this.meals.length) {
        this.selectAll = true;
      } else {
        this.selectAll = false;
      }
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
        }
      }

      // 将已选菜品添加到缓存
      uni.setStorage({
        key: 'meal-list',
        data: this.meals,
        success: function() {
          console.log('success');
        },
      });
    },

    // 全选
    tap: function() {
      this.selectAll = !this.selectAll;
      for (let i = 0; i < this.meals.length; i++) {
        this.meals[i].checked = this.selectAll;
      }

      if (this.selectAll == true) {
        this.flag = this.meals.length;
      } else {
        this.flag = 0;
      }
    },
  },

};

</script>

<style>
    image{
    width:140rpx;
    height:140rpx;
    }

  .dishitem{
    width:100%;
    display: flex;
    align-items: center;
    justify-content: space-around;
    margin: 30rpx 0;
  }
  .data{
    width:150rpx;
  }
  uni-number-box{
    width:70rpx;
  }
  .data>p:first-child{
    font-weight: 800;
    font-size:1em;
    color: #59453D;
  }
  .data>p:nth-child(2){
    font-weight: 800;
    color: #59453D;
    font-size:0.8em;
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
    width:100%;
    bottom:0;
    display:flex;
    justify-content:space-between;
    align-items:center;
    background-color:white;
    border-top: 4rpx solid #59453D;
    z-index:2;
    box-sizing: border-box;
    padding: 0 25rpx;
  }
  button{
    color:#3F536E;
    padding: 0 10rpx;
    margin: 0;
    border:  1px white solid !important;
  }
  button::after{
    border: none;
  }
  text{
    font-weight: 600;
    font-size:1em;
    color: #59453D;
  }
  .checkbox text{
    color:#3F536E
  }
</style>
