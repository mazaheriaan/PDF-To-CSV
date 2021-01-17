#from tabula import read_pdf

#df=read_pdf(r"/home/morteza/Downloads/melli.pdf",multiple_tables=True,encoding='utf-8', spreadsheet=True,pages='۱-130')
#with open(r'/home/morteza//melli.csv','a') as f:
#    for i in range(0,len(df)):
#        df[i].to_csv(f,line_terminator=',', index=False, header=False, encoding='utf-8')

f=open(r'/home/morteza//melli.csv','r')
a=f.read()
f.close()
a=a.split(',,,')
b=''
c=''
for i in range(0,len(a)):
    a[i]=a[i].replace('\n','')
    #for j in range(i,i+13):
    #    c+=a[j]+','

    #c=c.replace('\n','')
    #c=c[:-1]
    b+=a[i]+'\n'
f=open(r'/home/morteza/melli2.csv','w')
f.write(b)
f.close()