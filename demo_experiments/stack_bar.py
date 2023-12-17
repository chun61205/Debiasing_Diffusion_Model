import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

# Male : Female = 1 : 4
def dataset1():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])
        .add_yaxis("Male", [0.4, 0.4, 0.4, 0.4], stack="stack1", color='blue')
        .add_yaxis("Female", [0.6, 0.6, 0.6, 0.6], stack="stack1", color='pink')
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="A stacked bar chart",
                pos_top="5%",  # Adjust the position of the title to give more space
            ),
            legend_opts=opts.LegendOpts(
                pos_top="15%",  # Adjust the position of the legend to move it below the title
            ),
            yaxis_opts=opts.AxisOpts(
                name_gap=30,  # Adjust the gap between the y-axis name and the axis line
                axislabel_opts=opts.LabelOpts(
                    font_size=14,
                    margin=20,  # Adjust the margin to ensure labels don't overlap with axis line
                ),
            ),
        )
    )
    st_pyecharts(
        b, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

ST_STACKBAR_DEMOS = {
    "Male : Female = 1 : 4": (
        dataset1,
        None,
    )
}
