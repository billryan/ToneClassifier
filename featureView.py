#-*-coding:utf-8 -*-
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

if (len(sys.argv) != 3):
    print "Usage: %s data_root_directory save_figure_folder" %(sys.argv[0])
    sys.exit(1);
if not (os.path.exists(sys.argv[2])):
    os.makedirs(sys.argv[2])

path = sys.argv[1]
fig_out = sys.argv[2]
f0dict = {}
engydict = {}

f0files = []
# engyfiles = []

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

cnt_one = cnt_two = cnt_three = cnt_four = 0
plt.figure(1)
plt.subplots_adjust(hspace=0.4)
f0_tone_one = plt.subplot(221)
f0_tone_two = plt.subplot(222)
f0_tone_three = plt.subplot(223)
f0_tone_four = plt.subplot(224)
plt.figure(2)
plt.subplots_adjust(hspace=0.4)
engy_tone_one = plt.subplot(221)
engy_tone_two = plt.subplot(222)
engy_tone_three = plt.subplot(223)
engy_tone_four = plt.subplot(224)

#calculate the average value of pitch
for fn in f0files:
    strs = fn.split(".")
    engyfn = strs[0]+".engy"
    feature_f0 = np.loadtxt(fn)
    feature_engy = np.loadtxt(engyfn)

    if(fn.find('/one/') != -1):
        if(cnt_one > 7):
            continue
        else:
            cnt_one = cnt_one + 1
            t = np.arange(len(feature_f0))
            plt.figure(1)
            plt.sca(f0_tone_one)
            plt.plot(t, feature_f0)
            plt.xlabel("Time Slots")
            plt.ylabel("Frequency(Hz)")
            plt.title("F0 of Tone one")
            plt.figure(2)
            plt.sca(engy_tone_one)
            plt.plot(t, feature_engy)
            plt.xlabel("Time Slots")
            plt.ylabel("Energy")
            plt.title("Energy of Tone one")
    if(fn.find('/two/') != -1):
        if(cnt_two > 7):
            continue
        else:
            cnt_two = cnt_two + 1
            t = np.arange(len(feature_f0))
            plt.figure(1)
            plt.sca(f0_tone_two)
            plt.plot(t, feature_f0)
            plt.xlabel("Time Slots")
            plt.ylabel("Frequency(Hz)")
            plt.title("F0 of Tone two")
            plt.figure(2)
            plt.sca(engy_tone_two)
            plt.plot(t, feature_engy)
            plt.xlabel("Time Slots")
            plt.ylabel("Energy")
            plt.title("Energy of Tone two")
    if(fn.find('/three/') != -1):
        if(cnt_three > 7):
            continue
        else:
            cnt_three = cnt_three + 1
            t = np.arange(len(feature_f0))
            plt.figure(1)
            plt.sca(f0_tone_three)
            plt.plot(t, feature_f0)
            plt.xlabel("Time Slots")
            plt.ylabel("Frequency(Hz)")
            plt.title("F0 of Tone three")
            plt.figure(2)
            plt.sca(engy_tone_three)
            plt.plot(t, feature_engy)
            plt.xlabel("Time Slots")
            plt.ylabel("Energy")
            plt.title("Energy of Tone three")
    if(fn.find('/four/') != -1):
        if(cnt_four > 7):
            continue
        else:
            cnt_four = cnt_four + 1
            t = np.arange(len(feature_f0))
            plt.figure(1)
            plt.sca(f0_tone_four)
            plt.plot(t, feature_f0)
            plt.xlabel("Time Slots")
            plt.ylabel("Frequency(Hz)")
            plt.title("F0 of Tone four")
            plt.figure(2)
            plt.sca(engy_tone_four)
            plt.plot(t, feature_engy)
            plt.xlabel("Time Slots")
            plt.ylabel("Energy")
            plt.title("Energy of Tone four")

# plt.savefig(fig_out + '/F0_tone.pdf', bbox_inches='tight')
plt.show()