<template>
  <view>
    <view class="list">
      <image
        class="listImg"
        src="../../static/img.png"
        mode=""
      />
      <view
        class=""
        style="flex: 1;"
      >
        <view class="title">
          {{ foodname }}     <text>{{ calories }}kcal</text>
        </view>
        <view class="content">
          <view class="label">
            {{ canteen }}
          </view>
          <view class="label">
            {{ location }}
          </view>
          <view class="label">
            {{ state }}
          </view>
        </view>
        <view class="bottom">
          <view class="item">
            <button class="likeButton">
              <image style="width:40rpx;height:40rpx;opacity: 0.5;" src="../../static/happy.png"></image>
              LIKE {{like}}
            </button>
          </view>
          <view class="item">
            <button class="dislikeButton">
              <image style="width:40rpx;height:40rpx;opacity: 0.4;" src="../../static/dislike.png"></image>
              DISLIKE {{dislike}}
            </button>
          </view>
        </view>
      </view>
    </view>
  </view>
</template>

<script>
  export default {
    data() {
      return {
          like:666,
          dislike:555
      }
    },
    methods: {

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
    background-size: 50rpx;
    border: 0rpx;
    display:inline-flex;
    align-items: center;
  }
  .dislikeButton{
	  height: 50rpx;
	  font-size: 20rpx;
	  background-size: 50rpx;
	  border: 0rpx;
    display:inline-flex;
    align-items: center;
  }
</style>
