<template>
  <view>
    <picker mode="multiSelector" :range="cal" :value="value">
      <slot></slot>
    </picker>
  </view>
</template>

<script>
export default{
  data() {
    return{
      cal:[
        [1,2,3,4,5,6],
        [7,8,9,10,11,12]
      ],
      value:[0,0],
    }
  },
}
</script>

<style>
</style>
