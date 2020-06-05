# three_charts.py

import plotly
import plotly.graph_objs as go

#CHART 1 (PIE)

pie_data = [
    {"company": "Company X", "market_share": 0.55},
    {"company": "Company Y", "market_share": 0.30},
    {"company": "Company Z", "market_share": 0.15}
]

print("----------------")
print("GENERATING PIE CHART...")

# TODO: create a pie chart based on the pie_data

labels = [pie_data["company"] for pie_data in pie_data]
values = [pie_data["market_share"] for pie_data in pie_data]

trace = go.Pie(labels=labels, values=values)

plotly.offline.plot([trace], filename="basic_pie_chart.html", auto_open=True)                            

# CHART 2 (LINE)

line_data = [
    {"date": "2019-01-01", "stock_price_usd": 100.00},
    {"date": "2019-01-02", "stock_price_usd": 101.01},
    {"date": "2019-01-03", "stock_price_usd": 120.20},
    {"date": "2019-01-04", "stock_price_usd": 107.07},
    {"date": "2019-01-05", "stock_price_usd": 142.42},
    {"date": "2019-01-06", "stock_price_usd": 135.35},
    {"date": "2019-01-07", "stock_price_usd": 160.60},
    {"date": "2019-01-08", "stock_price_usd": 162.62},
]

print("----------------")
print("GENERATING LINE GRAPH...")
# TODO: create a line graph based on the line_data

x = [line_data['date'] for line_data in line_data]
y = [line_data["stock_price_usd"] for line_data in line_data]

line = go.Scatter(x=x, y=y)

plotly.offline.plot([line], filename="basic_line_graph.html", auto_open=True)          

# CHART 3 (HORIZONTAL BAR)

bar_data = [
    {"genre": "Thriller", "viewers": 123456},
    {"genre": "Mystery", "viewers": 234567},
    {"genre": "Sci-Fi", "viewers": 987654},
    {"genre": "Fantasy", "viewers": 876543},
    {"genre": "Documentary", "viewers": 283105},
    {"genre": "Action", "viewers": 544099},
    {"genre": "Romantic Comedy", "viewers": 121212}
]

print("----------------")
print("GENERATING BAR CHART...")
# TODO: create a horizontal bar chart based on the bar_data

genre = [bar_data["genre"] for bar_data in bar_data]
viewers = [bar_data["viewers"] for bar_data in bar_data]

bar = go.Bar(x=genre, y=viewers)
plotly.offline.plot([bar], filename="basic_bar_chart.html", auto_open=True)  