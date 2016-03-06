#coding = 'utf-8'
author = "changandao"

import random
import pandas as pd
#from pandas import *

f = open('Training Set/PPD_LogInfo_3_1_Training_Set.csv')
data = f.readlines()
f.close()
data = map(lambda x:x.decode('gbk').strip().split(',')+['train'],data)
LogInfo = pd.DataFrame(data[1:],columns=data[0][:-1]+['flag'])

f = open('Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv')
data = f.readlines()
f.close()
data = map(lambda x:x.decode('gbk').strip().split(',')+['train'],data)
Master = pd.DataFrame(data[1:],columns=data[0][:-1]+['flag'])

f = open('Training Set/PPD_Userupdate_Info_3_1_Training_Set.csv')
data = f.readlines()
f.close()
data = map(lambda x:x.decode('gbk').strip().split(',')+['train'],data)
Userupdate = pd.DataFrame(data[1:],columns=data[0][:-1]+['flag'])

#count = random.randint(1,10)
#rowser = Master.ix(count)
#print type(rowser)
#coulmn =   rowser[u'\u4e00'<= rowser <=u'\u9fa5']
Master = Master.drop(['UserInfo_2','UserInfo_4','UserInfo_7','UserInfo_8','UserInfo_9','UserInfo_19','UserInfo_20'],axis=1)
#print Master[1:5]

Masmin = Master.min()
Masmax = Master.max()
Masmwan = Master.mean()
Masstd = Master.std()
print Masmin,Masstd
fout = open('Output/out.txt','w')