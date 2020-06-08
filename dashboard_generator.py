# dashboard_generator.py

import pandas as pd
import os
import plotly
import easygui
import datetime

data = os.path.join("data")
filepath = os.path.dirname(data)

#User prompted to select file
filename = easygui.fileopenbox(msg="Please Select a File", default="data/*")

#TODO Calculate total sales for each item and total sales overall
#TODO Have the program output at least one chart or graph depicting relevant info

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")
print("  1) Button-Down Shirt: $6,960.35")
print("  2) Super Soft Hoodie: $1,875.00")
print("  3) etc.")

print("-----------------------")
print("VISUALIZING THE DATA...")