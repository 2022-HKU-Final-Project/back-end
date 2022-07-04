<template>
  <div id="Line-box">
      <div id="radioMap"></div>
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
      let mapDiv = document.getElementById('radioMap');
      let myChart = echarts.init(mapDiv);
	  var legendData = ['车辆数', '设计车位']; //图例
	  var indicator = [{
	          text: '小型车',
	          max: 6000,
	      },
	      {
	          text: '中型车',
	          max: 5000
	      },
	      {
	          text: '大型车',
	          max: 5000
	      },
	      {
	          text: '货车',
	          max: 5000,
	          //  axisLabel: {show: true, textStyle: {fontSize: 18, color: '#333'}}
	      },
	      {
	          text: '特种车',
	          max: 5000
	      },
	      {
	          text: '贵宾车',
	          max: 5000
	      }
	  ];
	  var dataArr = [{
	          value: [4300, 4700, 3600, 3900, 3800, 4200],
	          name: legendData[0],
	          itemStyle: {
	              normal: {
	                  lineStyle: {
	                      color: '#4A99FF',
	                      // shadowColor: '#4A99FF',
	                      // shadowBlur: 10,
	                  },
	                  shadowColor: '#4A99FF',
	                  shadowBlur: 10,
	              },
	          },
	          areaStyle: {
	                  normal: { // 单项区域填充样式
	                      color: {
	                          type: 'linear',
	                          x: 0, //右
	                          y: 0, //下
	                          x2: 1, //左
	                          y2: 1, //上
	                          colorStops: [{
	                              offset: 0,
	                              color: '#4A99FF'
	                          }, {
	                              offset: 0.5,
	                              color: 'rgba(0,0,0,0)'
	                          }, {
	                              offset: 1,
	                              color: '#4A99FF'
	                          }],
	                          globalCoord: false
	                      },
	                      opacity: 1 // 区域透明度
	                  }
	              }
	      },
	      {
	          value: [3200, 3000, 3400, 2000, 3900, 2000],
	          name: legendData[1],
	          itemStyle: {
	              normal: {
	                  lineStyle: {
	                      color: '#4BFFFC',
	                      // shadowColor: '#4BFFFC',
	                      // shadowBlur: 10,
	                  },
	                  shadowColor: '#4BFFFC',
	                  shadowBlur: 10,
	              },
	          },
	           areaStyle: {
	                  normal: { // 单项区域填充样式
	                      color: {
	                          type: 'linear',
	                          x: 0, //右
	                          y: 0, //下
	                          x2: 1, //左
	                          y2: 1, //上
	                          colorStops: [{
	                              offset: 0,
	                              color: '#4BFFFC'
	                          }, {
	                              offset: 0.5,
	                              color: 'rgba(0,0,0,0)'
	                          }, {
	                              offset: 1,
	                              color: '#4BFFFC'
	                          }],
	                          globalCoord: false
	                      },
	                      opacity: 1 // 区域透明度
	                  }
	              }
	      }
	  ];
	  var colorArr = ['#4A99FF', '#4BFFFC']; //颜色
	  var option = {
	      color: colorArr,
	      legend: {
	          orient:'vertical',
	          icon: 'circle', //图例形状
	          data: legendData,
	          bottom:35,
	          right:40,
	          itemWidth: 14, // 图例标记的图形宽度。[ default: 25 ]
	          itemHeight: 14, // 图例标记的图形高度。[ default: 14 ]
	          itemGap: 21, // 图例每项之间的间隔。[ default: 10 ]横向布局时为水平间隔，纵向布局时为纵向间隔。
	          textStyle: {
	              fontSize: 14,
	              color: '#00E4FF',
	          },
	      },
	      radar: {
	          // shape: 'circle',
	          name: {
	              textStyle: {
	                  color: '#fff',
	                  fontSize: 16
	              },
	          },
	          indicator: indicator,
	          splitArea: { // 坐标轴在 grid 区域中的分隔区域，默认不显示。
	              show: true,
	              areaStyle: { // 分隔区域的样式设置。
	                  color: ['rgba(255,255,255,0)', 'rgba(255,255,255,0)'], // 分隔区域颜色。分隔区域会按数组中颜色的顺序依次循环设置颜色。默认是一个深浅的间隔色。
	              }
	          },
	          axisLine: { //指向外圈文本的分隔线样式
	              lineStyle: {
	                  color: '#1D6B86'
	              }
	          },
	          splitLine: {
	              lineStyle: {
	                  color: '#1D6B86', // 分隔线颜色
	                  width: 1, // 分隔线线宽
	              }
	          },
	      },
	      series: [{
	          type: 'radar',
	          symbolSize: 8,
	          // symbol: 'angle',
	          data: dataArr
	      }]
	  };



      myChart.setOption(option);
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
  #radioMap {
  	width: 100%;
  	height: 300px;
  }
 
</style>