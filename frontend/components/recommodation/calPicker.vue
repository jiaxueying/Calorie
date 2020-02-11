<template>
  <view>
    <picker mode="multiSelector" :range='cal' :value='index' @change="pass">
      <slot></slot>
    </picker>
  </view>
</template>

<script>
export default{
  data() {
    return{
      cal:[
        [1,2,3,4,5,6,7,8,9],
        [1,2,3,4,5,6,7,8,9]
      ],
      index:[0,0]
    }
  },
  methods:{
    pass:function(event){
      this.index=event.detail.value;
      this.$emit('refresh',this.cal,this.index);
    }
  }
}
</script>

<style>
</style>
