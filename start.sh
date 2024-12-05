#!/bin/bash

# 1. 停止并移除任何现有的容器
echo "Stopping existing containers..."
docker-compose down

# 2. 启动容器
echo "Starting the containers..."
docker-compose up -d

# 3. 等待容器启动完成（可以根据需要调整时间）
echo "Waiting for containers to start..."
sleep 5

# 4. 进入容器的 Bash 终端
echo "Entering the container terminal..."
docker exec -it kali-linux /bin/bash

