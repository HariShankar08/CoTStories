import os
import csv
import matplotlib.pyplot as plt
import numpy as np

dir_prompt_scores = [0] * 4
dir_prompt_count = 0
no_follow_up_scores = [0] * 4
no_follow_up_count = 0
follow_up_scores = [0] * 4
follow_up_count = 0
directory = "responses"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    form_number = int(f.split("/")[-1][4])%2
    if os.path.isfile(f):
        file = open(f,"r")
        file_reader = csv.reader(file)
        response_num = 0
        for response in file_reader:
            if response_num == 0:
                response_num+=1
                continue
            response_num+=1
            for i in range(4):
                dir_prompt_scores[i]+=int(response[i+2])
                dir_prompt_count+=1/4
                if form_number == 0:
                    follow_up_count+=1/4
                    follow_up_scores[i]+=int(response[i+6])
                elif form_number == 1:
                    no_follow_up_count+=1/4
                    no_follow_up_scores[i]+=int(response[i+6])


dir_prompt_scores=[i/dir_prompt_count for i in dir_prompt_scores]
no_follow_up_scores = [i/no_follow_up_count for i in no_follow_up_scores]
follow_up_scores = [i/follow_up_count for i in follow_up_scores]
print(dir_prompt_scores)
print(no_follow_up_scores)
print(follow_up_scores)
questions = [
    "How logically consistent was the story?",
    "How smooth was the progression of the story?",
    "How engaging was the story?",
    "How abrupt was the ending of the story?"
]
X_axis = np.arange(len(questions))
plt.bar(X_axis - 0.3,dir_prompt_scores,0.3,label="no questions")
plt.bar(X_axis,no_follow_up_scores,0.3,label="questions without follow up")
plt.bar(X_axis + 0.3,follow_up_scores,0.3,label="questions with follow up")
plt.xticks(X_axis, questions)
plt.xlabel("Questions")
plt.ylabel("Average score(out of 10)")
plt.legend()
plt.show()