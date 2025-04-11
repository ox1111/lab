section .data
    n: dd 0

section .bss
    input: resd 1
    buffer: resb 0x100

section .text
    global _start

_start:
    xor rax, rax
    xor rdi, rdi
    mov rsi, input
    mov rdx, 1
    syscall

    xor rax, rax
    mov al, byte [input]
    sub rax, 0x30
    mov dword [n], eax

    xor r8, r8
    mov r8d, dword [n]
    xor rcx, rcx
.loop:
    inc rcx
    
    mov rdi, buffer
    mov al, 0x20
    push rcx
    mov rdx, rcx
    neg rdx
    lea rcx, [r8 + rdx]
    rep stosb

    pop rdx
    mov al, '*'
    lea rcx, [rdx * 2 + -1]
    push rdx
    rep stosb

    mov byte [rdi], 0xa
    
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    pop rcx
    lea rdx, [r8 + rcx]
    push rcx
    syscall
    
    pop rcx

    cmp rcx, r8
    jl .loop

    mov rax, 60
    xor rdi, rdi
    syscall

    

; n-1 1 * 2 - 1 n
; n-2 2 * 2 - 1 n + 1
; n-3 3 * 2 - 1
; n-4 4 * 2 - 1
; n-5 5 * 2 - 1
;     *
;    ***
;   *****
;  *******
; *********
