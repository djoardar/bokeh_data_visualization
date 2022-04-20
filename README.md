# bokeh_data_visualization
a simple hbar created with bokeh

takes 2 inputs : 
a. car models (categorical data) - python list
b. sales for each model - python list

creates a simple vertical bar plot with the same data.

steps : 
1. take data into a pandas dataframe and give name to columns.
2. Further parse using bokeh.plotting.Columndatasource for referring in the subsequenct bokeh functions
3. using bokeh.plotting.figure, create a plot object
4. on the plot object use the data from step 2 to create a simple VBAR plot
5. add tooltips on hovering over the bars.
6. show the plot
7. save the plot into output_file in HTML format
