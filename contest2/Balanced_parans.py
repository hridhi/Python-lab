
for _ in range(int(input())):
    string=list(input())
    n = len(string) 
    stk = [] 
    
    stk.append(-1) 
    result = 0
    req=[]
    for i in range(n): 
        if string[i] == '(': 
            stk.append(i) 
        elif(string[i]==')'):    
            if len(stk) != 0:
                m=stk.pop()
                req.append(m)
                req.append(i)
            if len(stk) != 0: 
                result = max(result,i - stk[len(stk)-1]) 
             
    req.sort()
    req=list(set(req))
    
    if -1 in req:
        req.remove(-1)
    if len(req)%2!=0:
        req.remove(n-1)
    str=""
    for i in req:
        str+=string[i]
  
    print(result,str)
  







#works for all test cases 

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''


for _ in range(int(input())):
    string=input()
    stack=[]
    stack.append(-1)
    result=0
    previ=0
        
    for i in range(len(string)):
        if string[i] =="(":
            stack.append(i)
            
        elif string[i]==")":
            if(len(stack)!=0):
                stack.pop()
            if len(stack)!=0:
                
                if(result>i-stack[len(stack)-1]):
                    s=prev
                    t=previ
                    prev=result
                    previ=t
                    res=string[s+1:t+1]
                        
                else:
                    s=stack[len(stack)-1]
                    result=i-stack[len(stack)-1]
                    prev=stack[len(stack)-1]
                    previ=i
                    res=string[s+1:i+1]
            else:
                stack.append(i)
    if(result==0):
        res=""
    print(result,res)
             



## other implementation , doesnt work for one case also 

for _ in range(int(input())):
    A=list(input())
    str1 = ""  
    #for ele in test_str:  
       # str1 += ele  
    B = [[ ]] 
    for i in range(len(A) + 1):   
       for j in range(i + 1, len(A) + 1):         
           sub = A[i:j] 
           B.append(sub) 
    #res = [str1[i: j] for i in range(len(str1)) 
     #     for j in range(i + 1, len(str1) + 1)]
    B.remove([])
    B.sort(key = lambda x:len(x))
    #print(B)
    hmax=-1
    strn=""
    
    for i in range(len(B)):
        string= B[i]
        #print(string)
        n=len(string)
        stk=[]
        stk.append(-1) 
  
    # Initialize result 
        result = 0
  
    
        for i in range(n): 
  
        
            if string[i] == '(': 
                stk.append(i) 
            else:    
                if len(stk) != 0: 
                    stk.pop()
                if len(stk) != 0: 
                    result = max(result,  
                                i - stk[len(stk)-1]) 
                    if (hmax<result):
                        ha = ""  
                        print(B[i])
                        for ele in B[i]:  
                            ha += ele   
                        strn=ha
                        hmax=result
        
            
    print(hmax,strn)
    
    


