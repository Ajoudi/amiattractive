# AmIAttractive

Just a fun project that uses a deep learning model to predict your attractiveness based on your picture. Check out my blog (https://databata.wordpress.com/2018/07/09/100-day-ml-challenge/) for a more detailed explanation of the project, and a sneak peak into the relatively small journey I went through to finish this project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes:

Ofcourse, you will need python installed on your computer. 

Firstly download the SCUT-FBP5500 data set from the corresponding URL ( https://github.com/HCIILAB/SCUT-FBP5500-Database-Release)

Find the All_Labels.txt file, that’s the file with the beauty scores given to each image. Then find the Images folder which has the 5500 images that we will train on. Both of these will be used to develop our training and testing dataset. 

Install the pip dependencies found in the requirements.txt file using pip install -r requirements.txt

Run the train.py file to save your trained deep learning model. ( as a model.h5 weights file and a model.json structure file).

Finally, run the app.py file to launch the web application!! 

## Demo 
When you finally run the app.py file, open to your local host on port 33507. (go to 127.0.0.1:33507 on your browser). And you should see the following Upload functionality in your browser: 

![alt text](https://github.com/Ajoudi/amiattractive/blob/master/img1.PNG)



Upload an image of your face, and then press the predict button to predict your attractiveness.

![alt text](https://github.com/Ajoudi/amiattractive/blob/master/img2.PNG)

The image in the example above is one of the images found in the SCUT-FBP5500 dataset. As you can see the prediction is very off point. And that is because I did not train the model very well. However, as you train the model more and more the prediction results would be better.


## Further considerations

If running the model is taking a lot of time, you can try running it on Google Colab, which allows you to train your model on Google's cloud servers. (refer to my blog for more information).

You can also run your application on heroku, which is a cloud based server that allows you to host your application on the cloud. This way you can share your application between your friends! (refer to my blog for more information). 
