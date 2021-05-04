file1='test1.csv'
file2='test2.csv'


#file2='home/karn/Downloads/work_dev/file/call_annalysis/test2.csv'

import pandas as pd 
import numpy as np 
import csv 
import argparse
import pprint
import timeit
import subprocess
import os
import re

#df1=pd.read_csv(file1)
df=pd.read_csv(r'/home/karn/Downloads/work_dev/file/call_annalysis/dump/TRACES_20210224150613.csv')


#print(df1)
combo=df


import argparse
import pprint

arg=argparse.ArgumentParser()
arg.add_argument('--num', help='num')
arg.add_argument('--id', help='num')
arg.add_argument('--fc', help='num')
args=arg.parse_args()
print(args.num)
os.chdir('/home/karn/Downloads/work_dev/file/call_annalysis/dump')

def find_alice(i):
        alice=df[df['sip.to.tag'].str.match(pat = i+'\S*', na=False)]
        j=alice['sip.Call-ID'].unique()
        for i in j:
            pass
        full_alice=df[df['sip.Call-ID']==i]
        return full_alice
        #return df[df['sip.to.tag'].str.match(pat = i+'\S*', na=False)]
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



#number_of_calls=int(input("enter the number of calls you want "))
#number_of_calls=-10
#combo[-10:-1]
if args.num:
    uni=combo['sip.Call-ID'].unique()
    number_of_calls=-int(args.num)
    faulty=uni[number_of_calls:]
    print('last calls is given  ')
    print(faulty)

    the=[]
    for i in faulty:
        k=combo[combo['sip.Call-ID']==i]
        the.append(k)

    #print(the)


    the_all_faulty=pd.concat(the)
    print('frame of last calls has been made')
    print(the_all_faulty.shape)
    print(the_all_faulty)


    print('other modules has been imported')
    frame_no=[]
    print('makeing the list of frame number')


    for i in the_all_faulty['frame.number']:
        i=str(i)
        frame_no.append(i)
    print('list of frame number has been made')


    frame_list=" ".join(frame_no)
    frame_list=" "+frame_list
    frame_list="{"+frame_list+"}"
    print('we are firing the tshark might take some time')
    start=timeit.timeit()
    subprocess.check_output('tshark -r TRACES_20210224150613.pcap -Y "frame.number in {}" -w new.pcap'.format(frame_list),shell=True)
    end==timeit.timeit()
    print(start-end)
#TODO ==== limit frame no to 100 and same calls in one pcap

if args.id:
     k=combo[combo['sip.Call-ID']==args.id]
     j=[]
     print(k)
     for i in k['frame.number']:
        i=str(i)
        j.append(i)
     


     k=" ".join(j)
     k=" "+k
     k="{"+k+"}"
     #tshark -r TRACES_20210224150613.pcap -Y "sip.Call-ID == 579ec0b9-5649ac17-36b6-7f25836d7058-ddf11f59-13c4-7225 "
     print('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k))
     subprocess.check_output('tshark -r TRACES_20210224150613.pcap -Y "frame.number in {}" -w new.pcap'.format(k),shell=True)

if args.fc:
        
    call_id=df[df['sip.Call-ID']==args.fc]

    k=[]
    #we need to make datframe of all the row with same sip.call-id
    for i in call_id['sip.Call-ID']:
        k.append(i)
    #here passing the last sip.call_id as first might not contain the from tag
    #who_called will return list of len 2 where l[0] contains who called and second index represent its tag
    tag=who_called(i)
    print(tag)
    if tag[0] == 'bob':
        #find_alice and find_bob returns dataframe 
        df=find_alice(tag[1])

    else :
        #print(tag)
        df=find_bob(tag[1])


    combo=pd.concat([df,call_id])
    combo

    j=[]
    for i in combo['frame.number']:
            i=str(i)
            j.append(i)
        
    sip.Call-ID


    k=" ".join(j)
    k=" "+k
    k="{"+k+"}"
    print(os.getcwd())
    os.chdir('/home/karn/Downloads/work_dev/file/call_annalysis/dump')
    #
    print('tshark -r TRACES_20210323140137.pcap -Y "frame.number in {}" -w new.pcap'.format(k))
    start=timeit.timeit()
    subprocess.check_output('tshark -r TRACES_20210224150613.pcap -Y "sip in {}" -w new.pcap'.format(k),shell=True)
    end=timeit.timeit()
    print(end-start)