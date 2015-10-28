
function test(tmp)
{
	alert(tmp);
}


function showchart(data){
	new iChart.Bar2D({
		render : 'weibototal',
		background_color : '#EEEEEE',
		data : data,
		title : 'weibo follows liking',
		subtitle : '10000 per one',
		footnote : 'data: east305',
		width : 800,
		height : 400,
		coordinate : {
			width : 640,
			height : 260,
			axis : {
				width : [0, 0, 1, 1]
			},
			scale : [{
				position : 'bottom',
				start_scale : 0,
				end_scale : 20000,
				scale_space : 2500
			}]
		},
		animation : true,
		sub_option : {
			listeners : {
				parseText : function(r, t) {
					return t ;
				}
			}
		},
		legend : {
			enable : false
		}
	}).draw();
}

function showsex(){
	var data = [
				{name : 'male',value : 52.5,color:'#4572a7'},
				{name : 'female',value : 34.3,color:'#aa4643'},
				{name : 'other',value : 8.4,color:'#89a54e'},
			];

	
	var chart = new iChart.Pie3D({
		render : 'weibosex',
		data: data,
		title : {
			text : 'weibo Sex ratio',
			height:40,
			fontsize : 30,
			color : '#282828'
		},
		footnote : {
			text : 'data:east305',
			color : '#486c8f',
			fontsize : 12,
			padding : '0 38'
		},
		sub_option : {
			mini_label_threshold_angle : 40,//迷你label的阀值,单位:角度
			mini_label:{//迷你label配置项
				fontsize:20,
				fontweight:600,
				color : '#ffffff'
			},
			label : {
				background_color:null,
				sign:false,//设置禁用label的小图标
				padding:'0 4',
				border:{
					enable:false,
					color:'#666666'
				},
				fontsize:11,
				fontweight:600,
				color : '#4572a7'
			},
			border : {
				width : 2,
				color : '#ffffff'
			},
			listeners:{
				parseText:function(d, t){
					return d.get('value')+"%";//自定义label文本
				}
			} 
		},
		legend:{
			enable:true,
			padding:0,
			offsetx:120,
			offsety:50,
			color:'#3e576f',
			fontsize:20,//文本大小
			sign_size:20,//小图标大小
			line_height:28,//设置行高
			sign_space:10,//小图标与文本间距
			border:false,
			align:'left',
			background_color : null//透明背景
		}, 
		shadow : true,
		shadow_blur : 6,
		shadow_color : '#aaaaaa',
		shadow_offsetx : 0,
		shadow_offsety : 0,
		background_color:'#f1f1f1',
		align:'right',//右对齐
		offsetx:-100,//设置向x轴负方向偏移位置60px
		offset_angle:-90,//逆时针偏移120度
		width : 800,
		height : 400,
		radius:150
	});
	//利用自定义组件构造右侧说明文本
	chart.plugin(new iChart.Custom({
			drawFn:function(){
				//在右侧的位置，渲染说明文字
				chart.target.textAlign('start')
				.textBaseline('top')
				.textFont('600 20px Verdana')
				.fillText('sex distribution',120,80,false,'#be5985',false,24)
				.textFont('600 12px Verdana')
				.fillText('Source:east305,2015',120,160,false,'#999999');
			}
	}));
	
	chart.draw();
};


