class MySet:
    
    def __init__(self, enumerable = []):
        ''' We might also want to pass in an existing collection of values, such as an list, 
        and create a new set with just the unique values:
        '''
        self.dictionary = {}
        for value in enumerable :
            self.dictionary[value] = True

    def has(self, value):
        '''
        This method checks if the value is already included in the set, and returns true if so, and false if not. 
        It also must have a O(1) runtime.
        '''
        # return self.dictionary[value] # Output: None
        return value in self.dictionary # Output false
    
    def add(self, value):
        '''
        This method needs to add a value to the set if it isn't already present, and return the updated set. 
        It also must have a O(1) runtime.
        '''
        self.dictionary[value]= True # Add a value as a key on the Dictionary
        return self
    
    def delete(self, value):
        '''
        The delete() method removes a value from the set, and returns the updated set. 
        It also must have a O(1) runtime.
        '''
        self.dictionary.pop(value, None)
        return self
    
    def size(self):
        '''
        Return the number of elements in the set.
        '''
        return len(self.dictionary)
    
    #Bonus
    def union(self, other_set):
        """
        Returns a new set that is the union of this set and another set.
        """
        union_set = set()
        union_set.dictionary = self.dictionary.copy()
        union_set.union_(other_set)
        return union_set
    
    def clear(self):
        updated_set= self.dictionary.clear()
        return updated_set.__str__()