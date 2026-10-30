import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"], df["CSIRO Adjusted Sea Level"]
    )

    years = pd.Series(range(1880, 2051))

    ax.plot(
        years, slope * years + intercept, color="red", label="Best fit line (1880-2014)"
    )

    recent_df = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, r_value, p_value, std_err = linregress(
        recent_df["Year"], recent_df["CSIRO Adjusted Sea Level"]
    )

    recent_years = pd.Series(range(2000, 2051))

    ax.plot(
        recent_years,
        slope_recent * recent_years + intercept_recent,
        color="green",
        label="Best fit line (2000-2050)",
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    ax.legend()

    fig.savefig("sea_level_plot.png")

    return ax
