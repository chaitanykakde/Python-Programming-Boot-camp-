def outer():
    var=10
    def inner():
        var=20
        print("Inner Variable:",var)
    inner()
    print("Outer Variable:",var)

outer()
