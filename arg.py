# def name(a, b, c, d):
#     print(a, b, c, d)
# name("gaurav", "prateek", "ankit", "satyam")

def name(*args) :
    for item in args :
        print(item)

list = ["gaurav", "prateek", "ankit", "satyam", "piyush"]
name(*list)