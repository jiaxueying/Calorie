<template>

  <scroll-view
    scroll-y="true"
    class="content"
  >

    <!-- <view style="height: 0rpx;width: 750rpx;"> </view> -->
    <view class="imgarea">
      <image
        :src="'https://calorie.liyangpu.com:8003'+food.picture"
        class="img"
        v-if="isimg"
        mode="aspectFill"
      /></image>
    </view>
    <view style="display:flex;flex-direction: column;align-items: center;">
      <view style="width: 600rpx;">

        <view style="display:flex;flex-direction:row; align-items:baseline;flex:auto">
          <view class="name">{{ food.name }}
          </view>
          <view class="equ">
            ≈1×<image
              :src="'https://calorie.liyangpu.com:8003'+food.equivalent"
              class="eimag"
            /></image>
          </view>

        </view>
        <view class="cal">{{ food.calorie }} KCAL/{{ food.weight }}g</view>
        <view class="tab">
          <tab>
            <ttr align="left">
              <tth style="width: 200rpx;">项目</tth>
              <tth style="width: 200rpx;">每100克(g)</tth>
              <tth style="width: 200rpx;">NRV%</tth>
            </ttr>
            <ttr
              v-for="(content,index) in nutrition"
              :key="index"
              align="left"
            >
              <ttd style="width: 200rpx;">{{ content.item }}</ttd>
              <ttd style="width: 200rpx;">{{ content.value }}</ttd>
              <ttd style="width: 200rpx;">{{ content.percent }}</ttd>
            </ttr>
          </tab>
        </view>
        <view style="font-size: 30rpx;color: gray;margin-left: 0;width: 600rpx;margin-top: 10px;">喜欢这道菜吗？给个评价吧！</view>
        <view class="buttonarea">
          <button
            class="likebutton"
            @click="like"
          > <image
            :src="'../../static/like.png'"
            class="likeimg"
          /></image>{{ like_count }}</button>
          <button
            class="likebutton"
            @click="dislike"
          ><image
            :src="'../../static/unlike.png'"
            class="likeimg"
          /></image>{{ dislike_count }}</button>
        </view>
        <view style="width: 550rpx;margin-top: 25rpx;">
          <view style="display: flex;align-items: center;">
            <view style="font-size: 30rpx;line-height: 30rpx;color: gray;">关键词</view>
          </view>
          <view style="display: flex;flex-direction: column;align-items: flex-start;margin-top: 10rpx;">
            <view
              v-for="(dishname,index) in dishnames"
              class="dishnames"
              :key="index"
            >No.{{ index+1 }} {{ dishname }}</view>
          </view>
        </view>
        <view class="tags">
          <view
            v-for="(tag,index) in tags"
            class="tag"
            :key="index"
            @click="taptag(index)"
          >{{ tag.name }}</view>
        </view>
      </view>
      <view style="background-color: #FFFFFF;width: 750rpx;height: 30rpx;"/>
    </view>
  </view>
    <view class="bottom">
      <image
        :src="'../../static/orders.png'"
        class="button"
        @click="mylist"
      /></image>
      <image
        :src="'../../static/add.png'"
        class="button"
        @click="add"
      /></image>
    </view>
    <view
      v-show="IsShow"
      class="orders"
    >
      <Orders :foods="ordered_food" />
    </view>

  </scroll-view>
</template>

