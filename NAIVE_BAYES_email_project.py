from sklearn.datasets import fetch_20newsgroups
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
#2.We're interested in seeing how effective our Naive Bayes classifier is at telling the difference between a baseball email and a hockey email. 

#We can select the categories of articles we want from fetch_20newsgroups by adding the parameter categories.
emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'])
#We now want to split our data into training and test sets. Change the name of your variable from emails to train_emails. Add these three parameters to the function call:
#subset='train'
#shuffle = True
#random_state = 108
train_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset='train', shuffle = True, random_state = 108) 
#Create another variable named test_emails and set it equal to fetch_20newsgroups. The parameters of the function should be the same as before except subset should now be 'test'.
test_emails = fetch_20newsgroups(categories = ['rec.sport.baseball', 'rec.sport.hockey'], subset = 'test', shuffle = True, random_state = 108)
#We want to transform these emails into lists of word counts. The CountVectorizer class makes this easy for us.
counter = CountVectorizer()
#We need to tell counter what possible words can exist in our emails. counter has a .fit() a function that takes a list of all your data.
counter.fit(test_emails.data + train_emails.data)
train_counts = counter.transform(train_emails.data)
test_counts = counter.transform(test_emails.data)
#Let's now make a Naive Bayes classifier that we can train and test on. Create a MultinomialNB object named classifier.
classifier = MultinomialNB()
#Call classifier's .fit() function. .fit() takes two parameters. The first should be our training set, which for us is train_counts. The second should be the labels associated with the training emails. Those are found in train_emails.target.
classifier.fit(train_counts, train_emails.target)
#Test the Naive Bayes Classifier by printing classifier's .score() function. .score() takes the test set and the test labels as parameters.
#.score() returns the accuracy of the classifier on the test data. Accuracy measures the percentage of classifications a classifier correctly made.
print(classifier.score(test_counts, test_emails.target))

