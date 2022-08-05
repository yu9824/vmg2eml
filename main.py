import os
import vmg2eml

dirpath_input = './input'
dirpath_input = os.path.abspath(dirpath_input)

for fname_input in os.listdir(dirpath_input):
    fpath_input = os.path.join(dirpath_input, fname_input)
    
    converter = vmg2eml.Convert(fpath_vmg=fpath_input)
    converter.convert()
    