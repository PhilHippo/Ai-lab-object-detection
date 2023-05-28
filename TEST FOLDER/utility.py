import os
import subprocess


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
        print(f"Command failed with return code {process.returncode}")
    else:
        print(f"Command finished successfully")

suffix = ' -info pos.txt -w 6 -h 16 -num 100 -vec pos.vec'
cmd = r'C:\Users\wangf\Myrepos\AI_PROJECT_STUFF\opencv\build\x64\vc15\bin\opencv_createsamples.exe' + suffix

run_cmd(cmd)

os.rename("pos.vec", "pos1.vec")
with open("pos.vec", "w") as f:
    pass

run_cmd(cmd)

#NICE