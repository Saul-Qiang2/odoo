odoo.define('bp_eam_supplier.SupplierIndex', ['web.ControlPanelMixin', 'web.AbstractAction', 'web.core', 'web.Widget'], function (require) {
    'use strict';

    var ControlPanelMixin = require('web.ControlPanelMixin');
    var AbstractAction = require('web.AbstractAction');
    var core = require("web.core");
    var QWeb = core.qweb;

    //核心方法，js渲染数据
    var ClientAction = AbstractAction.extend({
        //template定义页面视图t-name
        template: 'supplier_index_template',
        //  这里写入js方法给页面传值， 方法写法参考  搜索Widget.extend
        init: function (parent) {
            this._super(parent);
            var self = this;
            self.get_supplier_rating_rate();
        },

        // 获取统计信息并渲染

        // 获取 供应商分布比例 的渲染数据
        get_supplier_rating_rate:function (data) {
            var url = '/getSupplierRatingRate/';
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart1");
                var myChart1 = echarts.init(dom);
                // var app = {};
                var option = {
                    color: ['#F79646', '#66C383', '#33CC33', '#339933', '#FF00FF'],
                    title: {
                        text: '所有者价值对比',
                        x: 'center'
                    },
                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b} : {c} ({d}%)"
                    },
                    legend: {
                        // orient: 'vertical',
                        // top: 'middle',
                        bottom: 5,
                        left: 'center',
                        data: ['A仓库','B仓库','C仓库','D仓库','E仓库'],
                    },
                    series: [
                        {
                            name: '所有者价值对比',
                            type: 'pie',
                            radius: '65%',
                            center: ['50%', '50%'],
                            selectedMode: 'single',
                            label: {
                                normal: {
                                    show: false
                                },
                                emphasis: {
                                    show: false
                                }
                            },
                            data: [{value:335, name:'A仓库'},
                                    {value:310, name:'B仓库'},
                                    {value:234, name:'C仓库'},
                                    {value:135, name:'D仓库'},
                                    {value:1548, name:'E仓库'}
                            ],
                            itemStyle: {
                                emphasis: {
                                    shadowBlur: 10,
                                    shadowOffsetX: 0,
                                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                                }
                            }
                        }
                    ]
                };

                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart2");
                var myChart1 = echarts.init(dom);
                // var app = {};
                // var app.title = '环形图';

                var option = {
                    tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b}: {c} ({d}%)"
                    },
                    legend: {
                        orient: 'vertical',
                        x: 'left',
                        data:['A仓库','B仓库','C仓库','D仓库','E仓库'],
                    },
                    series: [
                        {
                            name:'库存量对比',
                            type:'pie',
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            label: {
                                normal: {
                                    show: false,
                                    position: 'center'
                                },
                                emphasis: {
                                    show: true,
                                    textStyle: {
                                        fontSize: '30',
                                        fontWeight: 'bold'
                                    }
                                }
                            },
                            labelLine: {
                                normal: {
                                    show: false
                                }
                            },
                            data:[
                                {value:335, name:'A仓库'},
                                {value:310, name:'B仓库'},
                                {value:234, name:'C仓库'},
                                {value:135, name:'D仓库'},
                                {value:1548, name:'E仓库'}
                            ]
                        }
                    ]
                };

                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart3");
                var myChart1 = echarts.init(dom);
                // var app = {};

                var xAxisData = [];
                var data1 = [];
                var data2 = [];
                var data3 = [];
                var data4 = [];


                for (var i = 0; i < 5; i++) {
                    xAxisData.push('Class' + i);
                    data1.push(Math.round(Math.random()*1000).toFixed(2));
                    data2.push(-Math.round(Math.random()*800).toFixed(2));
                    data3.push(Math.round(Math.random()*1000).toFixed(2));
                    data4.push(-Math.round(Math.random()*800).toFixed(2));
                }

                var itemStyle = {
                    normal: {
                    },
                    emphasis: {
                        barBorderWidth: 1,
                        shadowBlur: 10,
                        shadowOffsetX: 0,
                        shadowOffsetY: 0,
                        shadowColor: 'rgba(0,0,0,0.5)'
                    }
                };

                var option = {
                    backgroundColor: '#eee',
                    legend: {
                        data: ['A入库', 'A出库', 'B入库', 'B出库',],
                        align: 'left',
                        left: "center",
                        top: 'bottom',
                    },
                    brush: {
                        toolbox: ['rect', 'polygon', 'lineX', 'lineY', 'keep', 'clear'],
                        xAxisIndex: 0
                    },
                    toolbox: {
                        feature: {
                            magicType: {
                                type: ['stack', 'tiled']
                            },
                            dataView: {}
                        }
                    },
                    tooltip: {},
                    xAxis: {
                        data: xAxisData,
                        name: 'X Axis',
                        nameRotate: 90,
                        nameGap:5,
                        silent: false,
                        axisLine: {onZero: true},
                        splitLine: {show: false},
                        splitArea: {show: false}
                    },
                    yAxis: {
                        inverse: true,
                        splitArea: {show: false}
                    },
                    grid: {
                        left: 100
                    },
                    visualMap: {
                        type: 'continuous',
                        dimension: 1,
                        text: ['High', 'Low'],
                        inverse: true,
                        itemHeight: 200,
                        calculable: true,
                        min: -1000,
                        max: 1000,
                        top: "middle",
                        left: 5,
                        inRange: {
                            colorLightness: [0.4, 0.8]
                        },
                        outOfRange: {
                            color: '#bbb'
                        },
                        controller: {
                            inRange: {
                                color: '#2f4554'
                            }
                        }
                    },
                    series: [
                        {
                            name: 'A入库',
                            type: 'bar',
                            stack: 'one',
                            itemStyle: itemStyle,
                            data: data1
                        },
                        {
                            name: 'A出库',
                            type: 'bar',
                            stack: 'one',
                            itemStyle: itemStyle,
                            data: data2
                        },
                        {
                            name: 'B入库',
                            type: 'bar',
                            stack: 'two',
                            itemStyle: itemStyle,
                            data: data3
                        },
                        {
                            name: 'B出库',
                            type: 'bar',
                            stack: 'two',
                            itemStyle: itemStyle,
                            data: data4
                        }
                    ]
                };

                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart4");
                var myChart1 = echarts.init(dom);
                // var app = {};

                var data = [
                    [5000, 10000, 6785.71],
                    [4000, 10000, 6825],
                    [3000, 6500, 4463.33],
                    [2500, 5600, 3793.83],
                    [2000, 4000, 3060],
                    [2000, 4000, 3222.33],
                    [2500, 4000, 3133.33],
                    [1800, 4000, 3100],
                    [2000, 3500, 2750],
                    [2000, 3000, 2500],
                    [1800, 3000, 2433.33],
                    [2000, 2700, 2375],
                    [1500, 2800, 2150],
                    [1500, 2300, 2100],
                    [1600, 3500, 2057.14],
                    [1500, 2600, 2037.5],
                    [1500, 2417.54, 1905.85],
                    [1500, 2000, 1775],
                    [1500, 1800, 1650]
                ];
                var cities = ['北京', '上海', '深圳', '广州', '苏州', '杭州', '南京', '福州', '青岛', '济南', '长春', '大连', '温州', '郑州', '武汉', '成都', '东莞', '沈阳', '烟台'];
                var barHeight = 50;

                var option = {
                    title: {
                        text: '在中国租个房子有多贵？',
                        subtext: '市中心一室月租费（数据来源：https://www.numbeo.com）'
                    },
                    legend: {
                        show: true,
                        data: ['价格范围', '均值']
                    },
                    grid: {
                        top: 100
                    },
                    angleAxis: {
                        type: 'category',
                        data: cities
                    },
                    tooltip: {
                        show: true,
                        formatter: function (params) {
                            var id = params.dataIndex;
                            return cities[id] + '<br>最低：' + data[id][0] + '<br>最高：' + data[id][1] + '<br>平均：' + data[id][2];
                        }
                    },
                    radiusAxis: {
                    },
                    polar: {
                    },
                    series: [{
                        type: 'bar',
                        itemStyle: {
                            normal: {
                                color: 'transparent'
                            }
                        },
                        data: data.map(function (d) {
                            return d[0];
                        }),
                        coordinateSystem: 'polar',
                        stack: '最大最小值',
                        silent: true
                    }, {
                        type: 'bar',
                        data: data.map(function (d) {
                            return d[1] - d[0];
                        }),
                        coordinateSystem: 'polar',
                        name: '价格范围',
                        stack: '最大最小值'
                    }, {
                        type: 'bar',
                        itemStyle: {
                            normal: {
                                color: 'transparent'
                            }
                        },
                        data: data.map(function (d) {
                            return d[2] - barHeight;
                        }),
                        coordinateSystem: 'polar',
                        stack: '均值',
                        silent: true,
                        z: 10
                    }, {
                        type: 'bar',
                        data: data.map(function (d) {
                            return barHeight * 2
                        }),
                        coordinateSystem: 'polar',
                        name: '均值',
                        stack: '均值',
                        barGap: '-100%',
                        z: 10
                    }],
                    legend: {
                        show: true,
                        data: ['A', 'B', 'C']
                    }
                };


                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart5");
                var myChart1 = echarts.init(dom);
                // var app = {};
                var option = {
                    title: {
                        text: '折线图堆叠'
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data:['A仓库','B仓库','C仓库','D仓库','E仓库'],
                        left: '25%',
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['周一','周二','周三','周四','周五','周六','周日']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            name:'A仓库',
                            type:'line',
                            stack: '总量',
                            data:[120, 132, 101, 134, 90, 230, 210]
                        },
                        {
                            name:'B仓库',
                            type:'line',
                            stack: '总量',
                            data:[220, 182, 191, 234, 290, 330, 310]
                        },
                        {
                            name:'C仓库',
                            type:'line',
                            stack: '总量',
                            data:[150, 232, 201, 154, 190, 330, 410]
                        },
                        {
                            name:'D仓库',
                            type:'line',
                            stack: '总量',
                            data:[320, 332, 301, 334, 390, 330, 320]
                        },
                        {
                            name:'E仓库',
                            type:'line',
                            stack: '总量',
                            data:[820, 932, 901, 934, 1290, 1330, 1320]
                        }
                    ]
                };

                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });
            $.getJSON(url, function (data) {
                // 渲染供应商分布比例
                // var result = eval(data);
                var dom = document.getElementById("chart6");
                var myChart1 = echarts.init(dom);
                // var app = {};

                var data = [];

                for (var i = 0; i <= 100; i++) {
                    var theta = i / 100 * 360;
                    var r = 5 * (1 + Math.sin(theta / 180 * Math.PI));
                    data.push([r, theta]);
                }

                var option = {
                    title: {
                        text: '极坐标双数值轴'
                    },
                    legend: {
                        data: ['line']
                    },
                    polar: {},
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {
                            type: 'cross'
                        }
                    },
                    angleAxis: {
                        type: 'value',
                        startAngle: 0
                    },
                    radiusAxis: {
                    },
                    series: [{
                        coordinateSystem: 'polar',
                        name: 'line',
                        type: 'line',
                        data: data
                    }]
                };

                myChart1.setOption(option, true);

                window.addEventListener("resize", function () {
                    myChart1.resize();
                });
            });

        },

        });
    //绑定到对应界面
    core.action_registry.add("bp_eam_supplier.supplier_index_tag", ClientAction);
    return ClientAction

});