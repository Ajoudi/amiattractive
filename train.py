import os
from keras.applications import ResNet50
from keras.models import Sequential
from keras.layers import Dense
from scipy.misc import imread
import numpy as np


resnet = ResNet50(include_top=False, pooling='avg')
model = Sequential()
model.add(resnet)
model.add(Dense(1))
model.layers[0].trainable = False  

labels = open('All_labels.txt')  # change the location to where your All_labels.txt is located 
labels = labels.read()
labels = labels.split('\n')
print(labels)


split_labels =[]
for i in labels:
    split_labels += [i.split(' ')]
print(split_labels)

label_final = []
for fname in os.listdir('Images'): # change the location to where your Images is located
    for i in range(0,len(split_labels)):
        if fname == split_labels[i][0]:
            label_final += [float(split_labels[i][1])]
            break
print(label_final)


test = os.listdir('Images')

image_dataset3 = []
for i in range(0,5500):
  print('loading',i)
  try:
    image_dataset3+=[imread('Images/'+test[i])]
  except:
    print('Error')
print('DONE')


train_X = np.array(image_dataset3)
train_Y = np.array(label_final)

model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])

model.fit(batch_size=32, x=train_X, y=train_Y, validation_split=0.33, epochs=30)

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
    
model.save_weights("model.h5")
print("Saved model to disk")

