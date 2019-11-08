import pandas as pd
import matplotlib.pyplot as plt
with open("startup_funding.csv",encoding="utf-8") as file_obj:
    df_start = pd.read_csv(file_obj)
#File Closed and dataframe df_start saved all data

#Defining Possible Location where one can invest
PossibleLocation = ["Bangalore","Mumbai","Gurgaon","Noida","New Delhi"]

#Dropping NA/NAN values from City Location values and Investment Type
df_start.dropna(subset=['CityLocation','InvestmentType'],inplace=True)

#Correcting Names for cities
df_start['CityLocation'].replace("Delhi","New Delhi",inplace=True)
df_start['CityLocation'].replace("bangalore","Bangalore",inplace=True)
#Declaring empty ditionary
city_dictionary = {}

#Logic 
for cities in df_start['CityLocation']:
    cities = cities.split('/')
    for city in cities:
        city = city.strip()
        if city in PossibleLocation:
            if city in city_dictionary:
                city_dictionary[city] += 1
            else:
                city_dictionary[city] = 1

#Sorting  values as per there values
values = sorted(city_dictionary.items(), key=lambda x: x[1], reverse=True)

#Printing city name with highest number of Investors
numberList = []
cityList = []
for city,number in values:
    print(city,number)
    numberList.append(number)
    cityList.append(city)

plt.bar(*zip(*values),edgecolor='green',color='magenta')
plt.xlabel("Cities")
plt.xticks(rotation=30)
plt.ylabel("Number of Fundings")
plt.show()
explode = [0.1,0,0,0,0]
plt.pie(numberList,explode=explode,autopct="%.2f%%",counterclock=False,labels=cityList,startangle=90)
plt.show()
