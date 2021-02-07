#!/bin/sh
docker run -d --network host --name motion_prod --device=/dev/video0 --device=/dev/video2 motion &&
docker run --device=/dev/ttyACM0 --network host craneprojectv2