<template>
	<view>
    <view class="text-area">
      <text class="title">施工中</text>
      <text class="title">请选择要跳转的页面</text>
    </view>
    <view class="button">
      <dl>
        <dt>
          <navigator url="../recommondation/range">范围选择页面</navigator>
        </dt>
        <text>\n</text>
        <dt>
          <navigator url="../recommondation/list">今日推荐界面</navigator>
        </dt>
        <text>\n</text>
        <dt>
          <navigator url="../recommondation/shake">摇一摇页面</navigator>
        </dt>
      </dl>
    </view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
.text-area{
  justify-content: center;
  margin-top: 30px;
  margin-bottom: 30px;
}
.title{
  display: flex;
  justify-content: center;
  font-size: 30px;
  margin: 20px;
}
.button{
  margin-top: 20px;
  display: flex;
  justify-content: center;
}
</style>
