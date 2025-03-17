dict={"brand":"Ford",
      "model":"Mustang",
      "year":1964}

print(len(dict))
x=dict["model"]
x=dict.get("model")
x=dict.keys()
x=dict.values()
x=dict.items()
if "model" in dict:
    print("Yes")
dict["brand"]="chev"

dict.pop("model")
print(dict)