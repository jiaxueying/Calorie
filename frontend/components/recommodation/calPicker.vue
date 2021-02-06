<template>
  <view>
    <picker
      mode="multiSelector"
      :range="cal"
      :value="index"
      @change="pass"
    >
      <slot/>
    </picker>
  </view>
</template>

<script>
export default {
  data() {
    return {
      cal: [
        [100, 200, 300, 400, 500, 600, 700, 800, 900],
        [100, 200, 300, 400, 500, 600, 700, 800, 900],
      ],
      index: [0, 0],
    };
  },
  methods: {
    pass: function(event) {
      this.index = event.detail.value;
      this.$emit('refresh', this.cal, this.index);
    },
  },
};
</script>

<style>
</style>
