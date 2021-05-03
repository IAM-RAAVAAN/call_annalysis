file1='test1.csv'
file2='test2.csv'


#file2='home/karn/Downloads/work_dev/file/call_annalysis/test2.csv'

import pandas as pd 
import numpy as np 
import csv 
import argparse
import pprint
import timeit

df1=pd.read_csv(file1)
df2=pd.read_csv(file2)

#print(df1)
combo=pd.concat([df1,df2])

arg=argparse.ArgumentParser()
arg.add_argument('--i', help='num')
args=arg.parse_args()
print(args.i)



"""number_of_calls=-10
#combo[-10:-1]
uni=combo['sip.Call-ID'].unique()
faulty=uni[number_of_calls:]
print('last calls is given  ')
#print(faulty)"""

k=combo[combo['sip.Call-ID']==args.i]


#print(the)



import subprocess
import os




"""for i in the_all_faulty['frame.number']:
    i=str(i)
    frame_no.append(i)
print('list of frame number has been made')"""

#k=combo[combo['sip.Call-ID']==args.id]
j=[]
for i in k['frame.number']:
        i=str(i)
        j.append(i)
print('list of frame number has been made')


k=" ".join(j)
k=" "+k
k="{"+k+"}"
print('we are firing the tshark might take some time')
subprocess.check_output('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k),shell=True)
