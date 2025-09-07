import csv
from datetime import date, datetime, timedelta
import pandas as pd
import os
from colorama import init, Fore, Back, Style
from collections import Counter

# read data
# Hasan
def read_csv(path):
    """
    Read csv and return all data.
    """
    data= []
    # Read CV and save data in dictionary
    with open(path, mode= 'r', newline='') as file:
        content = csv.DictReader(file)
        data = list(content)
        return data


# function to search date
# Hasan
def search_date():
    while True:
        try:
            print(Fore.CYAN + "Please input the date in mm-dd-yyyy format: ", end=' ')
            new_date = input()
            
            if new_date == "exit":
                return new_date
            formatted_date = datetime.strptime(new_date, "%m-%d-%Y")
            inputdate =formatted_date.strftime("%m-%d-%Y")
            return inputdate
        except ValueError:
            print(Fore.RED + """Invalid input, please enter a date in mm-dd-yyyy format.
Try again or write exit""")

#add date
# Husain
def add_weather():
    """ Input all weather values"""
    columns= ["Date","Temp C","Humidity (%)", "Wind speed (km/h)", "Weather condition"]
    # if no file create a new one
    if not os.path.exists("Bahrain Weather.csv") or not os.path.getsize("Bahrain Weather.csv")>0:
        with open ("Bahrain Weather.csv", "w",newline="") as weather:
            Dictdata=csv.DictWriter(weather,fieldnames=columns)
            Dictdata.writeheader()
    
    # Add date
    while True:
        try:
            data = read_csv("Bahrain Weather.csv")
            print(Fore.CYAN + "Please input the date in mm-dd-yyyy format:" + Style.RESET_ALL)
            new_date = input()
            if new_date.lower() == "exit":
                return "Exited"
            formatted_date= datetime.strptime(new_date, "%m-%d-%Y")
            inputdate=formatted_date.strftime("%m-%d-%Y")
            if any(x['Date'] == inputdate for x in data):
                raise Exception
        except ValueError:
            print(Fore.RED + "Invalid date. Use MM-DD-YYYY (e.g., 07-20-2024) and try again.")   
        except:
            print(Fore.RED + "This record already exists in the system.") 
        break
    # Add temperature
    while True:
        try:
            print(Fore.CYAN + "Please input the temperature in Celsius"+ Style.RESET_ALL)
            input_temp= input()
            if input_temp.lower() == "exit":
                return "Exited"
            input_temp = float(input_temp)
            if input_temp >65 or input_temp<-100:
                print(Fore.RED + "Please enter a valid number\n")
            else:
                break
        except ValueError:
            print(Fore.RED + "Incorrect value, please enter a number\n")
            
    # Add weather condition        
    while True:
        try:
            print(Fore.CYAN + "Please input the weather condition: \n 1 for sunny \n 2 for cloudy \n 3 for dusty \n 4 for snowy \n 5 for rainy\n" 
                  + Style.RESET_ALL)
            int_weather= input()
            if int_weather.lower() == "exit":
                return "Exited"
            int_weather= int(int_weather)    
            if int_weather>5 or int_weather<1:
                #print("Please enter a valid value from 1 to 5")
                raise ValueError
            elif int_weather ==1:
                input_weather= "Sunny"
                break
            elif int_weather==2:
                input_weather= "Cloudy"
                break
            elif int_weather==3:
                input_weather="Dusty"
                break
            elif int_weather==4:
                input_weather= "Snowy"
                break
            elif int_weather==5:
                input_weather= "Rainy"
                break
            else:
                print(Fore.RED + "Incorrect value, please try again\n")
        except ValueError:
            print(Fore.RED + "Incorrect value, please try again\n")
            
    # Add wind speed        
    while True:
        try:
            print(Fore.CYAN + "Please input the wind speed in km/h (kph)\n"+ Style.RESET_ALL)
            input_wind= input()
            if input_wind.lower() == "exit":
                return "Exited"
            input_wind = float(input_wind)
            if input_wind >500 or input_wind<0:
                print(Fore.RED + "Please enter a valid number\n")
            else:
                break
        except ValueError:
            print(Fore.RED + "Incorrect value, please try again\n")

    # Add humidity 
    while True:
        try:
            print(Fore.CYAN + "Please input the humidity in percentage (0-100)\n"+ Style.RESET_ALL)
            input_hum= input()
            if input_hum.lower() == "exit":
                return "Exited"
            input_hum = float(input_hum)
            if input_hum >100 or input_hum<0:
                print(Fore.RED + "Please enter a valid number\n")
            else:
                break
        except ValueError:
            print(Fore.RED + "Incorrect value, please try again\n")
            
    with open ("Bahrain Weather.csv","a", newline="") as weather:
        #columns= ["Date","Temp (C)","Weather condition", "Wind speed (km/h)", "Humidity (%)"]
        #"Temp": inputtemp,
        #"Weather": inputweather,
        #"Humidity": inputhumidity,
        #"Wind": inputwind
        Dictdata=csv.DictWriter(weather,fieldnames=columns)
        Dictdata.writerow({"Date":inputdate,"Temp C": input_temp,"Weather condition": input_weather, "Wind speed (km/h)": input_wind, "Humidity (%)": input_hum })
        print(Fore.BLUE +"Weather status has been added successfully."+ Style.RESET_ALL)
        
