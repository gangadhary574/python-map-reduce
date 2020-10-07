# Case 1 - Mapper using Files
# Easy to test
# Not quite Hadoop-ready

# open returns a file object
with open("reduced_out.txt", "r") as input:
  with open("dept_bonus_out.txt", "w") as output:

    # iterate through each line in the file object
    for line in input:
      datalist = line.strip().split("\t")
      if (len(datalist) == 2) : 
        department, amount = datalist

        # output intermediate key-value pairs
        output.write(department + "\t" + amount + "\n")

        # display to console (not required - just for the user)
        print(department + "\t" + amount + "\n")

