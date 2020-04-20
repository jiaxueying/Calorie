 export default {
   	data() {
  		return {
        min:'',
        max:''
  		}
  	},
    methods:{
     
    },
    created() {
      uni.getStorage({
        key:'range',
        success: (res) => {
          this.min=res.data[0]
          this.max=res.data[1]
        }
      })
    }
  }