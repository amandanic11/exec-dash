# dashboard_generator.py

import pandas as pd
import os
import plotly
import plotly.express as px
import easygui
import datetime

data = os.path.join("data")
filepath = os.path.dirname(data)
def to_usd(my_price):
    return f"${my_price:,.2f}"

#User prompted to select file
filename = easygui.fileopenbox(msg="Please Select a File", default="data/*")
df = pd.read_csv(filename)

#month
m = df["date"].min()
monthinteger = int(m[5:7])
month = datetime.date(1900, monthinteger, 1).strftime('%B')

# year
y = df["date"].min()
yearinteger = int(y[0:4])
year = datetime.date(yearinteger, monthinteger, 1).strftime('%Y')

#total sales per item
product_sales = df.groupby("product")["sales price"].sum().rename("product sales").reset_index()
df_1 = df.merge(product_sales)
df_2 = df_1.sort_values(by='product sales', ascending=False).groupby('product sales').head(1)
df_4 = df_1.sort_values(by='product sales', ascending=True).groupby('product sales').head(1)
#top selling products
df_3 = df_2.head(3).reset_index()
t1_price = df_3["product sales"].max()
t1 = df_3["product"].max()

t2 = df_3.iloc[1, 2]
t2_price = df_3.iloc[1, 6]

t3 = df_3["product"].min()
t3_price = df_3["product sales"].min()

#total sales
total_sales = df["sales price"].sum()

#TODO Have the program output at least one chart or graph depicting relevant info

print("-----------------------")
print(f"MONTH: {month} {year}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(total_sales)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print(f"1) {t1}: {to_usd(t1_price)}")
print(f"2) {t2}: {to_usd(t2_price)}")
print(f"3) {t3}: {to_usd(t3_price)}")

print("-----------------------")
print("VISUALIZING THE DATA...")

df_chart = px.data.tips()
fig = px.bar(df_4, x="product sales", y="product", orientation='h',
            title=f'Top-selling Products: ({month} {year})')

# fig.update_layout(xaxis={'categoryorder':'total ascending'})
fig.show()

# import plotly.express as px
# df = px.data.tips()
# fig = px.bar(df, x="total_bill", y="sex", color='day', orientation='h',
#              hover_data=["tip", "size"],
#              height=400,
#              title='Restaurant bills')
# fig.show()