class list_node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def append(self, val):
        current = self
        while current.next:
            current = current.next
        current.next = list_node(val)


l1 = list_node(1)
l2 = list_node(1)
for i in range(2, 10):
    l1.append(i)
    l2.append(i)
s = list_node(None)
head = s
while l2 and l1:
    if l1.val <= l2.val:
        head.next = l1
        l1 = l1.next
    else:
        head.next = l2
        l2 = l2.next
    head = head.next
head.next = l1 or l2
