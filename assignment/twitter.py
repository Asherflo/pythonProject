twitters = [
    {"username": "asherflo", "age": 26, "verified": True, "tweet":["i will be the president of Nigeria in 2027", "God is good", "i am a software engineer","let me fix your bug", "the world is looping"]},
    {"username": "dipo_awoyele", "age": 45, "verified": True, "tweet": ["maybe Nigeria will be great again", "nothinng happen by accident ,be prepared","can python be the most used programming language"]},
    {"username": "sugar_daddy", "age": 19, "verified": False, "tweet": ["G.O.A.T", "mamaz prayers product"]},
    {"username": "chinos", "age": 21, "verified": False, "tweet": ["see my new benz", "do dont disturb", "is all about inheritance in oop", "built-in"]},
    {"username": "choxo_gal", "age": 26, "verified": False, "tweet": ["on God", "jah ,bless me so good"]},
    {"username": "pete_don_pee", "age": 27, "verified": False, "tweet": ["the president should be hold accountable", "Nigeria should be called state of emergence"]},
    {"username": "uncle bob", "age": 65, "verified": True, "tweet": ["clean code", "there must be clean pratice of software engineering","java is better than python is false","enjoy your spare with your family as a engineer","sentiel loop vs controlled structure","the power of whitespace"]},
    {"username": "chibuzor", "age": 32, "verified": False, "tweet": ["clean code", "uncle bob is my mentor","c10 is my cross","lagos is expensive","semicolon africa is my home"]},
    {"username": "sam_akin", "age": 24, "verified": False, "tweet": ["i dont have a penny"]},
    {"username": "_akintunde_alabi", "age": 19, "verified": False, "tweet": ["if i broke nah my business"]}
]

a1 =[user["username"] for user in twitters if user["verified"]]
a2= map(lambda y: y["username"],filter(lambda x :x["verified"], twitters ))
a3 = filter(lambda x: x, map(lambda x:x["username"] if x["verified"] else False,twitters))
print(list(a3))
print(list(a2))
print(list(dict.fromkeys(twitter["username"] for twitter in twitters if twitter["verified"] == True)))
print(list(dict.fromkeys(twitter["age"] for twitter in twitters if twitter["age"] >= 25)))
avg =sum(user["age"]for user in twitters) /len(twitters)
print(avg)
sum= sum(user["age"] for user in twitters)
print(sum)
max =max(user["age"] for user in twitters)
print(max)
min = min(user["age"] for user in twitters)
print(min)
from functools import reduce
from statistics import mean
print(mean(user["age"] for user in twitters))

avg2 = reduce(lambda x,y: x + y,(user["age"] for user in twitters)) /len(twitters)
print(avg2)
# max(len(user["tweet"] for user in twitters))


# most_tweet = max(twitters, key =lambda user: len(user["tweets"]))
# print(most_tweet)


ascend = sorted(twitters, key =lambda user:['age'], reverse=True)
print (ascend)
students_1 =[45,89,90]
students_2 =[45,89,23]
print(list(zip(students_1 ,students_2,strict =True)))
print(list(zip(students_1 ,students_2,strict =True)))