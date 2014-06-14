#-*-coding:utf-8 -*-
import os
import sys

if (len(sys.argv) != 3):
    print "Usage: %s testdata_root_directory trainmodel_file" %(sys.argv[0])
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

#读训练出的模型
fp = open(sys.argv[2],'r')
model_values_line=fp.readline().split(' ')
one_f0_value=float(model_values_line[1])
one_engy_value=float(model_values_line[2])

model_values_line=fp.readline().split(' ')
two_f0_value=float(model_values_line[1])
two_engy_value=float(model_values_line[2])

model_values_line=fp.readline().split(' ')
three_f0_value=float(model_values_line[1])
three_engy_value=float(model_values_line[2])

model_values_line=fp.readline().split(' ')
four_f0_value=float(model_values_line[1])
four_engy_value=float(model_values_line[2])

fp.close()

#评分&分类
score1=score2=score3=score4=0
true=false=float(0)
for (k,v) in f0dict.items():
    if k.find("1") != -1:
       score1=(v-one_f0_value)**2+(engydict[k]-one_engy_value)**2
       score2=(v-two_f0_value)**2+(engydict[k]-two_engy_value)**2
       score3=(v-three_f0_value)**2+(engydict[k]-three_engy_value)**2
       score4=(v-four_f0_value)**2+(engydict[k]-four_engy_value)**2
       z=[score1,score2,score3,score4]
       cla=min(z)
       if(cla==score1):
         true=true+1
       else:
         false=false+1
    elif k.find("2") != -1:
       score1=(v-one_f0_value)**2+(engydict[k]-one_engy_value)**2
       score2=(v-two_f0_value)**2+(engydict[k]-two_engy_value)**2
       score3=(v-three_f0_value)**2+(engydict[k]-three_engy_value)**2
       score4=(v-four_f0_value)**2+(engydict[k]-four_engy_value)**2
       z=[score1,score2,score3,score4]
       cla=min(z)
       if(cla==score2):
         true=true+1
       else:
         false=false+1

    elif k.find("3") != -1:
       score1=(v-one_f0_value)**2+(engydict[k]-one_engy_value)**2
       score2=(v-two_f0_value)**2+(engydict[k]-two_engy_value)**2
       score3=(v-three_f0_value)**2+(engydict[k]-three_engy_value)**2
       score4=(v-four_f0_value)**2+(engydict[k]-four_engy_value)**2
       z=[score1,score2,score3,score4]
       cla=min(z)
       if(cla==score3):
         true=true+1
       else:
         false=false+1
    elif k.find("4") != -1:
       score1=(v-one_f0_value)**2+(engydict[k]-one_engy_value)**2
       score2=(v-two_f0_value)**2+(engydict[k]-two_engy_value)**2
       score3=(v-three_f0_value)**2+(engydict[k]-three_engy_value)**2
       score4=(v-four_f0_value)**2+(engydict[k]-four_engy_value)**2
       z=[score1,score2,score3,score4]
       cla=min(z)
       if(cla==score4):
         true=true+1
       else:
         false=false+1

#算分类正确率
print "%s set accuracy: %f" %(sys.argv[1],float(true/(true+false)))


