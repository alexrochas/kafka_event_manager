# Kafka Event Manager
> Produce and consume Kafka messages with a simple server

## Installation

Linux:

```sh
~$ git clone https://github.com/alexrochas/kafka_event_manager
~$ cd ./kafka_event_manager
~$ pip install -r requirements.txt
```

## Usage example

Run kafka and the zookeeper
```bash
docker-compose up
```

From project root, start server with
```bash
~$ python __init__.py #don't judge me, work in progress
```

To produce a message, make requests to http://127.0.0.1:8081/produce?topic={topicName} with body like

```
{
  "idEndereco": null,
  "idMeioComunicacao": null,
  "idEntidadeComercial": "1264706",
  "tipoEvento": "I",
  "cadastroNacional": "M",
  "tabela": "ecm_clientes"
}
```

To consume and list topic, make a call to http://127.0.0.1:8081/consume?topic={topicName} and if you want to consume and commit
messages add query param to url like http://127.0.0.1:8081/consume?topic={topicName}auto_commit=True

As in code, Kafka host must be http://localhost:9092 and default topic is **ec_events_v1**. 
This will be fixed on next versions. I promisse.

## Development

Install dependencies
```
pip install -r requirements.txt
```

## Release History

* 0.0.1
    * Work in progress

## Meta

Alex Rocha - [about.me](http://about.me/alex.rochas)
