import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.decomposition import PCA
from imblearn.combine import SMOTEENN
from sklearn.metrics import roc_auc_score
from imblearn.under_sampling import RandomUnderSampler
import matplotlib.pyplot as plot

# Split the experimental samples and normalize the samples
data0 = np.load('data_selected_1980_2010.npy')
data1 = np.load('target_1980_2010.npy')

# Concatenate data_selected(features) with target
data = np.concatenate((data0, data1), axis = 1)
normalized_x = preprocessing.normalize(data0)
split = 9497
x_train, x_test, y_train, y_test = normalized_x[:split, :], normalized_x[split:, :], data1[:split, 1:], data1[split:, 1:]
#print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

# Create a random forest Classifier. By convention, clf means 'Classifier'
clf = RandomForestClassifier(random_state=0)

# Train the Classifier to take the training features and learn how they relate
# to the training y (the species)
sm = SMOTEENN()
X_resampled, y_resampled = sm.fit_sample(x_train, y_train.ravel())
clf.fit(X_resampled, y_resampled)
y_pred = clf.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(metrics.confusion_matrix(y_test, y_pred))
#print (classification_report(y_test,y_pred))
#print accuracy

# #Apply the random under-sampling
# rus = RandomUnderSampler(return_indices=True)
# X_resampled, y_resampled, idx_resampled = rus.fit_sample(x_train, y_train.ravel())
# clf.fit(X_resampled, y_resampled)
# y_pred = clf.predict(x_test)
# accuracy = metrics.accuracy_score(y_test, y_pred)
# print(metrics.confusion_matrix(y_test, y_pred))
# #print (classification_report(y_test,y_pred))
# print accuracy

# ROC_AUC_Score: Computing the area under the ROC-curve
#print "roc_auc_score = %f" % ras
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred)
roc_auc = metrics.auc(fpr, tpr)
# print y_test
# print y_pred
# print(fpr)
# print(tpr)
# print(thresholds)
print(roc_auc)

plot.title('ROC')
plot.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plot.legend(loc = 'lower right')
plot.plot([0, 1], [0, 1], 'r--')
plot.xlim([0, 1])
plot.ylim([0, 1])
plot.ylabel('True Positive Rate')
plot.xlabel('False Positive Rate')
plot.show()
