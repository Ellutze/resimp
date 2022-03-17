#open input file that checks the file it needs to reach - number of tables, name of tables....



null='' 
import VScn
import VCmd
import VistaDb
NULL=VistaDb.PythonCNULL() 
import VistaDb

import VE
import VExpMngr
import numpy as np




lPath='D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#'D:\\resimp'#

Ts = np.load(lPath+"\\temp_list.npy")

with open(lPath+"\\cp.txt", "a") as text_file:
    text_file.write(" start \n")

with open(lPath+"\\filename.txt",'r') as e:
    rsn = str(e.read())

#__________________ VhmCommand BEGIN __________________
var1=VCmd.Activate( 1, r"VHostManagerPlugin.VhmInterface", r"VhmCommand" )
#__________________ SessionCommand BEGIN __________________
var2=VCmd.Activate( 1, r"VSessionManager.Command", r"SessionCommand" )
#__________________ VEAction BEGIN __________________
var3=VCmd.Activate( 1, r"VToolKit.VSectionCutInterface", r"VEAction" )
ret=VE.ChangeContext( r"Visual-RTM" )
VE.SetActiveWindow( r"p1w1" )
VExpMngr.NewModel( r"" )
VE.SetCurrentPage( 1 )
ret=VE.ModelChange( "M  @0" )
#__________________ SimulationParameters BEGIN __________________
var4=VCmd.Activate( 1, r"VRTMUtilities.VRTMInterface", r"SimulationParameters" )
VCmd.Quit( var4 )
#__________________ SimulationParameters END __________________
#__________________ GenericMaterialEditor BEGIN __________________
var5=VCmd.Activate( 1, r"VMaterial.VMaterialInterface", r"GenericMaterialEditor" )
VCmd.SetStringValue( var5, r"SelectDb", r"Model" )
VCmd.SetStringValue( var5, r"ActiveCategoryTab", r"General" )
VCmd.SetStringValue( var5, r"SelectDb", r"User" )
VCmd.SetStringValue( var5, r"ActiveFolderClassID", r"Resin" )
VCmd.SetStringValue( var5, r"FolderPath", r"Resin" )
VCmd.SetStringValue( var5, r"ActiveClass", r"Resin" )
VCmd.SetStringValue( var5, r"ActiveMaterial", rsn )
VCmd.SetStringValue( var5, r"ActiveCategoryTab", r"General" )
VCmd.SetStringValue( var5, r"RecentMaterialList", r"User/"+rsn )
VCmd.SetStringValue( var5, r"ActiveCategoryTab", r"Thermal" )
VCmd.SetStringValue( var5, r"ActiveCategoryTab", r"Chemical" )
VCmd.SetStringValue( var5, r"ActiveProperty", r"Kinetic" )
VCmd.SetStringValue( var5, r"ActiveModelID", r"RTM_Chemical" )
#__________________ VisualPlotEditorOnlyPlotEmbeddedChild BEGIN __________________
var6=VCmd.Activate( 0, r"VGuiUtilCOM.VgucIVisualPlot", r"VisualPlotEditorOnlyPlotEmbeddedChild" )

i = 0 
while i < np.size(Ts,0):


    #__________________ CurveAttributes BEGIN __________________
    var7=VCmd.Activate( 1, r"VGuiUtilCOM.VgucIVisualPlot", r"CurveAttributes" )
    VCmd.SetIntValue( var6, r"Sort X and Do not Modify Table", 1 )

    #Really don't understand the repetition here, but without the repetition it simply doesn't work, whichcraft I guess....
    ret=VCmd.ExecuteCommand( var5, r"AddOrUpdateFixedParameterValue" )
    ret=VCmd.ExecuteCommand( var6, r"ClearSelectedCurves" )
    ret=VCmd.ExecuteCommand( var6, r"RemoveTempCurves" )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )    
    ret=VCmd.ExecuteCommand( var5, r"AddOrUpdateFixedParameterValue" )
    ret=VCmd.ExecuteCommand( var6, r"ClearSelectedCurves" )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )
    ret=VCmd.ExecuteCommand( var6, r"ClearSelectedObjects" )
    ret=VCmd.ExecuteCommand( var6, r"RemoveTempCurves" )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )   
    VCmd.SetIntValue( var5, r"CurveIndexList", 6 )
    VCmd.SetStringValue( var7, r"SetActiveTab", r"Edit" )
    VCmd.SetStringValue( var6, r"SetCurrentMode", r"Edit" )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )      
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )
    VCmd.SetIntValue( var5, r"CurveIndexList", 6 )

    
    #location will have to change
    f = open(lPath+"\\tt\\"+str(Ts[i])+".txt", "r")

    lSTR =""
    for line in f:
        lSTR = lSTR +" "+line+"  |  "
    lst1_count,lst1 =  VScn.Point2List( lSTR)
    
    VCmd.SetPoint2ArrayValue( var5, r"PropertyTValue", lst1_count, lst1 )
    VCmd.SetStringValue( var7, r"SetActiveTab", r"Edit" )
    VCmd.SetStringValue( var6, r"SetCurrentMode", r"Edit" )
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", r"TEMP" )
    VCmd.SetStringValue( var5, r"FixedPropertySValue", str(Ts[i]) )
    ret=VCmd.ExecuteCommand( var5, r"UpdateLookupBackup" ) # is this the line!?
    VCmd.SetStringValue( var5, r"ActiveFixedProperty", '' )
    ret=VCmd.ExecuteCommand( var5, r"Save" )
    VCmd.Accept( var5 )


    with open(lPath+"\\cp.txt", "a") as text_file:
        text_file.write(str(Ts[i])+" temperuture current \n")
    i = i + 1


VCmd.Quit( var5 )


#the below can be used for troubleshooting anywhere within the script

#with open(lPath+"\\cp.txt", "a") as text_file:
#    text_file.write("x") 