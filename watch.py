import watchdog.observers
import watchdog.events
import subprocess
import os
import logging

class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self,patterns=['*.pcap'],ignore_patterns=None
        ,ignore_directories=False ,case_sensitive=True)

    def on_created(self,event):
        print(f'file created {event.src_path}')
        s= event.src_path.split('/')[-1]
        print(s)
        cap=s[:s.index('.')]
        os.chdir("/home/karn/Downloads/work_dev/file/call_annalysis/dump")
        print(cap)
        subprocess.check_output(f"tshark -r {cap}.pcap -T fields -e frame.number -e frame.time -e ip.src -e ip.dst -e ip.proto -e sip.Call-ID -e sip.to.tag -e sip.from.tag -Eheader=y -E separator=, -E quote=d -E occurrence=f > {cap}.csv",shell=True)
        print('pcap to csv conversion was success')

event_handler=Handler()
observer=watchdog.observers.Observer()
observer.schedule(event_handler,r"/home/karn/Downloads/work_dev/file/call_annalysis/dump",recursive = False)
observer.start()
observer.join()