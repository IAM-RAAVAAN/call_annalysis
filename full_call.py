import pandas as pd
import numpy as np 
import csv 
import os
import subprocess
import argparse
import re 

arg=argparse.ArgumentParser()
arg.add_argument('--fc', help='num')

args=arg.parse_args()
print(args.fc)



df=pd.read_csv(r'/home/karn/Downloads/work_dev/file/call_annalysis/dump/TRACES_20210323140137.csv')
df.reset_index(drop=True)

call_id=df[df['sip.Call-ID']==args.fc]
call_id

def find_alice(i):
    return df[df['sip.to.tag'].str.match(pat = i+'\S*', na=False)]
def find_bob(i):
    return df[df['sip.from.tag'].str.match(pat = i+'\S*', na=False)]


def sbc_call(i):
    i=str(i)
    l=[]
    matched = re.match("s\d\d\d\d\dd", i)
    l.append(bool(matched))
    tag = re.compile(r"s\d\d\d\d\dd")
    try:
        mo = tag.search(i)
        l.append(mo.group())
    except:
        pass
    return l


def who_called(i):
    k=[]

    #fing=ding whether the alice called 
    for i in call_id['sip.to.tag']:
        k.append(i)

    l=sbc_call(i)#sbc will return list l[0]=is true or false  and his snnnnnd number 
    if l[0]:
        l[0]='alice'
        return l
    #finding whether bob called 
    for i in call_id['sip.from.tag']:
        k.append(i)
    l=sbc_call(i)
    if l[0]:
        l[0]='bob'
        return l


k=[]
#we need to make datframe of all the row with same sip.call-id
for i in call_id['sip.Call-ID']:
    k.append(i)
#here passing the last sip.call_id as first might not contain the from tag
#who_called will return list of len 2 where l[0] contains who called and second index represent its tag
tag=who_called(i)
if tag[0] == 'bob':
    #find_alice and find_bob returns dataframe 
    print(find_alice(tag[1]))

else :
    print(tag)
    df=find_bob(tag[1])


combo=pd.concat([df,call_id])
combo

j=[]
for i in combo['frame.number']:
        i=str(i)
        j.append(i)
     


k=" ".join(j)
k=" "+k
k="{"+k+"}"
print(os.getcwd())
os.chdir('/home/karn/Downloads/work_dev/file/call_annalysis/dump')
     
print('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k))
subprocess.check_output('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k),shell=True)
