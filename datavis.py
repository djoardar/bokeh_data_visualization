from bokeh.plotting import figure, show, output_file, save, ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
from bokeh.models.tools import HoverTool
import pandas as pd

# made up data - list of cars vs their sales
cars = ['desire', 'tiago', 'etios', 'celantro']
sales = [5, 7, 6, 8]

#take the data into a pandas dataframe and create columns
df = pd.DataFrame()
df['car'] = cars
df['sale'] = sales

# parse all data in source for referring in bokeh.plotting methods
source = ColumnDataSource(df)
car_list = source.data['car'].tolist()
sales_list = source.data['sale'].tolist()

print(car_list, "---", sales_list)

# output html file
output_file('carsales.html')

# create a plot object
plot = figure(
    title="car sales",
    y_axis_label='sales',
    x_range=car_list,  # for factoring categorical data (string) x_range is important.
    plot_height=300,
    plot_width=300,
    tools="pan,box_select,zoom_in,zoom_out,save,reset"

)
# for plotting a line:
# plot.line(cars, sales, legend_label="legend", line_width=2)
# for plotting a hbar:
# plot.hbar(y='car', right='sale', left=0, height=0.3, fill_alpha=0.5, color = 'orange')

plot.vbar(
    x='car',
    top='sale',
    bottom=0,
    fill_color=factor_cmap(
        'car',
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9,
    width=0.3,
    source=source,
    legend_label="legend"
)

# Add Legend
plot.legend.orientation = 'vertical'
plot.legend.location = 'top_right'
plot.legend.label_text_font_size = '10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
  <div>
    <h3>@car</h3>
    <div><strong>SALE: </strong>@sale</div>
  </div>
"""
plot.add_tools(hover)

show(plot)
save(plot)
