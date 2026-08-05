#CLEANING MESSY LIST

import re
states = ['Alabama!!', 'Barcerlona', 'Atlanta1', 'LAGOS']

def clean_strings(states):
    result = []
    for values in states:
        values = values.strip()
        values = re.sub('[!#$%?\d]', '', values)
        values = values.title()
        result.append(values)
    return result
   
cleaned = clean_strings(states)
print(cleaned)
