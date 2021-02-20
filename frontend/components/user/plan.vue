<template>
  <view class="content">
    <view class="askline">
      <view class="plan">近期是否有减肥计划?</view>
      <view class="buttons">
        <view
          :class="{chosen:choice,button:true}"
          @click="Switch(true)"
        >有</view>
        <view
          :class="{chosen:!choice,button:true}"
          @click="Switch(false)"
        >无</view>
      </view>
    </view>
    <view
      class="input"
      v-if="choice"
    >
      <view class="input0">
        <text style="color: #505050;font-size: 40rpx;">性别:</text><input
          :value="sex"
          type="string"
          :placeholder="sex"
          maxlength="6"
          @input="setsex"
        >
      </view>
      <view class="input3">
        <text style="color: #505050;font-size: 40rpx;">年龄:</text><input
          :value="age"
          type="string"
          :placeholder="age"
          maxlength="2"
          @input="setage"
        ><text style="color: #505050;font-size: 40rpx;">岁</text>
      </view>
      <view class="input4">
        <text style="color: #505050;font-size: 40rpx;">身高:</text><input
          :value="height"
          type="string"
          :placeholder="height"
          maxlength="3"
          @input="setheight"
        ><text style="color: #505050;font-size: 40rpx;">cm</text>

        <view class="input5">
          <text style="color: #505050;font-size: 40rpx;">体重:</text><input
            :value="weight"
            type="string"
            :placeholder="weight"
            maxlength="3"
            @input="setweight"
          ><text style="color: #505050;font-size: 40rpx;">KG</text>
        </view>
        <view class="input1">
          <text style="color: #505050;font-size: 40rpx;">目标体重:</text><input
            :value="targetweight"
            type="number"
            :placeholder="targetweight"
            maxlength="3"
            @input="set"
          ><text style="color: #505050;font-size: 40rpx;">KG</text>
        </view>
        <view class="input2">
          <text style="color: #505050;font-size: 40rpx;">所用天数:</text><input
            :value="day"
            type="number"
            maxlength="4"
            :placeholder="day"
            @input="changedate"
          ><text style="color: #505050;font-size: 40rpx;">Day</text>
        </view>
      </view>
    </view>
    <view
      class="tip"
      v-if="!choice"
    >恰如其分，就是最好的你😉

    </view>
  </view>
</template>

<script>
export default {
  props: ['sex', 'rate', 'age', 'height', 'targetweight', 'plan', 'weight'], // 子组件
  data() {
    return {

      choice: true,
      day: 60,
      string: '有计划',
    };
  },
  methods: {

    Switch: function(choi) {
      this.choice = choi;
      if (choi === false) {
        this.string = '暂无计划';
        this.rate = 0;
      } else {
        this.string = '有计划';
        this.rate = (this.targetweight - this.weight) / this.day;
        this.rate = this.rate.toFixed(2);
      }
      let data = {

        weight: this.weight,
        targetweight: this.targetweight,
        sex: this.sex,
        age: this.age,
        height: this.height,
        string: this.string,
        rate: this.rate,
      };
      this.$emit('input', data);
    },
    // 设置性别
    setsex: function(event) {
      if (event.detail.value !== '') {
        this.sex = event.detail.value;

        let data = {
          weight: this.weight,
          targetweight: this.targetweight,
          sex: this.sex,
          age: this.age,
          height: this.height,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },
    // 设置年龄
    setage: function(event) {
      if (event.detail.value !== '') {
        this.age = event.detail.value;

        let data = {
          weight: this.weight,
          targetweight: this.targetweight,
          sex: this.sex,
          age: this.age,
          height: this.height,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },
    // 设置身高
    setheight: function(event) {
      if (event.detail.value !== '') {
        this.height = event.detail.value;

        let data = {
          weight: this.weight,
          targetweight: this.targetweight,
          sex: this.sex,
          age: this.age,
          height: this.height,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },
    // 设置体重
    setweight: function(event) {
      if (event.detail.value !== '') {
        this.weight = event.detail.value;

        let data = {
          weight: this.weight,

          sex: this.sex,
          age: this.age,
          height: this.height,
          targetweight: this.targetweight,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },

    // 设置目标体重
    set: function(event) {
      if (event.detail.value !== '') {
        this.targetweight = event.detail.value;
        this.rate = (this.targetweight - this.weight) / this.day;
        this.rate = this.rate.toFixed(2);
        let data = {
          weight: this.weight,
          sex: this.sex,
          age: this.age,
          height: this.height,
          targetweight: this.targetweight,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },

    // 设置所用天数
    changedate: function(event) {
      if (event.detail.value !== '') {
        uni.setStorage({
          key: 'weightdate',
          data: event.detail.value,
        });
        this.day = event.detail.value;
        this.rate = (this.targetweight - this.weight) / event.detail.value;
        this.rate = this.rate.toFixed(2);
        let data = {
          weight: this.weight,
          sex: this.sex,
          age: this.age,
          height: this.height,
          targetweight: this.targetweight,
          string: this.string,
          rate: this.rate,
        };
        this.$emit('input', data);
      }
    },

  },

  // 组件创建函数
  created: function() {
    if (this.plan === '暂无计划') {
      this.choice = false;
    } else {
      this.choice = true;
    }
    this.day = uni.getStorageSync('weightdate');
  },
};
</script>

<style>
  .content {
    /* display: flex; */
    /* align-items: center; */
  }

  .askline {
    margin-top: 120rpx;
    display: flex;
  }

  .plan {
    color: #505050;
    font-size: 40rpx;
    align-items: center;
    /* display: inline-block */
  }

  .button {
    font-size: 30rpx;
    text-align: center;
    width: 30px;
    /* width: 50%; */
    /* height: 100%; */
    /* line-height: 80rpx; */
    margin: 10rpx;
    border: 2px #9a7c7c solid;
    color: #9a7c7c;
    border-radius: 12rpx;
    background-color: #FFFFFF;
    /* display: inline-block */
  }

  .chosen {
    color: #ffffff;
    background-color: #9a7c7c;
  }

  .input {
    color: #060404;
    font-size: 40rpx;
    margin-top: 10rpx;
    animation: pushup 1s;
  }

  .input1 {
    display: block;
    margin-top: 10rpx;
    margin-bottom: 10rpx;
  }

  .input2 {
    display: block;
  }

  .tip {
    font-size: 40rpx;
    color: #505050;
    margin-top: 10rpx;
    animation: pushup 1s;
  }

  @keyframes pushup {
    from {
      margin-top: 50rpx;
      opacity: 0;
    }

    to {
      margin-top: 10rpx;
    }
  }

  .buttons {
    display: flex;
  }

  input {
    width: 150rpx;
    /* margin-top: 8rpx; */
    border-bottom: #C09C79 4rpx solid;
    display: inline-block;
    vertical-align: middle;
    text-align: center;
    color: #bd7e7e;
  }

  text {
    display: inline-block;
    vertical-align: middle;
  }
</style>
