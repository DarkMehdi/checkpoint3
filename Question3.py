dictio={'a': 100, 'b': 200, 'c':300}
dictio2={'a': 300, 'b': 200, 'd':400}
for key in dictio2:
    if key in dictio:
        dictio2[key] = dictio2[key] + dictio[key]
    else:
        pass

dictio2=dictio | dictio2
print(dictio2)