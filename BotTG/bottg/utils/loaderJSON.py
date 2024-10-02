import json
from splogger import SPinfo

SPinfo('Загрузка файлов JSON')
with open('data/msg.json' , 'r', encoding='utf-8') as file:
    configJSON = json.load(file)