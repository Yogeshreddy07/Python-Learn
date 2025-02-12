"""Write a python function to remove a given word from a list ad strip it at the same 
time.
    """
def rem(n):
    l=["yogesh","reddy",5]
    l.remove(n)
    return l
print(rem("yogesh")) #['reddy', 5]