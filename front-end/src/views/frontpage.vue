<template>
  <div>
    <div id="main">
      <div id="Charts">
        <div id="mainTop">数据可视化大屏展示--{{ msg }}</div>
        <div id="LayLeft">
          <div class="Leftmains">
            <div id="chartsBar" ref="chartBar"></div>
          </div>
          <div class="Leftmains">
            <div id="chartsPie" ref="chartPie"></div>
          </div>
        </div>
        <div id="LayCenter">
          <div id="china">
            <china :MapData="MapData"></china>
          </div>
        </div>
        <div id="LayRight">
          <div class="Leftmains">
            <rightLine :pointData="Pointdata"></rightLine>
          </div>
          <div class="Leftmains">
            <rightRadio :ShowData="pushData"></rightRadio>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import china from "./china.vue";
import rightLine from "./rightLine.vue";
import rightRadio from "./rightRadio.vue";
import echarts from "echarts";
export default {
  data() {
    return {
      showData: "房地产/建筑",
      content: 0,
      index: 0,
      pushData: [],
      occupationData: [],
      Pointdata: [],
      MapData: [],
    };
  },
  watch: {
    msg: function (newval) {
      //监听行业选择事件
      this.showData = newval;
      this.getIndex();
      this.getPoint();
      this.getMap();
      this.ChartsPie();
      this.Chartsfuct();
    },
  },
  props: ["msg"],
  components: {
    rightLine,
    rightRadio,
    china,
  },
  methods: {
    getMap() {
      var that = this;
      this.request3
        .get("/dashboard/Map") //地图请求地址
        .then((response) => {
          var index = 0;
          // console.log(response)
          for (var i = 0; i < response.length; i++) {
            if (response[i].job == that.showData) {
              index = i;
            } else {
              continue;
            } //判断当前展示的数据类型
          }
          that.MapData = response[index].city;
          // let arr = []
          // 	    for (let key in echartsData) {
          // 	      arr.push({
          // 	        name: key,  // label 字段
          // 	        value: echartsData[key]   // value字段
          // 	      }
          // 	    }
          // 		that.MapData = arr
        });
    },
    getPoint() {
      var that = this;
      this.request3
        .get("/dashboard/heatmap") //heatmap请求地址
        .then((response) => {
          var index = 0;
          // console.log(response)
          for (var i = 0; i < response.length; i++) {
            if (response[i].name == that.showData) {
              index = i;
            } else {
              continue;
            } //判断当前展示的数据类型
          }
          that.Pointdata = response[index];
          // console.log(that.Pointdata)
        });
    },
    getIndex() {
      //获取饼状图数据
      this.pushData = [];
      this.content = {
        name: "总数",
        value: 0,
      };
      // console.log(this.showData)
      var that = this;
      this.request3
        .get("/dashboard/jobCount") //右下角pie chart请求地址
        .then((response) => {
          // console.log(that.showData)
          // console.log(response)
          var index = 0;
          for (var i = 0; i < response.length; i++) {
            var num = response[i].value;
            that.content.value += num; //获取总数
            if (response[i].name == that.showData) {
              index = i;
            } else {
              continue;
            } //判断当前展示的数据类型
          }
          that.occupationData = response[index];
          that.content.value -= that.occupationData.value;
          that.pushData.push(that.occupationData, that.content);
          // console.log(that.pushData)
        });
    },
    Chartsfuct() {
      var dom = this.$refs.chartBar;
      var myChart = this.$echarts.init(dom);
      var that = this;
      this.request3
        .get("/dashboard/heatmap") //左上角bar chart接口地址，同右上角heatmap地址一样
        .then((response) => {
          var index = 0;
          for (var i = 0; i < response.length; i++) {
            if (response[i].name == that.showData) {
              index = i;
            } else {
              continue;
            } //判断当前展示的数据类型
          }
          let yAxisData = [];

          var SetData = response[index];
          console.log(SetData);
          let seriesData = [];
          for (var j = 0; j < SetData.data.length; j++) {
            yAxisData.push(SetData.data[j].Edu);
            var sum = 0;
            for (var k = 0; k < SetData.data[j].value.length; k++) {
              for (let key in SetData.data[j].value[k]) {
                var a = SetData.data[j].value[k][key];
              }
              sum += a;
            }
            seriesData.push(sum);
          }

          console.log(seriesData);
          let colorArray = [
            {
              top: "#056CBB", //黄
              bottom: "rgba(11,42,84,.3)",
            },
            {
              top: "#1ace4a", //绿
              bottom: "rgba(11,42,84, 0.3)",
            },
            {
              top: "#4bf3ff", //蓝
              bottom: "rgba(11,42,84,.3)",
            },
            {
              top: "#4f9aff", //深蓝
              bottom: "rgba(11,42,84,.3)",
            },
            {
              top: "#9AFFF1", //粉
              bottom: "rgba(11,42,84,.3)",
            },
            {
              top: "#8AE1FF", //粉
              bottom: "rgba(11,42,84,.3)",
            },
            {
              top: "#F0E1C2", //粉
              bottom: "rgba(11,42,84,.3)",
            },
          ];
          var option = {
            tooltip: {
              show: true,
              formatter: "{b}:{c}",
            },
            grid: {
              left: "5%",
              top: "5%",
              right: "1%",
              bottom: "20%",
              containLabel: true,
            },

            xAxis: {
              type: "value",
              show: false,
              position: "top",
              axisTick: {
                show: false,
              },
              axisLine: {
                show: false,
                lineStyle: {
                  color: "#fff",
                },
              },
              splitLine: {
                show: false,
              },
            },
            yAxis: [
              {
                type: "category",
                axisTick: {
                  show: false,
                  alignWithLabel: false,
                  length: 5,
                },
                splitLine: {
                  //网格线
                  show: false,
                },
                inverse: "true", //排序
                axisLine: {
                  show: false,
                  lineStyle: {
                    color: "#fff",
                  },
                },
                data: yAxisData,
              },
            ],
            series: [
              {
                name: "能耗值",
                type: "bar",
                label: {
                  normal: {
                    show: true,
                    position: "right",
                    formatter: "{c}",
                    textStyle: {
                      color: "white", //color of value
                    },
                  },
                },
                itemStyle: {
                  normal: {
                    show: true,
                    color: function (params) {
                      let num = colorArray.length;
                      return {
                        type: "linear",
                        colorStops: [
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                          {
                            offset: 0,
                            color: colorArray[params.dataIndex % num].bottom,
                          },
                          {
                            offset: 1,
                            color: colorArray[params.dataIndex % num].top,
                          },
                        ],
                        //globalCoord: false
                      };
                    },
                    barBorderRadius: 70,
                    borderWidth: 0,
                    borderColor: "#333",
                  },
                },
                barGap: "0%",
                barCategoryGap: "50%",
                data: seriesData,
              },
            ],
          };
          myChart.setOption(option);
        })
        .catch(() => {});
    },
    ChartsPie() {
      var dom = this.$refs.chartPie;
      var myChart = this.$echarts.init(dom);
      var that = this;
      this.request3
        .get("/dashboard/salary") //左下角star chart地址
        .then((response) => {
          var index = 0;
          // console.log(response)
          for (var i = 0; i < response.length; i++) {
            if (response[i].job == that.showData) {
              index = i;
            } else {
              continue;
            } //判断当前展示的数据类型
          }
          // console.log(response);
          var salary = response[index].salary;
          var data = [];
          var AllData = [];
          for (var key in salary) {
            // console.log(key, salary[key])
            data.push({
              name: key,
              value: salary[key],
            });
            AllData.push(salary[key]);
          }
          console.log(AllData);
          const color = ["#4A99FF", "#4BFFFC"]; //线条边框颜色

          const title = {
            textStyle: {
              color: "#fff",
              fontSize: 16,
            },
            padding: 0,
            top: 35,
            left: 40,
          };

          const legend = {
            //data，就是取得每个series里面的name属性。
            orient: "vertical",
            icon: "circle", //图例形状
            padding: 0,
            top: 35,
            right: 40,
            itemWidth: 14, //小圆点宽度
            itemHeight: 14, // 小圆点高度
            itemGap: 21, // 图例每项之间的间隔。[ default: 10 ]横向布局时为水平间隔，纵向布局时为纵向间隔。
            textStyle: {
              fontSize: 14,
              color: "#00E4FF",
            },
          };
          const tooltip = {
            show: true,
          };
          const indicator = [];
          for (var key in salary) {
            // console.log(key, salary[key])
            indicator.push({
              name: key,
              max: 10000,
            });
          }
          var option = {
            color,
            title,
            legend,
            tooltip,
            radar: {
              center: ["50%", "50%"], //圆心坐标距离左边和上边的距离
              radius: ["1%", "75%"], //内外半径，不写默认是75%
              startAngle: 90, //可以旋转图形
              shape: "polygon",
              nameGap: 5,
              axisName: {
                color: "#fff",
                fontSize: 12,
              },
              indicator: indicator,
              splitArea: {
                show: false, //默认显示颜色分割区域，不需要显示
              },
              axisLine: {
                show: true, //是否显示十字交叉线
                //指向外圈文本的分隔线样式
                lineStyle: {
                  color: "#153269", //线条颜色
                },
              },
              splitLine: {
                //雷达一圈圈
                show: true,
                lineStyle: {
                  type: "solid",
                  color: "#113865", // 雷达一圈圈颜色分隔线颜色
                  width: 1, // 分隔线线宽
                },
              },
            },
            series: [
              {
                type: "radar",
                data: [
                  {
                    value: AllData,
                    name: "工资分布",
                    symbolSize: 8,
                    symbol: "circle",
                    lineStyle: {
                      width: 2,
                    },

                    areaStyle: {
                      // 单项区域填充样式
                      color: {
                        type: "linear",
                        x: 0, //右
                        y: 0, //下
                        x2: 1, //左
                        y2: 1, //上
                        colorStops: [
                          {
                            offset: 0,
                            color: color[1],
                          },
                          {
                            offset: 0.5,
                            color: "rgba(0,0,0,0)",
                          },
                          {
                            offset: 1,
                            color: color[1],
                          },
                        ],
                        global: false,
                      },
                      opacity: 1, // 区域透明度
                    },
                  },
                ],
              },
            ],
          };

          myChart.setOption(option);
        })
        .catch(() => {});
    },
  },
  mounted() {
    this.Chartsfuct();
    this.ChartsPie();
    this.getIndex();
    this.getPoint();
    this.getMap();
  },
  created() {
    this.$nextTick(() => {
      this.getMap();
    });
  },
};
</script>

<style scoped="scoped">
#mainTop {
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 30px;
  color: #ffffff;
  letter-spacing: 4px;
}

#Charts {
  width: 100%;
  height: 900px;
  float: left;
  background-color: #00265f;
}

#chartsBar {
  width: 100%;
  height: 300px;
  float: left;
}

#chartsPie {
  width: 100%;
  height: 300px;
}

#main {
  width: 88%;
  float: left;
}

#LayCenter {
  width: 46%;
  height: 800px;
  display: flex;
  justify-content: center;
  margin: 0 2%;
  float: left;
}

#LayLeft {
  width: 23%;
  float: left;
  margin-left: 2%;
  height: 900px;
}

#LayRight {
  width: 23%;
  float: left;
  margin-right: 2%;
  height: 900px;
}

.Leftmains {
  width: 100%;
  border: 1px solid #3370ff;
  margin-bottom: 20px;
  border-radius: 20px;
  height: 300px;
}

#china {
  width: 100%;
  border: 1px solid #00aaff;
  border-radius: 20px;
  height: 400px;
}
</style>
