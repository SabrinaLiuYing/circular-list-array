from contiguous import*

class Quack:

    def __init__(self):
        """
        Quack() produces a newly constructed empty quack that 
        has the size 10 and initialize two variable to none.
        Effects: Creates a new empty contiguous array
        __init__: -> Quack

        """
        self.con = Contiguous(10)
        self.first = None
        self.last = None

    def __repr__(self):
        """
        repr(self) produces a string of the data stored.
        __repr__: Quack -> Str

        """
        return repr(self)

    def is_empty(self):
        """
        self.is_empty() produces True if self is empty and
            False otherwise.
        is_empty: Quack -> Bool

        """
        if self.first == None:
            return True
        else:
            return False

    def look_up_first(self):
        """
        self.look_up_first() produces the first value in self.
        look_up_first: Quack -> Any
        Requires: self is nonempty

        """
        return self.first

    def look_up_last(self):
        """
        self.look_up_last() produces the last value in self.
        look_up_last: Quack -> Any
        Requires: self is nonempty

        """
        return self.last

    def add_first(self, value):
        """
        self.add_first(value) adds value to self in first position,
        and change two variables if needed.
        Effects: Mutates self by adding value in first position.
        add_first: Quack Any -> None

        """
        # i is for loop
        i = 0
        # next_data is the data that we need to pass to the next slot
        next_data = self.con.access(i)

        # the loop will break if the original next slot is empty
        while(next_data != None):
            # index is the data in the next slot
            index = self.con.access(i+1)
            # change the next slot to store the next_data
            self.con.store(i + 1, next_data)
            # change the value of next_data to original data in next slot 
            next_data = index
            i += 1
        
        # store the first value    
        self.con.store(0, value)
        # change self.first to value, and self.last if the self is empty
        self.first = value
        if self.last == None:
            self.last = value
        
    def add_last(self, value):
        """
        self.add_last(value) adds value to self in last position,
        and change two variables if needed.
        Effects: Mutates self by adding value in last position.
        add_last: Quack Any -> None

        """
        for pos in range(self.size()):
            # find the position of the first empty slot
            if self.con.access(pos) == None:
                self.con.store(pos, value)
                self.last = value
                break

    def delete_first(self):
        """
        self.delete_first() removes and returns the value in the
            first position.
        Effects: Mutates self by removing item in first position.
        delete_first: Quack -> Any
        Requires: self is nonempty

        """
        # the empty situation
        if (self.first == None):
            return None
        
        i = 0
        index = self.con.access(i+1)
        while(index != None):
            # index is the data in the next slot
            index = self.con.access(i+1)
            # change the current slot to store the index
            self.con.store(i, index)
            i += 1
        
        # record original first data
        value_return = self.first
        #change the first data and last data if the array become empty
        self.first = self.con.access(0)
        if self.first == None:
            self.last = None
        return value_return

    def delete_last(self):
        """
        self.delete_last() removes and returns the value in the
            last position.
        Effects: Mutates self by removing item in last position.
        delete_last: Quack -> Any
        Requires: self is nonempty

        """
        # record original last data
        value_return = self.last
        # the empty situation
        if (value_return == None):
            return None

        for pos in range(self.size()):
            # find the position of the first empty slot
            if self.con.access(pos) == None:
                # delete the last data
                self.con.store(pos-1, None)
                # change the last data, and first data if the array become empty
                if pos == 1:
                    self.last = None
                    self.first = None
                else:
                    self.last = self.con.access(pos-2)
                break
        return value_return
        
