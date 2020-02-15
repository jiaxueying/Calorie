<template>
  <view>
    <view class="list">
      <image
        class="listImg"
        src="../../static/chocolate.png"
        mode=""
      />
      <view
        class=""
        style="flex: 1;"
      >
        <view class="title">
          {{ food.name }}     <text>{{ food.calorie }}kcal</text>
        </view>
        <view class="content">
          <view class="label" v-for="tag in food.tag" :key="tag.id" >
            {{tag.name}}
          </view>
        </view>
        
        <view class="bottom">
          <view class="item">
            <button class="likeButton" @tap="like_">
              LIKE {{ food.like }}
            </button>
          </view>
          <view class="item">
            <button class="unlikeButton" @tap="dislike_">
              DISLIKE {{ food.dislike }}
            </button>
          </view>
        </view>
      
      </view>
    </view>
  </view>
</template>

<script>
  import { like, dislike } from '@/common/helper.js';
  import { backendUrl, request } from '@/common/helper.js';
  export default {
    props: ['food'],
    data() {
      return {
        like:100,
        dislike:100,
        isChoose:flase
      }
    },
    methods: {
      like_() {
        console.log("like clicked");
        like(this.food.id);
      },
      dislike_() {
        console.log("dislike clicked");
        dislike(this.food.id);
      },
    }
  }
</script>

<style lang="less">
    .list{
        padding: 40upx 30upx;
        display: flex;
        .title{
            font-size: 28upx;
            color: #333;
            margin: 10upx 0;
            text{
                font-size: 24upx;
                color: #666;
                margin-left: 60upx;
            }
        }
        .content{
            padding-bottom: 20upx;
            border-bottom: 2upx solid #999;
            .label{
                height: 40upx;
                line-height: 40upx;
                padding: 0 10upx;
                border-radius: 20upx;
                color: #666;
                border: 2upx solid #333;
                font-size: 24upx;
                display: inline-block;
                margin-right: 20upx;
            }
        }
    }
    .listImg{
        width: 160upx;
        height: 160upx;
        margin-right: 30upx;
    }
    .bottom{
        display: flex;
        padding: 20upx 0 ;
        .item{
            flex: 1;
            color: #666;
            font-size: 24upx;
            image{
                width: 40upx;
                height: 40upx;
                margin-right: 10upx;
            }
        }
    }
    .likeButton {
        height: 50rpx;
        font-size: 20rpx;
        background-image: url(../../static/like.png);
        background-color: #FFFFFF;
        background-repeat: no-repeat;
        background-size: 40rpx;
        background-position-y: 4rpx;
        border: 0rpx;
        padding: 0;
    }
    .unlikeButton {
        height: 50rpx;
        font-size: 20rpx;
        background-image: url(../../static/sad.png);
        background-color: #FFFFFF;
        background-repeat: no-repeat;
        background-size: 40rpx;
        border: 0rpx;
        background-position-y: 4rpx;
        padding: 0;
        padding-left: 38rpx;
    }
</style>
