import pandas
import numpy as np
from sklearn import model_selection
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pickle

names = ['Sensor1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5', 'Sensor 6', 'class']

dataframe = pandas.read_csv('ruasfix04.csv', names=names)
array = dataframe.values
X = array[:,0:6]
Y = array[:,6]
test_size = 0.3
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

NaiveBayes = MultinomialNB().fit(X_train, np.ravel(Y_train, order = 'C'))

filename = 'ruas6.sav'
pickle.dump(NaiveBayes, open(filename, 'wb'))
 

result2 = NaiveBayes.predict(X_test)
result = metrics.accuracy_score(Y_test, result2)
print(result2)
print("akurasi model :",result)

