import matplotlib.pyplot as plt
import os
from ast import literal_eval
directory1 = "Rouge_scores_Full_Conversation"
directory2 = "Rouge_scores_Outline_only"

avg_by_idea = []
avg_by_method = []
metrics = []
ideas = []
x_axis = []
file_count = 0
for filename in os.listdir(directory1):
    f = os.path.join(directory1, filename)
    # checking if it is a file
    if os.path.isfile(f):
        if("singleprompt" in f):
            continue
        avg_by_metric = {}  
        rouge_by_idea = 0
        # rouge_by_metric = 0
        file = open(f,"r")
        method_name = f.split("/")[1].split(".")[0][:-14]
        data = file.read().split("\n")[:-1]
        lendata = len(data)
        rouge = 0
        for i in range(lendata):
            data[i] = data[i].split(":",1)
            data[i][1] = literal_eval(data[i][1])
            if avg_by_metric == {}:
                avg_by_metric = {metric:data[i][1][metric] for metric in data[i][1]}
            else:
                avg_by_metric = {metric: avg_by_metric[metric] + data[i][1][metric] for metric in data[i][1]}
        for i in avg_by_metric:
            rouge += avg_by_metric[i]/lendata
        rouge/= len(avg_by_metric)
        avg_by_method.append(rouge)
        x_axis.append(method_name)
        if(metrics == []):
            metrics = [i for i in data[0][1].keys()]
        if(ideas == []):
            ideas = [i[0] for i in data]

plt.figure(figsize=(20,5))
plt.bar(x_axis,avg_by_method, label="Full Conversation")
plt.xlabel("Method")
# plt.xticks(rotation=15)
plt.ylabel("Average rouge score")
plt.savefig("full_convo_rouge.png")
plt.show()


avg_by_idea = []
avg_by_method = []
metrics = []
ideas = []
x_axis = []
file_count = 0
for filename in os.listdir(directory2):
    f = os.path.join(directory2, filename)
    # checking if it is a file
    if os.path.isfile(f):
        avg_by_metric = {}  
        rouge_by_idea = 0
        # rouge_by_metric = 0
        file = open(f,"r")
        method_name = f.split("/")[1].split(".")[0][:-14]
        data = file.read().split("\n")[:-1]
        lendata = len(data)
        rouge = 0
        for i in range(lendata):
            data[i] = data[i].split(":",1)
            data[i][1] = literal_eval(data[i][1])
            if avg_by_metric == {}:
                avg_by_metric = {metric:data[i][1][metric] for metric in data[i][1]}
            else:
                avg_by_metric = {metric: avg_by_metric[metric] + data[i][1][metric] for metric in data[i][1]}
        for i in avg_by_metric:
            rouge += avg_by_metric[i]/lendata
        rouge/= len(avg_by_metric)
        avg_by_method.append(rouge)
        x_axis.append(method_name)
        if(metrics == []):
            metrics = [i for i in data[0][1].keys()]
        if(ideas == []):
            ideas = [i[0] for i in data]

plt.figure(figsize=(20,5))
plt.bar(x_axis,avg_by_method, label="Outline only")
plt.xlabel("Method")
# plt.xticks(rotation=15)
plt.ylabel("Average rouge score")
plt.savefig("outline_only_rouge.png")
plt.show()