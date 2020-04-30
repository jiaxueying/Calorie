<!-- TODO:change onLoad -->

<template>
	<view>
		<DateChooser></DateChooser>
    <view v-if="breakfast.dishes.length == 0 && lunch.dishes.length == 0 && dinner.dishes.length == 0" class="warning">
      {{error}}
    </view>
    <MealClassifier :name="breakfast_name" :meallist="breakfast.dishes"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="lunch_name" :meallist="lunch.dishes"
      :modifyable="shows.modifyable" :countable="shows.countable">
    </MealClassifier>
    <MealClassifier :name="dinner_name" :meallist="dinner.dishes"
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
        hasMenu: false,
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
            console.log(res)
            this.breakfast = res[1].data.bre;
            this.lunch = res[1].data.lun;
            this.dinner = res[1].data.din;
            this.hasMenu = true;
          }
          else {
            this.hasMenu = false;
            this.breakfast = {menu_id:0, dishes:[]};
            this.lunch = {menu_id:0, dishes:[]};
            this.dinner = {menu_id:0, dishes:[]};
          }
        })
      },
      getIDs:function(a) {
        let ids = [];
        for(let i = 0; i < a.length; i++) {
          ids.push(a[i].dish_id);
        }
        return ids;
      },
      changeList:function(c) {
        console.log("changing list");
        console.log(c);
        let changed_id = 0;
        let bre_ids = [], lun_ids = [], din_ids = [], changed_ids = [];
        if(c.time === "\"早餐\"") {
          console.log("早餐 changed");
          this.breakfast.dishes = c.list;
          changed_id = this.breakfast.menu_id;
          bre_ids = this.getIDs(c.list);
          changed_ids = bre_ids;
        }
        else if(c.time === "\"午餐\"") {
          console.log("午餐 changed");
          this.lunch.dishes = c.list;
          changed_id = this.lunch.menu_id;
          lun_ids = this.getIDs(c.list);
          changed_ids = lun_ids;
        }
        else if(c.time === "\"晚餐\"") {
          console.log("晚餐 changed");
          this.dinner.dishes = c.list;
          changed_id = this.dinner.menu_id;
          din_ids = this.getIDs(c.list);
          changed_ids = din_ids;
        }
        console.log(this.hasMenu)
        if(this.hasMenu == false) {
          console.log("add menu")
          console.log(this.date)
          console.log(bre_ids)
          console.log(lun_ids)
          console.log(din_ids)
          this.hasMenu = true;
          request("/canteen/addmenu/", 'POST', {
            date:this.date, 
            bre:JSON.stringify(bre_ids),
            lun:JSON.stringify(lun_ids),
            din:JSON.stringify(din_ids)
          })
        }
        else {
          console.log("modify menu")
          console.log(changed_id)
          console.log(changed_ids)
          request("/canteen/editmenu/", 'POST', {
            menu_id: changed_id,
            dishes: JSON.stringify(changed_ids)
          })
        }
        this.searchDate(this.date);
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
	.warning{
    margin-left: 35%;
	}

</style>
