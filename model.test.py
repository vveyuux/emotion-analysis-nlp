import json

import tensorflow as tf

from chatbot import predict_class

""" Uncomment one of these test data to testing to model below """

testdata = json.loads(open("test_data\happy.json").read())
tp = "Happy"

# testdata = json.loads(open("test_data\love.json").read())
# tp = "Love"

# testdata = json.loads(open("test_data\sadness.json").read())
# tp = "Sadness"

# testdata = json.loads(open("test_data\surprise.json").read())
# tp = "Surprise"

# testdata = json.loads(open("test_data\\fear.json").read())
# tp = "Fear"

# testdata = json.loads(open("test_data\\anger.json").read())
# tp = "Anger"

""" Uncomment one of these test data to testing to model above """

length = len(testdata["sentences"])
corr = 0
num = 1

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
