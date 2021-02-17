<template>
  <view class="SearchHistory">
    <view class="SearchHistoryName">●&nbsp;{{ viewname }}</view>
    <view
      class="historyDetail"
      v-for="n in Names"
      :key="n"
    >
      <rec-button :name="n.name"/>
    </view>
  </view>
</template>

<script>
import RecButton from './rec-button.vue';
export default {
  components: {
    RecButton,
  },
  props: {
    viewname: {
      type: String,
      default: '',
    },
    Names: {
      type: Array,
      default: () => [],
    },
  },
  data() {
    return {
    };
  },
  onLoad() {

  },
  methods: {

  },
};
</script>

<style>
.SearchHistory {
float:left;
width: 100%;
padding-left: 20rpx;
padding-right: 20rpx;
margin-top: 25rpx;
box-sizing:border-box;
}
.SearchHistoryName {
    padding: 15rpx 0;
    color:#555C60;
  }
  .historyDetail {
    padding-left:20rpx;
  }
</style>
