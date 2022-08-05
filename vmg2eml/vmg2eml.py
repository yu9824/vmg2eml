from genericpath import isfile
import sys
import os
import math

class Convert:
    DIR_NAME = './EMLs/'

    def __init__(self, fpath_vmg=None, max_message_number:int=10_000_000_000):
        
        self.max_message_number = max_message_number

        if fpath_vmg is None:
            try:
                self.fpath_vmg = sys.argv[1]
            except IndexError:
                raise Exception('A command-line argument(path to VMG file) is required.')
        else:
            self.fpath_vmg = fpath_vmg
        
        # Check if the file exists
        if not os.path.isfile(self.fpath_vmg):
            raise FileNotFoundError(f'File not found: {self.fpath_vmg}')

        self.fname_vmg = os.path.basename(self.fpath_vmg)
        if not self.fname_vmg.endswith('.vmg'):
            raise Exception(f'File name must end with .vmg: {self.fname_vmg}')

        self.count = 0
        self.out_data = ''
        if not os.path.isdir(self.DIR_NAME):
            os.mkdir(self.DIR_NAME)

    def convert(self):
        with open(self.fpath_vmg, mode='r', encoding='utf-8') as file:
            for line in file.readlines():
                if self.count > self.max_message_number:
                    raise Exception(f'Maximum number of messages reached: {self.max_message_number}')
                if 'END:VBODY' in line:
                    count_str = str(self.count)
                    fpath_eml = os.path.join(self.DIR_NAME, f'{os.path.splitext(self.fname_vmg)[0]}_{count_str.zfill(math.ceil(math.log10(self.max_message_number)))}.eml')
                    with open(fpath_eml, mode='w', encoding='utf-8') as f:
                        f.write(self.out_data)
                self.out_data += line
                if 'BEGIN:VBODY' in line:
                    print('\rConvert # %s' % self.count, end='')
                    self.out_data = ''
                    self.count += 1
        print('\nDone.')
