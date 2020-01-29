from queue import Queue
def reversequeue(queue): 
    Stack = []  
    while (not queue.empty()):  
        Stack.append(queue.queue[0])  
        queue.get() 
    while (len(Stack) != 0):  
        queue.put(Stack[-1])  
        Stack.pop() 
q=Queue()
q.put('5')
q.put('6')
q.put('7')
q.put('8')
q.put('9')
q.put('10')
q.put('11')
q.put('12')
reversequeue(q)
while(not q.empty()):
    print(q.get(),end=" ")
