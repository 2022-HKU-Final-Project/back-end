<template>
  <div id="Line-box">
    <div id="linemain"></div>
  </div>
</template>
 
<script>
// import echarts from "echarts";
import * as echarts from "echarts";
export default {
  data() {
    return {
      echartData: [],
    };
  },
  watch: {
    pointData: function (newval) {
      this.echartData = newval;
      console.log(this.Data);
      this.initEchartMap();
    },
  },
  props: ["pointData"],
  methods: {
    //初始化折线图
    initEchartMap() {
      let mapDiv = document.getElementById("linemain");
      let myChart = echarts.init(mapDiv);
      const hours = this.echartData.y_label;
      // console.log(hours)
      // prettier-ignore
      var days = []
      var valData = this.echartData.data;
      // console.log(days)
      var newData = [];
      try {
        for (var j = 0; j < valData.length; j++) {
          days.push(valData[j].Edu);
          for (var k = 0; k < valData[j].value.length; k++) {
            var innerData = [];
            for (let key in valData[j].value[k]) {
              var a = valData[j].value[k][key];
              innerData.push(k, j, a);
            }

            newData.push(innerData);
          }
        }
      } catch (e) {
        console.log(e);
        //TODO handle the exception
      }
      // console.log(newData)
      // prettier-ignore

      newData.map(function (item) {
	      return [item[1], item[0], item[2] || '-'];
	  });
      var option = {
        tooltip: {
          position: "top",
        },
        grid: {
          top: 10,
          left: 50,
        },
        xAxis: {
          type: "category",
          data: hours,
          axisLabel: {
            interval: 0,
            fontSize: 8,
            rotate: 15,
            color: "#fff",
          },
          splitArea: {
            show: true,
          },
        },
        yAxis: {
          type: "category",
          data: days,
          splitArea: {
            show: true,
          },
          axisLabel: {
            interval: 0,
            // rotate:30,
            color: "#fff",
            fontSize: 8,
          },
        },
        visualMap: {
          min: 0,
          max: 1000,
          calculable: true,
          orient: "horizontal",
          itemHeight: 200,
          itemWidth: 15,
          left: "center",
          bottom: "1%",
          textStyle: {
            fontSize: 8,
            color: "#fff",
          },
        },
        series: [
          {
            name: "Punch Card",
            type: "heatmap",
            data: newData,
            label: {
              show: true,
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      };

      myChart.setOption(option);
    },
  },
  mounted() {
    this.$nextTick(() => {
      this.initEchartMap();
    });
  },
};
</script>
 
<style scoped="scoped">
#linemain {
  width: 100%;
  height: 300px;
}
</style>