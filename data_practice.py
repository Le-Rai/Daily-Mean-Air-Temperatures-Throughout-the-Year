import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv(r"C:\Users\admin\OneDrive\Desktop\Codes\practice_code\weather_data_o.csv", header=2) 
#changes file location where weather_data_o.csv is located 
#sets main header at the third row (python starts at zero index)

pd.set_option('display.width', 100)
pd.set_option('display.max_columns', 6)
#fixes data display

start_row = 0
end_row = 24
day = 0
temp_hold = []
temp_mean = []
days = []
months = ["Jan", "Feb", 'Mar', 'Apr', "May", 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


for i in range(1): #gets the daily mean temperature over the span of 24 hours and so on
    for index, row in df.iterrows():
        if start_row <= index <= end_row:
            temp_mean_hold = df.loc[start_row:end_row,("Temperature")].mean()
            temp_mean = np.append(temp_mean, temp_mean_hold)
            start_row += 24
            end_row +=24

for index1, row1 in enumerate(temp_mean): #creates an index for temp_mean
    days = np.append(days, day)
    day +=1

temp_mean = np.round(temp_mean, 1) #rounds off the mean to one decimal point

print("\n" + "Daily Mean Temperatures:")
print(temp_mean)

plt.title("Daily Mean Temperature")         
plt.xlabel("Day")         
plt.ylabel("Temperature (C)")  

plt.plot(days, temp_mean, linewidth=2)
plt.show()
