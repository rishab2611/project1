 
from subprocess import Popen, PIPE
from os import path

git_command = ['git', 'init']
g =['git', 'diff']
git_command1 = ['git', 'add .']
git_command2 = ['git', 'diff', 'Head^', 'Head']#it is supposed to create a text file
repository  = path.dirname('H:/Users/rishab_parihar/Desktop/e3/')

git_query = Popen(git_command, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status,error) = git_query.communicate()
print(git_status)

git_query1 = Popen(git_command1, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status1,error1) = git_query1.communicate()
print(git_status1)

git_query2 = Popen(git_command2, cwd = repository,stdout=PIPE,stderr=PIPE)
(git_status2,error2) = git_query2.communicate()
print(git_status2)

file=open("rrx.txt",'w')
file.write(str(git_status2))
file.close()
#code to store git_status2 in a file

print ("hllo")
    
    




