# resimp
PAM-RTM resin importer

This allows for importing resin tables into PAM-RTM, which include variation of degree of cure, kinetic and temperature.

This is done by importing number of temperature tables. (as many as is required to minimize interpolation errors)

Can be turned into executable using "pyinstaller -F resimp_UI.py" to run on machines without Python. 

There are 2 types of import formats available: .csv and .xlsx. 

The .csv formats consists of repeated sets of 3 columns: fixed temperature, degree of cure, kinetic. This is quite easily re-created manually or automatically, hence this format is recommended. 

The .xlsx follows a specific format that was requested.

The figure below shows an example import (this does not correspond to a real resin):

![image](https://user-images.githubusercontent.com/40354213/161074898-e94f3b83-20cb-4169-b04f-85411cebe986.png)
