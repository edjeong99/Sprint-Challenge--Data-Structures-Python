Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
   --> it runs through each node. so O(n)
2. What is the space complexity of your `depth_first_for_each` function?
   --> I didn't use any additional space for this method. cb might use some but I can't know about it. so O(1) or O(0)
3. What is the runtime complexity of your `breadth_first_for_each` method?
   --> still look at each Node once so O(n)
4. What is the space complexity of your `breadth_first_for_each` method?
   --> it needs to save nodes at the last level to keep track of what to look for next. It won't need to save every looked Node but just Nodes at the last level. so O(logN)

5) What is the runtime complexity of the provided code in `names.py`?
   --> there is loop inside of loop, so O(n^2)
6) What is the space complexity of the provided code in `names.py`?
   --> it create list for each input files. duplicate list is created but should not matter much. so O(N), where N is combined size of input files
7) What is the runtime complexity of your optimized code in `names.py`?
   --> it look at each items in the list once, if best case is when everything matches or all item in one list is bigger or smaller than the other O(n/2),
   worst case where nothing matches O(n)
8) What is the space complexity of your optimized code in `names.py`?
   --> it still uses the same list for 2 input files and duplicate list. so O(N)
