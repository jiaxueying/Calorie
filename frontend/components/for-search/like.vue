<template>
  <view>
    <view class="list">
      <image
        class="listImg"
        :src="'https://nkucalorie.top:8000'+food.picture"
        mode=""
        @tap="detail"
      />
      <view
        class=""
        style="flex: 1;"
      >
        <view class="title" @tap="detail">
          {{ food.name }}     
          <text>\n{{ food.calorie }}kcal</text>
        </view>
        <view class="content" >
          <view class="label" v-for="tag in food.tag" :key="tag.id" @tap="search_tag(tag)">
            {{tag.name}}
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
    props: ['food', 'menu_id'],
    data() {
      return {
        isChoose:false,
      }
    },
    methods: {
      like_() {
        console.log("like clicked");
        like(this.food.id);
        uni.$emit("search_key","");
      },
      dislike_() {
        console.log("dislike clicked");
        dislike(this.food.id);
        uni.$emit("search_key","");
      },
      detail() {
        console.log(this.food);
        this.$parent.IsShow = false;
        wx.navigateTo({
          url:'../others/detail?foodDetail='+JSON.stringify(this.food) + '&id=' + this.menu_id,
        });
      },
      search_tag(v) {
        console.log("tag clicked");
        uni.$emit("search_key", v.name);
      }
    },
  }
</script>

<style lang="less">
    .list{
        padding: 40upx 30upx;
        display: flex;
        .title{
            font-size: 36upx;
            color: #333;
            margin: 10upx 80upx;
            text{
                font-size: 30upx;
                color: #666;
                padding-top: 10upx;
            }
        }
        .content{
            padding-left: 80upx;
            padding-bottom: 20upx;
            .label{
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
        background-image: url(https://nkucalorie.top.com:8000/media/static/like.png);
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
        background-image: url(https://nkucalorie.top.com:8000/media/static/dislike.png);
        background-color: #FFFFFF;
        background-repeat: no-repeat;
        background-size: 40rpx;
        border: 0rpx;
        background-position-y: 4rpx;
        padding: 0;
        padding-left: 38rpx;
    }
</style>
