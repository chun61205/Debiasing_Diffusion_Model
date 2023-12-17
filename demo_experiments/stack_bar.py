import random
import streamlit as st
import pyecharts.options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts

# Male : Female = 1 : 4
def dataset1():
    b = (
        Bar()
        .add_xaxis(["ha", "Amazon", "IBM", "Oracle", "Google", "Alibaba"])
        .add_yaxis("2017-2018 Revenue in (billion $)", random.sample(range(100), 10))
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Top cloud providers 2018", subtitle="2017-2018 Revenue"
            ),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    st_pyecharts(
        b, key="echarts"
    )  # Add key argument to not remount component at every Streamlit run
    st.button("Randomize data")

ST_STACKBAR_DEMOS = {
    "Male : Female = 1 : 4": (
        dataset1,
        None,
    )
}
