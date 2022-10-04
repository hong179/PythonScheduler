import ssl
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import requests
import urllib.request

opener = urllib.request.build_opener()

# 输出时间
def job():
    try:
        opener.open("https://www.gxlcms.com/python-362621.html")
      
    except ssl.SSLCertVerificationError:
        print("ERROR!!!")
        exec(open('EmailSend.py').read())
    except urllib.error.URLError:
        print("URL IS DOWN!!!")
        exec(open('EmailSend.py').read())
    except Exception as e:
        print("DOESN'T WORK!!!",e)
        exec(open('EmailSend.py').read())

    url = 'https://www.gxlcms.com/python-362621.html'   
    data = requests.get(url)
    code = data.status_code
    if(code == 200):
        print('当前时间：' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '状态码：')
        print(code)
    else:
        print("HSCN IS DOWN!!!")
        exec(open('EmailSend.py').read())

sched = BlockingScheduler()
sched.add_job(job, "interval", minutes=3)
sched.start()