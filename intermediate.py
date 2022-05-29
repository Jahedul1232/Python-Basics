import json

person = {'name':'John','age':'30','city':'New York','hasChildern':False,'titles':['engineer', 'programmer']}
# print(person)

person_json = json.dumps(person,indent=4)
# print(person_json)
#
# with open('persons.json','w')as file:
#     json.dump(person,file,indent=4)

with open('persons.json','r') as file:
    persons = json.load(file)
    print(persons)