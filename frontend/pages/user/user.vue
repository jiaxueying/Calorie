<template>
  <view>
    <!--用户信息部分-->
    <view class="allinfo">
        <view class="userimg">
            <open-data type="userAvatarUrl"></open-data>
        </view>
        
        <view class="userinfor">
            <view class="editbut">
                <open-data class="nickname" type="userNickName"></open-data>
                <view class="button" @click="set">编辑模式</view>
                <switch color="#59453D" :checked="Switch" @click="set"></switch>
            </view>
            <image src="../../static/edit.png" class="edit" v-if="Switch" @click="changeweight"></image>
            <view><text class="weightSet">体重：{{weight}}KG\n目标体重：{{targetweightshow}}\n体重变化速率：{{weightrate}}KG/Day</text></view>
            <text class="calorieForDay">本日推荐摄入卡路里范围：\n{{minCalForDay}}kcal-{{maxCalForDay}}kcal</text>
        </view>
    </view>
      
    <!--历史菜单组件-->
    <view class="history" v-if="!Switch"><historylist></historylist></view>
    
    <!--计划设置组件-->
    <view class="plan" v-if="Switch">
        <plan @input="changetarget" :plan="targetweightshow" :targetweightrec="targetweight" :weight="weight"></plan>
        <!--弹出框组件-->
        <view class="popcontent" v-if="pop">
            <view class="popup">
                <view class="text">请输入您当前体重</view>
                <view class="popinput">
                    <input :value="weight" type="number" maxlength="3" :placeholder="weight" @input="refresh"/>KG
                </view>
                <view class="bottom">
                    <view class="popbutton1" @click="cancel">取消</view>
                    <view class="popbutton2" @click="confirm">确认</view>
                </view>
            </view>
        </view>
   </view>
   
  </view>
</template>

<script>
  import plan from "../../components/user/plan.vue"
  import historylist from "../../components/user/history.vue"
	export default {
    components:{
      plan,
      historylist
    },
		data() {
			return {
        weight:'100',
        minCalForDay:'1000',
        maxCalForDay:'1500',
        Switch:false,
        targetweight:600,
        pop:false,
        tempweight:1,//pop组件里的体重变量
        targetweightshow:"999KG",
        plan:true,
        weightrate:0,
			}
		},
		methods: {
      
      //编辑模式选择
			set:function(){
        this.Switch=!this.Switch
      },
      
      //此事件被子组件触发，a就是从子组件获取的数据，targetweight
      changetarget:function(data){
        if(data.string!="暂无计划")
        {
        this.targetweight=data.targetweight
        this.targetweightshow=data.targetweight+"KG"
        this.weightrate=data.rate//无法动态接受
        this.plan=true
        }
        else
        {
        this.targetweightshow="暂无计划"
        this.weightrate=data.rate
        this.plan=false
        }
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile/",
          method:"POST",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            user_id:uni.getStorageSync('userid'),
            plan:this.plan,
            weight:this.weight,
            target_weight:this.targetweight
          }
        })
        
      },
      
      //点击编辑图标，改变用户目前体重
      changeweight:function(){
        this.tempweight=this.weight
        this.pop=true
      },
      
      //填写当前体重popup的取消按钮对应函数
      cancel:function(){
        this.pop=false
      },
      
      //填写当前体重popup的确认按钮对应函数
      confirm:function(){
        this.weight=this.tempweight
        this.pop=false
        uni.request({
          url:"http://cal.hanlh.com:8000/user/profile/",
          method:"POST",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          data:{
            user_id:uni.getStorageSync('userid'),
            weight:this.weight,
            plan:this.plan,
            target_weight:this.targetweight
          }
        })
        /*uni.request({
          url:"http://cal.hanlh.com:8000/user/profile",
          method:"GET",
          header:{
            Authorization:'Token '+uni.getStorageSync('token')
          },
          success: (res) => {
            console.log(res.data.data)
          }
        })*/
      },
      
      //在pop里输入当前体重
      refresh:function(event){
        this.tempweight=event.detail.value
      }
		},
    
    
    
    onLoad() {
      //一个函数，在页面加载时自动执行
      //获取页面所需的所有用户数据
		uni.request({
			url:"http://cal.hanlh.com:8000/user/profile",
			method:"GET",
			header:{
				Authorization:"Token"+uni.getStorageSync("token")
			},
			success: (res) => {
				this.weight=res.data.data.weight
				this.targetweight=res.data.data.target_weight
        this.minCalForDay=res.data.data.min_calorie
        this.maxCalForDay=res.data.data.max_calorie
        this.plan=res.data.data.plan
        if(this.plan)
        {
          this.targetweightshow=this.targetweight+"KG"
        }
        else
        {
          this.targetweightshow="暂无计划"
        }
			}
		})
    
    }
	}
</script>

<style>
  .allinfo{
    display: flex;
  }
	.userimg{
    margin-top: 15%;
		width:200rpx;
		height:200rpx;
		border-radius:50%;
    overflow: hidden;
    position:relative;
    left:55rpx;
	}
  .userinfor{
    color: #505050;
    margin-top: 15%;
    display: flex;
    flex-direction: column;
    position:relative;
    left:100rpx
    
  }
  .button{
    font-size: 25rpx;
    background-color: #e8e8e8;
    height: 60rpx;
    line-height: 60rpx;
    width: 190rpx;
    border-radius: 15rpx;
    margin-top: 18rpx;
    margin-left: 20rpx;
    border-left: 5px #e8e8e8 solid;
  }
  @keyframes pushleft{
    from{margin-left: 750rpx;opacity: 0;}
    to{}
  }
  @keyframes pushright{
    from{margin-right: 750rpx;opacity: 0;}
    to{}
  }
  .edit{
    position: absolute;
    top:95rpx;
    left: 280rpx;
    height: 35rpx;
    width: 35rpx;
  }
  .popcontent{
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    justify-content: center;
    background-color: rgba(0,0,0,.50);
    width: 100%;
    height: 100%;
    z-index: 99;
  }
  .popup{
    background-color: #ffffff;
    width: 600rpx;
    height: 320rpx;
    margin-top: 40%;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    align-items: center;
    border: #000000 1px solid;
    border-radius: 15rpx;
    overflow: hidden;
  }
  .text{
    font-size: 40rpx;
    margin-bottom: 40rpx;
  }
  .popinput{
    display: flex;
    border-bottom: #000000 1px solid;
    width: 120rpx;
    margin-bottom: 40rpx;
  }
  .bottom{
    display: flex;
    width: 600rpx;
    background-color: #ffffff;
  }
  .popbutton1{
    border-top: #000000 2rpx solid;
    text-align: center;
    line-height: 90rpx;
    height: 90rpx;
    width: 300rpx;
    border-right: #000000 1px solid;
    color: #8F8F94;
  }
  .popbutton2{
    border-top: #000000 2rpx solid;
    text-align: center;
    line-height: 90rpx;
    height: 90rpx;
    width: 300rpx;
    border-left: #000000 1px solid;
    color: #00aa00;
  }
  .nickname{
    font-size: 2em;
    height:85rpx;
    }
  .editbut{
    display: flex;
    }
  .plan{
    display: flex;
    justify-content: center;
    animation: pushleft 500ms;
    }
  switch{
    transform: scale(0.6);
    /*缩放*/
    position: relative;
    right: 100rpx;
    top: 10rpx; 
   }
   .weightSet{
     font-size: 1em;
     margin-top: 6rpx;
     margin-bottom: 6rpx;
   }
   .calorieForDay{
     font-size: 0.7em;
   }
   .history{
     animation: pushright 1s;
   }
</style>
