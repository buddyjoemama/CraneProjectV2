#!/bin/sh
docker run -d --network host --device=/dev/video0 motion &&
docker run --device=/dev/$(ls /dev | grep ttyACM) --network host craneprojectv2