import requests
domain=input('Enter domain:  ')
wd=input('Enter wordlist:  ')
with open(wd,'r') as f:
    file=f.read()

def each_req(i,domain):
    r=requests.get('https://'+i+'.'+domain)
    if r.status_code==200:
        print(i+'.'+domain+'  active')

for i in file.split():
    each_req(i,domain)
