import json

import tensorflow as tf
from chatbot import predict_class

testdata = json.loads(open("test\surprise.json").read())
length = len(testdata["sentences"])
corr = 0
num = 1
tp = "surprise"

print(length)

# For testing in terminal

# Chatbot Start
print("This is testing model enjoy XD")

for msg in testdata["sentences"]:
    res = predict_class(msg)
    print(num)
    num = num + 1
    if res[0]["intent"] == tp:
        corr = corr + 1

print("Correct: ", corr)
print("Accuracy: ", (corr / length) * 100)
