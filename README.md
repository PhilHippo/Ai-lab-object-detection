# AI Lab: Computer Vision and NLP

Computer Vision project: Object Detection

## Intro

OpenCV supports a variety of machine learning algorithms and while deep neural networks have received a lot of attention lately
**Haar Cascade Classifiers** remain the easiest to get started with and they can still produce good results.

## Cascade Classifier Training

In order to train a Cascade Classifier we need:

1. a set of **negative samples** (containing everything you do not want to detect)
2. a set of **positive samples** (containing actual objects you want to detect)

### Negative Samples

Negative samples are images of environments not containing the object we want to detect, but where the object is likely to be found.
For this reason Negative Samples are also called Background Samples or Background Images.
These negative images should then be listed in a special **neg.txt** file containing one image path per line.

To build the neg.txt file we use the **generate_negative_description_file()** function in description_file_gen.py

### Positive Samples

Positive Samples are images containing the object you want to detect.
Once the positive images are obtained we must proceed with the creation of the **pos.txt** file containing
one image path per line, the number of occurances of the object, the coordinates of the object bounding rectangle.

To build the pos.txt file we can use the OpenCV's integrated annotation tool: **opencv_annotation**.

Next thing we need to do is we need to create a **pos.vec** file from our pos.txt file.
To do that we use the **opencv_createsamples** application.
Look at "create samples output.png".

### .xml file creation

The **cascade.xml** file in the cascade folder is the actual trained model.
To create that file we use the OpenCV's integrated **opencv_createsamples** application taking as input pos.vec and neg.txt

# ESP 32 cam

Per vedere lo stream wireless della camera in real time basta utilizzare un indirizzo https che metto di seguito:

http://192.168.178.146

Basta collegare la camera alla corrente, incollare l'indirizzo sul browser e cliccare "avvia stream" sulla pagina web che si apre.

Non sono sicuro che l'indirizzo rimanga lo stesso se si cambia rete.
La camera infatti ha bisongo del nome della rete e della password per poter streammare.
Per indicare nome e password bisogna scriverli sul codice che poi viene caricato sulla camera tramite il computer.