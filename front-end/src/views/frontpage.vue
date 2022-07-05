<template>
	<div>
		<div id="main">
			<div id="Charts">
			    <div id="mainTop">数据可视化大屏展示{{msg}}</div>
				<div id="LayLeft">
					<div class="Leftmains">
						<div id="chartsBar" ref="chartBar"></div>
					</div>
					<div class="Leftmains">
						<div id="chartsPie" ref="chartPie">
						</div>
					</div>
				</div>
				<div id="LayCenter">
					<div id="china"><china></china></div>
				</div>
				<div id="LayRight">
					<div class="Leftmains">
						<rightLine></rightLine>
					</div>
					<div class="Leftmains">
						<rightRadio></rightRadio>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import china from './china.vue';
	import rightLine from './rightLine.vue';
	import rightRadio from './rightRadio.vue';
	import echarts from 'echarts';
	export default {
		data(){
			return{
				
			}
		},
		props:['msg'],
		components: {
			rightLine,
			rightRadio,
			china
		},
		methods: {
			Chartsfuct() {
					var dom = this.$refs.chartBar;
					var myChart = this.$echarts.init(dom);
					this.request2
				.post("/dashboard/education", this.queryFilter)
				.then(response => {
					// console.log(response);
					// let seriesData = [60, 132, 89, 134, 60, 85, 105];
					// let yAxisData = ['物联网设备', '工控控制设备', '网络安全专用产品', '智能融合终端', '能源控制器', '5G CPE', '5G 模组'];
					let seriesData = [];
					let yAxisData = [];
					for(var i = 0; i < response.length; i++){
						yAxisData.push(response[i].education);
						seriesData.push(response[i].num);
					}
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
					var option = {
					    tooltip: {
					        show: true,
					        formatter: '{b}:{c}',
					    },
					    grid: {
					        left: '5%',
					        top: '5%',
					        right: '1%',
					        bottom: '20%',
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
				})
				.catch(() => {
				
				});
					
			},
			ChartsPie() {
				var dom = this.$refs.chartPie;
				var myChart = this.$echarts.init(dom);
				this.request2
				.post("/dashboard/salary", this.queryFilter)
				.then(response => {
					// console.log(response);
					var salary = response[0].salary;
					var data = []
					var legend = []
					for(var key in salary){
						// console.log(key, salary[key])
						data.push({
							name: key,
							value: salary[key]
						});
						legend.push(key)
					}
					var option = {
					legend: {
						orient: 'horizontal',
						bottom: 5,
						 itemWidth:10,
						data: legend, //有数据
						textStyle: {
							color: "#fff",
							fontSize: 10
						}
					},
					tooltip: {
						trigger: 'item',
						formatter: '{a} <br/>{b} : {c} ({d}%)'
					},
					series: [{
						name: '薪水',
						type: 'pie',
						radius: ['30%', '80%'],
						center: ['50%', '50%'],
						roseType: 'radius',
						data: data,
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
					}]
				};
					myChart.setOption(option);
				})
				.catch(() => {
				
				});
			}
		},
		mounted() {
			this.Chartsfuct()
			this.ChartsPie()
		}
	}
</script>

<style scoped="scoped">
	#mainTop{
		width: 100%;
		height: 100px;
		display: flex;
		justify-content: center;
		align-items: center;
		font-size: 30px;
		color: #FFFFFF;
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
	#LayCenter{
		width: 46%;
		height: 800px;
		display: flex;
		justify-content: center;
		margin: 0 2%;
		float: left;
	}
	#LayLeft{
		width: 23%;
		float: left;
		margin-left: 2%;
		height: 900px;
	}
	#LayRight{
		width: 23%;
		float: left;
		margin-right: 2%;
		height: 900px;
	}
	.Leftmains{
		width: 100%;
		border: 1px solid #3370FF;
		margin-bottom: 20px;
		border-radius: 20px;
		height: 300px;
	}
	#china{
		width: 100%;
	    border: 1px solid #00aaff;
		border-radius: 20px;
		height: 400px;
	}
</style>
