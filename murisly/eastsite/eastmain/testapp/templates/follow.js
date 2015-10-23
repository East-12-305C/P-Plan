
$(function() {
	var data = [{
		name : '微博小秘书',
		value : 15555,
		color : '#4572a7'
	}, {
		name : '新手指南',
		value : 12630,
		color : '#4572a7'
	}, {
		name : '微博管理员',
		value : 11651,
		color : '#4572a7'
	}, {
		name : '姚晨',
		value : 7841,
		color : '#4572a7'
	}, {
		name : '谢娜',
		value : 7541,
		color : '#4572a7'
	}, {
		name : '赵薇',
		value : 7491,
		color : '#4572a7'
	}, {
		name : '何炅',
		value : 7192,
		color : '#4572a7'
	}, {
		name : 'angelababy',
		value : 7152,
		color : '#4572a7'
	}, {
		name : '微博雷达',
		value : 6595,
		color : '#4572a7'
	}, {
		name : '林心如',
		value : 6518,
		color : '#4572a7'
	}];
	
	new iChart.Bar2D({
		render : 'canvasDiv',
		background_color : '#EEEEEE',
		data : data,
		title : 'weibo follows liking',
		subtitle : '10000 unit',
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
});