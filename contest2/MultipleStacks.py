class TwoStack():
    def __init__(self,size):
        self.stack = [None]*size
        #@start-editable@
        self.size=size
        self.top1=-1
        self.top2=self.size
	    #@end-editable@

    # define the push operation which  pushes the value into the stack1, must throw a stack full exception
    def push1(self, value):
        #@start-editable@
        if self.top1<self.top2-1:
            self.top1+=1
            self.stack[self.top1]=value
        else:
            print("StackFullException") 
            exit(1) 
	    #@end-editable@

    def push2(self, value):
        #@start-editable@
        if self.top1 < self.top2 - 1: 
            self.top2 = self.top2 - 1
            self.stack[self.top2] = value
        else : 
            print("StackFullException") 
            exit(1) 
	    #@end-editable@

    # returns top element of stack if not empty, else throws stack empty exception
    def pop1(self):
    
        #@start-editable@
        if self.top1 >= 0: 
            x = self.stack[self.top1] 
            self.stack[self.top1]=None
            self.top1 = self.top1 -1
            return x 
        else: 
            print("StackEmptyException") 
            exit(1)
	    #@end-editable@
        return 
        
        
    # returns top element without removing it if the stack is not empty, else throws exception   
    def pop2(self):
        #@start-editable@
        if self.top2 < self.size: 
            x = self.stack[self.top2] 
            self.stack[self.top2]=None
            self.top2 = self.top2 + 1
            return x 
        else: 
            print("StackEmptyException") 
            exit(1)
	    #@end-editable@
        return
        


    # returns the number of elements currently in stack2 
    def size1(self):
        #@start-editable@
        return self.top1+1
	    #@end-editable@

    # returns the number of elements currently in stack2 
    def size2(self):
        #@start-editable@
        return self.size-self.top2
	    #@end-editable@

    def printStacks(self):
        for i in range(self.size):
            print(self.stack[i],end=" ")
        print()
        return

# Driver code.---------------------------------------------

def teststacks():
    stacksize=int(input())
    st1 = TwoStack(stacksize)
    inputs=int(input())
    while inputs>0:
        command=input()
        operation=command.split()
        if(operation[0]=="S1"):
            print(st1.size1())
        elif(operation[0]=="S2"):
            print(st1.size2())
        elif(operation[0]=="P1"):
            st1.push1(int(operation[1]))
            st1.printStacks()
        elif(operation[0]=="P2"):
            st1.push2(int(operation[1]))
            st1.printStacks()
        elif(operation[0]=="O1"):
            print(st1.pop1())
            st1.printStacks()
        elif(operation[0]=="O2"):
            print(st1.pop2())
            st1.printStacks()
        inputs-=1


def main():
    teststacks()

if __name__ == '__main__':
    main()
