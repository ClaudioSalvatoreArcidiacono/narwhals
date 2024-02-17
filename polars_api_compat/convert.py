from typing import Any

from polars_api_compat.spec import LazyFrame, Namespace


def translate(df: Any, version: str) -> tuple[LazyFrame, Namespace]:
    if hasattr(df, "__polars_api_compat__"):
        return df.__polars_api_compat__()
    try:
        import polars as pl
    except ModuleNotFoundError:
        pass
    else:
        if isinstance(df, pl.DataFrame):
            from polars_api_compat.polars import translate

            return translate(df)
    try:
        import pandas as pd
    except ModuleNotFoundError:
        pass
    else:
        if isinstance(df, pd.DataFrame):
            from polars_api_compat.pandas import translate

            return translate(df)
    raise TypeError(
        f"Could not translate DataFrame {type(df)}, please open a feature request."
    )
