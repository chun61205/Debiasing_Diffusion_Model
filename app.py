import streamlit as st

from demo_introduction import ST_INTRODUCTION_DEMOS
from demo_experiments import ST_EXPS_DEMOS
from demo_datasets import ST_DATASETS_DEMOS
from demo_demos import ST_DEMO_DEMOS


def main():
    with st.sidebar:
        st.header("Configuration")
        api_options = ("Introduction", "Training Sets", "Experiments", "Demos")
        selected_api = st.selectbox(
            label="Options",
            options=api_options,
        )

        api_to_demo_dict = {
            "Introduction": ST_INTRODUCTION_DEMOS,
            "Training Sets": ST_DATASETS_DEMOS,
            "Experiments": ST_EXPS_DEMOS,
            "Demos": ST_DEMO_DEMOS,
        }
        selected_demo_dict = api_to_demo_dict[selected_api]

        page_options = list(api_to_demo_dict.get(selected_api, {}).keys())

        selected_page = st.selectbox(
            label="Choose an example",
            options=page_options,
        )

        demo, url = selected_demo_dict[selected_page]

    if selected_api == "Introduction":
        st.title("Introduction")
    elif selected_api == "Training Sets":
        st.title("Training Sets")
    elif selected_api == "Experiments":
        st.title("Experiments")
    elif selected_api == "Demos":
        st.title("Demos")

    demo()

    st.markdown(f"{url}")


if __name__ == "__main__":
    st.set_page_config(
        page_title="Debiasing Diffusion Model", page_icon=":chart_with_upwards_trend:"
    )
    main()