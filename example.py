# D1 - Move #2

# Goal:
# Build an SVM classifier with C=1 for D1.
# Use S1 as a training set and S2 as a testing set

# Rationale:
# We need somewhere to start. We might as well start here.

# Expected Accuracy
# Assessed using a held out test set: 0.5

# numpy provides the tools to easily load our data and split the
# features from the labels
import numpy as np

# We'll use an SVM from scikit learn
from sklearn import svm

# use numpy to load our training set
d1_train = np.loadtxt(open("data/D1_S1.csv", "rb"), delimiter=",")
# features are all rows for columns before 200
d1_train_features = d1_train[:, :200]
# labels are in all rows at the 200th column
d1_train_labels = d1_train[:, 200]

# use numpy to load our testing set
d1_test = np.loadtxt(open("data/D1_S2.csv", "rb"), delimiter=",")
# features are all rows for columns before 200
d1_test_features = d1_test[:, :200]
# labels are in all rows at the 200th column
d1_test_labels = d1_test[:, 200]

# Now we're going to construct a classifier. First we need to set up our
# parameters
classifier = svm.SVC(C=1, kernel='linear')

# Once our parameters are set, we can fit the classifier to our data
classifier.fit(d1_train_features, d1_train_labels)

# Once we have our classifier, we can apply it back to the examples and get our
# score. Since this is binary classification. We get an accuracy.
train_score = classifier.score(d1_train_features, d1_train_labels)
print("Training Accuracy: " + str(train_score))

# We can also apply it back to our testing dataset
test_score = classifier.score(d1_test_features, d1_test_labels)
print("Testing Accuracy: " + str(test_score))
