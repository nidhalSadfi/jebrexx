import os
import subprocess
import time

CURRENT_DIRECTORY = os.getcwd()
directories = os.listdir(CURRENT_DIRECTORY)
NON_ANGULAR_DIRS = ['static', 'templates']

for directory in directories:
    if "." not in directory and directory not in NON_ANGULAR_DIRS:
        ANGULAR_PROJECT_PATH = os.path.join(CURRENT_DIRECTORY, directory)
        DIST_PATH = os.path.join(ANGULAR_PROJECT_PATH, 'dist', directory)

FLASK_STATIC_PATH = os.path.join(CURRENT_DIRECTORY, 'static')
FLASK_TEMPLATES_PATH = os.path.join(CURRENT_DIRECTORY, 'templates')

print(FLASK_TEMPLATES_PATH)

subprocess.call(('cd ' + ANGULAR_PROJECT_PATH + ' && ng build --base-href /static/ &'), shell=True)

dir_exists = True

while dir_exists:
    try:
        files = os.listdir(DIST_PATH)
        static_files = ""
        html_files = ""
        for file in files:
            if '.js' in file or '.js.map' in file or '.ico' in file:
                static_files += (file + ' ')
            if '.html' in file:
                html_files += (file + ' ')
        print(static_files)
        print("*******************************")
        if len(static_files) > 0:
            subprocess.call(('cd ' + DIST_PATH + ' &&' + ' MOVE  ' + static_files + FLASK_STATIC_PATH), shell=True)
            print("could u copy?")
        if len(html_files) > 0:
            subprocess.call(('cd ' + DIST_PATH + ' &&' + ' MOVE  ' + html_files + FLASK_TEMPLATES_PATH), shell=True)
    except Exception as e:
        dir_exists = False
        print(e)
    time.sleep(10.0)