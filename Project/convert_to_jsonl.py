import pandas as pd
import spacy
import random
import json
nlp = spacy.load('en_core_web_sm')
df = pd.read_csv('short_stories.csv')
dict_list = []
delimiters = ['.', '!', '?']

def split_into_sentences(text):
    sents_list = []
    temp_sentence = []
    inside_quote = False

    for char in text:
        if char == '"':
            inside_quote = not inside_quote
        temp_sentence.append(char)
        if char in delimiters and not inside_quote:
            sents_list.append(''.join(temp_sentence).strip())
            temp_sentence = []

    if temp_sentence:
        sents_list.append(''.join(temp_sentence).strip())

    return sents_list

# Process each story in the DataFrame
for index, row in df.iterrows():
    # Initialize the dictionary for the current story
    d = {}

    # Remove the <para_break> tokens from the text
    text = row['text'].replace('<para_break>', ' ')

    # Split the text into sentences
    sents_list = split_into_sentences(text)

    # Tokenize the sentences using spaCy and populate the dictionary
    d['sentences'] = [[y.text for y in nlp(x)] for x in sents_list]
    d['text'] = text
    d['label'] = random.randint(0, 2)

    # Append the dictionary to the list
    dict_list.append(d)

# Write the list of dictionaries to a .jsonl file
with open('short_stories.jsonl', 'w') as outfile:
    for item in dict_list:
        json.dump(item, outfile)
        outfile.write('\n')
    
