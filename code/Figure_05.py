# Date: Apr 1, 2023 / Edited: Aug 17, 2023
# By: Adeshvir Dhillon

# Graph: Responses of undergraduates, master's, and PhDs to "Should universities implement a concise set of rules for the use of ChatGPT to prevent plagiarism from happening?"
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
labels = ["No", "Maybe", "Yes"] # Response Options
responses = [0,0,0] # Holds the responses of respondents

for index, row in df.iterrows(): # Iterates through the google sheets, updating the correct element in 'responses' depending on the response of the row
    if(row['What is the highest level of education that you have obtained / are currently obtaining?'] in ["Undergraduate", "Masters", "PhD"]): # If the respondent is in academia
        if(row['Should universities implement a concise set of rules for the use of ChatGPT to prevent plagiarism from happening?']=="No"): # Response "No"
            responses[0] += 1
        elif(row['Should universities implement a concise set of rules for the use of ChatGPT to prevent plagiarism from happening?']=="Maybe"): # Response "Maybe"
            responses[1] += 1
        elif(row['Should universities implement a concise set of rules for the use of ChatGPT to prevent plagiarism from happening?']=="Yes"): # Response "Yes"
            responses[2] += 1

# Plotting the graph
plt.rcParams['font.size'] = 30 # Increasing font size of graph for readability
fig, ax = plt.subplots()
ax.pie(responses, labels=labels, autopct='%1.1f%%', colors=["tab:red", "tab:orange", "tab:blue"]) # Plotting pie-chart, changed colours for aesthetics

# Formatting the graph
plt.title("Responses of undergraduates, master's, and PhDs to \"Should universities implement\na concise set of rules for the use of ChatGPT to prevent plagiarism from happening?\"", fontsize=28.5, x=0.475, y=1) # Title, changed font size and location for readability

# Opening the graph in a pop-up window
plt.show()