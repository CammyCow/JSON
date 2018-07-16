import json
# survey = {}
# def console():
#     x = input()
#     if x == "print":
#         print(survey)
#         console()
#     else:
#         name= input("what is your name?")
#         age = input("How old are you?")
#         height = input("How tall are you?")
#         candiedFruit= input("Do you prefer candy or fruit? *type [candy] or [fruit] ")
#         foodType= input("How many times a week do you eat out?")
#         personality= input("Would you describe yourself as introverted, extroverted, or both? *type [introverted], [extroverted], or [both]")
#
#         response=[age, height, candiedFruit, foodType, personality]
#         survey[name]= response
#         console()
#
# console()

list=[]
survey=[
    "what is your name?",
    "How old are you?",
    "How tall are you?",
    "Do you prefer candy or fruit? *type [candy] or [fruit] ",
    "How many times a week do you eat out?",
    "Would you describe yourself as introverted, extroverted, or both?"
]
keys = ["name", "age", "height", "candyOrFruit", "foodType", "personality"]
var ="yes"

while var =="yes":
    answer = {}
    for i in range(len(survey)):
        print(survey[i])
        user_input = input()
        answer[keys[i]] = user_input
    list.append(answer)
    var = input("continue? (yes or no)")

f = open("allanswers.json", "r")
olddata = json.load(f)
list.extend(olddata)
f.close()
f = open("allanswers.json", "w")
f.write('[\n')
index = 0
for answer in list:
    if(index < len(list)-1):
        json.dump(answer, f)
        f.write(',\n')
    else:
        json.dump(answer, f)
        f.write('\n')
    index += 1

f.write(']')
f.close()
