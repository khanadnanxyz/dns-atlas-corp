
**dns-atlas-corp**     
 [![Build Status](https://travis-ci.com/khanadnanxyz/dns-atlas-corp.svg?branch=master)](https://travis-ci.com/khanadnanxyz/dns-atlas-corp)  
[![codecov](https://codecov.io/gh/khanadnanxyz/dns-atlas-corp/branch/master/graph/badge.svg)](https://codecov.io/gh/khanadnanxyz/dns-atlas-corp)  
  
run dns-service with docker-compose  
  

     docker-compose up -d  

run dns-service from docker image  
  

     docker run -P -d khanadnanxyz/dns 

deploy dns-service with helm(v3.0.0) into K8s  
 
     helm install dns ./devops/dns

api documentation ( postman [collection](https://documenter.getpostman.com/view/814321/SzzhcxU5) )

api monitoring dashboard uri

  
>  your_base_url/dashboard
> 
>     USERNAME=admin  
>     PASSWORD=atlas-dns
