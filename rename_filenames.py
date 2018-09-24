# coding: utf-8
from pathlib import Path
import sys
nifti_dir = sys.argv[1]
suffixes = ['.nii','.json','.bval','.bvec']
if not nifti_dir:
	nifti_dir = 'dcm2niix_head'

for f in [x for x in Path(nifti_dir).glob('*') if x.suffix in suffixes]:
    filenum = f.stem.split('_')[-1]
    fname = '{:04d}'.format(int(filenum))  + '_' + f.name.replace('(','_').replace(')','_').replace('=','_')
    dest  = Path(nifti_dir) /  fname 
    print(dest)
    f.rename(dest)
