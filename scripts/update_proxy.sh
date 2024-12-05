#!/bin/bash

# 获取宿主机IP地址，这里使用的命令是示例，具体可能需根据容器网络配置和操作系统类型等进行调整
# 比如，如果容器网络模式是 bridge，可尝试以下方式通过网关来推断宿主机IP（不一定完全准确，需按实际情况优化）
GATEWAY=$(ip route | grep default | awk '{print $3}')
HOST_IP=$(nslookup $GATEWAY | grep Address | tail -n1 | awk '{print $2}')

# 更新代理环境变量
export http_proxy="http://$HOST_IP:7890"
export https_proxy="http://$HOST_IP:7890"
export all_proxy="socks5://$HOST_IP:7890"
echo "代理环境变量已更新为基于宿主机IP：$HOST_IP"