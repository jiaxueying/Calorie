<!-- TODO:change onLoad -->

<template>
	<view>
		<DateChooser></DateChooser>
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
        breakfast: [
          {"name":"菜品1", "pic":"logo.png", "count":10},
          {"name":"菜品2", "pic":"logo.png", "count":10},
          {"name":"菜品3", "pic":"logo.png", "count":10},
          {"name":"菜品4", "pic":"logo.png", "count":10},
          {"name":"菜品5", "pic":"logo.png", "count":10},
          {"name":"菜品6", "pic":"logo.png", "count":10},
          {"name":"菜品7", "pic":"logo.png", "count":10},
          {"name":"菜品8", "pic":"logo.png", "count":10},
        ],
				lunch: [
          {"name":"菜品9", "pic":"logo.png", "count":10},
          {"name":"菜品10", "pic":"logo.png", "count":10},
          {"name":"菜品11", "pic":"logo.png", "count":10},
          {"name":"菜品12", "pic":"logo.png", "count":10},
          {"name":"菜品13", "pic":"logo.png", "count":10},
          {"name":"菜品14", "pic":"logo.png", "count":10},
          {"name":"菜品15", "pic":"logo.png", "count":10},
          {"name":"菜品16", "pic":"logo.png", "count":10},
        ],
        dinner: [
          {"name":"菜品17", "pic":"logo.png", "count":10},
          {"name":"菜品18", "pic":"logo.png", "count":10},
          {"name":"菜品19", "pic":"logo.png", "count":10},
          {"name":"菜品20", "pic":"logo.png", "count":10},
          {"name":"菜品21", "pic":"logo.png", "count":10},
          {"name":"菜品22", "pic":"logo.png", "count":10},
          {"name":"菜品23", "pic":"logo.png", "count":10},
          {"name":"菜品24", "pic":"logo.png", "count":10},
        ]
			}
		},
		methods: {
			
		},
    onLoad(options) {
      this.shows = JSON.parse(options.booleans);
      console.log(this.shows);
      // 从后端获取breakfast等
    }
	}
</script>

<style>

</style>
