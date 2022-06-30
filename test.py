from pydub import AudioSegment
from pydub.utils import make_chunks
import os
import json
import time
import threading
print("[*] Deleting Cache...")
os.system("rm  output/*.*")
print("[*] Done!")
path="output/"
file_path="psybient.mp3"
names=[]
trackss={}
commands_base="songrec audio-file-to-recognized-song "
print("[*] Spliting Music...")
local_time = time.strftime("%Y-%m-%d_%H%M%S", time.localtime())
log_name=file_path+"_"+local_time+".log"
log_name_full=file_path+"_"+local_time+"_full"+".log"
logs=open(log_name,"w")
logs_full=open(log_name_full,"w")
def get_music_name(commands):
    try:
        StartTime=time.time()
        result=os.popen(commands)
        results=result.read()
        data = json.loads(results)
        name=data["track"]["title"]
        artist=data["track"]["subtitle"]
        url=data["track"]["url"]
        info=[StartTime,name,artist,url,1]
        if name in trackss:
            trackss[name][4]=trackss[name][4]+1
        else:
            trackss[name]=info
    except:
        pass
try:
	os.makedirs("output")
except:
	pass
audio = AudioSegment.from_file(file_path)
size = 30000  #切割的毫秒数 10s=10000
chunks = make_chunks(audio, size)  #将文件切割为10s一块
def chunk_out(chunk_name):
    chunk.export(chunk_name, format="mp3")
total_file=len(chunks)
for i, chunk in enumerate(chunks):
    if(len(str(i))==1):
        name_startwith="000"+str(i)
    if(len(str(i))==2):
        name_startwith="00"+str(i)
    if(len(str(i))==3):
        name_startwith="0"+str(i)
    if(len(str(i))==4):
        name_startwith=str(i)
    chunk_name = "output/{0}.dianshiju.mp3".format(name_startwith)
    while(len(threading.enumerate())>=32):
            time.sleep(1)
    threading.Thread(target=chunk_out,args=(chunk_name,),name=chunk_name).start()
    print("\r[*]",round((int(i)/total_file)*100,1),"%",end="")
    #print(chunk_name)
    
while(len(threading.enumerate())>=2):
            time.sleep(1)
print()
print("[*] Done!")
print("[*] Recognizing.....")
print("")
for root, dirs, files in os.walk(path):
    names=files
total=len(names)
count=1
for i in names:
    realpath=path+i
    commands=commands_base+realpath
    try:
        #get_music_name(commands)
        while(len(threading.enumerate())>=32):
            time.sleep(1)
        threading.Thread(target=get_music_name,args=(commands,),name=str(i)).start()
        print("\r[*]",round((count/total)*100,1),"%",end="")
    except Exception as e:
        pass
    count=count+1
print("\n[*] Please Waite......")
while(1):
    if(len(threading.enumerate())<=1):
        break
print("[*] Done")
print("[*] Results:")
for i in trackss:
    text=str(trackss[i][2])+"-"+str(trackss[i][1])+"\t"+str(trackss[i][3])+"\t"+str(trackss[i][4])
    if(trackss[i][4]>=2):
        logs.write(text+"\n")
        print(text)
    logs_full.write(text+"\n")
logs.close()
logs_full.close()
