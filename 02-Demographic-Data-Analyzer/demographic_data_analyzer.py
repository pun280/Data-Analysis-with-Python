import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    # 1. Count of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage of people with Bachelor's degree
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Advanced education
    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # 5. People without advanced education
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    # 6. Percentage of advanced education earners
    higher_education_rich = round(
        (higher_education["salary"] == ">50K").mean() * 100, 1
    )

    # 7. Percentage of non-advanced education earners
    lower_education_rich = round((lower_education["salary"] == ">50K").mean() * 100, 1)

    # 8. Minimum hours worked per week
    min_work_hours = df["hours-per-week"].min()

    # 9. Percentage of people working minimum hours
    num_min_workers = df[df["hours-per-week"] == min_work_hours]

    rich_percentage = round((num_min_workers["salary"] == ">50K").mean() * 100, 1)

    # 10. Country with highest percentage of rich people
    country_earning = df[df["salary"] == ">50K"]["native-country"].value_counts()

    country_population = df["native-country"].value_counts()

    country_percentage = (country_earning / country_population) * 100

    highest_earning_country = country_percentage.idxmax()

    highest_earning_country_percentage = round(country_percentage.max(), 1)

    # 11. Most popular occupation in India for people earning >50K
    top_IN_occupation = (
        df[(df["native-country"] == "India") & (df["salary"] == ">50K")]["occupation"]
        .value_counts()
        .idxmax()
    )

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelor's degree:", percentage_bachelors)
        print("Percentage with advanced education earning >50K:", higher_education_rich)
        print(
            "Percentage without advanced education earning >50K:", lower_education_rich
        )
        print("Minimum hours worked per week:", min_work_hours)
        print("Percentage of minimum-hour workers earning >50K:", rich_percentage)
        print("Country with highest percentage earning >50K:", highest_earning_country)
        print("Percentage:", highest_earning_country_percentage)
        print("Most popular occupation in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "rich_percentage": rich_percentage,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage": highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation,
    }
