# Reading a excel sheet and formatting columns as per requirement
# the excel sheet structure is following.

# Question, Who are you
# Answer,   Pradeep
# Question, Where do you live 
# Answer,   Hyderabad
# Question, What do you do
# Answer,   Nothing

# The final structure would be

#         1,      2 
# Who are you,Pradeep
# Where do you live,Hyderabad
# What do you do,Nothing


#!/bin/python
import pandas as pd
# Reading with no header 
data = pd.read_excel("data.xlsx","Sheet1",header=None)
# Fetch all the rows where row value = Question 
Queries = list(data.loc[data[0] == 'Question'][1])  
# Fetch all the rows where row value = Answer 
Resolutions = list(data.loc[data[0] == 'Answer'][1])
# Creating dataframe
final = pd.DataFrame({'1':Queries, '2': Resolutions})
final.to_csv("final.csv")