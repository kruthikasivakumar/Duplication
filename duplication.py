import json

with open('example1.json') as json_data:
    obj = json.load(json_data)
    #attr = lambda x: x['hdfs:batchprocessing'][0]['application']['app_id']+x['hdfs:batchprocessing'][0]['application']['app_id']
    el_set = set()
    el_list = []
    for el in obj:
        if str(el) not in el_set:
            el_set.add(str(el))
            el_list.append(el)
            
open("updated_structure.json", "w").write(
    json.dumps(el_list, sort_keys=True, indent=4, separators=(',', ': '))
)
