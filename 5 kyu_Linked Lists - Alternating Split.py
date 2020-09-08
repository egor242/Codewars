class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def push(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


def build_list(data):
    data.reverse()
    head = None
    for num in data:
        head = push(head, num)
    return head


def alternating_split(head):
    current_node = head
    if current_node is None or current_node.next is None:
        raise ValueError
    count = 1
    first = []
    second = []
    while current_node is not None:
        data = current_node.data
        if count % 2 != 0:
            first.append(data)
        else:
            second.append(data)
        current_node = current_node.next
        count += 1
    return Context(build_list(first), build_list(second))




