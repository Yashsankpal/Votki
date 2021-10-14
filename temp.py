# import requests

# msg = input("Enter word: ")
# body = {
#   'word':msg
# }
# data = requests.post('http://127.0.0.1:8081/vocabulary',json=body)
# data = data.json()
# print(data.keys())


# for i,y in data.items():
#   if type(y) is str:
#     print(y)
#   else:
#     for x in y:
#       print(x)

arrange = ["meaning","synonyms","antonyms","examples"]

# for i in arrange:
#   if type(data[i]) is str:
#     print(data[i])
#   else:
#     for x in data[i]:
#       print(x)

# print(data['status'])
print(",".join(arrange))