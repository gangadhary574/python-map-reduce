# Python Map Reduce

Basic Python introduction and concepts needed in preparation for working with map-reduce solutions.

## Requirements

- Install Chocolatey, the Windows package manager
- Install the Anaconda 3 version for Python + common packages
- Install Visual Studio Code for text editing
- Add Open Command Window Here as Administrator to your File Explorer context menu.

See: [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Case 1:  Local file-based

```PowerShell
py 11mapper.py
py 12sorter.py
py 13reducer.py
```

## Case 2:  Use standard input and output

Use the console (standard input and output) and shell commands to pipe information.  We'll use the built-in shell sort command, so we don't need that anymore. 

cat data | map | sort | reduce

PowerShell and Bash use the same commands:

```Bash
cat part.txt
cat part.txt | python 21mapper.py
cat part.txt | python 21mapper.py | sort
cat part.txt | python 21mapper.py | sort  | python 22reducer.py

```

### Inorder to process to larger file, we need to run following commands. 

```Bash
cat purchases.txt
cat purchases.txt | python 21mapper.py
cat purchases.txt | python 21mapper.py | sort
cat purchases.txt | python 21mapper.py | sort  | python 22reducer.py

```
### Bonus
- Created mapper, sorter and reducer files and supply the output of initial reducer to bonus mapper and run ``` python mapper_bonus.py ```. 
- Supply the output of above command as input to sorter file and run ``` python sorter_bonus.py ```
- suppy the output here to reducer and run ``` python reducer_bonus.py ```. The resulting output is stored in ``` sorted_bonus_out.txt ```.
- The first five records observed are 
``` 

1613.35 Cameras
1018.6  Books
992.51  Baby
848.56  Men's Clothing
837.69  Consumer Electronics
818.4200000000001       Sporting Goods

```



## References

- [Udacity "Introduction to Hadoop and MapReduce"](https://classroom.udacity.com/courses/ud617/)
- [IBM Python for Data Science](https://cognitiveclass.ai/courses/python-for-data-science)
- [Basic Setup for Big Data](https://github.com/denisecase/basic-setup-for-bigdata)

## Repository

- [https://github.com/denisecase/python-map-reduce](https://github.com/denisecase/python-map-reduce)
