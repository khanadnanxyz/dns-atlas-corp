**dns-atlas-corp**   
  
[![Build Status](https://travis-ci.com/khanadnanxyz/dns-atlas-corp.svg?branch=master)](https://travis-ci.com/khanadnanxyz/dns-atlas-corp)

run dns-service with docker-compose

    docker-compose up -d

run dns-service from docker image

    > docker run -P -d khanadnanxyz/dns
    bff5d13a37a72a1750852f857044d8cb36009506eecadf57cc668fa6b157f1ee
    > docker ps
    0.0.0.0:get_your_port_number->5000/tcp

deploy dns-service with helm(v3.0.0) into K8s

    helm install dns ./devops/dns
