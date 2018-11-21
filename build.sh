#!/bin/bash
	
docker rmi flaviodev-python -f

docker build -t flaviodev-python .

