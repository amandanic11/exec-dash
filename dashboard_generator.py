# dashboard_generator.py

import pandas as pd
import os
import plotly
import easygui
import datetime
import operator

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

#TODO Calculate total sales for each item
#total sales per item

product_sales = df.groupby("product")["sales price"].sum().rename("product sales").reset_index()
df_1 = df.merge(product_sales)
print(df_1.sort_values(by='product sales', ascending=False).groupby('product sales').head(1))





#total sales
total_sales = df["sales price"].sum()
# print(type(df))
# print(df.head())

#TODO Have the program output at least one chart or graph depicting relevant info

print("-----------------------")
print(f"MONTH: {month} {year}")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print(f"TOTAL MONTHLY SALES: {to_usd(total_sales)}")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
#print(f"1) : $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")