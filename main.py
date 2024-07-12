import random, os
import pandas
import matplotlib.pyplot as plt
os.system('cls')
largest_legs = 0
largest_arms = 0
x,y = [],[]
index = []
print("Welcome to Jamie's amazing data sample sampler")
while True:
    sample_size = input("Please input the size of the random sample: ")
    if sample_size.isalnum() == True:
        sample_size = int(sample_size)
        if sample_size <= 500:
            break
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
sample_list = random.sample(dic, k=sample_size)

for i in sample_list:
    index.append(dic.index(i))
    i.update({"Index": dic.index(i)})

df = pandas.DataFrame(sample_list)
print(df)
response = input("Would you like to export the data to excel? Y/N ")
if response == "Y" or response == "y":
    df.to_excel('output.xlsx', sheet_name='sheet1', index=False)
    print(f"Results saved to: {os.path.abspath('output.xlsx')}")
for i in sample_list:
    x.append(i["Shoulder to wrist (cm)"])
    y.append(i["Waist to floor (cm)"])
for i, txt in enumerate(index):
    plt.annotate(txt, (x[i], y[i]))
plt.scatter(x, y)
plt.xlim(0, 90)
plt.ylim(0, 140)
plt.xlabel("Shoulder to wrist (cm)")
plt.ylabel("Waist to floor (cm)")
plt.show()
print(f'largest arms: {largest_arms} largest legs: {largest_legs}')
