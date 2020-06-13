
  
**dns-atlas-corp**       
 [![Build Status](https://travis-ci.com/khanadnanxyz/dns-atlas-corp.svg?branch=master)](https://travis-ci.com/khanadnanxyz/dns-atlas-corp)    
[![codecov](https://codecov.io/gh/khanadnanxyz/dns-atlas-corp/branch/master/graph/badge.svg)](https://codecov.io/gh/khanadnanxyz/dns-atlas-corp)    
    
run dns-service with docker-compose    

     docker-compose up -d   

run dns-service from docker image    

     docker run -P -d khanadnanxyz/dns   

deploy dns-service with helm(v3.0.0) into K8s    

     cd ./devops/dns mv values.yaml.example values.yaml    
     # do your necessary changes in values.yaml  
     cd ..    
     helm install dns ./dns  

  
api monitoring dashboard url
  
    
>  your_base_url/dashboard  
> USERNAME=admin 
> PASSWORD=atlas-dns

API documentation for DNS service of Atlas Corporation.

POST 
your_base_url/api/v1/loc

BODY raw
```javascript
{
	"x": "123.12",
	"y": "456.56",
	"z": "789.89",
	"vel": "20.0"
}
```
Example Request
```javascript
curl --location --request POST 'http://your_base_url/api/v1/loc' \
--data-raw '{
	"x": "123.12",
	"y": "456.56",
	"z": "789.89",
	"vel": "20.0"
}'
```
Example Response
```javascript
{
    "loc": 1389.57,
    "message": "Calculation Completed",
    "status_code": 200
}
```

GET  
your_base_url/

```javascript
curl --location --request GET 'http://your_base_url/'
```
Example Response
```javascript
{
    "message": "hello, space!",
    "status": "OK"
}
```