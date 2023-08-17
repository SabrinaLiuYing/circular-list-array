from linked import*

class Quack:

    def __init__(self):
        """
        Quack() produces a newly constructed empty quack.
        __init__: -> Quack

        """
        self.last = None

    def __repr__(self):
        """
        repr(self) produces a string of the data stored.
        __repr__: Quack -> Str

        """
        return_value = ""
        node = self.last.next()
        while (node != self.last):
            return_value += str(node.access())
            node = node.next()
        if return_value == "":
            return repr(self)
        return return_value
        
        
    def is_empty(self):
        """
        self.is_empty() produces True if self is empty and
            False otherwise.
        is_empty: Quack -> Bool

        """
        if self.last == None:
            return True
        else:
            return False

    def look_up_first(self):
        """
        self.look_up_first() produces the first value in self.
        look_up_first: Quack -> Any
        Requires: self is nonempty
c
        """
        first = self.last.next()
        return first.access()

    def look_up_last(self):
        """
        self.look_up_last() produces the last value in self.
        look_up_last: Quack -> Any
        Requires: self is nonempty

        """
        return self.last.access()

    def add_first(self, value):
        """
        self.add_first(value) adds value to self in first position.
        Effects: Mutates self by adding value in first position.
        add_first: Quack Any -> None

        """
        if self.last == None:
            self.last = Single(value, None)
        elif self.last.next() == None:
            self.last.link(Single(value,self.last))
        else:
            self.last.link(Single(value,self.last.next()))
        
    def add_last(self, value):
        """
        self.add_last(value) adds value to self in last position.
        Effects: Mutates self by adding value in last position.
        add_last: Quack Any -> None

        """
        if self.last == None:
            self.last = Single(value, None)
        elif self.last.next() == None:
            self.last.link(Single(value,self.last))
        else:
            node= self.last.next
            while node.next() != self.last:
                node = node.next()
            node.link(Single(value,self.last))
            self.last.link(node.next())


    def delete_first(self):
        """
        self.delete_first() removes and returns the value in the
            first position.
        Effects: Mutates self by removing item in first position.
        delete_first: Quack -> Any
        Requires: self is nonempty

        """
        if (self.last == None):
            return None        
        return_value = self.last.next()
        if self.last.next() == self.last :
            self.last.link(None)
            return return_value
        self.last.link(self.last.next().next())
        return return_value

    def delete_last(self):
        """
        self.delete_last() removes and returns the value in the
            last position.
        Effects: Mutates self by removing item in last position.
        delete_last: Quack -> Any
        Requires: self is nonempty

        """
        return_value = self.last.access()
        if self.last.access() == None:
            return None
        if self.last.next() == self.last :
            self.last.link(None)
            return return_value
        node = self.last.next()
        while node.next() != self.last:
            node = node.next()
        node.link(self.last.next())
        self.last = node
        return return_value
