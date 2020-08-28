class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(l1: ListNode, l2: ListNode):
    if l1 == None and l2 == None:
        return
    newlist = []
            
    node1 = l1
            
    while node1:
        newlist.append(node1.val)
        node1 = node1.next
        node2 = l2
        while node2:
            newlist.append(node2.val)
            node2 = node2.next
        newlist.sort()
        
        cur_node = ListNode(newlist[0])
        head = cur_node
        for i, n in enumerate(newlist):
            if i > 0:
                cur_node.next = ListNode(n)
                cur_node = cur_node.next
        return head