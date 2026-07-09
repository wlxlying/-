"""
全国店面 KPI 对比雷达图
依赖: pip install pyecharts
运行: python store_kpi_radar.py
输出: store_kpi_radar.html
"""

from pyecharts import options as opts
from pyecharts.charts import Radar
from pathlib import Path

KPI_INDICATORS = [
    {"name": "销售额(万)", "max": 500},
    {"name": "客流量(千)", "max": 200},
    {"name": "转化率(%)", "max": 100},
    {"name": "客单价(元)", "max": 500},
    {"name": "复购率(%)", "max": 100},
    {"name": "满意度", "max": 100},
]

STORES = {
    "北京旗舰店": [420, 180, 72, 380, 65, 92],
    "上海中心店": [480, 195, 78, 420, 70, 95],
    "广州天河店": [350, 150, 68, 320, 58, 88],
    "成都春熙店": [310, 130, 62, 280, 55, 85],
    "武汉光谷店": [280, 120, 58, 260, 52, 82],
}


def build_radar_chart() -> Radar:
    radar = (
        Radar(init_opts=opts.InitOpts(width="900px", height="600px", page_title="全国店面KPI对比"))
        .add_schema(
            schema=KPI_INDICATORS,
            shape="polygon",
            center=["50%", "55%"],
            radius="65%",
            splitarea_opt=opts.SplitAreaOpts(is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=0.1)),
            splitline_opt=opts.SplitLineOpts(is_show=True),
            axisline_opt=opts.AxisLineOpts(linestyle_opts=opts.LineStyleOpts(color="#ccc")),
        )
    )

    for store_name, values in STORES.items():
        radar.add(
            series_name=store_name,
            data=[values],
            linestyle_opts=opts.LineStyleOpts(width=2),
            areastyle_opts=opts.AreaStyleOpts(opacity=0.15),
        )

    radar.set_global_opts(
        title_opts=opts.TitleOpts(
            title="全国店面 KPI 对比雷达图",
            subtitle="示例数据 · 双击图例可单独显示/隐藏门店",
            pos_left="center",
        ),
        legend_opts=opts.LegendOpts(orient="horizontal", pos_bottom="2%"),
        tooltip_opts=opts.TooltipOpts(trigger="item"),
    )
    return radar


def main() -> None:
    output = Path(__file__).parent / "store_kpi_radar.html"
    build_radar_chart().render(str(output))
    print(f"雷达图已保存至: {output}")


if __name__ == "__main__":
    main()
