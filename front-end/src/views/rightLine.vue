<template>
  <div id="Line-box">
      <div id="linemain"></div>
  </div>
</template>
 
<script>
// import echarts from "echarts";
import * as echarts from 'echarts' 
export default {
  data() {
    return {};
  },
  methods: {
    //初始化折线图
    initEchartMap() {
      let mapDiv = document.getElementById('linemain');
      let myChart = echarts.init(mapDiv);
	  let xData = ["2018年", "2019年", "2020年", "2021年"];
	  let legendData = ["第一产业", "第三产业"]; //图例
	  let firstIndustry = [72, 37, 4, 75]; //第一产业
	  let thirdIndustry = [8, 15, 34, 31]; //第三产业
	  var options = {
	      title: {
	          textStyle: { color: '#666', fontSize: 14, fontWeight: 'normal' },
	          padding: [5, 0, 0, 0],
	      },
	      legend: {
	          type: 'plain',
	          top: 10,
	          right: 20,
	          itemGap: 64,
	          itemWidth: 10,
	          icon: 'circle',
	          selectedMode: false,
	          textStyle: { padding: [0, 0, 0, 4] ,color:"#ffffff"},
	          data: ['新增登记', '完成服务'],
	      },
	      grid: { left: 0, top: 40, bottom: 20, right: 10, containLabel: true },
	      xAxis: {
	          type: 'category',
	          data: [
	              '12-26',
	              '12-27',
	              '12-28',
	              '12-29',
	              '12-30',
	              '12-31',
	              '01-01',
	              '01-02',
	              '01-03',
	              '01-04',
	              '01-05',
	              '01-06',
	              '01-07',
	              '01-08',
	              '01-09',
	          ],
	          axisLine: { lineStyle: { color: '#ccc' } },
	          axisTick: { length: 3 },
	          axisLabel: { color: '#999' },
	      },
	      yAxis: {
	          type: 'value',
	          axisLine: { show: true, lineStyle: { color: '#ccc' } },
	          axisLabel: { color: '#999' },
	          splitLine: { show: false },
	      },
	      tooltip: {
	          trigger: 'axis',
	          padding: [12, 17, 20, 23],
	          textStyle: { color: '#424242' },
	          renderMode: 'html',
	          className: 'tooltip',
	      },
	      series: [
	          {
	              name: '新增登记',
	              type: 'line',
	              data: [0, 10, 2, 4, 4, 7, 0, 0, 0, 3, 0, 9, 6, 0, 0],
	              smooth: true, // 平滑曲线
	              showSymbol: false,
	              itemStyle: { color: '#126EFC' },
	              lineStyle: { width: 3, color: '#126EFC' },
	              areaStyle: { color: 'rgba(0, 110, 254, 0.1)' },
	          },
	          {
	              name: '完成服务',
	              type: 'line',
	              data: [0, 0, 0, 5, 0, 2, 0, 0, 0, 2, 0, 4, 1, 0, 0],
	              smooth: true,
	              showSymbol: false,
	              itemStyle: { color: '#1BB389' },
	              lineStyle: { width: 3, color: '#1BB389' },
	              areaStyle: { color: 'rgba(27, 179, 137, 0.1)' },
	          },
	      ],
	  };


      myChart.setOption(options);
    },
  },
  mounted() {
      this.$nextTick(()=>{
          this.initEchartMap();
      })
  }
};
</script>
 
<style scoped="scoped">
  #linemain {
  	width: 100%;
  	height: 300px;
  }
 
</style>