function showsex2(){
	var data = [
				{name : 'male1',value : 68.34,color:'#3883bd'},
				{name : 'fema2',value : 26.83,color:'#3F5C71'},
				{name : 'Othe3',value : 4.83,color:'#a6bfd2'},
				{name : 'male4',value : 68.34,color:'#3883bd'},
/*				{name : 'fele5',value : 26.83,color:'#3F5C71'},
				{name : 'Oher6',value : 4.83,color:'#a6bfd2'},
				{name : 'male7',value : 68.34,color:'#3883bd'},
				{name : 'male8',value : 26.83,color:'#3F5C71'},
				{name : 'Oher9',value : 4.83,color:'#a6bfd2'},
				{name : 'male10',value : 68.34,color:'#3883bd'},
				{name : 'feme11',value : 26.83,color:'#3F5C71'},
				{name : 'Oter12',value : 4.83,color:'#a6bfd2'},
				{name : 'mlte13',value : 68.34,color:'#3883bd'},
				{name : 'fele14',value : 26.83,color:'#3F5C71'},
				{name : 'Oher15',value : 4.83,color:'#a6bfd2'},
				{name : 'male16',value : 68.34,color:'#3883bd'},
				{name : 'fale17',value : 26.83,color:'#3F5C71'},
				{name : 'ther18',value : 4.83,color:'#a6bfd2'},
				{name : 'male19',value : 68.34,color:'#3883bd'},
				{name : 'fale21',value : 26.83,color:'#3F5C71'},
				{name : 'Oher22',value : 4.83,color:'#a6bfd2'},
				{name : 'male23',value : 68.34,color:'#3883bd'},
				{name : 'fale24',value : 26.83,color:'#3F5C71'},
				{name : 'Oter25',value : 4.83,color:'#a6bfd2'},
				{name : 'male26',value : 68.34,color:'#3883bd'},
				{name : 'male27',value : 26.83,color:'#3F5C71'},
				{name : 'Oher28',value : 4.83,color:'#a6bfd2'},
				{name : 'male29',value : 68.34,color:'#3883bd'},
				{name : 'feme31',value : 26.83,color:'#3F5C71'},
				{name : 'Othr32',value : 4.83,color:'#a6bfd2'},
				{name : 'male33',value : 68.34,color:'#3883bd'},
				{name : 'fale34',value : 26.83,color:'#3F5C71'},
				{name : 'Oher35',value : 4.83,color:'#a6bfd2'},
				{name : 'male36',value : 68.34,color:'#3883bd'},
				{name : 'fale37',value : 26.83,color:'#3F5C71'},
				{name : 'Othr38',value : 4.83,color:'#a6bfd2'},
*/
			];
	
	var chart = new iChart.Pie3D({
		render : 'weibosex',
		title:{
			text:'weibo Sex ratio',
			color:'#e0e5e8',
			height:40,
			border:{
				enable:true,
				width:[0,0,2,0],
				color:'#343b3e'
			}
		},
		padding:'2 10',
		footnote:{
			text:'data:east305',
			color:'#e0e5e8',
			height:30,
			border:{
				enable:true,
				width:[2,0,0,0],
				color:'#343b3e'
			}
		},
		width : 800,
		height : 400,
		data:data,
		shadow:true,
		shadow_color:'#15353a',
		shadow_blur:8,
		background_color : '#3b4346',
		gradient:true,
		color_factor:0.28,
		gradient_mode:'RadialGradientOutIn',
		showpercent:true,
		decimalsnum:2,
		legend:{
			enable:true,
			padding:30,
			color:'#e0e5e8',
			border:{
				width:[0,0,0,2],
				color:'#343b3e'
			},
			background_color : null,
		},
		sub_option:{
			offsetx:-40,
			border:{
				enable:false
			},
			label : {
				background_color:'#fefefe',
				sign:false,//设置禁用label的小图标
				line_height:10,
				padding:4,
				border:{
					enable:true,
					radius : 4,//圆角设置
					color:'#e0e5e8'
				},
				fontsize:11,
				fontweight:600,
				color : '#444444'
			}
		},
		border:{
			width:[0,20,0,20],
			color:'#1e2223'
		}
	});
		
	chart.bound(0);
};


function showsex3(){
	var data = [
				{name : 'male1',value : 68.34,color:'#3883bd'},
				{name : 'fema2',value : 26.83,color:'#3F5C71'},
				{name : 'Othe3',value : 4.83,color:'#a6bfd2'},
				{name : 'male4',value : 68.34,color:'#3883bd'},
				{name : 'fele5',value : 26.83,color:'#3F5C71'},
				{name : 'Oher6',value : 4.83,color:'#a6bfd2'},
				{name : 'male7',value : 68.34,color:'#3883bd'},
				{name : 'male8',value : 26.83,color:'#3F5C71'},
				{name : 'Oher9',value : 4.83,color:'#a6bfd2'},
				{name : 'male10',value : 68.34,color:'#3883bd'},
				{name : 'feme11',value : 26.83,color:'#3F5C71'},
				{name : 'Oter12',value : 4.83,color:'#a6bfd2'},
				{name : 'mlte13',value : 68.34,color:'#3883bd'},
				{name : 'fele14',value : 26.83,color:'#3F5C71'},
				{name : 'Oher15',value : 4.83,color:'#a6bfd2'},
				{name : 'male16',value : 68.34,color:'#3883bd'},
				{name : 'fale17',value : 26.83,color:'#3F5C71'},
				{name : 'ther18',value : 4.83,color:'#a6bfd2'},
				{name : 'male19',value : 68.34,color:'#3883bd'},
				{name : 'fale21',value : 26.83,color:'#3F5C71'},
				{name : 'Oher22',value : 4.83,color:'#a6bfd2'},
				{name : 'male23',value : 68.34,color:'#3883bd'},
				{name : 'fale24',value : 26.83,color:'#3F5C71'},
				{name : 'Oter25',value : 4.83,color:'#a6bfd2'},
				{name : 'male26',value : 68.34,color:'#3883bd'},
				{name : 'male27',value : 26.83,color:'#3F5C71'},
				{name : 'Oher28',value : 4.83,color:'#a6bfd2'},
				{name : 'male29',value : 68.34,color:'#3883bd'},
				{name : 'feme31',value : 26.83,color:'#3F5C71'},
				{name : 'Othr32',value : 4.83,color:'#a6bfd2'},
				{name : 'male33',value : 68.34,color:'#3883bd'},
				{name : 'fale34',value : 26.83,color:'#3F5C71'},
				{name : 'Oher35',value : 4.83,color:'#a6bfd2'},
				{name : 'male36',value : 68.34,color:'#3883bd'},
				{name : 'fale37',value : 26.83,color:'#3F5C71'},
				{name : 'Othr38',value : 4.83,color:'#a6bfd2'},
			];
	
	new iChart.Pie2D({
		render : 'weibosex',
		data: data,
		title : 'weibo Sex ratio',
		background_color : '#EEEEEE',
		footnote : 'data: east305',
		legend : {
			enable : true
		},
		sub_option : {
			label : {
				background_color:null,
				sign:false,//设置禁用label的小图标
				padding:'0 4',
				border:{
					enable:false,
					color:'#666666'
				},
				fontsize:11,
				fontweight:600,
				color : '#4572a7'
			},
			border : {
				width : 2,
				color : '#ffffff'
			}
		},
		animation:true,
		showpercent:true,
		decimalsnum:2,
		width : 800,
		height : 680,
		radius:140
	}).draw();
};


