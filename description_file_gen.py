#once we have the positive folder and negative folder, we can generate the description file

import os

#The negative images should be listed in a special negative image file containing one image path per line
def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('testneg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('TEST_NEG'):
            f.write('TEST_NEG/' + filename + '\n')
generate_negative_description_file()

#The positive images should be listed in a special positive image file containing one image path per line,
#followed by the number of objects in the image, and the coordinates of each object.
    #img/img1.jpg  1  140 100 45 45
    #img/img2.jpg  2  100 200 50 50   50 30 25 25

#To do so, opencv helps us by providing a tool. We loop through all the images in the positive folder and draw rectagles where the objects are
#In the path "opencv\build\x64\vc15\bin" we find:
    #opencv_annotation.exe that will help us mark objects in positive images and generate the txt file
    #opencv_createsamples.exe uses the txt file to generate the vector file that the cascade trainer will use
    #opencv_traincascade.exe uses the vector file to train the model
#Note: works only in windows hehe

#Open the command line and run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=TESTPOS.txt --images=TEST_POS\"

#next we vectorize the images
#run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 20 -h 54 -num 3000 -vec pos.vec"

#finally we train the model and save it in the cascade folder
#run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 20 -h 54  -numPos 640 -numNeg 320 -numStages 10 -acceptanceRatioBreakValue 0.0001 -mode ALL"