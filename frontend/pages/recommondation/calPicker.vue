<template>
  <view>
    <picker mode="multiSelector" :range='cal' :value='index' @change="pass" @columnchange="changecolumn">
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
      cal2:
      [
        [1,2,3,4,5,6,7,8,9],
        [2,3,4,5,6,7,8,9],
        [3,4,5,6,7,8,9],
        [4,5,6,7,8,9],
        [5,6,7,8,9],
        [6,7,8,9],
        [7,8,9],
        [8,9],
        [9]
      ],
      index:[0,0]
    }
  },
  methods:{
    pass:function(event){
      this.index=event.detail.value;
      this.$emit('refresh',this.cal,this.index);
    },
    changecolumn:function(event){
      if(event.detail.column==0)
      {
        this.cal[1]=this.cal2[event.detail.value];
      }
      console.log(event.detail.column,event.detail.value)
    }
  }
}
</script>

<style>
</style>
