import os
import shutil

from_dir="/Users/sbshealth/Downloads"
to_dir="/Users/sbshealth/Documents/Document_Files"
list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files : 
    root,ext=os.path.splitext(file_name)
    print(root)
    print(ext)
    if ext =='':
        continue
    if ext in['.txt','.doc','.docx','.pdf']:
        path1= from_dir+'/'+file_name
        path2= to_dir+'/'+"Document_files"
        path3= to_dir+'/'+"Document_Files"+'/'+file_name
        print(path1)
        print(path3)
        if os.path.exists(path2):
            print("moving"+file_name+"..")

            shutil.move(path1,path3)
    
        else:
            os.makedirs(path2)
            print("moving"+file_name+"..")

            shutil.move(path1,path3)



