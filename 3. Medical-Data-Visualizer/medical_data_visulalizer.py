import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


def draw_cat_plot():
    df = pd.read_csv("medical_examination.csv")
    df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

    # Normalize cholesterol and glucose
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)
    df["gluc"] = (df["gluc"] > 1).astype(int)

    # Create categorical DataFrame
    df_cat = pd.melt(
        df,
        id_vars=["cardio"],
        value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"],
    )

    # Group and count values
    df_cat = (
        df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    )

    # Create categorical plot
    cat_plot = sns.catplot(
        data=df_cat, x="variable", y="total", hue="value", col="cardio", kind="bar"
    )

    cat_plot.set_axis_labels("variable", "total")

    fig = cat_plot.fig

    fig.savefig("catplot.png")

    return fig


def draw_heat_map():
    df = pd.read_csv("medical_examination.csv")
    df["overweight"] = (df["weight"] / ((df["height"] / 100) ** 2) > 25).astype(int)

    # Normalize cholesterol and glucose
    df["cholesterol"] = (df["cholesterol"] > 1).astype(int)

    df["gluc"] = (df["gluc"] > 1).astype(int)

    # Cleaning incorrect data
    df_heat = df[
        (df["ap_lo"] <= df["ap_hi"])
        & (df["height"] >= df["height"].quantile(0.025))
        & (df["height"] <= df["height"].quantile(0.975))
        & (df["weight"] >= df["weight"].quantile(0.025))
        & (df["weight"] <= df["weight"].quantile(0.975))
    ]

    corr = df_heat.corr()

    mask = np.triu(np.ones_like(corr, dtype=bool))

    fig, ax = plt.subplots(figsize=(12, 12))

    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".1f",
        square=True,
        linewidths=0.5,
        cbar_kws={"shrink": 0.5},
        center=0,
        ax=ax,
    )

    fig.savefig("heatmap.png")

    return fig
