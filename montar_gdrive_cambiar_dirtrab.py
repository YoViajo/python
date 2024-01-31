from google.colab import drive
drive.mount('/content/drive')

import os

# Replace 'path/to/your/folder' with the actual path to the folder you want to set as your workspace
folder_path = "/content/drive/MyDrive/path/to/your/folder"
os.chdir(folder_path)


