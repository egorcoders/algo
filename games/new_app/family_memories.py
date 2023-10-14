import json
from collections import namedtuple

Transformer = namedtuple('Transformer', (
    'id', 'name', 'hp', 'attack', 'weapon', 'description',
    'war_phrase', 'crit', 'regeneration', 'appearance'
))

transformers = []

with open('../transformers/data.json', 'r') as tr:
    data = tr.read()
    data_dct = json.loads(data)
    for d in data_dct:
        transformers.append(Transformer(**d))

print(transformers[0].name)
