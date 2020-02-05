<template>
    <div class="back" @tap="tap">
     <button size="mini" style="background-color: #59453D;color: #FFFFFF;">{{MIN}}</button>
     <text>&</text>
     <button size="mini" >{{MAX}}</button>
    </div>
</template>

<script>
  export default {
    props: ['MIN','MAX'],
    methods: {
      
    }
  }
</script>

<style>
  .back{
    border:1px solid #59453d;
    border-radius: 25px;
    width:200px;
    display:inline-flex;
    line-height: 35px;
    vertical-align: middle;
    
  }
  button{
    line-height: 35px;
    vertical-align: middle;
    margin-top: 5px;
    margin-bottom: 5px;
  }
  text{
    font-size: 18px;
    margin-top: 5px;
    margin-bottom: 5px;
    
  }
</style>