<script>
// import {
//   like,
//   // dislike
// } from '@/common/helper.js';
import {
  backendUrl,
  request,
} from '@/common/helper.js';
import Orders from '../../components/for-search/orders.vue';
import tab from '../../components/t-table/t-table.vue';
import ttr from '../../components/t-table/t-tr.vue';
import tth from '../../components/t-table/t-th.vue';
import ttd from '../../components/t-table/t-td.vue';
export default {
  components: {
    tab,
    ttr,
    tth,
    ttd,
    Orders,
  },
  data() {
    return {
      likeicon: 'https://calorie.liyangpu.com:8003/media/static/like.png',
      dislikeicon: 'https://calorie.liyangpu.com:8003/media/static/dislike.png',
      food: null,
      like_count: 666,
      liked: 0,
      disliked: 0,
      dislike_count: 666,
      X: Number,
      tempX: Number,
      min: '',
      max: '',
      isimg: true,
      name: '菜品名称',
      cal: '100KCAL/100g',
      equivalent: '等价物icon',
      tags: [{
        id: 1,
        name: '理科食堂',
      },
      {
        id: 2,
        name: '二楼',
      },
      {
        id: 3,
        name: '低卡',
      },
      {
        id: 1,
        name: '五号窗口',
      },
      ],
      nutrition: [],
      dishnames: [],
      IsShow: false,
      ordered_food: new Array(),
    };
  },
  onLoad: function(options) {
    uni.$on('refresh2', this.refresh);
    this.ordered_food = uni.getStorageSync('meal-list');
    uni.request({
      url: 'https://calorie.liyangpu.com:8003/dish/detail/',
      method: 'GET',
      header: {
        Authorization: 'Token ' + uni.getStorageSync('token'),
      },
      data: {
        dish_id: options.id,
      },
      success: (res) => {
        this.food = res.data.data.dish;
        console.log(res);
        this.like_count = this.food.like;
        this.equivalent = this.food.equivalent;
        this.dislike_count = this.food.dislike;
        this.tags = this.food.tag;
        this.nutrition.push({
          item: '能量(KJ)',
          value: this.food.energy + 'KJ',
          percent: (parseFloat(this.food.energy) / 8400 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '能量(KCal)',
          value: this.food.per_calorie + 'KCal',
          percent: (parseFloat(this.food.per_calorie) / 2000 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '蛋白质',
          value: this.food.protein + 'g',
          percent: (parseFloat(this.food.protein) / 60 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '脂肪',
          value: this.food.fat + 'g',
          percent: (parseFloat(this.food.fat) / 60 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '碳水化合物',
          value: this.food.carbohydrates + 'g',
          percent: (parseFloat(this.food.carbohydrates) / 300 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '膳食纤维',
          value: this.food.dietary_fiber + 'g',
          percent: (parseFloat(this.food.dietary_fiber) / 25 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '维生素C',
          value: this.food.vitaminC + 'mg',
          percent: (parseFloat(this.food.vitaminC) / 100 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '钙',
          value: this.food.calcium + 'mg',
          percent: (parseFloat(this.food.calcium) / 800 * 100).toFixed(2) + '%',
        });
        this.nutrition.push({
          item: '钠',
          value: this.food.sodium + 'mg',
          percent: (parseFloat(this.food.sodium) / 2000 * 100).toFixed(2) + '%',
        });
      },
    });

    uni.getStorage({
      key: 'range',
      success: (rec) => {
        this.min = rec.data[0];
        this.max = rec.data[1];
      },
    });
  },
  methods: {
    refresh: function() {
      this.ordered_food = uni.getStorageSync('meal-list');
      console.log('refresh');
    },
    refreshLikes: function() {
      uni.request({
        url: 'https://calorie.liyangpu.com:8003/dish/detail/',
        method: 'GET',
        header: {
          Authorization: 'Token ' + uni.getStorageSync('token'),
        },
        data: {
          dish_id: this.food.id,
        },
        success: (res) => {
          this.food = res.data.data.dish;
          this.like_count = this.food.like;
          this.dislike_count = this.food.dislike;
        },
      });
    },
    start: function(event) {
      this.X = event.touches[0].pageX;
      console.log(this.X);
    },
    end: function(event) {
      if (this.tempX > 50) {
        this.isimg = true;
      }
      if (this.tempX < -50) {
        this.isimg = false;
      }
      console.log(this.isimg);
    },
    move: function(event) {
      this.tempX = event.touches[0].pageX - this.X;
      console.log(this.tempX);
    },
    taptag: function(index) {
      console.log(this.tags[index]);
      uni.$emit('search_key', this.tags[index].name);
      wx.navigateBack();
    },
    mylist: function() {
      console.log('mylist');
      this.IsShow = true;
      this.ordered_food = uni.getStorageSync('meal-list');
    },
    dislike: function() {
      return request('/dish/like/', 'POST', {
        dish_id: this.food.id,
        like: 0,
        dislike: 1,
      }).then(res => {
        console.log(res);
        this.refreshLikes();
      });
    },
    like: function() {
      return request('/dish/like/', 'POST', {
        dish_id: this.food.id,
        like: 1,
        dislike: 0,
      }).then(res => {
        console.log(res);
        this.refreshLikes();
      });
    },
    add: function() {
      uni.showToast({
        title: '添加成功',
      });
      console.log('add');
      var OrderedFood = uni.getStorageSync('meal-list');
      for (let i = 0; i < OrderedFood.length; i++) {
        if (OrderedFood[i].name === this.food.name) {
          OrderedFood[i].sum += 1;
          uni.setStorageSync('meal-list', OrderedFood);
          return;
        }
      }
      OrderedFood.push({
        name: this.food.name,
        cal: this.food.calorie,
        sum: 1,
        picture: this.food.picture,
        id: this.food.id,
      });
      uni.setStorageSync('meal-list', OrderedFood);
    },
  },
};
</script>

<style>
  .content {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .head {
    display: flex;
    border: #000000 1rpx solid;
    justify-content: center;
    font-size: 26rpx;
    font-weight: 400;
    line-height: 200%;
    color: #505050;
    width: 750rpx;
    position: fixed;
    background-color: #FFFFFF;
    z-index: 3;
  }

  .imgarea {
    /* margin-top: 10rpx; */
    /* height: 700rpx; */
    /* width: 600rpx; */
    /* margin-left: 75rpx; */
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    /* background-color: #000000; */
  }

  /* .img {
    position: relative;
    border-radius: 20px;
    width: 600rpx;
    height: 600rpx;
    position: relative;
    top: 50rpx;
    animation: showimg 0.5s;
  }
  */
  .img {
    position: relative;
    width: 100%;
    border-radius: 0 0 40% 40%;
    text-align: center;
    /*    width: 600rpx;
    height: 600rpx; */
    /* top: 50rpx; */
    animation: showimg 0.5s;
  }

  .tab {
    /* position: relative; */
    top: 50rpx;
    width: 600rpx;
    /* height: 600rpx; */
    animation: showtab 0.5s;
    line-height: 37rpx;
    overflow: hidden;
    margin-top: 10px;
  }

  @keyframes showimg {
    from {
      right: 600rpx;
    }

    to {
      right: 0;
    }
  }

  @keyframes showtab {
    from {
      left: 600rpx;
    }

    to {
      left: 0;
    }
  }

  .blackspot {
    background-color: #000000;
    width: 20rpx;
    height: 20rpx;
    border-radius: 10rpx;
  }

  .whitespot {
    width: 20rpx;
    height: 20rpx;
    border-radius: 10rpx;
    background-color: #b0b0b0;
  }

  .detail {
    margin-top: 30rpx;
  }

  .name {
    font-size: 53rpx;
    font-weight: 800;
    color: #505050;
    padding-right: 10rpx;
    padding-top: 10rpx;
    padding-bottom: 10rpx;
  }
.equ{
  position: relative;
  left:0rpx;
  top:0rpx;
  width: 100rpx;
  font-size: 40rpx;
  font-weight: 800;
  color: #505050;
  line-height: 70rpx;
}
.eimag{
  position: absolute;
  right:-80rpx;
  top:0;
  bottom:0;
  width: 80rpx;
  height: 64rpx;
  margin:auto;
}
  .cal {
    width: 230rpx;
    font-size: 30rpx;
    text-align: center;
    background-color: #f3e2d2;
    border-radius: 10rpx;
    color: #505050;
    line-height: 50rpx;
  }

  .opinion {
    align-self: flex-end;
    margin-right: 50rpx;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 80rpx;
    opacity: 0.7;
  }

  .countimg {
    width: 40rpx;
    height: 40rpx;
    margin-left: 50rpx;
    margin-right: 10rpx;
  }

  .count {
    line-height: 80rpx;
    font-size: 30rpx;
  }

  .tags {
    display: flex;
    align-self: center;
    width: 550rpx;
    margin-top: 30rpx;
    flex-wrap: wrap;
  }

  .tag {
    background-color: #FFFFFF;
    height: 50rpx;
    border-radius: 20rpx;
    margin-right: 30rpx;
    font-size: 30rpx;
    line-height: 50rpx;
    padding-left: 30rpx;
    padding-right: 30rpx;
    border: #B0B0B0 1rpx solid;
    margin-bottom: 20rpx;
  }

  .bottom {
    position: fixed;
    width: 15%;
    height: 30%;
    z-index: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-end;
    bottom: 10px;
    right: 0;
  }

  .button {
    width:35px;
    height:35px;
    margin:10px;
  }

  .buttonarea {
    margin-top: 10px;
    width: 600rpx;
    overflow: hidden;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    /* align-items: center; */
  }

  .likebutton {
    font-size: 30rpx;
    justify-content: center;
    width: 40%;
    height: 30px;
    margin: 0;
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    align-items: center;
    /* margin: auto; */
    background-color: #efe5df;
    border: 0;
    outline:none;
    /* display: inline-block; */
  }

  .orders {
    width: 100%;
    position: fixed;
    right: 0;
    bottom: 0;
    z-index: 5;
  }

  .dishnames {
    color: #000000;
    font-size: 25rpx;
    line-height: 45rpx;
    height: 45rpx;
    font-weight: 350;
    margin-left: 40rpx;
  }

  .operation {
    background-color: rgba(219, 207, 202, 1);
    border-radius: 0 30px 0 0;
    box-shadow: 2px -0.5px 4px 0px rgba(0, 0, 0, 0.1);
    height: 110rpx;
  }

  .likeimg{
    height: 20px;
    width: 20px;
    margin-right: 5px;
    justify-content: center;
    align-items: center;
    padding: auto;
  }
</style>