# Show record breaking.
# Nadheer
def record_breaking():
    try:
        data = read_csv("Bahrain Weather.csv") #Leave it like this we want to show the error
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error

    #We need to call all the temrature and all the weather conditions
    x = Counter(round(float(x["Temp C"])) for x in data).most_common(1)
    y = Counter(x["Weather condition"] for x in data).most_common(1)
    result = f'{Fore.YELLOW}The breaking temprature record is: {x[0][0]} for {x[0][1]} days, and the breaking weather condition is: {y[0][0]} for {y[0][1]} days'
    return result

# Weather Statistics
# Nadheer
def stat():
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
    
    while True:
        try:
            print(Fore.CYAN + "Enter Start Date:"+ Style.RESET_ALL)
            start = search_date()
            if str(start.lower()) == "exit":
                return "Exited"
            print(Fore.CYAN + "Enter End Date:"+ Style.RESET_ALL)
            end = search_date()
            if str(end.lower()) == "exit":
                return "Exited"            
            start = datetime.strptime(start, "%m-%d-%Y")
            end = datetime.strptime(end, "%m-%d-%Y")
            
            if start > end:
                raise ValueError("The end date can not be before the start date.\n")
            
            filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y') >= start and datetime.strptime(x['Date'], '%m-%d-%Y') <= end]
            
            if filtred_data == []:
                raise ValueError("The selected range is outside the available data limits.")
            break
        except ValueError as error:
            print(Fore.RED, error)
    
    min_temps = min(float(x["Temp C"]) for x in filtred_data)
    max_temps = max(float(x["Temp C"]) for x in filtred_data)
    avg_temps = round(sum(float(x["Temp C"]) for x in filtred_data)/len(filtred_data),2)

    
    result = record_breaking()

    print(Fore.YELLOW,f'The maximum temprature for the whole period is {max_temps}°C')
    print(Fore.YELLOW,f'The minimum temprature for the whole period is {min_temps}°C')
    print(Fore.YELLOW,f'The average temprature for the whole period is {avg_temps}°C')
    print("--------------------------------------------------------------------------------------------------")
    print("The trend of temprature in the selected range")
    for i in range(len(filtred_data)):
        day = filtred_data[i]['Date'] #get the date 
        temp = int(round(float(filtred_data[i]['Temp C']),0)) #get the temp and make it int
        print(Fore.RESET + f"{day}: " +(
            (Fore.BLUE) if temp <= 15 else
            (Fore.LIGHTCYAN_EX) if temp <= 25 else
            (Fore.LIGHTYELLOW_EX) if temp <= 35 else
            (Fore.YELLOW) if temp <= 45 else
            (Fore.RED))
            + f"{'█' * temp} " + Fore.RESET
            + f"{temp}°C") #Display a text based graph.
    print("--------------------------------------------------------------------------------------------------")
    print(result)

