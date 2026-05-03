'''
Ellie Meredith
IS 303 - A01
 
Survey Analyzer
This program computes the average rating from a set of survey responses.
 
Inputs:
- Survey topic (string)
- Number of respondents (int)
- Total of all ratings (float)
 
Processes:
- Convert number of respondents to int and total ratings to float
- Calculate average rating: total ratings / number of respondents
 
Outputs:
- Print the survey topic, number of respondents, and average rating
'''
 
survey_topic = input("What is the survey topic? ")
num_respondents = int(input("How many people responded? "))
total_ratings = float(input("What is the total sum of all ratings? "))
 
average_rating = total_ratings / num_respondents
 
print("---")
print(f"Survey: {survey_topic} | Respondents: {num_respondents}")
print(f"Average rating: {average_rating}")