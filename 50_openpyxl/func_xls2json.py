import csv
import json


def datas2bestsales(datas):
    catalog = {}
    for data in datas:
        if data['Item'] not in catalog.keys():
            catalog[data['Item']] = {data['Rep']: int(data['Units'])}
        elif data['Rep'] not in catalog[data['Item']].keys():
            catalog[data['Item']][data['Rep']] = int(data['Units'])
        else:
            print(f"{catalog[data['Item']][data['Rep']]} + {data['Units']}")
            catalog[data['Item']][data['Rep']] += int(data['Units'])
    return catalog


with open('SampleData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    datas = [row for row in reader]

new_struc = json.dumps(datas2bestsales(datas), indent=4)
print(new_struc)
