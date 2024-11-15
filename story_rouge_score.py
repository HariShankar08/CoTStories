import csv
import evaluate
import os
rouge = evaluate.load("rouge")
directory = "outputs"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        rouge_scores = []
        file = open(f,"r")
        file_reader = csv.reader(file)
        for story in file_reader:
            idea = story[1]
            outline = story[2]
            full_story = story[3]
            story_rouge = rouge.compute(predictions=[full_story], references=[outline])
            rouge_scores.append(f"{idea}: {story_rouge}\n")
        file.close()
        with open("Rouge_scores/" + f.split("/")[-1][:-4] + "_rouge.txt","w") as file:
            file.writelines(rouge_scores)
