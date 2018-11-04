from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import numpy
import csv
import random as rn
# fix random seed for reproducibility
numpy.random.seed(42)

# The below is necessary for starting core Python generated random numbers
# in a well-defined state.

rn.seed(12345)
# load pima indians dataset
dataset=list(csv.reader( open("altitude_final.csv",'r'),delimiter=','))
# split into input (X) and output (Y) variables
X = numpy.array(dataset)[:,0:3]
Y = numpy.array(dataset)[:,3]

# create model
model = Sequential()
model.add(Dense(3, input_dim=3, init='uniform', activation='relu'))
model.add(Dense(3, init='uniform', activation='relu'))
model.add(Dense(1, init='uniform', activation='sigmoid'))
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, nb_epoch=150, batch_size=5,  verbose=2)
model.summary()


#save the model
"""tf.keras.models.save_model(
    model,
    home/anoxyde0/Downloads,
    overwrite=True,
    include_optimizer=True
)"""


# calculate predictions
dataset1=list(csv.reader( open("altitude1.csv",'r'),delimiter=','))
X1=numpy.array(dataset1)[:,0:3]
predictions = model.predict(X1)
# round predictions
rounded = [(X1[0]) for X1 in predictions]
print(rounded)
# round predictionsc
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))