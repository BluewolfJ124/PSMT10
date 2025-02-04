import random, os
import pandas
import matplotlib.pyplot as plt
import numpy as np
os.system('cls') # Clear the terminal 
largest_legs, largest_arms = 0, 0
index_list = []
print("Welcome to Jamie's amazing data sample sampler")
while True:
    sample_size = input("Please input the size of the random sample: ") # Get an string input
    if sample_size.isalnum() == True: # Check if the input is a number
        sample_size = int(sample_size) # Set the sample size to an integer
        if sample_size <= 500: # If the sample size is less than 500
            break # Continue
    print("Uh oh, you did not input a valid integer, please try again") 
df = pandas.read_excel('2024 Student Data.xlsx',skiprows=[0]) # Load the excel data into the program, skipping the first row

dic = df.to_dict('records') # Load the pandas data into a dictionary
for i in dic: 
    i["Shoulder to wrist (cm)"] = int(i["Shoulder to wrist (cm)"]) # Filter out some random spaces in the data
    if i["Shoulder to wrist (cm)"] > largest_arms:
        largest_arms = i["Shoulder to wrist (cm)"]
    i["Waist to floor (cm)"] = int(i["Waist to floor (cm)"]) # Filter out some random spaces in the data
    if i["Waist to floor (cm)"] > largest_legs:
        largest_legs = i["Waist to floor (cm)"]
x,y = [],[]
index_list = random.sample(range(0,500), k=sample_size) #
index_list.sort()
sample_list = []
for i in index_list:
    item = dic[i]
    item.update({"Index": i+3})
    x.append(item["Shoulder to wrist (cm)"])
    y.append(item["Waist to floor (cm)"])
    sample_list.append(item)

df = pandas.DataFrame(sample_list)
print(df)
response = input("Would you like to export the data to excel? Y/N ")
if response == "Y" or response == "y":
    df.to_excel('output.xlsx', sheet_name='sheet1', index=False)
    print(f"Results saved to: {os.path.abspath('output.xlsx')}")

plt.scatter(x, y)
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), 'r')
plt.xlim(40, 80)
plt.ylim(80, 120)
plt.xlabel("Shoulder to wrist (cm)")
plt.ylabel("Waist to floor (cm)")
plt.show()
print(f'largest arms: {largest_arms} largest legs: {largest_legs}')