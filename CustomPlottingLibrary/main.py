import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

"""
CustomCandlePlot(rows, columns, figsize=(12, 6), contrained_layout=True)

### Initilization Parameters:
+-------------------+----------------------------------------+----------+---------+
| Parameter         | Type: Description                      | Required | Default |
+-------------------+----------------------------------------+----------+---------+
| rows              | int: number of rows for entire plot    | Yes      |         |
| columns           | int: number of columns for entire plot | Yes      |         |
| figsize           | tuple: (width, height) for entire plot | No       | (12, 6) |
| contrained_layout | bool: True for tight layout            | No       | True    |
+-------------------+----------------------------------------+----------+---------+

Example:
[ ]
rows=1 columns=1

[ ] [ ]
row=1 columns=2

[ ] [ ]
[ ] [ ]
row=2 columns=2

### Custom Methods

CustomCandlePlot.plot(self, data, ax=0, chart_type="ohlc", signal=False, custom_column=None, custom_colors=["black"], legend=False, grid=False, grid_settings=None, title_labels=None):

+---------------+----------------------------------------------------+----------+-----------+
| Parameter     | Type: Description                                  | Required | Default   |
+---------------+----------------------------------------------------+----------+-----------+
| data          | pandas.DataFrame: data frame with columns          | Yes      |           |
|               | float: number for single "vline" and "hline" plots |          |           |
| ax            | int: index of axes to plot on                      | No       | 0         |
| chart_type    | string: chart type, see example below              | No       | "ohlc"    |
| signal        | bool: True to plot entry/exit levels               | No       | False     |
| custom_column | list: column names to plot values                  | No       | None      |
| custom_colors | list: color names for plots                        | No       | ["black"] |
| legend        | bool: True to plot legend                          | No       | False     |
| grid          | bool: True to plot grid lines                      | No       | False     |
| grid_settings | dict: settings to modify grid lines                | No       | None      |
| title_labels  | dict: settings to modify axis labels and title     | No       | None      |
+---------------+----------------------------------------------------+----------+-----------+

Example:
# chart_type="ohlc"
- required columns in data
-- Open, High, Low, Close

- default color
-- up candle green
-- down candle red

- optional columns in data
signal=True
-- Signal -> Draws a up marker for values > 0 / Draws a down marker for values < 0
-- Price -> Draws up / down market at specific prices

- signal default color
-- up marker dodgerblue
-- down market salmon

# chart_type="volume"
-- Volume -> Draws a bar chart with volume for values > 0 or < 0

- default color
-- up volume blue
-- down volume red

# chart_type="line"
-> Draws a line chart with veritcle axis values specified
- use custom_column with custom_colors
- default column
-- Close -> if custom_column not specified
- uses custom_colors

# chart_type="bar"
-> Draws a bar chart with heights specified
- use custom_column with custom_colors
- default column
-- Close -> if custom_column not specified
- uses custom_colors

# chart_type="hline"
-> Draws a horizontal line at data
- data should be a number like int / float
- uses custom_colors[0]

# chart_type="vline"
-> Draws a verticle line at data
- data should be a number like int / float
- uses custom_colors[0]

# Chart Options

- legend=True
-> Draws legend on chart with labels
-- supports chart_type=["line", "bar"]

- grid=True
-> Draws a grid for major ticks

- grid_setting=None or dict
-> Customize grid when grid=True
- default / supported settings:
{"which": "major",
 "linestyle": "--",
 "linewidth": 0.5}

- title_labels=None or dict
-> Draws Labels 
- default / supported settings:
{"xlabel": string,
 "ylabel": string,
 "title": string}
 
"""

