'''
months_Dq = collections.deque([ 'Mar’, ‘April’, ‘May’])
A.	Append ‘June’, ‘July’, ‘Aug’ to the right side of the deque. Display the updated deque.
B.	Append ‘Dec’, ‘Jan’, ‘Feb’ to the left side of the deque. Display the updated deque.
C.	Remove first item in the deque, then display the updated deque.
D.	Remove last item in the deque, then display the updated deque.
E.	Remove ‘June’ from the deque, then display the updated deque.
'''
import collections
months_Dq = collections.deque(['Mar', 'Apr', 'May'])

months_Dq.append('June')
months_Dq.append('July')
months_Dq.append('Aug')
print(months_Dq)

months_Dq.appendleft('Dec')
months_Dq.appendleft('Jan')
months_Dq.appendleft('Feb')
print(months_Dq)

#remove/pop the furthest left item in deque
months_Dq.pop()
print(months_Dq)
months_Dq.popleft()
print(months_Dq)

months_Dq.remove('June')
print(months_Dq)