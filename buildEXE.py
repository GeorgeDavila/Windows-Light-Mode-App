import os
import shutil

#uncomment these to have it remove your current build and dist directories before rebuilding the app
#might get some pollution after succesive builds or making mutiple builds of different files, remove old directories at your discretion
#shutil.rmtree('dist') 
#shutil.rmtree('build')

os.system("pyinstaller -w -F -i sun_102839.ico --add-data=state.txt:state.txt ToggleLightMode.py")

print("============ Done with build! ============")

shutil.copyfile('dist/ToggleLightMode.exe', 'ToggleLightMode.exe')
print("EXE copied to current directory")