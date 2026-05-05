thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
 
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
 
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
 