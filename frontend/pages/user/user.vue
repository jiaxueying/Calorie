<template>
  <view class="backgroud">
    <view class="nav">

      <navTab
        ref="navTab"
        :tab-title="tabTitle"
        :tab-chosen="2"
        @changeTab="changeTab"
      />
    </view>

    <!--用户信息部分-->
    <view class="allinfo">

      <recommendrange
        :min="min"
        :max="max"
      />

      <open-data
        class="userimg"
        type="userAvatarUrl"
      />

    </view>

    <view class="allinfo">

      <open-data
        class="nickname"
        type="userNickName"
        @click="administrator"
      />
    </view>
    <view class="userinfo">
      <view
        class="card"
        @click="set"
      >
        <text class="card_title">性别</text>
        <text class="card_value">{{ sex }}</text>
      </view>

      <view
        class="card"
        @click="set"
      >
        <text class="card_title" >体重/kg</text>
        <text class="card_value">{{ weight }}</text>
      </view>
      <view
        class="card"
        @click="set"
      >
        <text class="card_title">目标/kg</text>
        <text class="card_value">{{ targetweightshow }}</text>
      </view>
      <view
        class="card"
        @click="set"
      >
        <text class="card_title">体重变化速率</text>
        <text class="card_value">{{ weightrate }}</text>
      </view>
      <!--历史菜单组件-->
      <view v-if="!Switch">
        <historylist/>
      </view>

      <!--计划设置组件-->
      <view
        class="plan"
        v-if="Switch"
      >
        <plan
          @input="changetarget"
          :sex="sex"
          :plan="targetweightshow"
          :targetweightrec="targetweight"
          :weight="weight"
          :rate="weightrate"
        />
        <!--弹出框组件-->
        <view
          class="popcontent"
          v-if="pop"
        >
          <view class="popup">
            <view class="text">请输入您当前体重</view>
            <view class="popinput">
              <input
                :value="weight"
                type="number"
                maxlength="3"
                :placeholder="weight"
                @input="refresh"
              >KG
            </view>
            <view class="bottom">
              <view
                class="popbutton1"
                @click="cancel"
              >取消</view>
              <view
                class="popbutton2"
                @click="confirm"
              >确认</view>
            </view>
          </view>
        </view>
      </view>

    </view>
  </view>
</template>

<script>
import plan from '../../components/user/plan.vue';
import historylist from '../../components/user/history.vue';

export default {
  components: {
    plan,
    historylist,

  },
  data() {
    return {
      sex: '--',
      weight: '100',
      minCalForDay: '1000',
      maxCalForDay: '1500',
      Switch: false,
      targetweight: 0,
      pop: false,
      tempweight: 1, // pop组件里的体重变量
      targetweightshow: '999',
      plan: true,
      weightrate: 0,
      weightdate: 60,
      tabTitle: ['菜品查询', '菜品推荐', '个人中心'], // 导航栏格式
      min: 40,
      max: 50,
    };
  },
  methods: {

    // 编辑模式选择
    set: function() {
      this.Switch = !this.Switch;
      if (this.Switch == false) {
        uni.request({
          url: 'https://nkucalorie.top:8000/user/profile/',
          method: 'POST',
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
          },
          data: {

            plan: this.plan,
            weight: this.weight,
            target_weight: this.targetweight,
            rate: this.weightrate,
          },

        });
        uni.request({
          url: 'https://nkucalorie.top:8000/user/profile/',
          method: 'GET',
          header: {
            Authorization: 'Token ' + uni.getStorageSync('token'),
          },
          success: (res) => {
            console.log(res.data);
          },
        });
      }
    },

    // 此事件被子组件触发，a就是从子组件获取的数据，targetweight
    changetarget: function(data) {
      if (data.string != '暂无计划') {
        this.sex = data.sex;
        this.targetweight = data.targetweight;
        this.targetweightshow = data.targetweight;
        this.weightrate = data.rate;
        this.plan = true;
      } else {
        this.sex = data.sex;
        this.targetweightshow = '暂无计划';
        this.weightrate = data.rate;
        this.targetweightshow = this.weight;
        this.targetweight = 0;
        this.plan = false;
      }
    },

    // 点击编辑图标，改变用户目前体重
    changeweight: function() {
      this.tempweight = this.weight;
      this.pop = true;
    },

    // 填写当前体重popup的取消按钮对应函数
    cancel: function() {
      this.pop = false;
    },

    // 填写当前体重popup的确认按钮对应函数
    confirm: function() {
      this.weight = this.tempweight;
      this.pop = false;
      this.weightdate = uni.getStorageSync('weightdate');
      this.weightrate = (this.targetweight - this.weight) / this.weightdate;
      this.weightrate = this.weightrate.toFixed(2);
    },

    // 在pop里输入当前体重
    refresh: function(event) {
      this.tempweight = event.detail.value;
    },

    administrator: function() {
      console.log('in administrator');
      uni.navigateTo({
        url: './administrator',
      });
    },
  },

  onShow() {
    this.weightdate = uni.getStorageSync('weightdate');
    uni.request({
      url: 'https://nkucalorie.top:8000/user/profile/',
      method: 'GET',
      header: {
        Authorization: 'Token ' + uni.getStorageSync('token'),
      },
      success: (res) => {
        // this.sex = res.data.data.sex;
        this.weight = res.data.data.weight;
        this.targetweight = res.data.data.target_weight;
        this.plan = res.data.data.plan;
        this.weightrate = res.data.data.rate;
        // this.min;
        if (this.plan) {
          this.targetweightshow = this.targetweight;
        } else {
          this.targetweightshow = '暂无计划';
        }
      },
    });
  },

  onLoad() {
    this.weightdate = uni.getStorageSync('weightdate');
    uni.request({
      url: 'https://nkucalorie.top:8000/user/profile/',
      method: 'GET',
      header: {
        Authorization: 'Token ' + uni.getStorageSync('token'),
      },
      success: (res) => {
        // this.sex = res.data.data.sex;
        this.weight = res.data.data.weight;
        this.targetweight = res.data.data.target_weight;
        this.plan = res.data.data.plan;
        this.weightrate = res.data.data.rate;
        // this.min
        if (this.plan) {
          this.targetweightshow = this.targetweight;
        } else {
          this.targetweightshow = '暂无计划';
        }
      },
    }); //
  },
};
</script>

