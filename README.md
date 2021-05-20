# config - that is json
it should expose some config params , 
-config config file:

config file:
1. configurable time ?

# data-analysis

python 
create virtual env: python3 -m venv venv
activate: source venv/bin/activate

start a scrapy project: scrapy startproject projectname

result in a josn format: scrapy crawl indeed -o indeed.json  

find container: docker ps --format $FORMAT
jump in container: docker attach container_name
leave container: control-p or control-q

kill container: docker kill container_name
remove container: docker rm container_name

docker logs 

