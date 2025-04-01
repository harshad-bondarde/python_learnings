def func(term):
    print(term)

func("HHHHH")

def func2(*term):
    a=len(term)
    print(term[a-1])
func2("UUU","KKK","III")