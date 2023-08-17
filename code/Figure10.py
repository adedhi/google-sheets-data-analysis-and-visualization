# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: Level of Education vs. responses to "Do you believe that universities should allow or restrict the use of ChatGPT among students?"
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
y1_StronglyRestrict = np.array([0,0,0,]) # Holds response "Strongly restrict", by education level
y2_SomewhatRestrict = np.array([0,0,0]) # Holds response "Somewhat restrict", by education level
y3_NeitherAllowNorRestrict = np.array([0,0,0]) # Holds response "Neither allow nor restrict", by education level
y4_SomewhatAllow = np.array([0,0,0]) # Holds response "Somewhat allow", by education level
y5_StronglyAllow = np.array([0,0,0]) # Holds response "Strongly allow", by education level
x_Respondents = [0,0,0] # Holds total number of respondents, by education level

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in the responses arrays depending on the response of the row, also populates x_Respondents
    if(row['Do you believe that universities should allow or restrict the use of ChatGPT among students?']=="Strongly restrict"): # Response "Strongly restrict"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y1_StronglyRestrict[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y1_StronglyRestrict[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y1_StronglyRestrict[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that universities should allow or restrict the use of ChatGPT among students?']=="Somewhat restrict"): # Response "Somewhat restrict"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y2_SomewhatRestrict[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y2_SomewhatRestrict[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y2_SomewhatRestrict[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that universities should allow or restrict the use of ChatGPT among students?']=="Neither allow nor restrict"): # Response "Neither allow nor restrict"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y3_NeitherAllowNorRestrict[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y3_NeitherAllowNorRestrict[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y3_NeitherAllowNorRestrict[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that universities should allow or restrict the use of ChatGPT among students?']=="Somewhat allow"): # Response "Somewhat allow"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y4_SomewhatAllow[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y4_SomewhatAllow[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y4_SomewhatAllow[2] += 1
            x_Respondents[2] += 1
    elif(row['Do you believe that universities should allow or restrict the use of ChatGPT among students?']=="Strongly allow"): # Response "Strongly allow"
        if(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Undergraduate"): # Undergraduate respondents
            y5_StronglyAllow[0] += 1
            x_Respondents[0] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="Masters"): # Master's respondents
            y5_StronglyAllow[1] += 1
            x_Respondents[1] += 1
        elif(row['What is the highest level of education that you have obtained / are currently obtaining?']=="PhD"): # PhD respondents
            y5_StronglyAllow[2] += 1
            x_Respondents[2] += 1

# To convert responses into percentages, (100/total number of responses)*responses
y1_percentage = np.array([((100/x_Respondents[0])*y1_StronglyRestrict[0]), ((100/x_Respondents[1])*y1_StronglyRestrict[1]), ((100/x_Respondents[2])*y1_StronglyRestrict[2])]) # Response "Strongly restrict", in percentage
y2_percentage = np.array([((100/x_Respondents[0])*y2_SomewhatRestrict[0]), ((100/x_Respondents[1])*y2_SomewhatRestrict[1]), ((100/x_Respondents[2])*y2_SomewhatRestrict[2])]) # Response "Somewhat restrict", in percentage
y3_percentage = np.array([((100/x_Respondents[0])*y3_NeitherAllowNorRestrict[0]), ((100/x_Respondents[1])*y3_NeitherAllowNorRestrict[1]), ((100/x_Respondents[2])*y3_NeitherAllowNorRestrict[2])]) # Response "Neither allow nor restrict", in percentage
y4_percentage = np.array([((100/x_Respondents[0])*y4_SomewhatAllow[0]), ((100/x_Respondents[1])*y4_SomewhatAllow[1]), ((100/x_Respondents[2])*y4_SomewhatAllow[2])]) # Response "Somewhat allow", in percentage
y5_percentage = np.array([((100/x_Respondents[0])*y5_StronglyAllow[0]), ((100/x_Respondents[1])*y5_StronglyAllow[1]), ((100/x_Respondents[2])*y5_StronglyAllow[2])]) # Response "Strongly allow", in percentage

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
plt.bar(x_EducationLevels, y1_percentage, color='tab:red') # Plotting "Strongly restrict"
plt.bar(x_EducationLevels, y2_percentage, bottom=y1_percentage, color='tab:orange') # Plotting "Somewhat restrict"
plt.bar(x_EducationLevels, y3_percentage, bottom=y1_percentage+y2_percentage, color='tab:green') # Plotting "Neither allow nor restrict"
plt.bar(x_EducationLevels, y4_percentage, bottom=y1_percentage+y2_percentage+y3_percentage, color='tab:cyan') # Plotting "Somewhat allow"
plt.bar(x_EducationLevels, y5_percentage, bottom=y1_percentage+y2_percentage+y3_percentage+y4_percentage, color='tab:blue') # Plotting "Strongly allow"

# Formatting the graph
plt.xlabel("Level of Education") # X-Axis Label
plt.ylabel("Percentage of Responses") # Y-Axis Label
plt.ylim(0, 100) # Y-Axis Scale (Percentage)
plt.legend(["Strongly restrict", "Somewhat restrict", "Neither allow nor restrict", "Somewhat allow", "Strongly allow"], fontsize=19, loc=(0.71,0)) # Legend, changed font size and location for readability
plt.title("Level of Education vs. responses to \"Do you believe that universities should\nallow or restrict the use of ChatGPT among students?\"", fontsize=29, y=1.02) # Title, changed font size and location for readability

# Opening the graph in a pop-up window
plt.show()