#Filter by date.
# Hasan
def search_by_date():
    """
    Search data by date
    date = the date you want to search for in the following format: "MM-DD-YYYY"
    """
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
        
    while True:
        try:
            date = search_date()
            filtred_data = [x for x in data if x['Date'] == date]
            
            if date == "exit":
                break

            if filtred_data == []:
                raise ValueError("""Incorrect input, the data does not include this date.
Try again or write exit""")
                
            filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))
            return print(filtred_data)
            
        except ValueError as error:
            print(Fore.RED, error)

#Filter by month.
# Hasan
def search_by_month():
    """
    Search data by month, enter the month number
    """
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
        
    while True:
        try:
            print(Fore.CYAN + "Enter the month you want to search for: ")

            month = input()

            if month == "exit":
                return "Exited"

            if not month.isdigit():
                raise ValueError("Invalid input, text is not allowed. Please enter a valid month number between 1 and 12.\n")
                
            month = int(month)
            
            if month < 1 or month >12:
                raise ValueError("Incorrect input, enter a correct month number between 1 and 12.\n")

            filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y').month == month]
            
            if filtred_data == []:
                raise ValueError("""The data does not include this month.
Type 'help' to see available seasons or 'exit' to end this task.""")
            
            
            year = list(set([datetime.strptime(x['Date'], '%m-%d-%Y').year for x in filtred_data ]))

            if len(year) > 1:
                while True:
                    try:
                        print(Fore.BLUE + "Choose one of these year " + str(year) +":")
                        y = int(input())
                        if y not in year:
                             raise ValueError(Fore.RED + "Invalid input. Please enter a valid year from " + str(year))
                        filtred_data = [x for x in filtred_data if datetime.strptime(x['Date'], '%m-%d-%Y').year == y]
                        filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))
                        return print(Fore.YELLOW + f"Weather data for {month}-{y}" + Fore.RESET), print(filtred_data) 
                    except ValueError as error:
                        print(Fore.RED, error)
            
            filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))
            return print(Fore.YELLOW + f"Weather data for {month}-{year[0]}" + Fore.RESET), print(filtred_data)
        except ValueError as error:
            print(Fore.RED, error)
            
#Filter by season.
# Hasan    
def search_by_season():
    """
    Search data by season
    """
    # Read the data
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
    
    #run the loop to filter the data by season
    while True:
        try:
            while True:
                print(Fore.CYAN + "Please enter the season to search by:")
                season = input().lower() #user input of the season
                if season == "summer":
                    filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y').month in (6,7,8,9)]
                    break
                elif season == "winter":
                    filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y').month in (12,1,2)]
                    break
                elif season == "spring":
                    filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y').month in (3,4,5)]
                    break
                elif season == "autumn":
                    filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y').month in (10,11)]
                    break
                elif season == "exit": #user exiting the loop
                    return "Exited"
                elif season == "help": #list all available seasons
                    print(Fore.YELLOW + "Summer, Winter, Spring, Autumn")
                else:
                    raise ValueError("Invalid input. Please enter a valid season. Type 'help' to see available seasons.") #a error if no correct season was entered

            if filtred_data == []:
                raise ValueError("""The data does not include this season. 
Type 'help' to see available seasons or 'exit' to end this task.""")
            
            filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))    
            return print(filtred_data)
        except ValueError as error:
            print(Fore.RED, error)

