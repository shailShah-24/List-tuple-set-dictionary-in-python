# Python3 Program to check whether a
# Python code to merge dict using update() method
def M(dict1, dict2):
    return (dict2.update(dict1))


# Driver code
dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

M(dic1, dic2)
M(dic2,dic3)
print(dic3)



