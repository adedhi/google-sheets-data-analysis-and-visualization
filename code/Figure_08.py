# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: Level of Education vs. responses to "Do you believe that ChatGPT enables plagiarism?"
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
y1_DoesntEnable = np.array([0,0,0]) # Holds response "Doesn't enable", by education level
y2_SomewhatEnables = np.array([0,0,0]) # Holds response "Somewhat enables", by education level
y3_ModeratelyEnables = np.array([0,0,0]) # Holds response "Moderately enables", by education level
y4_HighlyEnables = np.array([0,0,0]) # Holds response "Highly enables", by education level
x_Respondents = [0,0,0] # Holds total number of respondents, by education level

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in the responses arrays depending on the response of the row, also populates x_Respondents
    if(row['Do you believe that ChatGPT enables plagiarism?']=="Doesn't enable"): # Response "Doesn't enable"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y1_DoesntEnable[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y1_DoesntEnable[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y1_DoesntEnable[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that ChatGPT enables plagiarism?']=="Somewhat enables"): # Response "Somewhat enables"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y2_SomewhatEnables[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y2_SomewhatEnables[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y2_SomewhatEnables[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that ChatGPT enables plagiarism?']=="Moderately enables"): # Response "Moderately enables"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y3_ModeratelyEnables[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y3_ModeratelyEnables[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y3_ModeratelyEnables[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that ChatGPT enables plagiarism?']=="Highly enables"): # Response "Highly enables"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y4_HighlyEnables[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y4_HighlyEnables[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y4_HighlyEnables[2] += 1
            x_Respondents[2] += 1

# To convert responses into percentages, (100/total number of responses)*responses
y1_percentage = np.array([((100/x_Respondents[0])*y1_DoesntEnable[0]), ((100/x_Respondents[1])*y1_DoesntEnable[1]), ((100/x_Respondents[2])*y1_DoesntEnable[2])]) # Response "Doesn't enable", in percentage
y2_percentage = np.array([((100/x_Respondents[0])*y2_SomewhatEnables[0]), ((100/x_Respondents[1])*y2_SomewhatEnables[1]), ((100/x_Respondents[2])*y2_SomewhatEnables[2])]) # Response "Somewhat enables", in percentage
y3_percentage = np.array([((100/x_Respondents[0])*y3_ModeratelyEnables[0]), ((100/x_Respondents[1])*y3_ModeratelyEnables[1]), ((100/x_Respondents[2])*y3_ModeratelyEnables[2])]) # Response "Moderately enables", in percentage
y4_percentage = np.array([((100/x_Respondents[0])*y4_HighlyEnables[0]), ((100/x_Respondents[1])*y4_HighlyEnables[1]), ((100/x_Respondents[2])*y4_HighlyEnables[2])]) # Response "Highly enables", in percentage

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
plt.bar(x_EducationLevels, y1_percentage, color='tab:green') # Plotting "Doesn't enable"
plt.bar(x_EducationLevels, y2_percentage, bottom=y1_percentage, color='tab:orange') # Plotting "Somewhat enables"
plt.bar(x_EducationLevels, y3_percentage, bottom=y1_percentage+y2_percentage, color='tab:red') # Plotting "Moderately enables"
plt.bar(x_EducationLevels, y4_percentage, bottom=y1_percentage+y2_percentage+y3_percentage, color='tab:blue') # Plotting "Highly enables"

# Formatting the graph
plt.xlabel("Level of Education") # X-Axis Label
plt.ylabel("Percentage of Responses") # Y-Axis Label
plt.ylim(0, 100) # Y-Axis Scale (Percentage)
plt.legend(["Doesn't enable", "Somewhat enables", "Moderately enables", "Highly enables"], fontsize=22.5, loc=(0.71,0.01)) # Legend, changed font size and location for readability
plt.title("Level of Education vs. responses to\n\"Do you believe that ChatGPT enables plagiarism?\"", y=1.01) # Title, changed location for readability

# Opening the graph in a pop-up window
plt.show()