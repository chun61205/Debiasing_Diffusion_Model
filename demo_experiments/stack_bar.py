import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

# Male : Female = 1 : 4
def dataset1():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.4, 0.4, 0.4, 0.4], stack="stack1", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.6, 0.6, 0.6, 0.6], stack="stack1", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="A stacked bar chart",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="10%",  # Increase this value to move the legend below the title
            ),
            yaxis_opts=opts.AxisOpts(
                name_gap=40,  # Adjust the gap between the y-axis name and the axis line
                axislabel_opts=opts.LabelOpts(
                    font_size=14,
                    margin=15,  # Adjust the margin to ensure labels don't overlap with axis line
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
