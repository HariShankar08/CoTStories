import evaluate
rouge = evaluate.load("rouge")
bleu = evaluate.load("bleu")
bertscore = evaluate.load("bertscore")
pred = ["together we shall devour the very gods"]
target = ["we shall devour the very gods together"]
print(rouge.compute(predictions=pred,references=target))
print(bleu.compute(predictions=pred,references=target))
print(bertscore.compute(predictions=pred,references=target,lang="en"))