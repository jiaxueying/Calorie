<template>
    <div class="back" @tap="tap">
     <button size="mini" style="background-color: #59453D;color: #FFFFFF;">MIN</button>
     <p style="margin-top: 4px;">&</p>
     <button size="mini" >MAX</button>
    </div>
</template>

<script>
  export default {
    props: [],
    methods: {
      tap:function(){
        this.$emit('tap1',"");
      }
    }
  }
</script>

<style>
  .back{
    position:absolute;
    left: 15%;
    top:170%;
    border:1px solid #59453d;
    border-radius: 25px;
    width:200px;
    height: 35px;
    text-align: center;
    vertical-align: middle;
    margin-top: 0px;
    display:inline-flex
  }
  button{
    position: relative;
    display:inline-block;
    height:25px;
    margin-top: 5px;
    
  }
</style>
