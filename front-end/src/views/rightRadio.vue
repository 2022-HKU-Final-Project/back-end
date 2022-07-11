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
    return {
		echartData:[]
	};
  },
  props:['ShowData'],
  watch:{
	  ShowData:function(newval){
		  this.echartData = newval
		  this.initEchartMap()
	  }
  },
  methods: {
    //初始化折线图
    initEchartMap() {
      let mapDiv = document.getElementById('radioMap');
      let myChart = echarts.init(mapDiv);
	  // console.log(this.echartData)
	  var LegendData = []
	  var content = 0
	  for(var i = 0;i<this.echartData.length;i++){
		  LegendData.push(this.echartData[i].name)
		  content += this.echartData[i].value
	  }
	  // console.log(LegendData)
	  var color = ['#4D88FE', '#50CCCB'];
	  var option = {
		  title: {
		        show: true,
		        text: '总:'+ content,
		        top: '50%',
		        left: 'center',
		        textStyle: {
		            fontSize: 14,
		            color: '#0AF4F4'
		        }
		    },
		  color:color,
	      legend: {
	          orient: 'horizontal',
	          top:5,
	          data: LegendData,    //有数据
	          textStyle: {
	              color: "#fff",
	              fontSize: 16
	          }
	      },
	      tooltip: {
	          trigger: 'item',
	          formatter: '{a} <br/>{b} : {c} ({d}%)'
	      },
	      series: [{
	          type: 'pie',
	          radius: ['40%', '75%'],
	          center: ['50%', '55%'],
	          // roseType: 'radius',
	          data: this.echartData,
	          label: {
	                  show: false,
	                  normal: {
	                        formatter: '{d}%',
	                      show: true,
	                      position: ''
	                  },
	              },
	              labelLine: {
	                  normal: {
	                      show: false
	                  }
	              },
	      }, {
							// 内圈
							type: 'pie',
							radius: ['40%', '60%'],
							center: ['50%', '55%'],
							silent: true,
							itemStyle: {
								normal: {
									color: 'rgba(255, 255, 255,.3)',
									label: {
										show: false,
									},
									labelLine: {
										show: false,
									},
								},
							},
							data: [1],
						},]
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