#Check that a tuple type cannot be changed in python. 
a=(32,333,"harry")
a[2]="yogesh"
""" a[2]="yogesh"
    ~^^^
TypeError: 'tuple' object does not support item assignment"""