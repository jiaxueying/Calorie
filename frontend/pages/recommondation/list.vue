<template>
  <view>
    <view>
      <Meal/>
    </view>
  </view>
</template>

<script>
import Meal from '../../components/recommodation/recommend.vue';
export default {
  components: {
    Meal,
  },
  data() {
    return {

    };
  },

  onPullDownRefresh() {

  },
  methods: {
  },
};
</script>

<style>
</style>
