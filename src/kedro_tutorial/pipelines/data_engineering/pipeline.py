from kedro.pipeline import node, Pipeline
from kedro_tutorial.pipelines.data_engineering.nodes import (
    preprocess_companies,
    preprocess_shuttles,
)


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=preprocess_companies,
                inputs="companies",
                outputs="preprocessed_companies",
                name="preprocessing_companies",
            ),
            node(
                func=preprocess_shuttles,
                inputs="shuttles",
                outputs="preprocessed_shuttles",
                name="preprocessing_shuttles",
            ),
        ]
    )