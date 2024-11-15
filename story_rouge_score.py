import csv
import evaluate
import os
from ast import literal_eval

rouge = evaluate.load("rouge")
directory = "outputs"

def find_assistant_dialogue(message_history:str):
    assistant_dialogue = ""
    dialogues = literal_eval(message_history)
    for message in dialogues:
        if message["role"] == "assistant":
            assistant_dialogue = assistant_dialogue + message["content"] + "\n"
    return assistant_dialogue

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        rouge_scores_outline_only = []
        rouge_scores_full_conversation = []
        file = open(f,"r")
        file_reader = csv.reader(file)
        for story in file_reader:
            if story[0] == "":
                continue
            idea = story[1]
            outline = story[2]
            full_story = story[3]
            assistant_messages = find_assistant_dialogue(story[4])
            story_rouge = rouge.compute(predictions=[full_story], references=[outline])
            rouge_scores_outline_only.append(f"{idea}: {story_rouge}\n")
            story_rouge = rouge.compute(predictions=[full_story], references=[assistant_messages])
            rouge_scores_full_conversation.append(f"{idea}: {story_rouge}\n")
        file.close()
        with open("Rouge_scores_Outline_only/" + f.split("/")[-1][:-4] + "_rouge.txt","w") as file:
            file.writelines(rouge_scores_outline_only)
        with open("Rouge_scores_Full_Conversation/" + f.split("/")[-1][:-4] + "_rouge.txt","w") as file:
            file.writelines(rouge_scores_full_conversation)
