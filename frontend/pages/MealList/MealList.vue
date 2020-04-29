<!-- TODO:change onLoad -->

<template>
	<view>
		<DateChooser></DateChooser>
    <view v-if="!breakfast.length && !lunch.length && !dinner.length">
      {{error}}
    </view>
    <MealClassifier :name="breakfast_name" :meallist="breakfast"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="lunch_name" :meallist="lunch"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="dinner_name" :meallist="dinner"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
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
        date: "",
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
        this.date = date;
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
      },
      changeList:function(c) {
        console.log("changing list");
        console.log(c);
        if(c.time === "\"早餐\"") {
          console.log("早餐 changed");
          this.breakfast = c.list;
        }
        else if(c.time === "\"午餐\"") {
          console.log("午餐 changed");
          this.lunch = c.list;
        }
        else if(c.time === "\"晚餐\"") {
          console.log("晚餐 changed");
          this.dinner = c.list;
        }
        let bre_ids = [], lun_ids = [], din_ids = [];
        for(let i = 0; i < this.breakfast.length; i++) {
          bre_ids.push(this.breakfast[i].dish_id);
        }
        for(let i = 0; i < this.lunch.length; i++) {
          lun_ids.push(this.lunch[i].dish_id);
        }
        for(let i = 0; i < this.lunch.length; i++) {
          din_ids.push(this.lunch[i].dish_id);
        }
        console.log(this.date)
        console.log(bre_ids)
        console.log(lun_ids)
        console.log(din_ids)
        request("/canteen/addmenu/", 'POST', {
          date:this.date, 
          bre:JSON.stringify(bre_ids),
          lun:JSON.stringify(lun_ids),
          din:JSON.stringify(din_ids)
        })
      }
		},
    onLoad(options) {
      uni.$on('date changed', this.searchDate);
      uni.$on('changeMealList', this.changeList);
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
