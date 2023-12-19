import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

# Male : Female = 1 : 4
def dataset1():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.36, 0.39, 0.58, 0.6], stack="stack1", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.64, 0.61, 0.42, 0.4], stack="stack1", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="male : female = 1 : 4 (training dataset)",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="10%",
            ),
            yaxis_opts=opts.AxisOpts(
                name_gap=40, 
                axislabel_opts=opts.LabelOpts(
                    font_size=14,
                    margin=15,
                ),
            ),
        )
    )
    st_pyecharts(
        b, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run

def dataset2():
    b = (
        Bar()
        .add_xaxis(["0", "0.01", "0.05", "0.1"])  # Alpha values as categories
        .add_yaxis("Male", [0.8, 0.89, 0.64, 0.9], stack="stack1", color='blue')  # Male proportions, stacked
        .add_yaxis("Female", [0.2, 0.11, 0.36, 0.1], stack="stack1", color='pink')  # Female proportions, stacked
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Male and Female Proportions at Different Alpha Values",
                subtitle="male : female = 4 : 1 (training dataset)",
            ),
            legend_opts=opts.LegendOpts(
                pos_top="10%",
            ),
            yaxis_opts=opts.AxisOpts(
                name_gap=40, 
                axislabel_opts=opts.LabelOpts(
                    font_size=14,
                    margin=15,
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
    ),
    "Male : Female = 4 : 1": (
        dataset2,
        None,
    )
}