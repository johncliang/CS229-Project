import time

import numpy as np
## import libaries
from numpy import arange, cos, pi


#import scipy.interpolate
import os.path


#from scipy import interpolate
import operator
from numpy.linalg import inv

from numpy import linalg as LA
import glob, os
import os.path
import gc
import itertools

from tempfile import TemporaryFile
import numpy.random as rnd
import itertools



FolderName='/farmshare/user_data/jliu99/data'
jobName = 'refined_regression_graph'

with open(jobName+'.sbatch', 'w') as file:
	file.write(str('#!/bin/bash'+'\n'))
	file.write(str('#'+'\n'))
	file.write(str('#SBATCH --job-name='+jobName+'\n' ) )
	file.write(str('#'+'\n'))
	file.write(str('#SBATCH --time=40:00:00'+'\n'))
	file.write(str('#SBATCH --ntasks=1'+'\n'))
	file.write(str('#SBATCH --cpus-per-task=1'+'\n'))
	file.write(str('#SBATCH --mem-per-cpu=4G'+'\n'))
	file.write(str('#SBATCH -p normal'+'\n')) 
	file.write(str('#'+'\n'))

       # file.write(str('module load python/2.7.13'+'\n'))
       # file.write(str('module load labs poldrack anaconda/5.0.0-py36'+'\n'))
       # file.write(str('module load anaconda'+'\n'))
       # file.write(str('module load py-numpy/1.14.3_py27 py-scipy/1.1.0_py27'+'\n'))

	file.write(str('conda activate deepchem'+'\n'))
	file.write(str('srun python sims_pred_graph.py'+'\n'))
	file.write(str('conda deactivate'+'\n'))
	print("Submitted")

# submit jobscript to cluster
os.system("sbatch "+jobName+'.sbatch')
# mark jobscript as 'submitted'
os.system("mv "+jobName+'.sbatch '+jobName+'.sbatch_sub')
os.system("cp "+jobName+'.sbatch_sub '+FolderName+'/'+jobName+'.sbatch_sub ')
os.system("rm "+jobName+'.sbatch_sub')
