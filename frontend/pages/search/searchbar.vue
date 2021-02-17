<template>
  <view
    class="search"
    :style="{ backgroundColor: backgroundColor }"
  >
    <!-- <view class="button" :class="{ active: show || active }" @click="showall">重置</view> -->
    <view
      class="content"
      :style="{ 'border-radius': radius + 'px', border: border }"
    >
      <view
        class="content-box"
        :class="{ center: mode === 2 }"
      >
        <text class="icon icon-search">&#xe61c;</text>
        <input
          class="input"
          :class="{ center: !active && mode === 2 }"
          :focus="isFocus"
          :placeholder="placeholder"
          v-model="inputVal"
          @focus="focus"
          @blur="blur"
        >
        <!-- <view v-if="!active && mode === 2" class="input sub" @click="getFocus">请输入搜索内容</view> -->
        <text
          v-if="isDelShow"
          class="icon icon-del"
          @click="clear"
        >&#xe644;</text>
      </view>
      <view
        v-show="(active && show && button === 'inside') || (isDelShow && button === 'inside')"
        class="searchBtn"
        @click="search"
      >搜索</view>
    </view>
    <view
      v-if="button === 'outside'"
      class="button"
      :class="{ active: show || active }"
      @click="search"
    >
      <view class="button-item">{{ !show ? searchName : '搜索' }}</view>
    </view>
  </view>
</template>

<script>
export default {
  props: {
    mode: {
      type: Number,
      default: 1,
    },
    button: {
      type: String,
      default: 'outside',
    },
    show: {
      type: Boolean,
      default: true,
    },
    radius: {
      type: String,
      default: '60',
    },
    placeholder: {
      type: String,
      default: '请输入搜索内容',
    },
    backgroundColor: {
      type: String,
      default: 'rgb(244, 241, 236)',
    },
    border: {
      type: String,
      default: '1px #f5f5f5 solid',
    },
    val: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      active: false,
      inputVal: '',
      searchName: '取消',
      isDelShow: false,
      isFocus: false,
    };
  },
  methods: {
    focus() {
      this.active = true;
    },
    blur() {
      this.isFocus = false;
      if (!this.inputVal) {
        this.active = false;
      }
    },
    clear() {
      this.inputVal = '';
      this.active = false;
      this.showall();
    },
    getFocus() {
      this.isFocus = true;
    },
    search() {
      if (!this.inputVal) return;
      console.log(this.inputVal);
      this.$emit('search', this.inputVal);
    },
    showall() {
      console.log('CAN');
      this.inputVal = '';
      this.$emit('showall');
    },
  },
  watch: {
    inputVal(newVal) {
      if (newVal) {
        this.searchName = '搜索';
        this.isDelShow = true;
      } else {
        this.searchName = '取消';
        this.isDelShow = false;
        this.showall();
      }
    },
    val(fatherVal) {
      this.inputVal = fatherVal;
      if (fatherVal) this.active = true;
    },
  },
};
</script>

<style lang="scss" scoped>
  .search {
    display: flex;
    width: 100%;
    border-bottom: 1px #f5f5f5 solid;
    box-sizing: border-box;
    padding: 15upx;
    font-size: $uni-font-size-base;
    background: #fff;
    position: fixed;
    top:96rpx;
    left:0rpx;
    background: #fff;
    z-index: 999;

    .content {
      display: flex;
      align-items: center;
      width: 100%;
      height: 60upx;
      border: 1px #ccc solid;
      background: #fff;
      overflow: hidden;
      transition: all 0.2s linear;
      border-radius: 30px;

      .content-box {
        width: 100%;
        display: flex;
        align-items: center;
        background-color: #FFF;

        &.center {
          justify-content: center;
        }

        .icon {
          padding: 0 15upx;

          &.icon-del {
            font-size: 38upx;

          }
        }

        .input {
          width: 100%;
          max-width: 100%;
          line-height: 60upx;
          height: 60upx;
          color: #333;
          font-size: 28upx;

          // transition: all 0.2s linear;
          &.center {
            width: 200upx;
          }

          &.sub {
            // position: absolute;
            width: auto;
            color: grey;
          }
        }
      }

      .searchBtn {
        height: 100%;
        flex-shrink: 0;
        padding: 0 30upx;
        background: $uni-color-success;
        line-height: 60upx;
        color: #fff;
        border-left: 1px #ccc solid;
        transition: all 0.3s;
      }
    }

    .button {
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      flex-shrink: 0;
      width: 0;
      transition: all 0.2s linear;
      white-space: nowrap;
      overflow: hidden;

      &.active {
        padding-left: 15upx;
        width: 100upx;
        // color: #8BC34A;
      }
    }
  }

  @font-face {
    font-family: 'iconfont';
    src: url('https://at.alicdn.com/t/font_989023_efq0mtli526.ttf') format('truetype');
  }

  .icon {
    font-family: iconfont;
    font-size: 32upx;
    font-style: normal;
    color: #999;
  }
</style>
