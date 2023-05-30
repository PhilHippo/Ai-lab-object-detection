# Real-World Aim Assist

Object Detection using Haar Cascade Classifier

## Introduction

The aim of this project is to build a prototype of a real-world gun aim assist using object detection and audio signals.

OpenCV supports a variety of machine learning algorithms and while deep neural networks have received a lot of attention lately, **Haar Cascade Classifiers** remain a valid choice when dealing with object detection.

The reason for this is that Cascade Classifiers represent a compromise between *speed* and *robustness*:

1. they are computationally efficient and can process images in real-time or near real-time, even on resource-constrained devices
2. they have been proven to work well in a variety of real-world scenarios and lighting conditions

The training of a Cascade Classifier involves many steps starting from the creation of the data set.

## Cascade Classifier Training

In order to train a Cascade Classifier we need first and foremost:

1. a set of **negative samples** (containing everything you do not want to detect)
2. a set of **positive samples** (containing actual objects you want to detect)

### Negative Samples

Negative samples are images of environments not containing the object we want to detect, but where the object is likely to be found. For this reason Negative Samples are also called Background Samples or Background Images.

These negative images should then be listed in a special **Negative Description File** file whose structure is shown below:

***DA COMPLETARE UNA VOLTA SISTEMATE LE CARTELLE***

To build it we use the **negDesFileGenerator()** function in fileGeneration.py.

### Positive Samples

Positive Samples are images containing the object you want to detect.

Once the positive images are obtained we must proceed with the creation of the **Positive Description File** which contains the following information for each line:

1. the image path
2. the number of occurances of the object in that image
3. the coordinates of the object's bounding rectangle (x, y, width, height)

To build it we use the OpenCV's integrated annotation tool: **opencv_annotation**.

### .xml file creation

Next thing we need to do is creating a **pos.vec** file from our pos.txt file.
To do that we use the **opencv_createsamples** application.
Look at "create samples output.png".

The **cascade.xml** file in the cascade folder is the actual trained model.
To create that file we use the OpenCV's integrated **opencv_createsamples** application taking as input pos.vec and neg.txt

# ESP 32 cam

Per vedere lo stream wireless della camera in real time basta utilizzare un indirizzo https che varia a seconda della rete
con la quale si configura la camera:

*http://192.168.178.146*    Wi-Fi casa di Simone

*http://192.168.178.146*    hotspot telefono di Simone

Basta collegare la camera alla corrente, incollare l'indirizzo sul browser e cliccare "avvia stream" sulla pagina web che si apre.

1. L'indirizzo https generato per una rete in particolare non cambia nel tempo, rimane lo stesso.
2. Affinchè funzioni, camera e computer devono essere collegati alla stessa rete Wi-Fi.
3. Le impostazioni della camera possono essere cambiate in real time usando la pagina web

(tranne la risoluzione: meglio non cambiarla se no si bugga la finestra di openCV)

Per indicare nome e password bisogna scriverli sul codice che poi viene caricato sulla camera tramite Arduino IDE.