<style>
  .nav {
    left: 0;
    top: 0;
    color: #C8A57E;
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-start;
    font-size: 24upx;
    background-color: #FFFFFF;
    z-index: 99999;
    margin-bottom: 50rpx;
    }

  .backgroud {
    background-color: rgb(255, 255, 255);
    position: absolute;
    height: 100%;
    width: 100%;
  }
 recommendrange{
   position:absolute;
  top:92rpx;}

  .allinfo {
    display: flex;
    width: 100%;
    justify-content: center;
  }

  .userimg {
    width: 150rpx;
    height: 150rpx;
    border-radius: 50%;
    overflow: hidden;
    margin: 0 auto;
  }

  .userinfor {
    color: #505050;
    margin-top: 15%;
    display: flex;
    flex-direction: column;
    position: relative;
    left: 100rpx
  }

  .button {
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

  @keyframes pushleft {
    from {
      margin-left: 750rpx;
      opacity: 0;
    }

    to {}
  }

  @keyframes pushright {
    from {
      margin-right: 750rpx;
      opacity: 0;
    }

    to {}
  }

  .edit {
    position: absolute;
    top: 95rpx;
    left: 280rpx;
    height: 35rpx;
    width: 35rpx;
  }

  .popcontent {
    display: flex;
    position: fixed;
    top: 0;
    left: 0;
    justify-content: center;
    background-color: rgba(0, 0, 0, .50);
    width: 100%;
    height: 100%;
    z-index: 99;
  }

  .popup {
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

  .text {
    font-size: 40rpx;
    margin-bottom: 40rpx;
  }

  .popinput {
    display: flex;
    border-bottom: #000000 1px solid;
    width: 120rpx;
    margin-bottom: 40rpx;
  }

  .bottom {
    display: flex;
    width: 600rpx;
    background-color: #ffffff;
  }

  .popbutton1 {
    border-top: #000000 2rpx solid;
    text-align: center;
    line-height: 90rpx;
    height: 90rpx;
    width: 300rpx;
    border-right: #000000 1px solid;
    color: #8F8F94;
  }

  .popbutton2 {
    border-top: #000000 2rpx solid;
    text-align: center;
    line-height: 90rpx;
    height: 90rpx;
    width: 300rpx;
    border-left: #000000 1px solid;
    color: #00aa00;
  }

  .nickname {
    font-size: 15px;
    margin: 5px;
  }

  .editbut {
    display: flex;
  }

  .plan {
    display: flex;
    justify-content: center;
    animation: pushleft 500ms;
  }

  switch {
    transform: scale(0.6);
    /*缩放*/
    position: relative;
    right: 100rpx;
    top: 10rpx;
  }

  .weightSet {
    font-size: 1em;
    margin-top: 6rpx;
    margin-bottom: 6rpx;
    word-break: break-all;
    word-wrap: break-word;
  }

  .calorieForDay {
    font-size: 0.7em;
  }

  .userinfo {
    border-radius: 0 30px 0 0;
    background-color: rgba(248, 245, 244, 1);
    box-shadow: 10px -2px 10px #888888;
    height: 100%;
    width: 100%;
    padding-top: 15px;
    /* padding-left: 10px; */
    margin-top: 5px;
  }

  .card {
    width: 25%;
    display: inline-block;
  }

  .card_title {
    display: block;
    font-size: 10px;
    color: #B0B0B0;
    text-align:center;

  }

  .card_value {
    display: block;
    font-size: 17px;
    text-align:center;
  }
</style>
