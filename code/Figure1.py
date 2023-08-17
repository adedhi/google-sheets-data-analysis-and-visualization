# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: "What is the highest level of education that you have obtained / are currently obtaining?"
# Type: Pie-Chart

from matplotlib import pyplot as plt    # for graph
import pandas as pd                     # for importing google sheets and data manipulation

# Opening Google Sheets
gSheet_Url = "https://docs.google.com/spreadsheets/d/1guRRNQRalo12LvA9j50nzzUuswxRjOwQJA0L14R2-o4/edit?usp=sharing"
gSheet_ID = "1guRRNQRalo12LvA9j50nzzUuswxRjOwQJA0L14R2-o4"
gSheet_Name = "ChatGPT Study (Responses)"

url = 'https://docs.google.com/spreadsheets/d/{}/export?format=csv&id={}'.format(gSheet_ID, gSheet_ID)
df = pd.read_csv(url) # Creates a dataframe object using the survey results google sheets

# Initial Data
labels = ["Other", "High School", "Undergraduate", "Master's", "PhD"] # Education Levels
responses = [0,0,0,0,0] # Holds the number of respondents per education level

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in 'responses' depending on the education level of the row
    if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Other"): # If education level is "Other"
        responses[0] += 1
    elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="High School"): # If education level is "High School"
        responses[1] += 1
    elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # If education level is "Undergraduate"
        responses[2] += 1
    elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # If education level is "Masters"
        responses[3] += 1
    elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # If education level is "PhD"
        responses[4] += 1

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
fig, ax = plt.subplots()
ax.pie(responses, labels=labels, autopct='%1.1f%%') # Plotting pie-chart

# Formatting the graph
plt.title("What is the highest level of education that\nyou have obtained / are currently obtaining?") # Title

# Opening the graph in a pop-up window
plt.show()