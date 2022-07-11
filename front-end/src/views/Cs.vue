<template>
  <div>
    <div id="chartsMain">
      <div id="chartsNav">
        <div v-for="a in text" v-on:click="getMsg(a.name, a.index)">
          <div class="navs">{{ a.name }}</div>
        </div>
      </div>
    </div>
    <frontPage :msg="Msg"></frontPage>
  </div>
</template>
<script>
import frontPage from "./frontpage.vue";
//图表主体部分在frontpage.vue，这里有侧边栏
//房地产/建筑
//服务业
//高级管理
//供应链/物流
//技术
//教育培训
//金融
//旅游
//贸易
//传媒
//翻译
//农/林/牧/渔
//人事/财务/行政
//设计
//生产制造
//销售
//医疗健康
//运营
export default {
  data() {
    return {
      Msg: "房地产/建筑",
      dataIndex: 0,
      text: [
        {
          name: "房地产/建筑",
          index: 0,
        },
        {
          name: "服务业",
          index: 1,
        },
        {
          name: "高级管理",
          index: 2,
        },
        {
          name: "供应链/物流",
          index: 3,
        },
        {
          name: "技术",
          index: 4,
        },
        {
          name: "教育培训",
          index: 5,
        },
        {
          name: "金融",
          index: 6,
        },
        {
          name: "旅游",
          index: 7,
        },
        {
          name: "贸易",
          index: 8,
        },
        {
          name: "传媒",
          index: 9,
        },
        {
          name: "翻译",
          index: 10,
        },
        {
          name: "农/林/牧/渔",
          index: 11,
        },
        {
          name: "人事/财务/行政",
          index: 12,
        },
        {
          name: "设计",
          index: 13,
        },
        {
          name: "生产制造",
          index: 14,
        },
        {
          name: "销售",
          index: 15,
        },
        {
          name: "医疗健康",
          index: 16,
        },
        {
          name: "运营",
          index: 17,
        },
        {
          name: "产品",
          index: 18,
        },
        {
          name: "人事",
          index: 19,
        },
        {
          name: "咨询",
          index: 20,
        },
        {
          name: "市场",
          index: 21,
        },
        {
          name: "采购",
          index: 22,
        },
      ],
    };
  },
  components: {
    frontPage,
  },
  methods: {
    getMsg(data, index) {
      this.Msg = data;
      this.dataIndex = index;
      var Tag = document.getElementsByClassName("navs");
      for (var i = 0; i < Tag.length; i++) {
        Tag[i].id = "";
      }
      Tag[index].id = "changeStyle";
    },
  },
  mounted() {
    this.getMsg(this.Msg, this.dataIndex);
  },
};
</script>
<style lang="less" scoped>
#chartsMain {
  width: 12%;
  float: left;
  height: 900px;
}
#changeStyle {
  background-color: #3370ff;
}
#chartsNav {
  width: 100%;
  float: left;
  height: 900px;
  background-color: #002f76;
}
.navs {
  width: 100%;
  height: 38px;
  border-bottom: 1px solid #ffffff;
  font-size: 14px;
  color: #fff;
  display: flex;
  justify-content: center;
  align-items: center;
}
.navs:hover {
  background-color: #ffffff;
  color: rgba(0, 0, 0, 0.7);
}
</style>
