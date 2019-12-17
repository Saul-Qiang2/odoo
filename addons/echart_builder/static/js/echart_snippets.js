odoo.define('echart_builder.EchartSnippets', ['web.ControlPanelMixin', 'web.AbstractAction', 'web.core', 'web.Widget'], function (require) {
    'use strict';

    var AbstractAction = require('web.AbstractAction');
    var core = require("web.core");

    //核心方法，js渲染数据
    var ClientAction = AbstractAction.extend({
        //template定义页面视图t-name
        template: 'echart_snippets_template',
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

        },

        });
    //绑定到对应界面
    core.action_registry.add("echart_builder.echart_snippets_tag", ClientAction);
    return ClientAction

});

// myChart 为 echart 初始化的 dom 元素；
// ckey 为两种可能，一种是该 ssdb 的 key；另一种为该 ssdb 的 key 的 df 数据；
// height 为该插件的高度；
// width 为该插件的宽度；
// div 为该插件的 dom 元素；
// res 为该插件的高级参数；参数顺序固定不可更改；
function draw_echart(mychart, ckey, height, width, div, res){
    var width = parseFloat(width)
    var height = parseFloat(height)
    
//    配置项参数设置
    
//    获取数据
    data_base(ckey, function (dataAll) {
        var data = dataAll.data;
        var columns = dataAll.columns;
        
    })
    
    
    
}