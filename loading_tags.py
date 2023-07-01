import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re
with open("data/file.html","r") as f:
        html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')

sk={"codes_trending":[]}

codes = soup.find_all('div',attrs={'class':'d-flex jc-space-between ai-center mb12'})
sl = []
def append_data(codes):
    for i in codes:
        sl.append(i.text)

jk = []
def remove_spaces(sl):
    for i in sl:
        jk.append(re.sub('\n','',i))
    
sk["codes_trending"] = jk

def get_csv_ready(sk):
    df=pd.DataFrame(sk)
    df.to_csv("tags_data.csv",mode='w',index=False)

def main():
    append_data(codes)
    remove_spaces(sl)
    get_csv_ready(sk)

if '__name__' == '__main__':
    try:
        main()
    except Exception as e:
        print("Inside main")
        print("The error is :",e)
    finally:
        print("Execution completed")

