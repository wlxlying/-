// 全国店面 KPI 对比雷达图 — 可直接粘贴到 ECharts 编辑器或 setOption(option)
// 使用方式: chart.setOption(option);

var option = {
  title: {
    text: '全国店面 KPI 对比雷达图',
    subtext: '示例数据 · 点击图例显示/隐藏门店',
    top: 10,
    left: 10
  },
  tooltip: {
    trigger: 'item',
    formatter: function (params) {
      var indicators = ['销售额(万)', '客流量(千)', '转化率(%)', '客单价(元)', '复购率(%)', '满意度'];
      var lines = ['<b>' + params.name + '</b>'];
      for (var i = 0; i < params.value.length; i++) {
        lines.push(indicators[i] + '：' + params.value[i]);
      }
      return lines.join('<br/>');
    }
  },
  legend: {
    type: 'scroll',
    bottom: 10,
    data: ['北京旗舰店', '上海中心店', '广州天河店', '成都春熙店', '武汉光谷店']
  },
  color: ['#5470c6', '#91cc75', '#fac858', '#ee6666', '#73c0de'],
  radar: {
    center: ['50%', '52%'],
    radius: '62%',
    shape: 'polygon',
    splitArea: {
      areaStyle: {
        color: ['rgba(114, 172, 209, 0.05)', 'rgba(114, 172, 209, 0.1)']
      }
    },
    axisLine: {
      lineStyle: { color: '#ccc' }
    },
    indicator: [
      { text: '销售额(万)', max: 500 },
      { text: '客流量(千)', max: 200 },
      { text: '转化率(%)', max: 100 },
      { text: '客单价(元)', max: 500 },
      { text: '复购率(%)', max: 100 },
      { text: '满意度', max: 100 }
    ]
  },
  series: (function () {
    var storeList = [
      { name: '北京旗舰店', value: [420, 180, 72, 380, 65, 92], color: '#5470c6' },
      { name: '上海中心店', value: [480, 195, 78, 420, 70, 95], color: '#91cc75' },
      { name: '广州天河店', value: [350, 150, 68, 320, 58, 88], color: '#fac858' },
      { name: '成都春熙店', value: [310, 130, 62, 280, 55, 85], color: '#ee6666' },
      { name: '武汉光谷店', value: [280, 120, 58, 260, 52, 82], color: '#73c0de' }
    ];

    var series = [];
    for (var i = 0; i < storeList.length; i++) {
      var store = storeList[i];
      series.push({
        type: 'radar',
        name: store.name,
        symbol: 'circle',
        symbolSize: 6,
        lineStyle: {
          width: 2,
          color: store.color
        },
        itemStyle: {
          color: store.color
        },
        areaStyle: {
          color: store.color,
          opacity: 0.15
        },
        label: {
          show: true,
          color: store.color,
          fontSize: 11,
          distance: 4,
          formatter: function (params) {
            return params.value;
          }
        },
        emphasis: {
          areaStyle: {
            opacity: 0.35
          },
          label: {
            show: true,
            fontSize: 12,
            fontWeight: 'bold'
          }
        },
        data: [
          {
            value: store.value,
            name: store.name
          }
        ]
      });
    }
    return series;
  })()
};

// 若在 HTML 中使用:
// var chart = echarts.init(document.getElementById('main'));
// chart.setOption(option);
