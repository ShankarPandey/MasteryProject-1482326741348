# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
import pickle

# load data
data = read_csv('d1_train.csv', header=None, names=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])
#print(data)

array = data.values
#print array

X = array[:,0:5]
Y = array[:,5]

print X
print Y

# feature extraction
model = LogisticRegression()
rfe = RFE(model, 5)
fit = rfe.fit(X, Y)
print("Num Features: %d") % fit.n_features_
print("Selected Features: %s") % fit.support_
print("Feature Ranking: %s") % fit.ranking_
print("Feature Estimator: %s") % fit.estimator

with open('test3_model.pkl', 'wb') as f:
    pickle.dump(fit, f)