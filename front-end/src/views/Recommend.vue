<template>
  <div class="page-wrapper">
    <el-dialog
      title="信息填写"
      :visible.sync="dialogFormVisible"
      width="500px"
      custom-class="dialogType"
      :close-on-click-modal="false"
      :close-on-press-escape="false"
    >
      <el-form :model="form">
        <el-form-item label="学历" :label-width="formLabelWidth">
          <el-select v-model="form.diploma" placeholder="请选择">
            <el-option
              v-for="item in education"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="工作经验" :label-width="formLabelWidth">
          <el-select v-model="form.workage" placeholder="请选择">
            <el-option
              v-for="item in WorkAge"
              :key="item.value"
              :label="item.label"
              :value="item.value"
            >
            </el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="期望薪资(/月):" :label-width="formLabelWidth">
          <el-input-number
            v-model="form.salary"
            controls-position="right"
            :min="0"
            :max="600000"
          ></el-input-number>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="requestData">确 定</el-button>
      </div>
    </el-dialog>
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
            v-model="form.desc"
          >
          </el-input>
        </div>
      </div>
      <div class="center-line"></div>
      <div class="item">
        <div class="title" style="line-height: 40px">Job Recommendation</div>
        <div id="tst" class="recommendation-box">Recommendation</div>
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
              <img src="../assets/doctor.jpg" width="70" height="60" />
              <div style="font-size: 13px">
                Doctor, person that qualified to treat people who are illed,
                high requirement in education, in great demand in most area.
              </div>
            </div>
            <div class="item" @click="JumpJobs(2222222)">
              <img src="../assets/reporter.png" width="70" height="60" />
              <div style="font-size: 13px">
                Reporter. Complete planning and reporting tasks of the
                newspaper; They should have keen news antennae, excellent
                writing skills, solid knowledge reserve.
              </div>
            </div>
            <div class="item" @click="JumpJobs(3333333333)">
              <img src="../assets/delivery.png" width="70" height="60" />
              <div style="font-size: 13px">
                Courier, Cooperate with sales staff to do delivery work.Arrange
                route and deliver goods to customer's designated place.Cooperate
                with warehouse staff to handle.
              </div>
            </div>
          </div>
        </el-carousel-item>
        <el-carousel-item>
          <div class="item-wrap">
            <div class="item" @click="JumpJobs(4444444444)">
              <img src="../assets/lawyer.png" width="70" height="60" />
              <div style="font-size: 13px">
                Lawyer, who conducts civil and commercial litigation, non
                litigation and criminal defense cases, need judicial examination
                and qualification certificate.
              </div>
            </div>
            <div class="item" @click="JumpJobs(55555555)">
              <img src="../assets/clerk.png" width="70" height="60" />
              <div style="font-size: 13px">
                Clerk. Operate the document system according to the needs, work
                tasks including but are not limited to information analysis,
                proofreading, compilation, and timely issue relevant work
                reports.
              </div>
            </div>
            <div class="item" @click="JumpJobs(666666666666)">
              <img src="../assets/cusm.png" width="70" height="60" />
              <div style="font-size: 13px">
                Customer service, conduct telephone solicitation and tracking
                work for customers, and register the results in relevant
                statements or systems in time.
              </div>
            </div>
          </div>
        </el-carousel-item>
        <el-carousel-item>
          <div class="item-wrap">
            <div class="item" @click="JumpJobs(777777777)">
              <img src="../assets/police.jpg" width="70" height="60" />
              <div style="font-size: 13px">
                Police. Maintain public order and stop acts endangering public
                order; Protect the safety of the person and property of
                citizens, prevent illegal and criminal activities.
              </div>
            </div>
            <div class="item" @click="JumpJobs(888888888)">
              <img src="../assets/worker.jpg" width="70" height="60" />
              <div style="font-size: 13px">
                Workers, performing production tasks. Comply with the company's
                rules and regulations, in accordance with the operation process
                requirements. Complete production on time.
              </div>
            </div>
            <div class="item" @click="JumpJobs(999999999)">
              <img src="../assets/chef.jpg" width="70" height="60" />
              <div style="font-size: 13px">
                Chef, responsible for canteen cooking and production, increase
                the style of dishes; Plan materials, seiko; work with other
                chefs to cook and manage the canteen, and prepare recipes.
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
      language: "Chinese",
      options: [
        { label: "Chinese", value: "Chinese" },
        { label: "English", value: "English" },
        { label: "Janpanese", value: "Janpanese" },
        { label: "Korean", value: "Korean" },
        { label: "French", value: "French" },
        { label: "German", value: "German" },
      ], //语言下拉选项
      dialogFormVisible: false,
      WorkAge: [
        {
          value: "0",
          label: "经验不限",
        },
        {
          value: "1",
          label: "无工作经验/无经验/经验不限,可接收应届生",
        },
        {
          value: "2",
          label: "1年以下/1年以下,可接收应届生",
        },
        {
          value: "3",
          label: "1年经验/2年经验/1-2年/1-2年，可接收应届生/1-3年",
        },
        {
          value: "4",
          label: "3-5年/3-4年经验/3-5年,可接收应届生",
        },
        {
          value: "5",
          label: "5-7年经验/6-7年/6-7年,可接收应届生/5-10年",
        },
        {
          value: "6",
          label: "8-9年经验/8-10年/8-10年,可接收应届生",
        },
        {
          value: "7",
          label: "10年以上,可接收应届生/10年以上/10年以上经验",
        },
      ],
      education: [
        {
          value: "0",
          label: "学历不限",
        },
        {
          value: "1",
          label: "初中及以下",
        },
        {
          value: "2",
          label: "技校/中技",
        },
        {
          value: "3",
          label: "高中",
        },
        {
          value: "4",
          label: "大专",
        },
        {
          value: "5",
          label: "本科",
        },
        {
          value: "6",
          label: "硕士",
        },
        {
          value: "7",
          label: "博士",
        },
        {
          value: "8",
          label: "无",
        },
      ],
      form: {
        diploma: "",
        workage: "",
        salary: "",
        desc: "",
      },
      formLabelWidth: "140px",
    };
  },
  methods: {
    //获取数据
    requestData() {
      console.log(this.form);
      this.dialogFormVisible = false;
    },
    // 点击submit
    submit() {
      console.log(this.form);
      this.request.post("/recommend", this.form).then((response) => {
        this.result = response.desc;
        this.re = document.getElementById("tst");
        this.re.innerHTML = this.result;
      });
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
  mounted() {
    this.dialogFormVisible = true;
  },
};
</script>
<style lang="less" scoped>
/deep/.el-dialog {
  border-radius: 10px;
}
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
