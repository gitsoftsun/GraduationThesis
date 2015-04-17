#!/usr/bin/env python
# -*- coding: utf-8 -*-


# coding: utf-8

## Five-Line Sentiment Analysis Classifier

# In this notebook, I will explain how to develop sentiment analysis classifiers that are based on a bag-of-words model. 
# Then, I will demonstrate how these classifiers can be utilized to solve Kaggle's "When Bag of Words Meets Bags of Popcorn" challenge.

### Code Recipe: Creating Sentiment Classifier 

# Using GraphLab it is very easy and straight foward to create a sentiment classifier based on bag-of-words model. Given a dataset stored as a CSV file, you can construct your sentiment classifier using the following code: 

# In[ ]:

import graphlab as gl
train_data = gl.SFrame.read_csv(traindata_path,header=True, delimiter='\t',quote_char='"', column_type_hints = {'id':str, 'sentiment' : int, 'review':str } )
train_data['1grams features'] = gl.text_analytics.count_ngrams(train_data['review'],1)
train_data['2grams features'] = gl.text_analytics.count_ngrams(train_data['review'],2)
cls = gl.classifier.create(train_data, target='sentiment', features=['1grams features','2grams features'])


# In the rest of this notebook, we will explain this code recipe in details, by demonstrating how this recipe can used to create IMDB movie reviews sentiment classifier.

### Set up

# Before we begin constructing the classifiers, we need to import some Python libraries: graphlab (gl), and IPython display utilities. We also set IPython notebook and GraphLab Canvas to produce plots directly in this notebook.

# In[2]:

import graphlab as gl
from IPython.display import display
from IPython.display import Image

gl.canvas.set_target('ipynb')


### Dataset

# Throughout this notebook, I will use Kaggle's IMDB movies reviews datasets that is available to download from the following link: https://www.kaggle.com/c/word2vec-nlp-tutorial/data. I downloaded labeledTrainData.tsv and testData.tsv files, and unzipped them to the following local files.

# In[3]:

traindata_path = "/home/graphlab/data/sentiment/labeledTrainData.tsv"
testdata_path = "/home/graphlab/data/sentiment/testData.tsv"


### Loading Data

# We will load the data with IMDB movie reviews to an SFrame using SFrame.read_csv function.

# In[4]:

movies_reviews_data = gl.SFrame.read_csv(traindata_path,header=True, delimiter='\t',quote_char='"', column_type_hints = {'id':str, 'sentiment' : str, 'review':str } )


# By using the SFrame show function, we can visualize the data and notice that the train dataset consists of 12,500 positive and 12,500 negative, and overall 24,932 unique reviews.

# In[5]:

movies_reviews_data.show()


### Constructing Bag-of-Words Classifier 

# One of the common techniques to perform document classification (and reviews classification) is using Bag-of-Words model, in which the frequency of each word in the document is used as a feature for training a classifier. GraphLab's text analytics toolkit makes it easy to calculate the frequency of each word in each review. Namely, by using the count_ngrams function with n=1, we can calculate the frequency of each word in each review. By running the following command:

# In[6]:

movies_reviews_data['1grams features'] = gl.text_analytics.count_ngrams(movies_reviews_data ['review'],1)


# By running the last command, we created a new column in movies_reviews_data SFrame object. In this column each value is a dictionary object, where each dictionary's keys are the different words which appear in the corresponding review, and the dictionary's values are the frequency of each word.
# We can view the values of this new column using the following command.

# In[7]:

movies_reviews_data.show(['review','1grams features'])


# We are now ready to construct and evaluate the movie reviews sentiment classifier using the calculated above features. But first, to be able to perform a quick evaluation of the constructed classifier, we need to create labeled train and test datasets. We will create train and test datasets by randomly splitting the train dataset into two parts. The first part will contain 80% of the labeled train dataset and will be used as the training dataset, while the second part will contain 20% of the labeled train dataset and will be used as the testing dataset. We will create these two dataset by using the following command:  

# In[8]:

train_set, test_set = movies_reviews_data.random_split(0.8, seed=5)


