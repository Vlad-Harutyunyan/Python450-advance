def func(*args,**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(args)
    print(type(args))

func(1,2,4,5,6,a=5,b=7)



