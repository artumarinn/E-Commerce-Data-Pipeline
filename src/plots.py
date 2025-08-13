import matplotlib
import matplotlib.pyplot as plt

import plotly.express as px
import seaborn as sns

from pandas import DataFrame
import pandas as pd


def plot_revenue_by_month_year(df: DataFrame, year: int):
    """Plot revenue by month in a given year

    Args:
        df (DataFrame): Dataframe with revenue by month and year query result
        year (int): It could be 2016, 2017 or 2018
    """
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df[f"Year{year}"], marker="o", sort=False, ax=ax1)
    ax2 = ax1.twinx()

    sns.barplot(data=df, x="month", y=f"Year{year}", alpha=0.5, ax=ax2)
    ax1.set_title(f"Revenue by month in {year}")

    plt.show()


def plot_real_vs_predicted_delivered_time(df: DataFrame, year: int):
    """Plot real vs predicted delivered time by month in a given year

    Args:
        df (DataFrame): Dataframe with real vs predicted delivered time by month and
                        year query result
        year (int): It could be 2016, 2017 or 2018
    """
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)

    _, ax1 = plt.subplots(figsize=(12, 6))

    sns.lineplot(data=df[f"Year{year}_real_time"], marker="o", sort=False, ax=ax1)
    ax1.twinx()
    g = sns.lineplot(
        data=df[f"Year{year}_estimated_time"], marker="o", sort=False, ax=ax1
    )
    g.set_xticks(range(len(df)))
    g.set_xticklabels(df.month.values)
    g.set(xlabel="month", ylabel="Average days delivery time", title="some title")
    ax1.set_title(f"Average days delivery time by month in {year}")
    ax1.legend(["Real time", "Estimated time"])

    plt.show()


def plot_global_amount_order_status(df: DataFrame):
    """Plot global amount of order status

    Args:
        df (DataFrame): Dataframe with global amount of order status query result
    """
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in df["order_status"]]

    wedges, autotexts = ax.pie(df["Ammount"], textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Order Status",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Order Status Total")

    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    plt.show()


def plot_revenue_per_state(df: DataFrame):
    """Plot revenue per state

    Args:
        df (DataFrame): Dataframe with revenue per state query result
    """
    fig = px.treemap(
        df, path=["customer_state"], values="Revenue", width=800, height=400
    )
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def plot_top_10_least_revenue_categories(df: DataFrame):
    """Plot top 10 least revenue categories

    Args:
        df (DataFrame): Dataframe with top 10 least revenue categories query result
    """
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in df["Category"]]

    revenue = df["Revenue"]
    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Least Revenue Categories ammount")

    plt.show()


def plot_top_10_revenue_categories_ammount(df: DataFrame):
    """Plot top 10 revenue categories

    Args:
        df (DataFrame): Dataframe with top 10 revenue categories query result
    """
    # Plotting the top 10 revenue categories ammount
    _, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    elements = [x.split()[-1] for x in df["Category"]]

    revenue = df["Revenue"]
    wedges, autotexts = ax.pie(revenue, textprops=dict(color="w"))

    ax.legend(
        wedges,
        elements,
        title="Top 10 Revenue Categories",
        loc="center left",
        bbox_to_anchor=(1, 0, 0.5, 1),
    )

    plt.setp(autotexts, size=8, weight="bold")
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    p = plt.gcf()
    p.gca().add_artist(my_circle)

    ax.set_title("Top 10 Revenue Categories ammount")

    plt.show()


def plot_top_10_revenue_categories(df: DataFrame):
    """Plot top 10 revenue categories

    Args:
        df (DataFrame): Dataframe with top 10 revenue categories query result
    """
    fig = px.treemap(df, path=["Category"], values="Num_order", width=800, height=400)
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.show()


def plot_freight_value_weight_relationship(df: DataFrame):
    """Plot freight value weight relationship

    Args:
        df (DataFrame): Dataframe with freight value weight relationship query result
    """
    # TODO: plot freight value weight relationship using seaborn scatterplot.
    # Your x-axis should be weight and, y-axis freight value.
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    plt.figure(figsize=(12, 8))
    
    # Create scatterplot with weight on x-axis and freight value on y-axis
    sns.scatterplot(data=df, x='product_weight_g', y='freight_value', 
                    alpha=0.6, s=30, color='steelblue')
    
    # Add trend line
    sns.regplot(data=df, x='product_weight_g', y='freight_value', 
                scatter=False, color='red', line_kws={'linewidth': 2})
    
    plt.title('Freight Value vs Product Weight Relationship', fontsize=16, fontweight='bold')
    plt.xlabel('Product Weight (grams)', fontsize=12)
    plt.ylabel('Freight Value (BRL)', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    correlation = df['product_weight_g'].corr(df['freight_value'])
    plt.text(0.05, 0.95, f'Correlation: {correlation:.3f}', 
             transform=plt.gca().transAxes, fontsize=12, 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    # Set reasonable axis limits
    plt.xlim(0, df['product_weight_g'].quantile(0.95))
    plt.ylim(0, df['freight_value'].quantile(0.95))
    
    plt.tight_layout()
    plt.show()


def plot_delivery_date_difference(df: DataFrame):
    """Plot delivery date difference

    Args:
        df (DataFrame): Dataframe with delivery date difference query result
    """
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    plt.figure(figsize=(12, 8))
    
    sns.barplot(data=df, x="Delivery_Difference", y="State")
    plt.title("Difference Between Delivery Estimate Date and Delivery Date", fontsize=14, fontweight='bold')
    plt.xlabel("Delivery Difference (days)", fontsize=12)
    plt.ylabel("State", fontsize=12)
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


def plot_order_amount_per_day_with_holidays(df: DataFrame):
    """Plot order amount per day with holidays

    Args:
        df (DataFrame): Dataframe with order amount per day with holidays query result
    """
    # TODO: plot order amount per day with holidays using matplotlib.
    # Mark holidays with vertical lines.
    # Hint: use plt.axvline.
    
    matplotlib.rc_file_defaults()
    sns.set_style(style=None, rc=None)
    
    plt.figure(figsize=(15, 8))
    
    # Convert date column to datetime if it's not already
    df_copy = df.copy()
    df_copy['date'] = pd.to_datetime(df_copy['date'])
    
    # Sort by date
    df_copy = df_copy.sort_values('date')
    
    # Create the main plot
    plt.plot(df_copy['date'], df_copy['order_count'], 
             marker='o', linewidth=1.5, markersize=4, 
             color='steelblue', label='Orders per Day', alpha=0.8)
    
    # Mark holidays with vertical lines
    holiday_dates = df_copy[df_copy['holiday'] == True]['date']
    for holiday_date in holiday_dates:
        plt.axvline(x=holiday_date, color='red', linestyle='--', 
                   alpha=0.8, linewidth=1.5, label='Holiday' if holiday_date == holiday_dates.iloc[0] else "")
    
    # Customize the plot
    plt.title('Orders per Day in 2017 with Holiday Markers', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Orders', fontsize=12)
    plt.grid(True, alpha=0.2)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add legend
    plt.legend()
    
    # Add annotations for some holidays (limit to avoid clutter)
    for holiday_date in holiday_dates[:3]:  # Annotate first 3 holidays
        order_count = df_copy[df_copy['date'] == holiday_date]['order_count'].iloc[0]
        plt.annotate('Holiday', 
                     xy=(holiday_date, order_count),
                     xytext=(10, 10), textcoords='offset points',
                     bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7),
                     arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=0"),
                     fontsize=10)
    
    # Set y-axis to start from 0
    plt.ylim(bottom=0)
    
    plt.tight_layout()
    plt.show()
