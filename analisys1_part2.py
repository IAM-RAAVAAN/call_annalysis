# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
file1='test1.csv'
file2='test2.csv'


# %%
import pandas as pd 
import numpy as np 
import csv 
import argparse
import pprint


# %%
df1=pd.read_csv(file1)
df2=pd.read_csv(file2)
import argparse
import pprint

"""arg=argparse.ArgumentParser()
arg.add_argument('--num', help='num')
args=arg.parse_args()
print(args.num)
number_of_calls=int(args.num)"""
number_of_calls=7


# %%
combo=pd.concat([df1,df2])
print('frames concatinated')


# %%
combo[-10:-1]


# %%
combo.columns


# %%
uni=combo['sip.Call-ID'].unique()


# %%
faulty=uni[number_of_calls:]
print('last calls is given  ')


# %%
the=[]
for i in faulty:
    k=combo[combo['sip.Call-ID']==i]
    the.append(k)


# %%
the_all_faulty=pd.concat(the)
print('frame of last calls has been made')


# %%
print(the_all_faulty.shape)


# %%
import subprocess
import os
print('other modules has been imported')

# %%
#os.system('/home/swaraj/Downloads/pcap')


# %%
frame_no=[]
print('makeing the list of frame number')
for i in the_all_faulty['frame.number']:
    i=str(i)
    frame_no.append(i)
print('list of frame number has been made')

# %%
k=" ".join(frame_no)
k=" "+k
k="{"+k+"}"
print('we are firing the tshark might take some time')
subprocess.check_output('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k),shell=True)


# %%



# %%



# %%



# %%



