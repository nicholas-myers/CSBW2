# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # put the nums in the right order
    cur_num1 = l1
    num1_str = ""
    while cur_num1 != None:
        num1_str = str(cur_num1.val) + num1_str
        cur_num1 = cur_num1.next
        
    cur_num2 = l2
    num2_str = ""
    while cur_num2 != None:
        num2_str = str(cur_num2.val) + num2_str
        cur_num2 = cur_num2.next

    # get the sum
    summation = int(num1_str) + int(num2_str)
    sum_str = str(summation)
    # put the sum in reverse order
    reverse_sum = ""
    for n in sum_str:
        reverse_sum = n + reverse_sum
    # return the digits as a Linked list
    sum_node = ListNode(int(reverse_sum[0]))
    cur_node = sum_node
    for i, c in enumerate(reverse_sum):
        if i > 0:
            cur_node.next = ListNode(int(c))
            cur_node = cur_node.next

    return sum_node
        

node1 = ListNode(2)
node1.next = ListNode(4)
node1.next.next = ListNode(3)
node2 = ListNode(5)
node2.next = ListNode(6)
node2.next.next = ListNode(4)


addTwoNumbers(node1, node2)