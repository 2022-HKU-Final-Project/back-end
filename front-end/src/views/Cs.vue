<template>
  <div>
    <div id="chartsMain">
      <div id="chartsNav">
        <div v-for="a in text" v-on:click="getMsg(a.msg)">
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
export default {
  data() {
    return {
      Msg: "",
      text: [
        {
          name: "charts",
          msg: "aaaaaa",
          index: 0,
        },
        {
          name: "charts",
          msg: "bbbbbb",
          index: 1,
        },
        {
          name: "charts",
          msg: "cccccc",
          index: 2,
        },
      ],
    };
  },
  components: {
    frontPage,
  },
  methods: {
    getMsg(data) {
      this.Msg = data;
      console.log(this.Msg);
    },
  },
};
</script>
<style lang="less" scoped>
#chartsMain {
  width: 12%;
  float: left;
  height: 900px;
}
#chartsNav {
  width: 100%;
  float: left;
  height: 900px;
  background-color: #002f76;
}
.navs {
  width: 100%;
  height: 100px;
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
