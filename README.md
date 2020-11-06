# Конфигурация для docker-compose с one-shot сервисом :sunglasses:	
## Описание
Данный проект разворачивает два контейнера: 
1. Один с сервисом elasticsearch
2. Второй с python скриптом для заполнения индекса в elasticsearch

## Запуск
1. Склонировать проект
2. Перейти в директорию OneShotService в файле main.py поменять параметр <your_ip> на ip ваш ip адрес: ```es = Elasticsearch([{'host': '<your_ip>', 'port': 9200}])```
3. Затем выполнить команду: ```docker build . -t local/python_elasticsearch```
4. Затем вернуться в корневую директорию и запустить docker-compose.yml: ```docker-compose up```

## Проверка 
Выполнить в браузере запрос http://<your_ip>:9200/oleg/_search
Если все правильно сработало, то в браузере должен появиться такой результат:
```
{
  "took": 12,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1.0,
    "hits": [
      {
        "_index": "oleg",
        "_type": "_doc",
        "_id": "1",
        "_score": 1.0,
        "_source": {
          "author": "Oleg",
          "text": "Всем привет, я только проснулся",
          "timestamp": "2020-11-06T09:49:10.972974"
        }
      }
    ]
  }
}
```
