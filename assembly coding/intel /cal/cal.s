section .data
    guide: db "type a fomula like '2*4': "
    guide_len: equ $ - guide

section .bss
    input: resb 0x10
    buffer: resb 0x10

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, guide
    mov rdx, guide_len
    syscall

    xor rax, rax
    xor rdi, rdi
    mov rsi, input
    mov rdx, 0x10
    syscall

    mov rdi, input
    call atoi
    movzx rdx, byte [rdi]
    inc rdi
    mov rbx, rax
    call atoi

    mov rdi, rbx
    mov rsi, rax
    call cal

    mov rdi, rax
    mov rsi, buffer
    call itoa

    mov rdx, rax
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    syscall

_exit:
    mov rax, 60
    xor rdi, rdi
    syscall


; rdi = 수
; rsi = 쓸 버퍼
; rax = 줄바꿈 포함 버퍼 크기 반환
itoa:
    push rcx
    push rdx
    push rbx

    mov rax, rdi    ; 수 대입
    mov rbx, 10
    mov rcx, 1
    
    push 0xa

.push_loop:
    inc rcx
    xor rdx, rdx
    
    div rbx
    add dl, 0x30
    push rdx

    test rax, rax
    jnz .push_loop

.pop_loop:
    pop rax

    mov byte [rsi], al
    inc rsi

    cmp rax, 0xa
    jnz .pop_loop

.ret:
    mov rax, rcx

    pop rbx
    pop rdx
    pop rcx
    ret


; rdi = 읽을 버퍼(문자열 수)
; rax = 수 반환
; rdi 버퍼를 계속 읽으며 수로 변환하다가
; 수에 해당하지 않는 문자(<0, >9)가 나오면 중단
atoi:
    push rdx
    push rbx
    push r8

    xor rax, rax
    xor rdx, rdx
    mov rbx, 10
    xor r8, r8
.loop:
    movzx rax, word [rdi]

    inc rdi

    sub al, 0x30
    add dl, al

    cmp ah, 0x30
    jl .ret
    cmp ah, 0x39
    jg .ret

    mov rax, rdx
    xor rdx, rdx
    mul rbx
    mov rdx, rax

    jmp .loop

.ret:
    mov rax, rdx
    pop r8
    pop rbx
    pop rdx
    ret

; rdi = a
; rsi = b
; rdx = symbol
; rax = 계산 결과
cal:
    push rbx
    mov rax, rdi
    mov rbx, rsi

    cmp rdx, '+'
    je .plus

    cmp rdx, '-'
    je .minus

    cmp rdx, '*'
    je .multiple

    cmp rdx, '/'
    je .divide

    xor rax, rax
    jmp .ret

.plus:
    add rax, rbx

    jmp .ret

.minus:
    sub rax, rbx

    jmp .ret


.multiple:
    mul rbx

    jmp .ret


.divide:
    push rdx
    xor rdx, rdx
    
    test rbx, rbx
    jz .divide_by_zero

    div rbx

    pop rdx

    jmp .ret

.divide_by_zero:
    xor rax, rax
    pop rdx

.ret:
    pop rbx
    ret
