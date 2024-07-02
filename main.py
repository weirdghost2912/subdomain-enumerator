import requests
domain=input('Enter domain:  ')
wd=input('Enter wordlist:  ')
with open(wd,'r') as f:
    file=f.read()

def each_req(i,domain):
    r=requests.get(i+'.'+domain)
    if r.status_code==200:
        dict
def enum_req():
    for i in file:
        each_req(i,domain)







