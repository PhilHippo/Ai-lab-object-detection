import os

def generate_negative_description_file():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

#To do so, opencv helps us by providing a tool. We loop through all the images in the positive folder and draw rectagles where the objects are
#In the path "opencv\build\x64\vc15\bin" we find:
    #opencv_annotation.exe that will help us mark objects in positive images and generate the txt file
    #opencv_createsamples.exe uses the txt file to generate the vector file that the cascade trainer will use
    #opencv_traincascade.exe uses the vector file to train the model
#Note: works only in windows hehe

#Open the command line and run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_annotation.exe --annotations=TESTPOS.txt --images=TEST_POS\"

#next we vectorize the images
#run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 65 -num 3000 -vec pos.vec"

#C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 24 -h 65 -num 1000 -maxxangle 1.5 -maxyangle 1.5 -maxzangle 0.6 -vec pos.vec -bg neg.txt


#finally we train the model and save it in the cascade folder
#run "C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 24 -h 65  -numPos 650 -numNeg 325 -numStages 10 -acceptanceRatioBreakValue 0.0001 -mode ALL"


#D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -img cans\c1.jpg -bg neg.txt -info info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 3200
#D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples -info info.lst -num 1000 -w 15 -h 41 -vec pos.vec
#D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 15 -h 41 -numPos 4000 -numNeg 2000 -numStages 12 -acceptanceRatioBreakValue 0.0005


#run "D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -info pos.txt -w 20 -h 55 -num 1300 -vec pos.vec"

#D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_traincascade.exe -data cascade/ -vec pos.vec -bg neg.txt -w 20 -h 55  -numPos 1000 -numNeg 500 -numStages 10 -acceptanceRatioBreakValue 0.0001