# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 14:50:17 2022

@author: jakub.kucera
"""

#layout:
# import file field, PAM-RTM install location, initiate button



#accomodate for file formats (default the excel from Cristian, 2nd singular csv table (3rows, repeated?)(3rows with various temp in same col?)

from resimp_UI import rUI

#eLoc is the location of PAM-RTM installation
#rnm is the resin name
#fl is the source file for data (either csv or xlsx)
eLoc, rnm, fl = rUI()
print(eLoc)
print(rnm)
print(fl)

# upon button press:

#translate any input file to importable .txt files 


#for command line use:
import subprocess
#for excel imports:
import openpyxl
#for general mathematical operations
import numpy as np

import os
lPath = os.getcwd()
print(lPath)
# Give the location of the file
path = lPath+"\\TestRes1.xlsx"  # replace this with the above
fn = "filenametest" # replace with the UI input
 
#workbook open
wb_obj = openpyxl.load_workbook(path,data_only = True)
#active sheet (make sure it is always on the correct sheet?)
sheet_obj = wb_obj.active

r = 14
c = 2 
e = True
i = 0
Ts = []
while e == True:
    cell_obj = sheet_obj.cell(row = r, column = c)
    
    try:
        if i > 0 and int(cell_obj.value) <= 0:
            e = False
        else:
            t = float(cell_obj.value) + 273.15 # assuming source always in C? what if in Kelvin
            print(t)
            t = str(t)
            Ts.append(t)
            c = c + 7
            i = i + 1    
    
    #if i > 0 and int(cell_obj.value) <= 0:
    except: 
        # Print value of cell object
        # using the value attribute
        e = False
print(Ts)
i = 0
#M = np.zeros([1,2])
for t in Ts:
    r = 19
    c = 3 + 7*i
    with open('tt\\'+str(t)+'.txt', 'w') as f:
        e = True
        while e == True:
            a = sheet_obj.cell(row = r, column = c)
            dadt = sheet_obj.cell(row = r, column = c+3)
        
            if a.value != None:
                a = format(a.value,'.30f')
                dadt = format(dadt.value,'.30f')
                f.write(str(a)+" "+str(dadt)+"\n")
                #m_temp = np.matriix([a,dadt])
                #M = np.concatenate((M,m_temp),axis=0)
                r = r + 1
            else:
                e = False
    #delete the 0 row 
    
    #save matrix as txt file
    
    i = i + 1


#outputs to be picked up by the PAM-RTM script
np.save(lPath+"\\temp_list.npy",Ts,allow_pickle=True, fix_imports=True)
with open("filename.txt",'w') as f:
    f.write(fn)



#save file with meta-data  

#initiate command line 
    
#REPLACE FILE -- RELATIVE LOCATION TO THIS SCRIPT
  
    
def cmd2(command,RTMFile=""):
    #Passes command to command line.
    #Required due to Visual-RTM having it's own library of python packages.
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, cwd="C:\\Program Files\\ESI Group\\Visual-Environment\\17.0\\Windows-x64")
    proc_stdout = process.communicate()#[0].strip()
    print(command)
    print(proc_stdout)
    
cmd2("VEBatch -activeconfig Trade:CompositesandPlastics -activeapp VisualRTM -sessionrun "+lPath+"\\imp_PR.py")
#after import is done make sure to delete everything in "tt" (temporary temperature tables)