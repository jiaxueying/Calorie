<template>
	<view>
		<view>
      名称:<br><input v-model="name" class="input">
    </view>
    <view>
      能量(千卡):<br><input v-model="calorie" class="input">
    </view>
    <view>
      能量(千焦):<br><input v-model="energy" class="input">
    </view>
    <view>
      蛋白质(g):<br><input v-model="protein" class="input">
    </view>
    <view>
      脂肪(g):<br><input v-model="fat" class="input">
    </view>
    <view>
      碳水化合物(g):<br><input v-model="carbohydrates" class="input">
    </view>
    <view>
      膳食纤维(g):<br><input v-model="dietary_fiber" class="input">
    </view>
    <view>
      维生素C(mg):<br><input v-model="vitaminC" class="input">
    </view>
    <view>
      钙(mg):<br><input v-model="calcium" class="input">
    </view>
    <view>
      钠(mg):<br><input v-model="sodium" class="input">
    </view>
    <button @click="submit">提交</button>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				name:"",
        calorie:"",
        energy:"",
        protein:"",
        fat:"",
        carbohydrates:"",
        dietary_fiber:"",
        vitaminC:"",
        calcium:"",
        sodium:"",
        id:"",
        edit:false
			}
		},
    onLoad: function(res){
      if(res.edit=="true"){
        this.edit=true
        this.name=res.name
        this.calorie=res.calorie
        this.energy=res.energy
        this.protein=res.protein
        this.fat=res.fat
        this.carbohydrates=res.carbohydrates
        this.dietary_fiber=res.dietary_fiber
        this.vitaminC=res.vitaminC
        this.calcium=res.calcium
        this.sodium=res.sodium
        this.id=res.id
      }
    },
		methods: {
			submit:function(){
        if(this.edit){
          this.IngredientEdit()
        }
        else
        {
          this.IngredientAdd()
        }
      },
      IngredientAdd:function(){
        if(this.veri())
        {
          uni.request({
            url:'https://comi.hi.cn:8000/administrate/ingredient/add/',
            method:'POST',
            header:{
              'administrator-token':uni.getStorageSync('adtoken'),
              Authorization:"Token "+uni.getStorageSync("token")
            },
            data:{
              name:this.name,
              calorie:this.calorie,
              energy:this.energy,
              protein:this.protein,
              fat:this.fat,
              carbohydrates:this.carbohydrates,
              dietary_fiber:this.dietary_fiber,
              vitaminC:this.vitaminC,
              calcium:this.calcium,
              sodium:this.sodium
            },
            success:(res)=> {
              if(res.data.error=="Auth time out!")
              {
                uni.reLaunch({
                  url:"../user/administrator"
                })
                return
              }
              uni.redirectTo({
                url:"./IngredientManage"
              })
            }
          })
        }
      },
      IngredientEdit:function(){
        if(this.veri())
        {
          uni.request({
            url:'https://comi.hi.cn:8000/administrate/ingredient/edit/',
            method:'POST',
            header:{
              'administrator-token':uni.getStorageSync('adtoken'),
              Authorization:"Token "+uni.getStorageSync("token")
            },
            data:{
              id:this.id,
              name:this.name,
              calorie:this.calorie,
              energy:this.energy,
              protein:this.protein,
              fat:this.fat,
              carbohydrates:this.carbohydrates,
              dietary_fiber:this.dietary_fiber,
              vitaminC:this.vitaminC,
              calcium:this.calcium,
              sodium:this.sodium
            },
            success:(res)=> {
              if(res.data.error=="Auth time out!")
              {
                uni.reLaunch({
                  url:"../user/administrator"
                })
                return
              }
              uni.redirectTo({
                url:"./IngredientManage"
              })
            }
          })
        }
      },
      veri:function(){
        if(this.name==""||this.calorie==""||this.energy==""||this.protein==""||this.fat==""||this.carbohydrates==""||this.dietary_fiber==""||this.vitaminC==""||this.calcium==""||this.sodium=="")
        {
          uni.showToast({
            icon:"none",
            title:"请填写所有未填项"
          })
          return false
        }
        if(!/^[0-9]+.?[0-9]*$/.test(this.calorie)
           ||!/^[0-9]+.?[0-9]*$/.test(this.energy)
           ||!/^[0-9]+.?[0-9]*$/.test(this.protein)
           ||!/^[0-9]+.?[0-9]*$/.test(this.fat)
           ||!/^[0-9]+.?[0-9]*$/.test(this.carbohydrates)
           ||!/^[0-9]+.?[0-9]*$/.test(this.dietary_fiber)
           ||!/^[0-9]+.?[0-9]*$/.test(this.vitaminC)
           ||!/^[0-9]+.?[0-9]*$/.test(this.calcium)
           ||!/^[0-9]+.?[0-9]*$/.test(this.sodium))
        {
          uni.showToast({
            icon:"none",
            title:"除名称外，其他项请输入数字"
          })
          return false
        }
        return true
      }
		}
	}
</script>

<style>
  .input {
    border: solid 1px black;
    border-radius: 2px;
    margin: 30rpx 10rpx;
    padding: 2px 1px;
  }
</style>
