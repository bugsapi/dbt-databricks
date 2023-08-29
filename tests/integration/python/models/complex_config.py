import pandas as pd  # type: ignore


def model(dbt, spark):
    dbt.config(materialized="incremental")
    dbt.config(partition_by="date")
    dbt.config(unique_key="name")
    if dbt.is_incremental:
        data = [[2, "Teo"], [2, "Fang"], [3, "Elbert"]]
    else:
        data = [[2, "Teo"], [2, "Fang"], [1, "Elia"]]
    pdf = pd.DataFrame(data, columns=["date", "name"])

    df = spark.createDataFrame(pdf)

    return df
