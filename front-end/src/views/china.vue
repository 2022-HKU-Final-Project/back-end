<template>
  <div id="china_map_box">
      <div id="china_map" ></div>
  </div>
</template>

<script>
// import echarts from "echarts";
import * as echarts from 'echarts'
import '../helper/china.js'
export default {
  data() {
    return {
		echartData:[],
		ShowData:[]
      //echart 配制option
	  }
  },
  props:["MapData"],
  watch:{
	  MapData:function(newval){
		  this.echartData = newval
		  this.initEchartMap()
	  }
	  
  },
  methods: {
    //初始化中国地图
    initEchartMap() {
	  console.log(this.echartData)
	  let arr = []
	  	    for (let key in this.echartData) {
	  	      arr.push({
	  	        name: key,  // label 字段
	  	        value: this.echartData[key]   // value字段
	  	      })
	  	    }
			 this.ShowData = JSON.parse(JSON.stringify(arr))
			var that = this
			let mapDiv = document.getElementById('china_map');
			let myChart = echarts.init(mapDiv);
			var option = {
          tooltip: {
              triggerOn: "mousemove",
              formatter: function(e, t, n) {
                  return '.5' == e.value ? e.name + "：有疑似病例" : e.seriesName + "<br />" + e.name + "：" + e.value
              }
          }, 
          visualMap: {//左边的图标
              min: 0,
              max: 1500,
              left: 26,
              bottom: 30,
              showLabel: !0,
			  textStyle:{
				  color:"#fff"
			  },
              text: ["高", "低"],
              inRange: {
                color: ["#DCEDFF", "#DCEDFF", "#A7D6FF", "#68B1FF", "#3193EE"]
              },
              // pieces: [{
              //     gt: 10000,
              //     label: "> 10000人",
              //     color: "#3193EE"
              // }, {
              //     gte: 1000,
              //     lte: 10000,
              //     label: "1000 - 10000人",
              //     color: "#68B1FF"
              // }, {
              //     gte: 100,
              //     lt: 1000,
              //     label: "100 - 1000人",
              //     color: "#A7D6FF"
              // }, {
              //     gt: 1,
              //     lt: 100,
              //     label: "1 - 100人",
              //     color: "#DCEDFF"
              // }, {
              //     value: 0,
              //     label: "0",
              //     color: "#DCEDFF"
              // }],
              show: !0
          },
          grid: [{
                      right: '5%',
                      top: '20%',
                      bottom: '10%',
                      width: '20%'
                  },
              
              ],
          
          geo: {
              map: "china",
              // right:'25%',
              // left:'18%',
              center: [105, 26.71],
              roam: !1,
              scaleLimit: {//通过鼠标控制的缩放
                  min: 1,
                  max: 2
              },
              zoom: 1.1,//当前缩放比例
              top: 120,//组件离容器上方的距离
              label: {
                  normal: {
                      show: !0,
                      fontSize: "14",
                      color: "rgba(0,0,0,0.7)"
                  }
              },
      
              itemStyle: {
                  normal: {
                      //shadowBlur: 50,
                      //shadowColor: 'rgba(0, 0, 0, 0.2)',
                      borderColor: "rgba(0, 0, 0, 0.5)"
                  },
                  emphasis: {
                      areaColor: "#f2d5ad",//鼠标放上去的颜色
                      shadowOffsetX: 0,
                      shadowOffsetY: 0,
                      borderWidth: 0
                  }
              }
          },
          series: [{
              name: "职位数",
              type: "map",
              geoIndex: 0,
              data: that.ShowData}]
          // },
          // {
          //         name: '哈喽喽',
          //         type: 'scatter',
          //         itemStyle: itemStyle,
          //         data: window.dataList
          //     }
          // ]
      }
			console.log(that.ShowData)
			 console.log(option)
			 myChart.setOption(option);
      // this.request3
      //   .get("/m1/1260169-0-default/getMap")
      //   .then(response => {
      //     console.log(response[0].city);
      //    
      //     console.log(this.options);
      //     myChart.setOption(this.options);
      //   })
      //   .catch(() => {
          
      // });
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
  #china_map {
  	width: 100%;
  	height: 400px;
  }
</style>