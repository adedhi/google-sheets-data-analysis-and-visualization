# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: Level of Education vs. responses to "Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?"
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
y1_StronglyDisagree = np.array([0,0,0]) # Holds response "Strongly disagree", by education level
y2_SlightlyDisagree = np.array([0,0,0]) # Holds response "Slightly disagree", by education level
y3_NeitherAgreeNorDisagree = np.array([0,0,0]) # Holds response "Neither agree nor disagree", by education level
y4_SlightlyAgree = np.array([0,0,0]) # Holds response "Slightly agree", by education level
y5_StronglyAgree = np.array([0,0,0]) # Holds response "Strongly agree", by education level
x_Respondents = [0,0,0] # Holds total number of respondents, by education level

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in the responses arrays depending on the response of the row, also populates x_Respondents
    if(row['Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?']=="Strongly disagree"): # Response "Strongly disagree"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y1_StronglyDisagree[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y1_StronglyDisagree[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y1_StronglyDisagree[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?']=="Slightly disagree"): # Response "Slightly disagree"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y2_SlightlyDisagree[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y2_SlightlyDisagree[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y2_SlightlyDisagree[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?']=="Neither agree nor disagree"): # Response "Neither agree nor disagree"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y3_NeitherAgreeNorDisagree[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y3_NeitherAgreeNorDisagree[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y3_NeitherAgreeNorDisagree[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?']=="Slightly agree"): # Response "Slightly agree"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y4_SlightlyAgree[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y4_SlightlyAgree[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y4_SlightlyAgree[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you agree or disagree that ChatGPT will play a major role in shaping the future of education?']=="Strongly agree"): # Response "Strongly agree"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y5_StronglyAgree[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y5_StronglyAgree[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y5_StronglyAgree[2] += 1
            x_Respondents[2] += 1

# To convert responses into percentages, (100/total number of responses)*responses
y1_percentage = np.array([((100/x_Respondents[0])*y1_StronglyDisagree[0]), ((100/x_Respondents[1])*y1_StronglyDisagree[1]), ((100/x_Respondents[2])*y1_StronglyDisagree[2])]) # Response "Strongly disagree", in percentage
y2_percentage = np.array([((100/x_Respondents[0])*y2_SlightlyDisagree[0]), ((100/x_Respondents[1])*y2_SlightlyDisagree[1]), ((100/x_Respondents[2])*y2_SlightlyDisagree[2])]) # Response "Slightly disagree", in percentage
y3_percentage = np.array([((100/x_Respondents[0])*y3_NeitherAgreeNorDisagree[0]), ((100/x_Respondents[1])*y3_NeitherAgreeNorDisagree[1]), ((100/x_Respondents[2])*y3_NeitherAgreeNorDisagree[2])]) # Response "Neither agree nor disagree", in percentage
y4_percentage = np.array([((100/x_Respondents[0])*y4_SlightlyAgree[0]), ((100/x_Respondents[1])*y4_SlightlyAgree[1]), ((100/x_Respondents[2])*y4_SlightlyAgree[2])]) # Response "Slightly agree", in percentage
y5_percentage = np.array([((100/x_Respondents[0])*y5_StronglyAgree[0]), ((100/x_Respondents[1])*y5_StronglyAgree[1]), ((100/x_Respondents[2])*y5_StronglyAgree[2])]) # Response "Strongly agree", in percentage

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
plt.bar(x_EducationLevels, y1_percentage, color='tab:red') # Plotting "Strongly disagree"
plt.bar(x_EducationLevels, y2_percentage, bottom=y1_percentage, color='tab:orange') # Plotting "Slightly disagree"
plt.bar(x_EducationLevels, y3_percentage, bottom=y1_percentage+y2_percentage, color='tab:green') # Plotting "Neither agree nor disagree"
plt.bar(x_EducationLevels, y4_percentage, bottom=y1_percentage+y2_percentage+y3_percentage, color='tab:cyan') # Plotting "Slightly agree"
plt.bar(x_EducationLevels, y5_percentage, bottom=y1_percentage+y2_percentage+y3_percentage+y4_percentage, color='tab:blue') # Plotting "Strongly agree"

# Formatting the graph
plt.xlabel("Level of Education") # X-Axis Label
plt.ylabel("Percentage of Responses") # Y-Axis Label
plt.ylim(0, 100) # Y-Axis Scale (Percentage)
plt.legend(["Strongly disagree", "Slightly disagree", "Neither agree nor disagree", "Slightly agree", "Strongly agree"], fontsize=18, loc=(0.7,0.01)) # Legend, changed font size and location for readability
plt.title("Level of Education vs. responses to \"Do you agree or disagree\nthat ChatGPT will play a major role in shaping the future of education?\"", fontsize=27.5, x=0.485, y=1.025) # Title, changed font size and location for readability

# Opening the graph in a pop-up window
plt.show()