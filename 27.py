s = {1, 2, 3, 4} 
s.discard(2)   # safely removes 2, no error if not present 
s.remove(3)    # removes 3, error if not present 
popped = s.pop()   # removes and returns an arbitrary item 
print("Set after removals:", s) 
print("Popped element:", popped)
