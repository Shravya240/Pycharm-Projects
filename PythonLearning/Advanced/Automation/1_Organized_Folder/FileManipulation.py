# Libararies : os, shutil, pathlib
import os
import shutil
import pathlib

def organize_folder(target_dir):

   # 1. Get The Taregt Folder
   directory = pathlib.Path(target_dir)  # Convert String Path to Path Object
   print("TARGET PATH:" , directory)

   extension_dic = {'.pdf' :  'Documents',
                     '.docx' : 'Documents',
                     '.txt'  : 'Documents',
                     '.png' : 'Images',
                     '.jpg' : 'Images',
                     '.mp4' : 'Videos',
                     '.mp3' : 'Audio',
                     '.zip' : 'Compressed',
                     '.mov' : "Videos"
   }

   # 2. Iterate/Loop each item in a directory
   for item in directory.iterdir():
       if item.is_file():
            # Extract extension of the file in lowercase
            file_extension = item.suffix.lower()

            if file_extension in extension_dic:
                new_folder = directory/extension_dic[file_extension]
                print(new_folder)

                # 3. Create the new Folder as SubFolder if it doesn't exist yet:
                new_folder.mkdir(exist_ok= True)

               #  4. Move the File to New  Folder
                shutil.move(str(item), str(new_folder/item.name))
                print("Moved the file to new folder: ", item.name ,"->" , extension_dic[file_extension])





#1. Define the folder you want to organize
source_folder = "/Users/shravyagupta/Downloads"
# 2. Calling the Function to Organize my source Folder
organize_folder(source_folder)