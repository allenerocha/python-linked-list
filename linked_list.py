"""

@author allen
@version 1.0 - added Node class and LinkedList class
@date May/06/2019

"""


# Nodes of the linked list
class Node:
    # initializer
    def __init__(self, value=None):
        # sets the default value to null if not specified
        self.value = value
        # sets it's next node to null
        self.next = None


# what is called to make the linked list
class LinkedList:
    # initializer
    def __init__(self):
        # sets the default value of this root
        self.root = Node()
        # initializes the size of the linked list
        self.length = 0

    # adds new node to the end of the linked list
    def append(self, value):
        # new node to be added
        new_node = Node(value)
        # sets the current node to the root
        current_node = self.root
        # iterates through the list until the last element is reached
        while current_node.next is not None:
            # iterates to the next node
            current_node = current_node.next
        # replaces the null tail of the last element with the element to be appended
        current_node.next = new_node
        # increments the length of the node by 1
        self.length += 1

    def insert(self, index, value):
        if 0 <= index < self.length:
            # new node to be added
            new_node = Node(value)
            # sets the current node to the root
            current_node = self.root
            # current index
            current_index = 0
            # iterates through the list until the last element is reached
            while current_index in range(self.length):
                # initializes the previous Node
                previous_node = current_node
                # iterates to the next node
                current_node = current_node.next
                # checks to see if we've reached the desired index
                if current_index is index:
                    # sets the next nodes to add to the inserted element
                    successor_node = current_node.next
                    # sets the this node the inserted node
                    previous_node.next = new_node
                    # appends the following nodes to the newly added node
                    new_node.next = successor_node
                    # increments the length of the linked list
                    self.length += 1
                    # since we've inserted the value we wanted to, we break out of the loop and function
                    return
                current_index += 1
        else:
            return False

    def get(self, index):
        # bind acceptable values between [0, self.length)
        if 0 <= index < self.length:
            # current working index
            current_index = 0
            # sets the current node to the root
            current_node = self.root
            # iterates through the loop
            while True:
                # iterates to the next node
                current_node = current_node.next
                # checks to see if we've reached the desired index
                if current_index is index:
                    # since were at the desired index, we return its's value thus terminating the loop
                    return current_node.value
                # increments the current index since we've not reached it
                current_index += 1
        # index is out of bounds
        else:
            # returns False since desired index is out of bounds
            return False

    # removes an element at the index
    def remove_at(self, index):
        # bind acceptable values between [0, self.length)
        if 0 <= index < self.length:
            # current working index
            current_index = 0
            # sets the current node to the root
            current_node = self.root
            # iterates through the loop
            while True:
                # initializes the previous Node
                previous_node = current_node
                # iterates to the next node
                current_node = current_node.next
                # checks to see if we've reached the desired index
                if current_index is index:
                    # this only replaces the node at the index with its successor nodes
                    previous_node.next = current_node.next
                    # decrements the length of the linked list since we've "removed" one node
                    self.length -= 1
                    # since we've deleted the value we want we break out of the loop and function
                    return
                # increments the current index since we've not reached it
                current_index += 1
        # index is out of bounds
        else:
            # returns False since desired index is out of bounds
            return False

    # searches and removes a specific value
    def remove_element(self, element):
        # current working index
        current_index = 0
        # sets the current node to the root
        current_node = self.root
        # iterates through the loop
        while current_index in range(self.length):
            # initializes the previous Node
            previous_node = current_node
            # iterates to the next node
            current_node = current_node.next
            # checks to see if we've reached the desired index
            if element is current_node.value:
                # this only replaces the node at the index with its successor nodes
                previous_node.next = current_node.next
                # decrements the length of the linked list since we've "removed" one node
                self.length -= 1
                # since we've deleted the value we wanted to, we break out of the loop and function
                return
            # increments the current index since we've not reached it
            current_index += 1
        # returns False since desired index is out of bounds
        return False

    # returns the linked list formatted
    def __str__(self):
        # string that is being output
        output = ""
        # sets the current node to the root
        current_node = self.root
        # iterates through the nodes until the last element
        while current_node.next is not None:
            # iterates to the next node
            current_node = current_node.next
            # appends the value of the current node to output formatted
            output += "{} ".format(current_node.value)
        # returns a string version of the linked list with no trailing spaces
        # formatted via index number "0\s1\s2\s3\s...\sn-2\sn-1\sn"
        return output.rstrip()
