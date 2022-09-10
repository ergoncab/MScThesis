# Get if a certain day was holiday or not, source: https://github.com/nicholasjhana/short-term-energy-demand-forecasting/blob/master/data_creation_day_types.ipynb

def get_holidays(start, stop, country='ES', frequency='H'):
    """
    Takes in a start and stop date and a country.
    
    Produces a dataframe with a daily date time index and columns:
    day_of_week - numerical day of the week identifier 0 for monday
    holiday_bool - boolean true or false for holiday
    holiday_name - name of the holiday if holiday_bool is true
    
    Returns a dataframe
    """
    import pandas as pd
    import holidays
    
    #generate the range of daily dates
    dates = pd.date_range(start=start, end=stop, freq=frequency)
    
    #create the holiday object
    country_holidays = holidays.CountryHoliday(country)

    #create a list for the holiday bool and name
    holiday_list = []
    
    #loop through the dates
    for date in dates:
        #true if holiday in object, false otherwise
        holiday_bool = date in country_holidays
        #holiday_names = country_holidays.get(date)
        
        holiday_list.append([holiday_bool])#, holiday_names])
        
    #create return dataframe
    holidays_data = pd.DataFrame(holiday_list, index=dates, columns=['Holiday'])#, 'holiday_name'])
                  
    return holidays_data