import json
from collections import defaultdict
dict_ = {}
with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)
    
    for i in data['linia']:
       dict_[i['name']] = []
       if 'przystanek' in i:
           for j in i['przystanek']:
                key = i['name']
                dict_[key].append(j['name'][:-3])
       dict_[i['name']] = tuple(dict_[i['name']])
    for k in sorted(dict_, key=lambda k: len(dict_[k]), reverse=True):
        print(f"Liczba przystankow dla tramwaju {k} to {len(dict_[k])}")
    set_ = set()
    for key in dict_:
        if dict_[key]:
            set_.update(dict_[key])
    print("Liczba wszystkich przystankow:", len(set_))




with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
        json.dump(dict_, file, ensure_ascii=False)



