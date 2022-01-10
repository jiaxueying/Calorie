<!-- TODO:emit changing -->

<template>
  <view>
    <picker
      mode="date"
      :value="date"
      :start="startDate"
      :end="endDate"
      @change="bindDateChange"
    >
      <view class="uni-input">{{ date }}</view>
    </picker>
  </view>
</template>

<script>
export default {
  data() {
    const currentDate = this.getDate({
      format: true,
    });
    return {
      date: '请在这里选择订餐日期哦',
    };
  },
  computed: {
    startDate() {
      return this.getDate('start');
    },
    endDate() {
      return this.getDate('end');
    },
  },
  methods: {
    bindDateChange: function(e) {
      this.date = e.target.value;
      uni.$emit('date change', this.date);
      console.log('date changed ' + this.date);
    },
    getDate(type) {
      const date = new Date();
      let year = date.getFullYear();
      let month = date.getMonth() + 1;
      let day = date.getDate();

      if (type === 'start') {
        year = year - 60;
      } else if (type === 'end') {
        year = year + 2;
      }
      month = month > 9 ? month : '0' + month;
      day = day > 9 ? day : '0' + day;
      return `${year}-${month}-${day}`;
    },
  },
  onLoad() {
  },
};
</script>

<style>
  picker{
    text-align: center;
    border: #59453D 7rpx solid;
    border-radius: 40rpx;
    font-size: 1.0em;
    color:#59453D;
  }
</style>
