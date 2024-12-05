#!/bin/bash
###
 # @Author: 谢嘉伟 wei17306927526@gmail.com
 # @Date: 2024-11-28 15:16:46
 # @LastEditors: 谢嘉伟 wei17306927526@gmail.com
 # @LastEditTime: 2024-12-04 14:27:49
 # @FilePath: /undefined/Users/xiejiawei/codeSecurity/kali/run_kali.sh
 # @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
### 

# 容器名称
CONTAINER_NAME="my-kali-container-2"
HOST_IP="host.docker.internal"

# 检查容器是否已经存在
if docker ps -a --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
  echo "容器 $CONTAINER_NAME 已存在，尝试启动并进入容器..."
  
  # 启动容器（如果未运行）
  if ! docker ps --format "{{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
    docker start $CONTAINER_NAME
  fi

  # 进入容器
  docker exec -it $CONTAINER_NAME /bin/bash
else
  echo "容器 $CONTAINER_NAME 不存在，创建新的容器..."

  # 启动新的容器
  docker run -it --platform linux/amd64 \
    --name $CONTAINER_NAME \
    -e http_proxy="http://$HOST_IP:7890" \
    -e https_proxy="http://$HOST_IP:7890" \
    -e all_proxy="socks5://$HOST_IP:7890" \
    -e NO_PROXY="localhost,127.0.0.1,.local" \
    -v $(pwd)/scripts:/mnt/scripts \
    -p 5901:5901 \
    --network bridge \
    my-kali:v1 /bin/bash
fi
