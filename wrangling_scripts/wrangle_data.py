import pandas as pd
import plotly.graph_objs as go

###############################################################################
def return_figures_renova():
    """ Loads spectral irradiation and returns the plotly figures
    
    """
    # import global data
    df_bogota_agg=pd.read_csv('./data/data_webapp/bogota_agg.csv')
    
    ###import spectral data
    df_280_859=pd.read_csv('data/data_webapp/spectral_data_short.csv')
    wavelengths=df_280_859.columns[23:]
    wavelengths_nm=[float(text.split(' ')[0])*1000 for text in wavelengths]
    
    #####spectral data
    hours_to_plot=[7,12,17]
    month_text=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov', 'Dec']
    month_nr=[1,2,3,4,5,6,7,8,9,10,11,12]
    month_dict=dict(zip(month_nr, month_text))
    hours_nr=[i for i in range(24)]
    hours_text=[str(i)+'h' for i in hours_nr]
    hours_dict=dict(zip(hours_nr, hours_text))
    #######Graph_one
    
    graph_one=[]
    for hour in hours_to_plot:
        df= df_280_859[df_280_859.Month==1]
        df=df[df.Hour==hour]
        x_val = wavelengths_nm
        y_val =  df.iloc[:,23:].values.tolist()[0]
        graph_one.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = hours_dict.get(hour)
                        )
                )
          
    layout_one = dict(title = 'Enero 2018',
                xaxis = dict(title = 'Wavelength/nm',
                autotick=False, tick0=200, dtick=50),
                yaxis = dict(title = 'Irradiance in W/m2/um',range=(1, 1500)),
                )          
    #######Graph_two
    
    graph_two=[]
    for hour in hours_to_plot:
        df= df_280_859[df_280_859.Month==3]
        df=df[df.Hour==hour]
        x_val = wavelengths_nm
        y_val =  df.iloc[:,23:].values.tolist()[0]
        graph_two.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = hours_dict.get(hour)
                        )
                )
          
    layout_two = dict(title = 'Marzo 2018',
                xaxis = dict(title = 'Wavelength/nm',
                autotick=False, tick0=200, dtick=50),
                yaxis = dict(title = 'Irradiance in W/m2/um',range=(1, 1500)),
                ) 
    #######Graph_three
    
    graph_three=[]
    for hour in hours_to_plot:
        df= df_280_859[df_280_859.Month==7]
        df=df[df.Hour==hour]
        x_val = wavelengths_nm
        y_val =  df.iloc[:,23:].values.tolist()[0]
        graph_three.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = hours_dict.get(hour)
                        )
                )
          
    layout_three = dict(title = 'Julio 2018',
                xaxis = dict(title = 'Wavelength/nm',
                autotick=False, tick0=200, dtick=50),
                yaxis = dict(title = 'Irradiance in W/m2/um',range=(1, 1500)),
                ) 
    #######Graph_four
    
    graph_four=[]
    for hour in hours_to_plot:
        df= df_280_859[df_280_859.Month==9]
        df=df[df.Hour==hour]
        x_val = wavelengths_nm
        y_val =  df.iloc[:,23:].values.tolist()[0]
        graph_four.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name =hours_dict.get(hour)
                        )
                )
          
    layout_four = dict(title = 'Septiembre 2018',
                xaxis = dict(title = 'Wavelength/nm',autotick=False, tick0=200, dtick=50),
                yaxis = dict(title = 'Irradiance in W/m2/um',range=(1, 1500)),
                )                 

    
    ####graph five
    graph_five=[]
    for month in [1,3,5,7,9,11]:
        df= df_bogota_agg[df_bogota_agg.region_type=='city']
        df=df[df.Month==month]
        x_val = df.Hour.to_list()
        y_val =  df.GHI.to_list()
        graph_five.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = month_dict.get(month)
                        )
                )
          
    layout_five = dict(title = 'Irradiacion global horizontal',
                xaxis = dict(title = 'Hour',
                autotick=False, tick0=4, dtick=2),
                yaxis = dict(title = 'GHI W/m2',range=(1, 900)),
                )   

    ####graph six
    graph_six=[]
    for month in [1,3,5,7,9,11]:
        df= df_bogota_agg[df_bogota_agg.region_type=='city']
        df=df[df.Month==month]
        x_val = df.Hour.to_list()
        y_val =  df.Temperature.to_list()
        graph_six.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = month_dict.get(month)
                        )
                )
          
    layout_six = dict(title = 'Temperatura',
                xaxis = dict(title = 'Hour',
                autotick=False, tick0=4, dtick=2),
                yaxis = dict(title = 'T/ °C', range=(5, 25)),
                ) 
    
        ####graph seven
    graph_seven=[]
    for month in [1,3,5,7,9,11]:
        df= df_bogota_agg[df_bogota_agg.region_type=='city']
        df=df[df.Month==month]
        x_val = df.Hour.to_list()
        y_val = df['Relative Humidity'].to_list()
        graph_seven.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = month_dict.get(month)
                        )
                )
          
    layout_seven = dict(title = 'Humedad relativa',
                xaxis = dict(title = 'Hour',
                autotick=False, tick0=4, dtick=2),
                yaxis = dict(title = 'Rel. Hum/%'),
                ) 
    graph_eight=[]
    for month in [1,3,5,7,9,11]:
        df= df_bogota_agg[df_bogota_agg.region_type=='city']
        df=df[df.Month==month]
        x_val = df.Hour.to_list()
        y_val = df['Wind Speed'].to_list()
        graph_eight.append(
                go.Scatter(
                        x = x_val,
                        y = y_val,
                        mode = 'lines',
                        name = month_dict.get(month)
                        )
                )
          
    layout_eight = dict(title = 'Velocidad del viento',
                xaxis = dict(title = 'Hour',
                autotick=False, tick0=4, dtick=2),
                yaxis = dict(title = 'Wind Speed/ m/s'),
                ) 
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))
    figures.append(dict(data=graph_five, layout=layout_five))
    figures.append(dict(data=graph_six, layout=layout_six))
    figures.append(dict(data=graph_seven, layout=layout_seven))
    figures.append(dict(data=graph_eight, layout=layout_eight))
    return(figures)