#Filter by weather condition.
# Hasan
def search_by_condition():
    """
    Disply the data based on weather condition.
    """
    # Read the data
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error

    #run the loop to filter the data by condition
    while True:
        try:
            print(Fore.CYAN + "Please enter the weather condition to search by:")
            condition = input().lower() #user input of the season
            if condition == "help": #list all available seasons
                conditions = list(set([x["Weather condition"]for x in data ]))
                print(Fore.YELLOW, conditions)
            
            elif condition == "exit": #user exiting the loop
                break
                
            elif condition not in ("sunny", "cloudy", "dusty", "snowy", "rainy"):                        
                raise ValueError("""Incorrect input, enter a correct weather condition.
Type 'help' to see available conditions or 'exit' to end this task.""") #an error if no correct season was entered
            
            filtred_data = [x for x in data if x["Weather condition"].lower() == condition]
            if filtred_data == []:
                raise ValueError("""The data does not include this weather condition. 
Type 'help' to see available conditions or 'exit' to end this task.""")
            
            min_date = min(datetime.strptime(x['Date'], '%m-%d-%Y') for x in filtred_data).strftime("%m-%d-%Y")
            max_date = max(datetime.strptime(x['Date'], '%m-%d-%Y') for x in filtred_data).strftime("%m-%d-%Y")
            min_temp = min(float(x["Temp C"]) for x in filtred_data)
            max_temp = max(float(x["Temp C"]) for x in filtred_data)
            avg_temp = round(sum(float(x["Temp C"]) for x in filtred_data)/len(filtred_data),2)
            label = f"""{Fore.YELLOW}Start Date:{Fore.RESET} {min_date}      {Fore.YELLOW}End Date:{Fore.RESET} {max_date}
{Fore.YELLOW}Minimum Temprature:{Fore.RESET} {min_temp}°C   {Fore.YELLOW}Maximum Temprature:{Fore.RESET} {max_temp}°C
{Fore.YELLOW}Average Temprature:{Fore.RESET} {avg_temp}°C"""
            filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))
            
            return print(label), print(filtred_data)
        except ValueError as error:
            print(Fore.RED, error)

#Filter by weather temperature.
# Hasan
def search_by_temp():
    """
    Disply the data based on temperature in Celsius.
    Note: this will disply all valuse by ±0.5.
    """
    # Read the data
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error

    #run the loop to filter the data by condition
    while True:
        try:
            print(Fore.CYAN + "Please enter the temperature in Celsius to search by:")
            try:
                temp = input() #user input of the season
                if temp == "exit": #user exiting the loop
                    break
                temp = int(temp)
            except ValueError:
                raise ValueError("Please enter a valid number\n")
            
                
            if temp >65 or temp<-100:
                raise ValueError("Please enter a valid temperature between -100°C and 65°C\n")
            
            filtred_data = [x for x in data if round(float(x["Temp C"]),0) == temp]
            
            
            if filtred_data == []:
                raise ValueError("""The data does not include this weather temperature.
Try again or write exit""")
            
            filtred_data = pd.DataFrame(filtred_data).to_markdown(colalign=('center','center','center','center','center','center'))    
            return print(filtred_data)
        except ValueError as error:
            print(Fore.RED, error)

# Compare this year with last year.
# Nadheer
def forcast():
    
    # Read the data
    try:
        data = read_csv("Bahrain Weather.csv")
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
        
    #After calling the last 7 days record
    days = (sorted([x['Date'] for x in data], key=lambda x: datetime.strptime(x, "%m-%d-%Y"), reverse= True))[:7]
    last_days = [datetime.strptime(x, "%m-%d-%Y") for x in days]
    filtred_data = [x for x in data if datetime.strptime(x['Date'], '%m-%d-%Y') in last_days]
    
    if len(last_days) < 3:
        return print('There is no enough data to forcast tomorrow\'s temprature. ')
    else:
        tomrw_temp = round(sum(float(x["Temp C"]) for x in filtred_data)/len(filtred_data),1)
        return print(f'{Fore.YELLOW}Tomorrow temprature is {tomrw_temp}°C') 

# View all data
# Hasan
def view_all():
    """
    Display all data
    """
    try:
        data = read_csv("Bahrain Weather.csv") #Leave it like this we want to show the error
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error
        
    min_date = min(datetime.strptime(x['Date'], '%m-%d-%Y') for x in data).strftime("%m-%d-%Y")
    max_date = max(datetime.strptime(x['Date'], '%m-%d-%Y') for x in data).strftime("%m-%d-%Y")
    min_temp = min(float(x["Temp C"]) for x in data)
    max_temp = max(float(x["Temp C"]) for x in data)
    avg_temp = round(sum(float(x["Temp C"]) for x in data)/len(data),2)
    label = f"""{Fore.YELLOW}Start Date:{Fore.RESET} {min_date}      {Fore.YELLOW}End Date:{Fore.RESET} {max_date}
{Fore.YELLOW}Minimum Temprature:{Fore.RESET} {min_temp}     {Fore.YELLOW}Maximum Temprature:{Fore.RESET} {max_temp}
{Fore.YELLOW}Average Temprature:{Fore.RESET} {avg_temp}"""
    #convert to table
    data = pd.DataFrame(data)
    if data.empty:
        print(Fore.RED + "The data is empty.")
    return print(label), print(data.to_markdown(colalign=('center','center','center','center','center','center')))

