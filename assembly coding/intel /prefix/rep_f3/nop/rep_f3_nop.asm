section .text
    global _start

_start:
    rep nop

    ; exit(0)
    mov rax, 60
    xor rdi, rdi
    syscall
