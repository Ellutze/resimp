# resimp
PAM-RTM resin importer

This allows for importing resin tables into PAM-RTM, which include variation of degree of cure, kinetic and temperature.

This is done by importing number of temperature tables. (as many as is required to minimize interpolation errors)

Can be turned into executable using "pyinstaller -F resimp_UI.py" to run on machines without Python. The resulting executable needs to be put into a folder with: cp.txt, imp_PR.py. This is because the files run through command line (due to PAM-RTM using separate Python library) will not be packaged using pyinstaller. It is recommended to place the 2 import example in the folder as well for reference.

There are 2 types of import formats available: .csv and .xlsx. 

The .csv formats consists of repeated sets of 3 columns: fixed temperature, degree of cure, kinetic. This is quite easily re-created manually or automatically, hence this format is recommended. 

The .xlsx follows a specific format that was requested.

The figure below shows an example import (This does not represent a real resin):

![image](https://user-images.githubusercontent.com/40354213/161074898-e94f3b83-20cb-4169-b04f-85411cebe986.png)
