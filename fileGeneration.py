import os
import subprocess
import time

def negDesFileGenerator():
    # open the output file for writing. will overwrite all existing data in there
    with open('neg.txt', 'w') as f:
        # loop over all the filenames
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')

def new_info(can):
    # Get the current working directory
    cwd = os.getcwd()

    # Define the folder name and the new name
    folder_name = "info"
    new_folder_name = folder_name + can

    # Rename the folder
    os.rename(os.path.join(cwd, folder_name), os.path.join(cwd, new_folder_name))

    # Create the new folder with the same name as the original folder
    os.mkdir(os.path.join(cwd, folder_name))

    # Create the empty file inside the new folder
    with open(os.path.join(cwd, new_folder_name, "info.lst"), "w") as f:
        pass


#run command in terminal
def run_cmd(cmd):

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(stderr.decode("utf-8"))
    else:
        print(f"Command finished successfully")

#for each can in cans folder we create 3200 samples with different angles, store the images and the relative annotations in the info folder, rename the folder
for can in os.listdir("cans"):
    cmd = fr'D:\REPOSITORIES\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe -img cans\{can} -bg neg.txt -info info\info.lst -pngoutput info -maxxangle 0.4 -maxyangle 0.4 -maxzangle 0.4 -num 3200'

    run_cmd(cmd)
    time.sleep(0.2)
    new_info(can.split(".")[0])