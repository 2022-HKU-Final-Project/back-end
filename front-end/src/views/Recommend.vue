<template>
  <div class="page-wrapper">
    <div class="main-wrap">
      <div class="item">
        <div class="title">
          <span>Self-description</span>
          <el-select
            v-model="language"
            placeholder="Language"
            style="margin-left: 24px"
            @change="changeLanguage"
          >
            <el-option
              v-for="item in options"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </div>
        <div style="margin-top: 20px">
          <el-input
            type="textarea"
            :rows="22"
            placeholder="Please input description here"
            v-model="selfDescription"
          >
          </el-input>
        </div>
      </div>
      <div class="center-line"></div>
      <div class="item">
        <div class="title" style="line-height: 40px">Job Recommendation</div>
        <div class="recommendation-box">Recommendation</div>
      </div>
    </div>
    <div class="operate-btn">
      <el-button type="primary" style="margin-right: 12px" @click="submit"
        >Submit</el-button
      >
      <el-button type="success" @click="handleReset">Reset</el-button>
    </div>
    <div class="bottom-wrapper">
      <el-carousel indicator-position="outside">
        <el-carousel-item>
          <div class="item-wrap">
            <div class="item" @click="JumpJobs(1111111111)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_writing.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(2222222)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_writing.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(3333333333)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_writing.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
          </div>
        </el-carousel-item>
        <el-carousel-item>
          <div class="item-wrap">
            <div class="item" @click="JumpJobs(4444444444)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyi.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(55555555)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyi.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(666666666666)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyi.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
          </div>
        </el-carousel-item>
        <el-carousel-item>
          <div class="item-wrap">
            <div class="item" @click="JumpJobs(777777777)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyiwang.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(888888888)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyiwang.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
            <div class="item" @click="JumpJobs(999999999)">
              <img
                src="https://shared.ydstatic.com/fanyi/fanyi-ad-place/online/0.0.2/images/logo_fanyiwang.png"
              />
              <div>
                测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字测试文字文字文字
              </div>
            </div>
          </div>
        </el-carousel-item>
      </el-carousel>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      selfDescription: "", //左侧输入内容
      language: "Chinese", //当前选中语言
      options: [
        { label: "Chinese", value: "Chinese" },
        { label: "English", value: "English" },
        { label: "Janpanese", value: "Janpanese" },
        { label: "Korean", value: "Korean" },
        { label: "French", value: "French" },
        { label: "German", value: "German" },
      ], //语言下拉选项
    };
  },
  methods: {
    // 点击submit
    submit() {
      console.log(this.selfDescription);
    },
    //重置
    handleReset() {
      this.selfDescription = "";
    },
    // 选择语言
    changeLanguage() {
      console.log(this.language);
    },
    // 跳转
    JumpJobs(id) {
      this.$router.push(`/jobs/${id}`);
    },
  },
};
</script>
<style lang="less" scoped>
.page-wrapper {
  width: 85%;
  margin: auto;
  padding: 50px;
  height: auto;
  overflow: hidden;
  .main-wrap {
    display: flex;
    align-items: flex-end;
    .item {
      flex: 1;
      .recommendation-box {
        height: 475px;
        margin-top: 20px;
        border: 1px solid #dcdfe6;
        border-radius: 5px;
        padding: 12px;
      }
    }
    .center-line {
      margin: 0 30px;
      background: #dcdfe6;
      width: 1px;
      height: 475px;
    }
  }
  .operate-btn {
    padding: 20px 0;
    border-bottom: 2px solid #dcdfe6;
  }
  .bottom-wrapper {
    margin-top: 20px;
    .item-wrap {
      height: 100%;
      display: flex;
      padding: 30px;
      .item {
        text-align: center;
        flex: 1;
        margin: 0 50px;
        cursor: pointer;
      }
    }
  }
}
</style>