# We are now ready to create a classifier using the following command:

# In[9]:

model_1 = gl.classifier.create(train_set, target='sentiment', features=['1grams features'])


# We can evaluate the performence of the classifier by evaluating it on the test dataset

# In[10]:

result1 = model_1.evaluate(test_set)


# In order to get an easy view of the classifier's prediction result, we define and use the following function

# In[11]:

def print_statistics(result):
    print "*" * 30
    print "Accuracy        : ", result["accuracy"]
    print "Confusion Matrix: \n", result["confusion_matrix"]
print_statistics(result1)


# As can be seen in the results above, in just a few relatively straight foward lines of code, we have developed a sentiment classifier that has accuracy of about ~0.88. Next, we demonstrate how we can improve the classifier accuracy even more.

### Improving The Classifier

# One way to improve the movie reviews sentiment classifier is to extract more meaningful features from the reviews. One method to add additional features, which might be meaningful, is to calculate the frequency of every two consecutive words in each review. To calculate the frequency of each two consecutive words in each review, as before, we will use GraphLab's count_ngrams function only this time we will set n to be equal 2 (n=2) to create new column named '2grams features'.  

# In[12]:

movies_reviews_data['2grams features'] = gl.text_analytics.count_ngrams(movies_reviews_data['review'],2)


# As before, we will construct and evaluate a movie reviews sentiment classifier. However, this time we will use both the '1grams features' and the '2grams features' features

# In[13]:

train_set, test_set = movies_reviews_data.random_split(0.8, seed=5)
model_2 = gl.classifier.create(train_set, target='sentiment', features=['1grams features','2grams features'])
result2 = model_2.evaluate(test_set)
print_statistics(result2)


# Indeed, the new constructed classifier seems to be more accurate with an accuracy of about ~0.9.

### Unlabeled Test File

# To test how well the presented method works, we will use all the 25,000 labeled IMDB movie reviews in the train dataset to construct a classifier. Afterwards, we will utilize the constructed classifier to predict sentiment for each review in the unlabeled dataset. Lastly, we will create a submission file according to Kaggle's guidelines and submit it. 

# In[14]:

#creating classifier using all 25,000 reviews
traindata_path = "/home/graphlab/data/sentiment/labeledTrainData.tsv"
train_data = gl.SFrame.read_csv(traindata_path,header=True, delimiter='\t',quote_char='"', column_type_hints = {'id':str, 'sentiment' : int, 'review':str } )
train_data['1grams features'] = gl.text_analytics.count_ngrams(train_data['review'],1)
train_data['2grams features'] = gl.text_analytics.count_ngrams(train_data['review'],2)

cls = gl.classifier.create(train_data, target='sentiment', features=['1grams features','2grams features'])
#creating the test dataset
test_data = gl.SFrame.read_csv(testdata_path,header=True, delimiter='\t',quote_char='"', column_type_hints = {'id':str, 'review':str } )
test_data['1grams features'] = gl.text_analytics.count_ngrams(test_data['review'],1)
test_data['2grams features'] = gl.text_analytics.count_ngrams(test_data['review'],2)

#predicting the sentiment of each review in the test dataset
test_data['sentiment'] = cls.classify(test_data)['class'].astype(int)

#saving the prediction to a CSV for submission
test_data[['id','sentiment']].save("/home/graphlab/data/sentiment/predictions.csv", format="csv")


# We then submitted the predictions.csv file to the Kaggle challange website and scored AUC of about 0.88.

### Further Readings

# Further reading materials can be found in the following links:
# 
# http://en.wikipedia.org/wiki/Bag-of-words_model
# 
# https://dato.com/products/create/docs/generated/graphlab.SFrame.html
# 
# https://dato.com/products/create/docs/graphlab.toolkits.classifier.html
# 
# https://www.kaggle.com/c/word2vec-nlp-tutorial/details/part-1-for-beginners-bag-of-words
# 
# Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, and Christopher Potts. (2011). "Learning Word Vectors for Sentiment Analysis." The 49th Annual Meeting of the Association for Computational Linguistics (ACL 2011).
# 
