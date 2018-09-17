# coding: utf-8
from pathlib import Path
for f in Path('nifti_dir').glob('*'):
    filenum = f.stem.split('_')[-1]
    fname = '{:04d}'.format(int(filenum))  + '_' + f.name.replace('(','_').replace(')','_').replace('=','_')
    dest  = Path('nifti_dir') /  fname 
    print(dest)
    f.rename(dest)
