from keras.models import Model, Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten
import tensorflow as tf


def init(): 

	json_file = open('model.json','r')
	loaded_model_json = json_file.read()
	json_file.close()
	loaded_model = model_from_json(loaded_model_json)
	#load woeights into new model
	loaded_model.load_weights("model.h5", by_name = True)
	
	print("Loaded Model from disk")
	loaded_model.compile(loss='mean_squared_error', optimizer='adam',metrics=['accuracy'])

	graph = tf.get_default_graph()
	return loaded_model,graph
	