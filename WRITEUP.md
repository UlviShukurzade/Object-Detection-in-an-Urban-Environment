# Project Writeup
## Object Detection in an Urban Environment


### Project overview
Object detection is the most important part of building self-driving cars. This project is designed to leverage the great [TensorFlow Object Detection API](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md) for object detection specifically in urban environments. <br/>
[TensorFlow Object Detection API](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2.md) procide us huge [zoo of models](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) with easy to use approach.<br/>

Our goal with this project is to finetune the pretrained model to detect cars , pedestrians and cyclists in traffic. <br/>

### Set up:
The project is structured as follows:
```
Workspace
│   
└───experiments
│   └───reference
│       │   pipeline_new.config         # initial model config 
│   └───experiment5
│       │   pipeline_new.config         #improved model config 
└───images
│   └───reference                    # initial model learning outputs
│   └───experiment5                  # final experiment learning outputs            
│   └───gif_final                    # inference video for improved model  
│   Exploratory Data Analysis.ipynb         #EDA notebook
|   Explore augmentations.ipynb             #Augmentation notebook
|   LICENSE.md
|   README.md
|   WRITEUP.md
|   edit_config.py
|   filenames.txt
|   inference_video.py
|   label_map.pbtxt
|   launch_jupyter.sh
|   pipeline.config
│   requirements.txt
│   utils.py
```

The steps to run the code is given in README.md file<br/>

### Dataset
Dataset we work is Waymo Open dataset which provides high quality video frames in urban environment. The frames contains object in 3 different classes. Cars, Pedestrians, Cyclists.<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/download.png?raw=true )<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/download_1.png?raw=true )<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/download_2.png?raw=true )<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/download_3.png?raw=true )<br/>

in the following image, there is blo annotation box in the upper part of image, which can be considered as weakness of the dataset.<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/annotation_error.png?raw=true )<br/>

From the simple analisys it is seen that there is significant difference between the amount of car objects vs other 2 classes, which might cause our model be less precise on pedestrian and bicycle detection.<br/>
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/eda/class_distribution.png?raw=true )<br/>

Dataset is split into Train Eval and Test sets in workspace.
### Reference experiment
The reference model used for this task is SSD Resnet 50 640x640. Which is Singe Shot Detector on Resnet Architecture. However the Resnet architecture is quite well-performing model, the pretrained data is probably different than our dataset. which caused very high amount of loss for training steps and ended up not converging.
![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/reference/combine_images.jpg?raw=true  "Learning process" )

The inference video proved that out network was not able to learn to detect objects.

![Inference video]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/reference/animation_ref.gif?raw=true "Inference Video of reference model in night time" )

Model was not able to detect any object.



### Improve on the reference

To improve the model I reduced batchsize to 8, and set a learning rate base of 0.001 which is a lot lower than pre-set rate, and initial warmup rate of 0.00033.
At the same time, increased training steps to 3000.

![Example images]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/experiment5/Screenshot%202022-12-21%20at%2003.09.39.png?raw=true )
However, the learning rate still does not seem to sattle. But it is significantly more stable than reference model.
But the learning rate would not be enough, from the previous experiments I observed that model severely suffer in the dark videos which are taken in the night trips.
To reduce this effect and make my network to learn better I applied some data augmentation mechanisms, especially the ones that changes color, hue, brightness.
The ide was to simulate different light conditions. And also changing hue, and saturation, i might trick the model to see same cars with different colors.

In fact, it worked, and improved model preformance significantly.
![Improved results in the night time]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/5356f4db6a985ea03f9c8f339dedf797b496c40b/images/gif_final/animation_mini.gif?raw=true "Night time recording" )


![Improved results in the night time]( https://github.com/UlviShukurzade/Object-Detection-in-an-Urban-Environment/blob/main/images/gif_final/animation_daytime_mini.gif?raw=true )

It is very impressive that now model can predict some objects with more than 90% confidence in both day and night recordings. However, there is quite a large space for improvements as the overall confidence is low. And especially the model thinks the water hydrants are pedestrians in the daytime video :D 
This especially can be caused by the dataset being highly unbalanced. There is significantly more car objects than all other classes.
I believe a better results can be achieved by increasing data quality, data varity, and additional data augmentation steps.
