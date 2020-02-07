<template>
	<view style="display: flex;flex-direction: column;align-items: center;">
		<navigator url="indexOfRecommondation" open-type="redirect">推荐功能</navigator>
    <navigator url="indexOfSearch" open-type="redirect">查询功能</navigator>
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
navigator{
  margin-top: 50px;
  font-size: 30px;
  color: #968f8c;
}
</style>
