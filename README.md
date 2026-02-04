# custom-plotting-library

Custom `matplotlib` charts for trading & financial related data

## Installation

Run the command:

```sh
pip install --upgrade --no-cache-dir git+https://github.com/ganjk/custom-plotting-library.git
```

## Usage

`CustomCandlePlot(rows, columns, figsize=(12, 6), contrained_layout=True)`

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
`rows=1 columns=1`

[ ] [ ]
`row=1 columns=2`

[ ] [ ]
[ ] [ ]
`row=2 columns=2`

### Custom Methods

`CustomCandlePlot.plot(self, data, ax=0, chart_type="ohlc", signal=False, custom_column=None, custom_colors=["black"], legend=False, grid=False, grid_settings=None, title_labels=None)`

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
`chart_type="ohlc"`
- required columns in data
-- Open, High, Low, Close

- default color
-- up candle green
-- down candle red

- optional columns in data
`signal=True`
-- Signal -> Draws a up marker for values > 0 / Draws a down marker for values < 0
-- Price -> Draws up / down market at specific prices

- signal default color
-- up marker dodgerblue
-- down market salmon

`chart_type="volume"`
-- Volume -> Draws a bar chart with volume for values > 0 or < 0

- default color
-- up volume blue
-- down volume red

`chart_type="line"`
-> Draws a line chart with veritcle axis values specified
- use custom_column with custom_colors
- default column
-- Close -> if custom_column not specified
- uses custom_colors

`chart_type="bar"`
-> Draws a bar chart with heights specified
- use custom_column with custom_colors
- default column
-- Close -> if custom_column not specified
- uses custom_colors

`chart_type="hline"`
-> Draws a horizontal line at data
- data should be a number like int / float
- uses custom_colors[0]

`chart_type="vline"`
-> Draws a verticle line at data
- data should be a number like int / float
- uses custom_colors[0]

### Chart Options

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
