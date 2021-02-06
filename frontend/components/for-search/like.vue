<template>
  <view>
    <view class="list">
      <image
        class="listImg"
        :src="'https://nkucalorie.top:8000'+food.picture"
        mode="aspectFill"
        @tap="detail"
      />
      <view
        class="info"
        style="flex: 1;"
      >
        <view
          class="title"
          @tap="detail"
        >
          {{ food.name }}
          <text class="kal">{{ food.calorie }}kcal</text>
        </view>
        <view class="content">
          <view
            class="label"
            v-for="tag in food.tag"
            :key="tag.id"
            @tap="search_tag(tag)"
          >
            {{ tag.name }}
          </view>
        </view>

        <view class="bottom">
          <view class="item">
            <button
              class="likeButton"
              @tap="like_"
            >
              <image
                :src="'../../static/like.png'"
                class="likeimg"
              />{{ food.like }}</image>
            </button>
          </view>
          <view class="item">
            <button
              class="unlikeButton"
              @tap="dislike_"
            >
              <image
                :src="'../../static/unlike.png'"
                class="unlikeimg"
              />{{ food.dislike }}</image>
            </button>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
import {
  like,
  dislike,

  backendUrl,
  request,
} from '@/common/helper.js';

export default {
  props: ['food', 'menu_id'],
  data() {
    return {
      isChoose: false,
    };
  },
  methods: {
    like_() {
      console.log('like clicked');
      like(this.food.id);
      uni.$emit('get_likes', this.food.id);
    },
    dislike_() {
      console.log('dislike clicked');
      dislike(this.food.id);
      uni.$emit('get_likes', this.food.id);
    },
    detail() {
      console.log(this.food);
      this.$parent.IsShow = false;
      wx.navigateTo({
        url: '../others/detail?id=' + this.food.id,
      });
    },
    search_tag(v) {
      console.log('tag clicked');
      uni.$emit('search_tag', v.name);
    },
  },
};
</script>

<style lang="less">
  .list {
    padding: 10upx 30upx;
    margin: 5px 0;
    display: flex;
    box-shadow: darkgrey 0 0px 5px;

    .title {
      font-size: 36upx;
      color: #333;
      margin: 10upx 0upx;

      text {
        font-size: 30upx;
        color: #666;
        padding-top: 10upx;
      }
    }

    .content {
      padding-left: 0upx;
      margin-bottom: 10upx;
      padding-bottom: 10upx;

      .label {
        height: 40upx;
        line-height: 40upx;
        padding: 0 10upx;
        border-radius: 20upx;
        color: #333;
        border: 1upx solid #DCDCDC;
        font-size: 24upx;
        display: inline-block;
        margin-right: 5upx;
      }
    }
  }

  .listImg {
    width: 180upx;
    height: 180upx;
    // margin-right: 30upx;
    border-radius: 10rpx;
    margin: auto;
  }

  // .bottom {
  //   display: flex;
  //   padding: 0upx 0;

  //   .item {
  //     flex: 1;
  //     color: #666;
  //     font-size: 24upx;

  //     image {
  //       width: 40upx;
  //       height: 40upx;
  //       margin-right: 10upx;
  //     }
  //   }
  // }

  .bottom {
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    padding: 0upx 0;

    .item {
      // flex: 1;
      color: #666;
      font-size: 24upx;

      image {
        width: 30upx;
        height: 30upx;
        margin-right: 10upx;
      }
    }
  }

  .likeButton {
    height: 50rpx;
    text-align: center;
    font-size: 25rpx;
    // background-image: url(https://nkucalorie.top:8000/media/static/like.png);
    // background-color: rgb(217, 207, 202);
    // background-repeat: no-repeat;
    // background-size: 40rpx;
    // background-position-y: 4rpx;
    border: 0rpx;
    padding: 0;
    margin-right: 10px;
    display: flex;
    background-color: rgba(255, 255, 255, 0);
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }

  .unlikeButton {
    height: 50rpx;
    text-align: center;
    font-size: 25rpx;
    border: 0rpx;
    padding: 0;
    margin-right: 10px;
    background-color: rgba(255, 255, 255, 0);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }

  .info {
    margin-left: 30rpx;
  }

  .kal {
    margin-left: 30rpx;
    // text-align: right;
  }

  .likeimg {
    height: 15px;
    width: 15px;
    margin-right: 5px;
    justify-content: center;
    align-items: center;
    padding: auto;
  }

  .unlikeimg {
    height: 20px;
    width: 20px;
    margin-right: 5px;
    justify-content: center;
    align-items: center;
    padding: auto;
  }
</style>
