import pandas
import numpy as np
from sklearn import model_selection
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
import pickle

#names = ['Sensor1','Sensor2', 'Sensor3', 'Sensor4', 'Sensor5', 'Sensor6', 'ruasd', 'class']
names = ['Sensor1','Sensor2', 'Sensor3', 'Sensor4', 'Sensor5', 'Sensor6', 'Sensor 7', 'Sensor 8', 'Sensor 9', 'Sensor 10', 'Sensor 11', 'Sensor 12', 'Class']

dataframe = pandas.read_csv('datasetruas6x6.csv', names=names)
array = dataframe.values
X = array[:,0:12]
Y = array[:,12]
test_size = 0.3
seed = 0
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

NaiveBayes = MultinomialNB().fit(X_train, np.ravel(Y_train, order = 'C'))

filename = 'modelruas6x6.sav'
pickle.dump(NaiveBayes, open(filename, 'wb'))
 

result2 = NaiveBayes.predict(X_test)
result = metrics.accuracy_score(Y_test, result2)
print(result2)
print("akurasi model :",result)

print(X_test)
#print(dataframe)