class CustomCandlePlot:
    custom_color_index = 0
    
    def __init__(self, rows, columns, figsize=(12, 6), constrained_layout=True):
        self.rows = rows
        self.columns = columns
        self.figsize = figsize
        self.constrained_layout = constrained_layout
        if self.rows * self.columns == 1:
            self.fig, self.ax = plt.subplots(figsize=self.figsize, constrained_layout=self.constrained_layout)
        else:
            self.fig, self.ax = plt.subplots(self.rows, self.columns, figsize=self.figsize, constrained_layout=self.constrained_layout)

    def iterate_custom_color_index(self, colors=["black"]):
        max_index = len(colors) - 1
        current_index = self.custom_color_index
        next_index = self.custom_color_index + 1
        self.custom_color_index = next_index
        if next_index > max_index:
            self.custom_color_index = 0
        return current_index
    
    def rename_columns(self, data):
        col_names = {"Open": ["OPEN", "O"],
                     "High": ["HIGH", "H"],
                     "Low": ["LOW", "L"],
                     "Close": ["CLOSE", "C"],
                     "Signal": ["SIGNAL", "S"],
                     "Price": ["Price", "Trade Price", "P"],
                     "Volume": ["Volume", "V"]}
        for col in col_names.keys():
            for name in data.columns:
                if name.upper() in col_names[col]:
                    data.rename(columns={name: col}, inplace=True)
                    break
        
    def plot(self, data, ax=0, chart_type="ohlc", signal=False, custom_column=None, custom_colors=["black"], legend=False, grid=False, grid_settings=None, title_labels=None):
        if type(data) == pd.DataFrame:
            self.rename_columns(data)
        
        if self.rows * self.columns == 1:
            if chart_type == "ohlc":
                for i, row in data.iterrows():
                    self.ax.vlines(x=i, ymin=row["Low"], ymax=row["High"], color="black", linewidth=1)
                    if row["Close"] > row["Open"]:
                        self.ax.vlines(x=i, ymin=row["Open"], ymax=row["Close"], color="green", linewidth=3)
                    elif row["Close"] < row["Open"]:
                        self.ax.vlines(x=i, ymin=row["Close"], ymax=row["Open"], color="red", linewidth=3)
                    elif row["Close"] == row["Open"]:
                        self.ax.vlines(x=i, ymin=row["Open"], ymax=row["Close"]+0.000001, color="black", linewidth=6)
            elif chart_type == "volume":
                self.ax.bar(data.index, data["Volume"], color=np.where(data["Volume"] > 0, "blue", np.where(data["Volume"] < 0, "red", "black")), alpha=0.5)
                self.ax.axhline(y=0, color="black")
            elif chart_type == "line":
                if custom_column:
                    for col in custom_column:
                        self.ax.plot(data[col], color=custom_colors[self.iterate_custom_color_index(custom_colors)], label=col)
                else:
                    self.ax.plot(data["Close"], color=custom_colors[0], label="Close")
            elif chart_type == "bar":
                if custom_column:
                    for col in custom_column:
                        self.ax.bar(data.index, data[col], color=custom_colors[self.iterate_custom_color_index(custom_colors)], label=col)
                else:
                    self.ax.bar(data.index, data["Close"], color=custom_colors[0], label="Close")
            elif chart_type == "hline":
                self.ax.axhline(y=data, color=custom_colors[0])
            elif chart_type == "vline":
                self.ax.axvline(x=data, color=custom_colors[0])
            if signal and "Signal" in data.columns:
                for i, row in data.iterrows():
                    if row["Signal"] > 0:
                        self.ax.plot(i, row["Price"], "^", color="dodgerblue", alpha=0.5)
                    elif row["Signal"] < 0:
                        self.ax.plot(i, row["Price"], "v", color="salmon", alpha=0.5)
            if legend:
                self.ax.legend()
            if grid:
                if grid_settings:
                    grid_settings["which"] = grid_settings.get("which", "major")
                    grid_settings["linestyle"] = grid_settings.get("linestyle", "--")
                    grid_settings["linewidth"] = grid_settings.get("linewidth", 0.5)
                    self.ax.grid(which=grid_settings["which"], linestyle=grid_settings["linestyle"], linewidth=grid_settings["linewidth"])
                else:
                    self.ax.grid()
            if title_labels:
                if title_labels.get("xlabel"):
                    self.ax.set_xlabel(title_labels.get("xlabel"))
                if title_labels.get("ylabel"):
                    self.ax.set_ylabel(title_labels.get("ylabel"))
                if title_labels.get("title"):
                    self.ax.set_title(title_labels.get("title"))
        else:
            if chart_type == "ohlc":
                for i, row in data.iterrows():
                    self.ax[ax].vlines(x=i, ymin=data["Low"].iloc[i], ymax=data["High"].iloc[i], color="black", linewidth=1)
                    if data["Close"].iloc[i] > data["Open"].iloc[i]:
                        self.ax[ax].vlines(x=i, ymin=data["Open"].iloc[i], ymax=data["Close"].iloc[i], color="green", linewidth=3)
                    elif data["Close"].iloc[i] < data["Open"].iloc[i]:
                        self.ax[ax].vlines(x=i, ymin=data["Close"].iloc[i], ymax=data["Open"].iloc[i], color="red", linewidth=3)
                    elif data["Close"].iloc[i] == data["Open"].iloc[i]:
                        self.ax[ax].vlines(x=i, ymin=data["Open"].iloc[i], ymax=data["Close"].iloc[i]+0.000001, color="black", linewidth=6)
            elif chart_type == "volume":
                self.ax[ax].bar(data.index, data["Volume"], color=np.where(data["Volume"] > 0, "blue", np.where(data["Volume"] < 0, "red", "black")), alpha=0.5)
                self.ax[ax].axhline(y=0, color="black")
            elif chart_type == "line":
                if custom_column:
                    for col in custom_column:
                        self.ax[ax].plot(data[col], color=custom_colors[self.iterate_custom_color_index(custom_colors)], label=col)
                else:
                    self.ax[ax].plot(data["Close"], color=custom_colors[0], label="Close")
            elif chart_type == "bar":
                if custom_column:
                    for col in custom_column:
                        self.ax[ax].bar(data.index, data[col], color=custom_colors[self.iterate_custom_color_index(custom_colors)], label=col)
                else:
                    self.ax[ax].bar(data.index, data["Close"], color=custom_colors[0], label="Close")
            elif chart_type == "hline":
                self.ax[ax].axhline(y=data, color=custom_colors[0])
            elif chart_type == "vline":
                self.ax[ax].axvline(x=data, color=custom_colors[0])
            if signal and "Signal" in data.columns:
                for i, row in data.iterrows():
                    if row["Signal"] > 0:
                        self.ax[ax].plot(i, row["Price"], "^", color="dodgerblue", alpha=0.5)
                    elif row["Signal"] < 0:
                        self.ax[ax].plot(i, row["Price"], "v", color="salmon", alpha=0.5)
            if legend:
                self.ax[ax].legend()
            if grid:
                if grid_settings:
                    grid_settings["which"] = grid_settings.get("which", "major")
                    grid_settings["linestyle"] = grid_settings.get("linestyle", "--")
                    grid_settings["linewidth"] = grid_settings.get("linewidth", 0.5)
                self.ax[ax].grid(which=grid_settings["which"], linestyle=grid_settings["linestyle"], linewidth=grid_settings["linewidth"])
            if title_labels:
                if title_labels.get("xlabel"):
                    self.ax[ax].set_xlabel(title_labels.get("xlabel"))
                if title_labels.get("ylabel"):
                    self.ax[ax].set_ylabel(title_labels.get("ylabel"))
                if title_labels.get("title"):
                    self.ax[ax].set_title(title_labels.get("title"))

 
