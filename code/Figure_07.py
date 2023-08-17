# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: Level of Education vs. responses to "Have you ever used ChatGPT?"
# Type: Percent Stacked Bar Graph

from matplotlib import pyplot as plt    # for graph
import numpy as np                      # for np.array()
import pandas as pd                     # for importing google sheets and data manipulation

# Opening Google Sheets
gSheet_Url = "https://docs.google.com/spreadsheets/d/1guRRNQRalo12LvA9j50nzzUuswxRjOwQJA0L14R2-o4/edit?usp=sharing"
gSheet_ID = "1guRRNQRalo12LvA9j50nzzUuswxRjOwQJA0L14R2-o4"
gSheet_Name = "ChatGPT Study (Responses)"

url = 'https://docs.google.com/spreadsheets/d/{}/export?format=csv&id={}'.format(gSheet_ID, gSheet_ID)
df = pd.read_csv(url) # Creates a dataframe object using the survey results google sheets

# Initial Data
x_EducationLevels = ["Undergraduate", "Master's", "PhD"] # Education Levels
y1_No = np.array([0,0,0]) # Holds response "No", by education level
y2_Yes = np.array([0,0,0]) # Holds response "Yes", by education level
x_Respondents = [0,0,0] # Holds total number of respondents, by education level

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in the responses arrays depending on the response of the row, also populates x_Respondents
    if(row['Have you ever used ChatGPT?']=="No"): # Response "No"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y1_No[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y1_No[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y1_No[2] += 1
            x_Respondents[2] += 1
    elif(row['Have you ever used ChatGPT?']=="Yes"): # Response "Yes"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y2_Yes[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y2_Yes[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y2_Yes[2] += 1
            x_Respondents[2] += 1

# To convert responses into percentages, (100/total number of responses)*responses
y1_percentage = np.array([((100/x_Respondents[0])*y1_No[0]), ((100/x_Respondents[1])*y1_No[1]), ((100/x_Respondents[2])*y1_No[2])]) # Response "No", in percentage
y2_percentage = np.array([((100/x_Respondents[0])*y2_Yes[0]), ((100/x_Respondents[1])*y2_Yes[1]), ((100/x_Respondents[2])*y2_Yes[2])]) # Response "Yes", in percentage

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
plt.bar(x_EducationLevels, y1_percentage, color='tab:red') # Plotting "No"
plt.bar(x_EducationLevels, y2_percentage, bottom=y1_percentage, color='tab:blue') # Plotting "Yes"

# Formatting the graph
plt.xlabel("Level of Education") # X-Axis Label
plt.ylabel("Percentage of Responses") # Y-Axis Label
plt.ylim(0, 100) # Y-Axis Scale (Percentage)
plt.legend(["No", "Yes"], loc=(0.805,0.805)) # Legend, changed location for readability
plt.title("Level of Education vs. responses to\n\"Have you ever used ChatGPT?\"", fontsize=30, y=1.02) # Title, changed font size and location for readability

# Opening the graph in a pop-up window
plt.show()