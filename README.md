# About The Project

---

This project is part of the Advanced AI course, and the chatbot can figure out what the emotion of text is.

**Made By Veerayuth Bussararungsee 2010711102013**

## About Library

---

-   [**TensorFlow**](https://www.tensorflow.org/) | for using text classification and machine learing for NLP.

-   [**NLTK :: Natural Language Toolkit**](https://www.nltk.org/) | for tokenizing and stemming texts.

## About files in this project

---

-   #### Json folder

    **intents.json** | contained the dataset of simply questions and reponses.

    **emotion.json** | contained the dataset of emotion in text., [Emotions in text | Kaggle](https://www.kaggle.com/datasets/ishantjuyal/emotions-in-text?resource=download)

    **emotion_responses.json** | contained response text according to emotion.

-   #### Assets folder

    Contained pickle file to use for predicating messages in **chatbot.py.**

-   #### Model folder

    Contained chatbot model that was trained and created by **train.py** for using in **app.py**.

-   #### Important files

    **train.py** | This file is about training the dataset and modelling for using in **chatbot.py** and **app.py**.

    **chatbot.py** | This file contained function for using in **app.py** and for testing the **chatbot_model.h5**.

    **app.py** | This file is about GUI Chatbot that can use to chat.

## Getting Started

---

This is how to setting up your project locally.

#### Prerequisites

Create and Activate your virtual environment

```
# Create virtual environment
python -m venv env

# Activate virtual environment
env\Scripts\activate
```

Install necessary libraries for thi project.

```
# Tensorflow
python -m pip install tensorflow

# NLTK :: Natural Language Toolkit
python -m pip install nltk
```
