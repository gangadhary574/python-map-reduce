# Case 1 - Reducer using Files
# Easy to test
# Not quite Hadoop-ready

with open("sorted_bonus_out.txt","r") as sorted:
  with open("bonus_reduced_out.txt", "w") as output:

    thisKey = 0.0
    thisValue = ""

    for line in sorted:
      datalist = line.strip().split('\t')
      if (len(datalist) == 2) : 
        department, amount = datalist

        if amount != thisKey:
          if thisKey:
            # output the previous key-summaryvalue result
            output.write(thisKey + '\t' + str(thisValue)+'\n')
            print(thisKey + '\t' + str(thisValue)+'\n')

          # start over for each new key
          thisKey = amount 
          thisValue = department
  
        # apply the aggregation function
        # thisValue += float(amount)

    # output the final key-summaryvalue result outside the loop
    # output.write(thisKey + '\t' + str(thisValue)+'\n')
    print(str(thisKey) + '\t' + thisValue +'\n')