# Ali
def compare():
     #This function will compare the last years seasons data with the current year
    # Load rows from your CSV
    
    try:
        data = read_csv("Bahrain Weather.csv") #Leave it like this we want to show the error
    except FileNotFoundError:
        value = "End"
        error = f"{Fore.RED}System Issue: The file Bahrain Weather.csv does not exist. Please contact the backend developer for assistance."
        return value, error

    current_moment = datetime.now()
    current_year = current_moment.year
    last_year = current_year -1
    
    last =   {"winterT": [], "springT": [], "summerT": [], "autumnT": [],"winterH": [], "springH": [], "summerH": [], "autumnH": [],"winterW": [], "springW": [], "summerW": [], "autumnW": []}
    current = {"winterT": [], "springT": [], "summerT": [], "autumnT": [],"winterH": [], "springH": [], "summerH": [], "autumnH": [],"winterW": [], "springW": [], "summerW": [], "autumnW": []}
    Rain_days_current = 0
    Rain_days_last = 0
    #  Fill
    for r in data:
        dat = r.get("Date")
        temV = r.get("Temp C")
        Hum = r.get("Humidity (%)")
        WinS = r.get("Wind speed (km/h)")
        wCon = r.get("Weather condition")
        if not dat or temV is None:
            continue
        parts = parts = dat.split("/") if "/" in dat else dat.split("-")
        try:
            mm = int(parts[0])      # month
            yy = int(parts[2])      # year
            t = float(temV)         # temperature
            h = float(Hum)         #Humidity
            w = float(WinS)         #Speed
        except:
            continue
        if mm in (12, 1, 2):   s = "winter"
        elif mm in (3, 4, 5):  s = "spring"
        elif mm in (6, 7, 8, 9): s = "summer"
        else:                  s = "autumn"
        if yy == last_year:
            last[s + 'T'].append(t)
            last[s + 'H'].append(h)
            last[s + 'W'].append(w)
            if wCon=="Rainy":
                Rain_days_last+=1
        elif yy == current_year:
            current[s + 'T'].append(t)
            current[s + 'H'].append(h)
            current[s + 'W'].append(w)
            if wCon=="Rainy":
                Rain_days_current+=1
    # Small helper for average
    def avg(lst):
        return round(sum(lst) / len(lst), 2) if lst else None
    #  Print results per season (T, H, W)
    print(f"Comparing {current_year} (this year) vs {last_year} (last year)")
    def report(season, suffix, label, unit):
        last_list = last[season + suffix]
        curr_list = current[season + suffix]
        a = avg(last_list)   # last year average
        b = avg(curr_list)   # this year average
        if a is None or b is None or a == 0:
            print(f"{season.capitalize()} {label}: not enough data (last year rows n={len(last_list)}, this year rows={len(curr_list)}).")
        else:
            change = round(((b - a) / a) * 100, 1)
            sign = "+" if change > 0 else ""
            print(f"{season.capitalize()} {label}: last year avg={a}{unit}, this year avg={b}{unit}, change={sign}{change}%")
    for s in ("winter", "spring", "summer", "autumn"):
        report(s, "T", "Temp", "°C")
        report(s, "H", "Humidity", "%")
        report(s, "W", "Wind", " km/h")
        print()
    print(f"Total rainy days for last year {Rain_days_last} and for current year {Rain_days_current}")

# Hasan
def search():
    """ Search Data"""
    fun = f"""
{Fore.MAGENTA}#- Search Data -#
{Fore.BLUE}
1. Search observations by date
2. Search observations by temperature
3. Search observations by condition
4. Search observations by season
{Fore.LIGHTYELLOW_EX}
Please choose a function by entering it's number or 'exit' or 'help:{Fore.RESET}"""
    ask = f"""\n{Fore.LIGHTYELLOW_EX}Please choose a search function by entering it's number.
Type 'help' to see available options or 'exit' to end this part'.{Fore.RESET}"""
    print(fun)
    while True:
        try:
            choose = input().lower()
            if choose == "exit":
                return "Exited"
            if choose == "help":
                print(fun)
            elif int(choose) == 1:
                returned = search_by_date()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        return value, error                                   
                print(ask)
            elif int(choose) == 2:
                returned = search_by_temp()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        return value, error                   
                print(ask)
            elif int(choose) == 3:
                returned = search_by_condition()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        return value, error                   
                print(ask)
            elif int(choose) == 4:
                returned = search_by_season()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        return value, error                   
                print(ask)
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Enter correct number or type 'help' to see available options or 'exit' to end this part.")

