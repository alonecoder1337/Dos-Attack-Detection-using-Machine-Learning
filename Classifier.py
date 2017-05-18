from sklearn import svm
from sklearn.tree import DecisionTreeClassifier

class Classififer:
    def __init__(self):
        pass

    def get_classifier(self):
        '''
            returns Classifier object
        '''
        clf = DecisionTreeClassifier()
        return clf
