<!-- TODO:change onLoad -->

<template>
	<view>
		<DateChooser></DateChooser>
    <MealClassifier :name="breakfast_name" :meallist="breakfast"  v-if="breakfast.length"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="lunch_name" :meallist="lunch" v-if="lunch.length"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="dinner_name" :meallist="dinner" v-if="dinner.length"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <view v-if="!breakfast.length && !lunch.length && !dinner.length">
      {{error}}
    </view>
	</view>
</template>

<script>
  import MealClassifier from "../../components/for-meallist/meal-classifier.vue"
  import DateChooser from "../../components/all/date-chooser.vue"
  import {request, backendurl} from "../../common/helper.js"
	export default {
    components: {
      DateChooser,
      MealClassifier
    },
		data() {
			return {
        shows: null,
        breakfast_name: "早餐",
        lunch_name: "午餐",
        dinner_name: "晚餐",
        error:"该日期没有菜单哦～",
        breakfast: [],
				lunch: [],
        dinner: []
			}
		},
		methods: {
			searchDate:function(date) {
        console.log('searched date:' + date);
        request('/canteen/menuview', 'GET', {
          'Content-Type': 'application/x-www-form-urlencoded',
          'token':uni.getStorageSync('token'),
          'date':date
          }).then(res => {
          if(res[1].statusCode != 404) {
            console.log('OK!');
            this.breakfast = res[1].data.bre.dishes;
            this.lunch = res[1].data.lun.dishes;
            this.dinner = res[1].data.din.dishes;
          }
        })
      }
		},
    onLoad(options) {
      uni.$on('date changed', this.searchDate);
      this.shows = JSON.parse(options.booleans);
      console.log(this.shows);
      // 从后端获取breakfast等
      const date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();
      month = month > 9 ? month : '0' + month;;
      day = day > 9 ? day : '0' + day;
      var d = `${year}-${month}-${day}`;
      this.searchDate(d);
    }
	}
</script>

<style>

</style>
