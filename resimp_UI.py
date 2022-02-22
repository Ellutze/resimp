# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:58:04 2022

@author: jakub.kucera
"""

import PySimpleGUI as sg
#Run GUI

def rUI():
    
    
    
    #implement a searchbox .... 


    layoutx = [[sg.Text('resin name', size=(15, 1)), sg.InputText("", key='rnm',size=(20, 1))], 
               [sg.Text('Filename', size=(15, 1)), sg.InputText('', key='fl',size=(20, 1))],
               [sg.Text('PAM-RTM location', size=(15, 1)), sg.InputText('', key='eloc',size=(20, 1))],
               [sg.Button('Import material',size=(35,1))]
               ]
    
    window = sg.Window('PAM-RTM resin material importer', layoutx, default_element_size=(12,1),size=(320,150))
    
    #GUI function loop
    while True: 
        #read all potential user inputs
        event, values = window.read()    
        
        if event is None: # way out!    
            break  
        
        if event in 'Import material':
            #sanitize username

            
            #implement checks... what if empty... etc...  break only if all available ....
            
            eloc = str(values['rnm'])
            rnm = str(values['eloc'])
            fl = str(values['fl'])
            break
                
         
    return(eloc, rnm,fl)
    
#rUI()