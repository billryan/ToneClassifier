#-*-coding:utf-8 -*-
import os
import sys
import numpy as np

if (len(sys.argv) != 2):
    print "Usage: %s data_root_directory" %(sys.argv[0])
    sys.exit(1);

path = sys.argv[1]
if (path[-1] == '/'):
    dataset_new = path[:-1] + '_ops'
else:
    dataset_new = path + '_pos'

if not (os.path.exists(dataset_new)):
    os.makedirs(dataset_new)

f0dict = {}
engydict = {}

f0files = []
# engyfiles = []

def get_max_interval_nonzero(np_ndarray):
    pos_index = []
    indices = np.where(np_ndarray > 0)
    if (indices[0][-1]-indices[0][0]+1 == len(indices[0])):
        return indices
    elif (indices[0][-1]-indices[0][0]+1 < len(indices[0])):
        return -1
    else:
        for i in xrange(indices[0][0], indices[0][-1]+1):
            pos_index.append(i)
    return pos_index

#get the f0 file recursively
def get_recursive_file_list(path):
    current_files = os.listdir(path)
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        
        if  os.path.isdir(full_file_name):
            get_recursive_file_list(full_file_name)
        elif file_name.find('.f0') != -1:
            f0files.append(full_file_name)
 
    return 0

#
get_recursive_file_list(path)

# moving average filter
window = 3
maf = []
for i in xrange(window):
    maf.append(1.0/window)

# max interval non-zero
inter_nonzero = []
#calculate the average value of pitch
for fn in f0files:
    strs = fn.split(".")
    engyfn = strs[0]+".engy"
    feature_f0 = np.loadtxt(fn)
    feature_f0 = np.convolve(feature_f0, maf, 'same')
    feature_engy = np.loadtxt(engyfn)
    feature_engy = np.convolve(feature_engy, maf, 'same')

    pos_index = get_max_interval_nonzero(feature_f0)
    feature_f0_new = np.take(feature_f0, pos_index)
    feature_engy_new = np.take(feature_engy, pos_index)

    dirs = fn.split('/')
    dataset_newdir = dataset_new+'/'+dirs[-2]+'/'
    if not (os.path.exists(dataset_newdir)):
        os.makedirs(dataset_newdir)
    np.savetxt(dataset_newdir+os.path.basename(fn),feature_f0_new, delimiter='\n',fmt='%s')
    np.savetxt(dataset_newdir+os.path.basename(fn).replace('f0','engy'),feature_engy_new, delimiter='\n',fmt='%s')
