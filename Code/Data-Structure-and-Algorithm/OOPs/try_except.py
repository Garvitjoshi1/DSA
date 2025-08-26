import sys
l = ['a', 0, 2]
for ele in l:
    try:#This block might raise an exception while executing
        print("The entry is", ele)
        r = 1/int(ele)
        break
    except:
#This block executes in case of an exception in "try"
          print("Oops!", sys.exc_info()[0], "occurred.")
          print()
print("The reciprocal of", ele, "is", r)
