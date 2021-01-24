def main():
    l1 = list(map(int,input().strip().split()))
    l2= list(map(int,input().strip().split()))
    n=int(input())
    for _ in range(n):
        op=input()
        ans=DoOp(l1,l2,op)
        print(' '.join(map(str, ans)))  
        
def DoOp(l1,l2,op):
    l3=[]
    if op=="I":
         n=list(set(l1) & set(l2))
         n.sort()
         return(n)
    if op=="D":
         n=list(set(l2)-set(l1))
         n.sort()
         return(n)
    if op=="B":
        for i in l1:
            if i in l2:
                l2.remove(i)
        l2.sort()
        return(l2)
                    
                    
if __name__=="__main__":
    main()
