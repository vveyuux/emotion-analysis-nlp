# About The Project

This project is part of the Advanced AI course, and the chatbot can figure out what the emotion of text is.

**Made By Veerayuth Bussararungsee 2010711102013**

## About Library

-   [**TensorFlow**](https://www.tensorflow.org/) | for using text classification and machine learing for NLP.

-   [**NLTK :: Natural Language Toolkit**](https://www.nltk.org/) | for tokenizing and stemming texts.

## About files in this project

-   #### Json folder

    **intents.json** | contained the dataset of simply questions and reponses.

    **emotion.json** | contained the dataset of emotion in text., [Emotions in text | Kaggle](https://www.kaggle.com/datasets/ishantjuyal/emotions-in-text?resource=download)

    **emotion_responses.json** | contained response text according to emotion.

-   #### Assets folder

    Contained pickle file to use for predicating messages in **chatbot.py.**

-   #### Model folder

    Contained chatbot model that was trained and created by **train.py** for using in **app.py**.

-   #### test_data folder

    Contained testing data as json files.

-   #### Important files

    **train.py** | This file is about training the dataset and modelling for using in **chatbot.py** and **app.py**.

    **train.ipynb** | This file is about training as well, just like **train.py**, but it has a plotting graph to show how model accuracy and loss were.

    **chatbot.py** | This file contained function for using in **app.py** and for testing the **chatbot_model.h5**.

    **app.py** | This file is about GUI Chatbot that can use to chat.

    **model.test.py** | a testing file, to test the model how good in predcition it was.

## Getting Started

This is how to setting up your project locally.

### Prerequisites

#### Create and Activate your virtual environment

-   ##### Create virtual environment

```cmd
python -m venv env
```

-   ##### Activate virtual environment

```cmd
env\Scripts\activate
```

#### Install necessary libraries for thi project.

-   ##### Tensorflow

```cmd

python -m pip install tensorflow
```

-   ##### NLTK :: Natural Language Toolkit

```cmd
python -m pip install nltk
```

#### To run this chatbot in the project.

-   ##### Run app.py to run up a chatbot.

```
python app.py
```

### Here is how model was build.

![Build Model Image](./assets\mb_images\model.png)

With splitting 25% of all data to be the testing data
and this how summary, accuracy and loss of the model was.

#### Summary

![Summary Image](./assets\mb_images\summary.png)

#### Accuracy plot

![Auccuracy plot Image](./assets\mb_images\accuracy.png)

#### Loss plot

![Loss plot Image](./assets\mb_images\loss.png)

### Result of Testing the model

For testing you can uncomment one of these in the picture to testing for good model was for prediction.

![Testing data Image](./assets\mb_images\testing_data.png)

For example in this image I uncomment happy emotion, and this what the result was.

To start testing, use command

```cmd
python model.test.py
```

#### Result (Happy Emotion)

![Testing Happy Emotion data Image](./assets\mb_images\happy_emotion_testing_result.png)
