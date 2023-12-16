import inspect
import textwrap

import streamlit as st

from demo_model import ST_MODEL_DEMOS
from demo_experiments import ST_EXPS_DEMOS
from demo_results import ST_RESULTS_DEMOS


def main():
    st.title("Streamlit ECharts Demo")

    with st.sidebar:
        st.header("Configuration")
        api_options = ("model", "experiments", "results")
        selected_api = st.selectbox(
            label="Options",
            options=api_options,
        )

        api_to_demo_dict = {
            "model": ST_MODEL_DEMOS,
            "experiments": ST_EXPS_DEMOS,
            "results": ST_RESULTS_DEMOS
        }
        selected_demo_dict = api_to_demo_dict[selected_api]

        page_options = list(api_to_demo_dict.get(selected_api, {}).keys())

        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )

        demo, url = selected_demo_dict[selected_page]

        if selected_api == "echarts":
            st.caption(
                """ECharts demos are extracted from https://echarts.apache.org/examples/en/index.html, 
            by copying/formattting the 'option' json object into st_echarts.
            Definitely check the echarts example page, convert the JSON specs to Python Dicts and you should get a nice viz."""
            )
        if selected_api == "pyecharts":
            st.caption(
                """Pyecharts demos are extracted from https://github.com/pyecharts/pyecharts-gallery,
            by copying the pyecharts object into st_pyecharts. 
            Pyecharts is still using ECharts 4 underneath, which is why the theming between st_echarts and st_pyecharts is different."""
            )

    demo()

    sourcelines, _ = inspect.getsourcelines(demo)
    with st.expander("Source Code"):
        st.code(textwrap.dedent("".join(sourcelines[1:])))
    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="De-Biasing Diffusion Model", page_icon=":chart_with_upwards_trend:"
    )
    main()