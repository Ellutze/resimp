# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:58:04 2022

@author: jakub.kucera
"""

#import imp_PR # keep this here for executable development, the script is run through cmd.... so pyinstaller wouldnt know

ImportNotes = "Accepted formats are .xlsx and csv. To see how the format \n"+\
              "should look, please see examples in provided folder. \n"+\
              "For .csv it is simple repeating columns [Fixed temperature,\n"+\
              "degree of cure (a), da/dt]\n"+\
              "All temperatures should be provided in deg.C, the script \n"+\
              "translates everything to kelvin for the use within PAM-RTM."

import PySimpleGUI as sg
#Run GUI
from resimp_main import resimp

def rUI():
    
    
    
    #UI for basic inputs only


    layoutx = [[sg.Text('resin name', size=(15, 1)), sg.InputText("", key='rnm',size=(40, 1))], 
               [sg.Text('PAM-RTM location', size=(15, 1)), sg.InputText("C:\\Program Files\\ESI Group\\Visual-Environment\\17.0\\Windows-x64", key='esi',size=(40, 1))],
               [sg.Text('Enter one of the following files:')],
               [sg.FileBrowse('Source file (.xlsx)',file_types=(("Text Files", "*.xlsx"),),key='x',size=(15, 1)),sg.InputText("", key='fl1',size=(40, 1))],
               [sg.FileBrowse('Source file (.csv)',file_types=(("Text Files", "*.csv"),),key='x',size=(15, 1)),sg.InputText("", key='fl2',size=(40, 1))],
               [sg.Button('Import material',size=(45,1)),sg.Button('?',size=(2,1),key='q2')]
               ]
    
    window = sg.Window('PAM-RTM resin material importer', layoutx, default_element_size=(12,1),size=(450,175))
    
    #GUI function loop
    while True: 
        #read all potential user inputs
        event, values = window.read()    
        
        if event is None: # way out!    
            break  
        
        if event in 'Import material':

            
            
            #implement checks... what if empty... etc...  break only if all available ....
            if values['rnm'] == "" or (values['fl1'] =="" and values['fl2'] =="") :
                print("the resin name and source file must be specified")
            else:
                #use one of the two import boxes
                if values['fl1'] !="":
                    fl = str(values['fl1'])
                elif values['fl2'] !="":
                    fl = str(values['fl2'])
                print(fl)  
                    
                if ".csv" in fl or ".xlsx" in fl:
                    esi = str(values['esi'])
                    rnm = str(values['rnm'])
                    fn = fl
                    resimp(rnm, fn,esi)
                    print("verify in PAM-RTM that your resin has imported succesfully")
                    print("You can now close the window, or chose next file to import")
                else:
                    print("Only .csv and .xlsx file formats are currently supported")
            
        if event in 'Source file':
            window.Element('fl').Update(str(values['x']))

        if event in 'q2':

            l12 = [[sg.Multiline(ImportNotes,size=(450,450),key=('out'),enter_submits=True)]]
            w2 = sg.Window('...',l12,size=(500,200))
            e2, v2 = w2.read()

    
rUI()
