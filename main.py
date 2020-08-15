l = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", 
"1.1.1", "2.0"]
rev=[]
major=[]
minor=[]
final=[]
working=[]
solution=[]
string1=""
string2=""
string3=""
#l.sort()
#print(','.join(map(str,l)))
for x in l:
    #working.append(x.split(".")) 
    #print(x.split("."))
    if(x.count('.'))==2:
       rev.append(list(map(int, x.split("."))))
    elif(x.count('.'))==1:
       minor.append(list(map(int, x.split("."))))
    elif(x.count('.'))==0:
       major.append(list(map(int, x.split("."))))
    #else
        #return("this is wrong")
rev.sort(key = lambda x: x[2])
#print(rev)
rev.sort(key = lambda x: x[1])
#print(rev)
rev.sort(key = lambda x: x[0])
#print(rev)
minor.sort(key = lambda x: x[1])
minor.sort(key = lambda x: x[0])
for x in minor:
    working.append(x)
for x in rev:
    working.append(x)
working.sort(key = lambda x: x[1])
working.sort(key = lambda x: x[0])
#print(working)
#major.sort(key = lambda x: x[0])
for x in major:
    final.append(x)
for x in working:
    final.append(x)
final.sort(key = lambda x: x[0])
#print(solution)
for ele in final:
    #print(ele)
    #print(len(ele))
    #print(ele)
    if len(ele)==1:
        for i in ele:
            #print(i)
            ele=str(i)
        #print(ele)
            #print(i,ele,'this is 1i')
    elif len(ele)==2:
        count = 0
        #print(ele,'thisis 2ele')
        for i in ele:
            #print(i,ele, 'this is 2i')
            if count==0:
                string1=str(i)
            elif count ==1:
                string2=str(i)
            count+=1
            #print(string1,'this is 2i string1')
            #print(string2,'this is 2i string2')
        ele=string1+'.'+string2
        #print(ele)
    elif len(ele)==3:
        count=0
        #print(ele,'this is 3eke')
        for i in ele:
            if count==0:
                string1=str(i)
            elif count ==1:
                string2=str(i)
            elif count==2:
                string3=str(i)
            count+=1
        ele=string1+'.'+string2+'.'+string3
    solution.append(ele)
    
        #print(ele)

            #print(i,ele,'this is 3i')
    #else:
        #return("this is wrong")
    #print(''.join(str(ele)))
    #ele=str(ele)
    #ele=(ele.replace('[', ''))
    #ele=(ele.replace(']', ''))
    #ele=(ele.replace('[', ''))
    #ele=(ele.replace(', ', '.'))
    #print(ele)
    #solution[count]=ele
    #count+=1
        #for x in ele:
        #if (x == '[' or x ==',' or x == ']'):
            #ele.remove(x)
        #solution.append(x)
        #print(solution)
        
        #ele = ['.'.join(solution)]
        #print(ele)
        #print('.'.join(x))
    #print(final)
    #print final[i]
    #solution.append('.'.join(str(i)))
    #print(solution)
    #for ele in final:
        #solution[i]=".".join(str(ele))
        #print(ele)
#for i in range(len(final)):
    #print i
    #print final[i]
    #solution.append('.'.join(str(final[i])))
    #print(solution)
    #for ele in final:
        #solution[i]=".".join(str(ele))
        #print(ele)
#print(','.join(solution))       
#print(solution)
#print(final)
        
#print(solution)
#for x in major:
    #final.append(x)
#for x in minor:
    #final.append(x)
#final.sort(key=lambda x:x[0])
#for x in rev:
    #final.append(x)

#final.sort(key = lambda x: x[0])
#working.sort()
#rev.sort()
#minor.sort()
#major.sort()
#final.append(rev)
#final.append(minor)
#final.sort()
#print(rev)
#print(minor)
#print(major)
#print(final)
#print(working)
#print(x.count('.'))
print((",".join(solution)))