function showlocation() {
	var data = [
				{name : 'MISE',value : 55.11,color : '#4572a7'},
				{name : 'Firefox',value : 29.84,color : '#aa4643'},
				{name : 'Chrome',value : 24.88,color : '#89a54e'},
				{name : 'Safari',value : 6.77,color : '#80699b'},
				{name : 'Opera',value : 2.02,color : '#3d96ae'},
				{name : 'MISE',value : 55.11,color : '#4572a7'},
				{name : 'Firefox',value : 29.84,color : '#aa4643'},
				{name : 'Chrome',value : 24.88,color : '#89a54e'},
				{name : 'Safari',value : 6.77,color : '#80699b'},
				{name : 'Opera',value : 2.02,color : '#3d96ae'},
				{name : 'MISE',value : 55.11,color : '#4572a7'},
				{name : 'Firefox',value : 29.84,color : '#aa4643'},
				{name : 'Chrome',value : 24.88,color : '#89a54e'},
				{name : 'Safari',value : 6.77,color : '#80699b'},
				{name : 'Opera',value : 2.02,color : '#3d96ae'},
				{name : 'MISE',value : 55.11,color : '#4572a7'},
				{name : 'Firefox',value : 29.84,color : '#aa4643'},
				{name : 'Chrome',value : 24.88,color : '#89a54e'},
				{name : 'Safari',value : 6.77,color : '#80699b'},
				{name : 'Opera',value : 2.02,color : '#3d96ae'},
			];

	var chart = new iChart.Column2D({
		render : 'weibolocation',
		data : data,
		title : {
			text : 'This is a sample spirit from HighCharts',
			color : '#3e576f'
		},
		subtitle : {
			text : 'Browser market share,April,2011 from 1 to 29 Feb 2012',
			color : '#6d869f'
		},
		footnote : {
			text : 'ichartjs.com',
			color : '#909090',
			fontsize : 11,
			padding : '0 38'
		},
		width : 800,
		height : 400,
		label : {
			fontsize:11,
			color : '#666666'
		},
		animation : true,//开启过渡动画
		animation_duration:800,//800ms完成动画
		shadow : true,
		shadow_blur : 2,
		shadow_color : '#aaaaaa',
		shadow_offsetx : 1,
		shadow_offsety : 0,
		column_width : 62,
		sub_option : {
			listeners : {
				parseText : function(r, t) {
					return t + "%";
				}
			},
			label : {
				fontsize:11,
				fontweight:600,
				color : '#4572a7'
			},
			border : {
				width : 2,
				color : '#ffffff'
			}
		},
		coordinate : {
			background_color : null,
			grid_color : '#c0c0c0',
			width : 680,
			axis : {
				color : '#c0d0e0',
				width : [0, 0, 1, 0]
			},
			scale : [{
				position : 'left',
				start_scale : 0,
				end_scale : 60,
				scale_space : 10,
				scale_enable : false,
				label : {
					fontsize:11,
					color : '#666666'
				}
			}]
		}
	});
	
	/**
	 *利用自定义组件构造左侧说明文本。
	 */
	chart.plugin(new iChart.Custom({
			drawFn:function(){
				/**
				 *计算位置
				 */	
				var coo = chart.getCoordinate(),
					x = coo.get('originx'),
					y = coo.get('originy'),
					H = coo.height;
				/**
				 *在左侧的位置，设置逆时针90度的旋转，渲染文字。
				 */
				chart.target.textAlign('center')
				.textBaseline('middle')
				.textFont('600 13px Verdana')
				.fillText('Total percent market share',x-40,y+H/2,false,'#6d869f', false,false,false,-90);
				
			}
	}));
	
	chart.draw();
};
