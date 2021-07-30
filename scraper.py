import json
from urllib.request import urlopen
from bs4 import BeautifulSoup


url_scrape="https://attack.mitre.org/matrices/enterprise/"
request_page=urlopen(url_scrape)
page_html=request_page.read()
request_page.close()

html_soup=BeautifulSoup(page_html,'html.parser')
tactics = html_soup.find('div',class_="overflow-x-auto matrix-scroll-box pb-3")
tactics_title=tactics.find_all('td',class_="tactic name")

tactics_dict={}
for titles in tactics_title:
    name=titles.find('a').text
    dataid=titles.find('a').attrs['title']
    tactics_dict[dataid]=name
#with open('tactics.json', 'w') as fp:
    #json.dump(tactics_dict, fp)
tech_dict=tactics_dict
tech=html_soup.find_all('div',class_="technique-cell")#use super technique cell format to orient based on its format search all instances of technique cell and 
print("TECHNIQUES")                                  #store the ones without dot
pure_tech=[]
for data in tech:
    dataid=data.find('a').attrs['title']
    if '.' not in dataid:
        #make an array to contain each id, then iterate over that
        pure_tech.append(dataid)
#print(pure_tech)
dataA=[]
for ids in pure_tech[0:10]:
    dataA.append(ids)
tech_dict["TA0043"]=dataA
dataB=[]
for ids in pure_tech[10:17]:
    dataB.append(ids)
tech_dict["TA0042"]=dataB
dataC=[]
for ids in pure_tech[17:26]:
    dataC.append(ids)
tech_dict['TA0001']=dataC
dataD=[]
for ids in pure_tech[26:38]:
    dataD.append(ids)
tech_dict['TA0002']=dataD
dataE=[]
for ids in pure_tech[38:57]:
    dataE.append(ids)
tech_dict['TA0003']=dataE
dataF=[]
for ids in pure_tech[57:70]:
    dataF.append(ids)
tech_dict['TA0004']=dataF
dataG=[]
for ids in pure_tech[70:109]:
    dataG.append(ids)
tech_dict['TA0005']=dataG
dataH=[]
for ids in pure_tech[109:124]:
    dataH.append(ids)
tech_dict['TA0006']=dataH
dataI=[]
for ids in pure_tech[124:151]:
    dataI.append(ids)
tech_dict['TA0007']=dataI
dataJ=[]
for ids in pure_tech[151:160]:
    dataJ.append(ids)
tech_dict['TA0008']=dataJ
dataK=[]
for ids in pure_tech[160:177]:
    dataK.append(ids)
tech_dict['TA0009']=dataK
dataL=[]
for ids in pure_tech[177:193]:
    dataL.append(ids)
tech_dict['TA0011']=dataL
dataM=[]
for ids in pure_tech[193:202]:
    dataM.append(ids)
tech_dict['TA0010']=dataM
dataN=[]
for ids in pure_tech[202:215]:
    dataN.append(ids)
tech_dict['TA0040']=dataN

#find . and split for the dict

sub_dict={}
total_dict={}
sub=[]
#find only dots, if the consecutive are same for the first couple make under with first part as key, and append later part as an array
for data in tech:
        name=data.find('a').text
        dataid=data.find('a').attrs['title']
        sub_dict[dataid]=name
        if '.'not in dataid:
                sub.append(dataid)
#print(sub_dict)


countarr=[]
arr=[]
for key in sub_dict:
        arr.append(key[0:5])
final={}
for x in sub:
        final[x]=arr.count(x)

        """if dataid=='T1574':
                final['fix']=0
        if dataid=='T1505':
                final['fix2']=0
        if dataid=='T1548':
                final['fix3']=0
        if dataid=='T1484':
                final['fix4']=0
                final['fix5']=0
                final['fix6']=0
                final['fix7']=0
                final['fix8']=0"""
        


for key in final:
        if final[key]==1:
                final[key]={'.000':''}
        if final[key]==2:
                final[key]={'.000':'','.001':''}
        if final[key]==3:
                final[key]={'.000':'','.001':'','.002':''}
        if final[key]==4:
                final[key]={'.000':'','.001':'','.002':'','.003':''}
        if final[key]==5:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':''}
        if final[key]==6:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':''}
        if final[key]==7:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':''}
        if final[key]==8:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':'','.007':''}
        if final[key]==9:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':'','.007':'','.008':''}
        if final[key]==12:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':'','.007':'','.008':'','.009':'','.010':'','.011':''}
        if final[key]==15:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':'','.007':'','.008':'','.009':'','.010':'','.011':'','.012':'','.013':'','.014':''}
        if final[key]==16:
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.006':'','.007':'','.008':'','.009':'','.010':'','.011':'','.012':'','.013':'','.014':'','.015':''}
        if key=='T1574':
                final[key]={'.000':'','.001':'','.002':'','.004':'','.005':'','.006':'','.007':'','.008':'','.009':'','.010':'','.011':'','.012':''}
        if key=='T1055':
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.008':'','.009':'','.011':'','.012':'','.013':'','.014':''}
        if key=='T1562':
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.006':'','.007':'','.008':''}
        if key=='T1218':
                final[key]={'.000':'','.001':'','.002':'','.003':'','.004':'','.005':'','.007':'','.008':'','.009':'','.010':'','.011':'','.012':''}
#print(final)
#print(arr.count('T1525'))

for key in final:
        for k in final[key]:    
                        if k=='.000':
                                name=key
                        else:
                                name=key + k
                        final[key][k]=sub_dict[name]
                        
with open('subtechniques.json', 'w') as fp:
    json.dump(final, fp)



#or i could the amoundd of times it appears
#iterate through, if the key for the first couple letter are the same, make that the new key and remove it, add .000 if there is not dot.
#check via the format, last few etc

  #simplecounting system? if corresponds add it it in. could work
        #maybe use the tech itself to count and and store
        #itll count the number of times, and then list them, then use the things to add the values


  #simplecounting system? if corresponds add it it in. could work
        #maybe use the tech itself to count and and store
        #itll count the number of times, and then list them, then use the things to add the values
        

                

#use this and string matching to correspond with new array for each one








        
    
    

