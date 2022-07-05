<template>
  <div id="china_map_box">
      <div id="china_map"></div>
  </div>
</template>

<script>
// import echarts from "echarts";
import * as echarts from 'echarts'
import '../helper/china.js'
export default {
  data() {
    return {
      //echart 配制option  
      options: {
        tooltip: {
          triggerOn: "mousemove",   //mousemove、click
          padding:8,
          borderWidth:1,
          borderColor:'#409eff',
          backgroundColor:'rgba(255,255,255,0.7)',
          textStyle:{
            color:'#ffffff',
            fontSize:13
          },
          // formatter: function(e, t, n) {
          //   let data = e.data;
          //   //模拟数据
          //   data.specialImportant = Math.random()*1000 | 0;
          //   data.import = Math.random()*1000 | 0;
          //   data.compare = Math.random()*1000 | 0;
          //   data.common = Math.random()*1000 | 0;
          //   data.specail = Math.random()*1000 | 0;
 
          //   let context = `
          //      <div>
          //          <p><b style="font-size:15px;">${data.name}</b>(2020年第一季度)</p>
          //          <p class="tooltip_style"><span class="tooltip_left">事件总数</span><span class="tooltip_right">${data.value}</span></p>
          //          <p class="tooltip_style"><span class="tooltip_left">特别重大事件</span><span class="tooltip_right">${data.specialImportant}</span></p>
          //          <p class="tooltip_style"><span class="tooltip_left">重大事件</span><span class="tooltip_right">${data.import}</span></p>
          //          <p class="tooltip_style"><span class="tooltip_left">较大事件</span><span class="tooltip_right">${data.compare}</span></p>
          //          <p class="tooltip_style"><span class="tooltip_left">一般事件</span><span class="tooltip_right">${data.common}</span></p>
          //          <p class="tooltip_style"><span class="tooltip_left">特写事件</span><span class="tooltip_right">${data.specail}</span></p>
          //      </div>
          //   `
          //   return context;
          // }
        },
        visualMap: {
          show:true,
          left: 26,
          bottom: 40,
          showLabel:true,
		  textStyle:{
		    color:'#ffffff',
		    fontSize:13
		  },
          pieces: [
            {
              gte: 100,
              label: ">= 1000",
              color: "#1f307b"
            },
            {
              gte: 500,
              lt: 999,
              label: "500 - 999",
              color: "#3c57ce"
            },
            {
              gte: 100,
              lt:499,
              label: "100 - 499",
              color: "#6f83db"
            },
            {
              gte: 10,
              lt: 99,
              label: "10 - 99",
              color: "#9face7"
            },
            {
              lt:10,
              label:'<10',
              color: "#bcc5ee"
            }
          ]
        },
        geo: {
          map: "china",
          scaleLimit: {
            min: 1,
            max: 2
          },
          zoom: 1,
          top: 50,
          label: {
            normal: {
              show:true,
              fontSize: "14",
              color: "rgba(255, 255, 255, 0.7)"
            }
          },
          itemStyle: {
            normal: {
              //shadowBlur: 50,
              //shadowColor: 'rgba(0, 0, 0, 0.2)',
              borderColor: "rgba(0, 0, 0, 0.2)"
            },
            emphasis: {
              areaColor: "#f2d5ad",
              shadowOffsetX: 0,
              shadowOffsetY: 0,
              borderWidth: 0
            }
          }
        },
        series: [
          {
            name: "突发事件",
            type: "map",
            geoIndex: 0,
            data:[]
          }
        ]
      },
    };
  },
  methods: {
    //初始化中国地图
    initEchartMap() {
      let mapDiv = document.getElementById('china_map');
      let myChart = echarts.init(mapDiv);
      this.request2
        .post("/dashboard/map", this.queryFilter)
        .then(response => {
          console.log(response);
          this.options.series[0]['data'] = response;
          console.log(this.options);
          myChart.setOption(this.options);
        })
        .catch(() => {
          
      });
    },
  },
  created() {
    
  },
  mounted() {
    this.initEchartMap();
  }
};
</script>
 
<style scoped="scoped">
  #china_map {
  	width: 100%;
  	height: 400px;
  }
</style>