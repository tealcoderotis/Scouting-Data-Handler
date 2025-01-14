import os
import subprocess
import inspect
import database as db #Needs to be run from main folder

preset_path = "ModifyData\\ModifyPresets"
presetpreset = "ModifyData\\ModifyPresetPreset.py"
conversion_path = "ModifyData\\ConversionPresets\\"

def openFolder(): 
    os.startfile(preset_path)

def createFile(name):
    filepath = f"{preset_path}\\{name}"

    with open(presetpreset,'r') as firstfile, open(filepath,'a') as secondfile:
        for line in firstfile:
            secondfile.write(line)

def delFile(name):
    filepath = f"{preset_path}\\{name}"
    os.remove(filepath)

def getParams(file, custom = False): #list of strings
    import importlib
    if custom == True:
        presetFolder = "ModifyPresets"
    else:
        presetFolder = "DefaultModifyPresets"
    
    function_string = f'ModifyData.{presetFolder}.{os.path.splitext(file)[0]}.funct'
    mod_name, func_name = function_string.rsplit('.',1)
    mod = importlib.import_module(mod_name)
    funct = getattr(mod, func_name)
    return [tupleData[0] for tupleData in inspect.signature(funct).parameters]

def saveConversion(data, name):
    db.write_csv(f"{name}", data)

def readConversion(name):
    return db.read_csv(f"{name}")