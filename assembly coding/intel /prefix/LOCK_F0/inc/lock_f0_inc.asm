section .data
    target: dd 123             ; 4바이트 정수 값 (초기값: 123)

section .text
    global _start

_start:
    ; RAX에 target 주소를 담는다
    lea rax, [rel target]

    ; 메모리 값을 증가 (4바이트 → DWORD)
    lock inc dword [rax]

    ; exit(0)
    mov rax, 60
    xor rdi, rdi
    syscall

