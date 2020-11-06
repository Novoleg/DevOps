from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch([{'host': '192.168.100.7', 'port': 9200}])

doc_oleg = {
    'author': 'Oleg',
    'text': 'Всем привет, я только проснулся',
    'timestamp': datetime.now(),
}

doc_index = {
    'author': 'test-index',
    'text': 'Вот это да, я test-index...',
    'timestamp': datetime.now(),
}
res_oleg = es.index(index="oleg", id=1, body=doc_oleg)
res_index = es.index(index="test-index", id=2, body=doc_index)

res_oleg = es.get(index="oleg", id=1)
print('Результат get doc_oleg: ', res_oleg['_source'])

res_index = es.get(index="test-index", id=2)
print('Результат get doc_index: ', res_index['_source'])