#  function to display main funcions name.  
# Hasan
def functions():
    print(f"""
{Fore.MAGENTA}##-- Bahrain Weather Function --##
{Fore.BLUE}
1. Record a new weather observation.
2. View weather statistics.
3. Search Data.
4. Forecast for tomorrow’s weather.
5. View all observations.
6. Compare Current Year with Last Year.
{Fore.LIGHTYELLOW_EX}
Please choose a function by entering it's number or 'help' for more details:{Fore.RESET}""")

#  function to see all model details.
# Hasan            
def functions_help():
    print(f"""
{Fore.MAGENTA}##-- Bahrain Weather Function Details--##
{Fore.BLUE}
1. Record a new weather observation
    - Enter the date in MM-DD-YYYY format. (Example: 12-20-2023)
    - Enter the temperature in Celsius. (Example: 24.5)
    - Enter the weather condition. (Example: Sunny)
    - Enter the wind speed in km/h. (Example: 40)
2. View weather statistics
    - Enter a date range to receive the minimum, maximum, and average temperature.
    - View a graph displaying the temperature across the selected date range.
    - View record breaking info across the data.
3. Search Data.
    1. Search observations by date
        - Enter a specific date to see detailed information for that day in a table view.
    2. Search observations by temperature
        - Enter a temperature value (°C).
        - The system will display all records within ±0.5°C of the entered value.
    3. Search observations by condition
        - Enter a weather condition (e.g., Sunny, Rainy, Cloudy).
        - The system will display matching records along with statistics.
    4. Search observations by season
        - Enter a season (e.g., Summer, Winter).
        - The system will display matching records along with statistics.
4. Forecast for tomorrow’s weather.
    - The system will display a prediction for tomorrow’s temperature based on the previous 7 days of records.
5. View all observations
    - Display all recorded data along with relevant statistics.
6. Compare Current Year with Last Year.
{Fore.LIGHTYELLOW_EX}
Please choose a function by entering it's number or 'exit':{Fore.RESET}""")

    
# main function to run the model.
# Hasan
def run_Thunder():
    """Main application function."""
    print("Hello there welcome to Bahrain Weather by Thunder Team")
    print("This app helps you build and maintain bahrain weather data.")
    ask = f"""\n{Fore.LIGHTYELLOW_EX}Please choose a main function by entering it's number.
Type 'help' to see available options or 'exit' to end this part.{Fore.RESET}"""
    functions()
    while True:
        try:
            choose = input().lower()
            if choose == "exit":
                return 'Exited'
            elif choose == "help":
                functions_help()
            elif int(choose) == 1:
                add_weather()                
                print(ask)
            elif int(choose) == 2:
                returned = stat()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        print(error)
                        break 
                print(ask)
            elif int(choose) == 3:
                returned = search()
                if isinstance(returned, tuple):
                    value, error = search()
                    if value == "End":
                        print(error)
                        break                
                print(ask)
            elif int(choose) == 4:
                returned = forcast()
                if isinstance(returned, tuple):
                    value, error = view_all()
                    if value == "End":
                        print(error)
                        break                
                print(ask)
            elif int(choose) == 5:
                returned = view_all()
                if isinstance(returned, tuple):
                    value, error = view_all()
                    if value == "End":
                        print(error)
                        break
                print(ask)
            elif int(choose) == 6:
                returned = compare()
                if isinstance(returned, tuple):
                    value, error = compare()
                    if value == "End":
                        print(error)
                        break
                print(ask)
            else:
                raise ValueError
        except ValueError:
            print(Fore.RED + "Enter correct number or type 'help' to see available options or 'exit' to close.")