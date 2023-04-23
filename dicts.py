# d = {
#     'key1' : 'value1',
#     'key2' : 'value2',
#     'key3' : 'value3'
# }
# d['key2'] = 'value5'
# print(d)
# p = {
#     'Света' : 27,
#     'Юра' : 30,
#     'Саша' : 18
# }

# print(str(p['Юра']) + ' let')
# d['key4'] = 'value4'
# print(d)

nd = {
    'Svetlana' : {
    'pol' : 'female',
    'age' : 18,
    'hobby' : ['flowers', 'singing']
    },
    'Andre' : {
    'pol' : 'male',
    'age' : 34,
    'hobby' : ['eating', 'cats']
    }
}
# print(nd['Svetlana']['hobby'])
# d = nd.items()
# print(list(d)[0])
print(nd.keys())
print(nd.values())