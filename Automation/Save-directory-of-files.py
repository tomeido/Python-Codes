import os
import os.path
import sys

# =================
# NOTES
# It is a function of storing directories by dividing them into each text file as many as the number of text files.
# =================

# =================
# Method
# =================

def WriteDirectoryOfFile(txtfile_Count, path, file_list, file_Count, txtDir, txtExtend):
    numbering = 1
    cnt = 0
    
    # get file list in the dirrectory
    file_list = os.listdir(path) 
    # get count of files
    file_Count = len(file_list) 
    
    sys.stdout = open(txtDir + str(numbering) + txtExtend, 'w')
    for _file in file_list :
        if((file_Count / txtfile_Count) * numbering > cnt) :
            print(path + "\\" + _file)
        else :
            sys.stdout.close()
            numbering += 1
            sys.stdout = open(txtDir + str(numbering) + txtExtend, 'w')
            print(path + "\\" + _file)
        
        cnt += 1

    sys.stdout.close()

# =================
# Main
# =================

# count of .txt file
txtfile_Count = 3

# directory where save .txt file
txtDir = r'C:\temp\MyDirectory' 
txtExtend = r'.txt'

# directory of files
path = r"C:\temp" 

WriteDirectoryOfFile(txtfile_Count, path, file_list, file_Count, txtDir, txtExtend)