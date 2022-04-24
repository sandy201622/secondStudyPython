
def test1111():
    str_a="studyPython"
    print(str_a[1:])
    print(str_a[1::])
    print(str_a[1:5])
    print(str_a[1:5:2])
    print(str_a[1:7:2])
    print(str_a[1:-1])
    print(str_a[::])
    list_a=[1,2,3,4,5,6,7]
    print(list_a[1:])
    print(list_a[1::])
    print(list_a[1:-1])


#字符串基本操作
def test222():
    print(("this is str %s" % "string1"))
    print(("this is str %d" % 111))
    print(("this is str %f" % 111.3))
    print(("this is format_string {} {} {}").format("yes", "or","no"))
    print(("this is format_string {2} {1} {0}").format("yes", "or","no"))

    print(("this is format_string {yes} {or_1} {no}").format(yes="yes", or_1="or",no="no"))
    name="sandy"
    print(f"my name is {name}")
    str1="|it is very good|"
    list1= str1.split(" ")
    print(list1)
    print("@".join(list1))
    print(str1.strip("|"))
    print(str1.replace("good", "bad"))

def testdev():
    pass

if __name__ == '__main__':
    test222()