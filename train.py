#-*-coding:utf-8 -*-
import os
import sys

if (len(sys.argv) != 3):
    print "Usage: %s data_root_directory savemodel_file" %(sys.argv[0])
    sys.exit(1);

path = sys.argv[1]
f0dict = {}
engydict = {}

f0files = []
# engyfiles = []

#获取目录下所有f0文件
def get_recursive_file_list(path):
    current_files = os.listdir(path)
    for file_name in current_files:
        full_file_name = os.path.join(path, file_name)
        
        if  os.path.isdir(full_file_name):
            get_recursive_file_list(full_file_name)
        elif file_name.find('.f0') != -1:
            f0files.append(full_file_name)
 
    return 0

#调用函数，获取所有f0文件
get_recursive_file_list(path)

#对于每种音节和音调，统计其均值
for fn in f0files:
    strs = fn.split(".")
    engyfn = strs[0]+".engy"
    fp = open(fn, 'r')
    efp = open(engyfn, 'r')
    engy = f0 = n = 0
    filename = os.path.basename(fn)
    strs = filename.split(".")
    filename = strs[0]
#     print filename
    ss = fp.readline()
    ess = efp.readline()
    while ss:
        ss = ss[0:len(ss)-1]
        #print ss
        if abs(float(ss)) > 1E-6:
            f0 += float(ss)
            engy += float(ess)
            n = n+1
        if (n != 0):
            f0dict[filename] = f0/n
            engydict[filename] = engy/n
            
        ss = fp.readline()
        ess = efp.readline()
        
    fp.close()
    efp.close()

#统计每个目录对应的音调
onef0 = twof0 = threef0 = fourf0 = 0
onegy = twogy = threegy = fourgy = 0
n1 = n2 = n3 = n4 = 0

for (k,v) in f0dict.items():
    if k.find("1") != -1:
        onef0 += v
        onegy += engydict[k]
        n1 = n1+1
    elif k.find("2") != -1:
        twof0 += v
        twogy += engydict[k]
        n2 = n2+1
    elif k.find("3") != -1:
        threef0 += v
        threegy += engydict[k]
        n3 = n3+1
    elif k.find("4") != -1:
        fourf0 += v
        fourgy += engydict[k]
        n4 = n4+1
fp =open(sys.argv[2],'w')
fp.write("one: %f %f\n" %(onef0/n1, onegy/n1))        
fp.write("two: %f %f\n" %(twof0/n2, twogy/n2))
fp.write("three: %f %f\n" %(threef0/n3, threegy/n3))
fp.write("four: %f %f\n" %(fourf0/n4, fourgy/n4))
fp.close()
print "one: %f %f" %(onef0/n1, onegy/n1)
print "two: %f %f" %(twof0/n2, twogy/n2)
print "three: %f %f" %(threef0/n3, threegy/n3)
print "four: %f %f" %(fourf0/n4, fourgy/n4)
    


