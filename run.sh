#!/bin/bash

app_path=`pwd`

docker rm flaviodev-python -f
docker run -it --name flaviodev-python -v $app_path/src:/usr/src:rw flaviodev-python bash
