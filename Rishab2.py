import re
from subprocess import Popen, PIPE
from os import path
print ("------------------------to run git commands--------------------------")
git_command = ['git', 'init']
g =['git', 'diff']
git_comm

git_query = Popen(git_command, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status,error) = git_query.communicate()
print(git_status)

git_query1 = Popen(git_command1, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status1,error1) = git_query1.communicate()

git_query2 = Popen(git_command2, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status2,error2) = git_query2.communicate()
print(git_status2)

file=open("rr3.txt",'r+')
file.write(str(git_status2))

regex=re.compile('^-')
regex1=re.compile('^[+][\w]+')

x1= str(git_status2)
mylist = [line.rstrip('\n') for line in file]

old=[]
new=[]
newf=[]

for n in mylist:   
    if re.match(regex, n):
        old.append(n.rstrip())
    else:
        new.append(n.rstrip())

del old[0]
a=len(old)
print ("Values before",old)
for m in new:
    if re.match(regex1, m):
        newf.append(m.rstrip())
b=len(newf)     
print ("Values after",newf)

if len(newf)>len(old):
    for i in range(len(newf)-len(old)):
        old.append(" ")
else:
    for i in range(len(old)-len(newf)):
        newf.append(" ")
z=0.00       

#loop to find changes linewise
for x in range(len(newf)):
    
    if newf[x]==old[x]:
        print ("No change in line",x+1," of this file")
        
    elif old[x]==" ":
        print ((x+1)," is a new line")
        
    elif newf[x]==" ":
        print (x+1,"line is deleted")
        
    else:
        
        z=((float(len(newf[x]))/float(len(old[x])))*100)
        print ("In Line",x+1," (",newf[x],") change is made","with",(z))



print ("======================")
#to find criticality 
for y in range(len(newf)):
    
    z=((len(newf[y])/len(old[y]))*100)
    if z>50:
        print ("line",y+1,"is critical ")
    elif newf[y]==" ":
        print ("line",y+1,"is critical ")
    else:
        print ("line",y+1,"is not critical ") 
    



print ("--------to do--------------------")

if ((b/a)*100) > 50:
    print ("The File is critical")
else:
    print ("The file is not critical it can be pulled successfully")


    
        
    
    
