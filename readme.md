# REDIS DEMO
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<p><img width="180" height="180" src="https://github.com/yurijserrano/Github-Profile-Readme-Logos/blob/master/databases/redis.svg"></p>

## ABSTRACT
*Redis* is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. 
<br>
Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.
<br>
This repo contains a simple demo to show Redis interaction via a Flask web app.

## PREREQUISITE
`docker` and  `docker-compose`

## INSTRUCTIONS
Clone this repo and build build the stack via docker compose:
```console
git clone https://github.com/R3DRUN3/redis-demo.git  \
&& cd redis-demo \
&& docker-compose up
```

Visit the root of our web app at `http://localhost:8754`:
<br>
![alt_text](https://github.com/R3DRUN3/redis-demo/blob/main/images/root-endpoint.png)
<br>
reload the page and you will see that the counter is incrementing via Redis.

Now you can submit a custom key value via a *POST* HTTP call to the key endpoint, you can to this either via curl or postman:
<br>
![alt_text](https://github.com/R3DRUN3/redis-demo/blob/main/images/post-endpoint.png)

You can retrieve the current value of your custom key with a *GET* HTTP call to the same endpoint:
<br>
![alt_text](https://github.com/R3DRUN3/redis-demo/blob/main/images/get-endpoint.png)


