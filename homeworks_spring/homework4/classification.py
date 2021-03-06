#!/home/barbitoff/anaconda3/bin/python

import numpy as np
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics.classification import accuracy_score
from random import shuffle


# Data preparation
# 4601 letters to classify - 1813 of one class, 2788 - of the other (as indicated by dataset specification)
# Link to d/s -> http://archive.ics.uci.edu/ml/datasets/Spambasehttp://archive.ics.uci.edu/ml/datasets/Spambase
spam = []
non_spam = []
with open('spambase.data', 'r') as ifile:
    for line in ifile:
        letter = [float(x) for x in line.strip().split(',')]
        isSpam = bool(letter[57])
        letter = np.array(letter[:57])
        if isSpam:
            spam.append(letter)
        else:
            non_spam.append(letter)

spam = np.array(spam)
non_spam = np.array(non_spam)

np.random.shuffle(spam)
np.random.shuffle(non_spam)

train_spam = spam[:1500, ]
validation_spam = spam[1500:, ]

train_non_spam = non_spam[:2200, ]
validation_non_spam = non_spam[2200:, ]

training_set = np.concatenate((train_spam, train_non_spam))
validation_set = np.concatenate((validation_spam, validation_non_spam))

training_classes = np.concatenate((np.ones(1500), np.zeros(2200)))
validation_classes = np.concatenate((np.ones(313), np.zeros(588)))

# Classification and evaluation - RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier
ns = [10, 20, 40, 80, 100, 150, 200, 300, 400, 500, 1000]

with open('accuracy_measures.txt', 'w') as ofile:
    ofile.write('\t'.join(['Algo', '10', '20', '40', '80', '100', '150', '200', '300', '400', '500', '1000']) + '\n')
    # Sluchayniy perelesok
    rf_scores = []
    for i in ns:
        blackbox = RandomForestClassifier(n_estimators=i)
        blackbox = blackbox.fit(training_set, training_classes)
        predictions = blackbox.predict(validation_set)
        acc = accuracy_score(validation_classes, predictions)
        rf_scores.append(str(acc))
    ofile.write('RandomForestClassifier\t' + '\t'.join(rf_scores) + '\n')
    
    # Bolshe derevyev
    et_scores = []
    for i in ns:
        blackbox = ExtraTreesClassifier(n_estimators=i)
        blackbox = blackbox.fit(training_set, training_classes)
        predictions = blackbox.predict(validation_set)
        acc = accuracy_score(validation_classes, predictions)
        et_scores.append(str(acc))
    ofile.write('ExtraTreesClassifier\t' + '\t'.join(et_scores) + '\n')
    
    # Adovoe uskorenie
    ab_scores = []
    for i in ns:
        blackbox = AdaBoostClassifier(n_estimators=i)
        blackbox = blackbox.fit(training_set, training_classes)
        predictions = blackbox.predict(validation_set)
        acc = accuracy_score(validation_classes, predictions)
        ab_scores.append(str(acc))
    ofile.write('AdaBoostClassifier\t' + '\t'.join(ab_scores) + '\n')
    
    # Gradientniy pinok
    gb_scores = []
    for i in ns:
        blackbox = GradientBoostingClassifier(n_estimators=i)
        blackbox = blackbox.fit(training_set, training_classes)
        predictions = blackbox.predict(validation_set)
        acc = accuracy_score(validation_classes, predictions)
        gb_scores.append(str(acc))
    ofile.write('GradientBoostClassifier\t' + '\t'.join(gb_scores) + '\n')

# All done!
