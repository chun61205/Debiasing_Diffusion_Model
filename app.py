import inspect
import textwrap

import streamlit as st

from demo_model import ST_MODEL_DEMOS
from demo_experiments import ST_EXPS_DEMOS
from demo_results import ST_RESULTS_DEMOS


def main():
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

    demo()

    if selected_api == "model":
        st.title("Model")
    elif selected_api == "experiments":
        st.title("Experiments")
    elif selected_api == "results":
        st.title("Results")

    st.markdown(f"Credit: {url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="De-Biasing Diffusion Model", page_icon=":chart_with_upwards_trend:"
    )
    main()