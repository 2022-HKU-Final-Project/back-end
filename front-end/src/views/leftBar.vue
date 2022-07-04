<template>
	<div>
		<div id="chartsBar" ref="chartBar"></div>
	</div>
</template>

<script>
import echarts from 'echarts';
export default{
methods:{
	Chartsfuct() {
		var dom = this.$refs.chartBar;
		var myChart = this.$echarts.init(dom);
		let colorArray = [
		    {
		        top: '#056CBB', //黄
		        bottom: 'rgba(11,42,84,.3)',
		    },
		    {
		        top: '#1ace4a', //绿
		        bottom: 'rgba(11,42,84, 0.3)',
		    },
		    {
		        top: '#4bf3ff', //蓝
		        bottom: 'rgba(11,42,84,.3)',
		    },
		    {
		        top: '#4f9aff', //深蓝
		        bottom: 'rgba(11,42,84,.3)',
		    },
		    {
		        top: '#9AFFF1', //粉
		        bottom: 'rgba(11,42,84,.3)',
		    },
		    {
		        top: '#8AE1FF', //粉
		        bottom: 'rgba(11,42,84,.3)',
		    },
		    {
		        top: '#F0E1C2', //粉
		        bottom: 'rgba(11,42,84,.3)',
		    },
		];
		let seriesData = [60, 132, 89, 134, 60, 85, 105];
		let yAxisData = ['物联网设备', '工控控制设备', '网络安全专用产品', '智能融合终端', '能源控制器', '5G CPE', '5G 模组'];
		var option = {
		    tooltip: {
		        show: true,
		        formatter: '{b}:{c}',
		    },
		    grid: {
		        left: '5%',
		        top: '12%',
		        right: '1%',
		        bottom: '8%',
		        containLabel: true,
		    },
		
		    xAxis: {
		        type: 'value',
		        show: false,
		        position: 'top',
		        axisTick: {
		            show: false,
		        },
		        axisLine: {
		            show: false,
		            lineStyle: {
		                color: '#fff',
		            },
		        },
		        splitLine: {
		            show: false,
		        },
		    },
		    yAxis: [
		        {
		            type: 'category',
		            axisTick: {
		                show: false,
		                alignWithLabel: false,
		                length: 5,
		            },
		            splitLine: {
		                //网格线
		                show: false,
		            },
		            inverse: 'true', //排序
		            axisLine: {
		                show: false,
		                lineStyle: {
		                    color: '#fff',
		                },
		            },
		            data: yAxisData,
		        },
		    ],
		    series: [
		        {
		            name: '能耗值',
		            type: 'bar',
		            label: {
		                normal: {
		                    show: true,
		                    position: 'right',
		                    formatter: '{c}',
		                    textStyle: {
		                        color: 'white', //color of value
		                    },
		                },
		            },
		            itemStyle: {
		                normal: {
		                    show: true,
		                    color: function (params) {
		                        let num = colorArray.length;
		                        return {
		                            type: 'linear',
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
		                    borderColor: '#333',
		                },
		            },
		            barGap: '0%',
		            barCategoryGap: '50%',
		            data: seriesData,
		        },
		    ],
		};
		myChart.setOption(option);
	}
}
},
mounted:{
	this.Chartsfuct()
}
</script>

<style scoped="scoped">
	#chartsBar {
		width: 40%;
		height: 300px;
		float: left;
	}

</style>
