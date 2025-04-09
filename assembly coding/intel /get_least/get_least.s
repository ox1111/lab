; 256바이트까지 사용자 입력을 받고 공백으로 구분된 수들 중 가장 작은 수를 출력하는 코드
;
section .data
    least: dd 0xffffffff

section .bss
    input: resb 0x100
    input_len: equ $ - input

    input_size: resd 1

    buffer: resb 0x100
    buffer_len: equ $ - buffer

section .text
    global _start

_start:
    xor rax, rax            ; read(0, input, input_len)
    xor rdi, rdi
    mov rsi, input
    mov rdx, input_len
    syscall
                            ; 실제 입력된 바이트 저장
    mov dword [input_size], eax

    lea rdi, [input]        ; 인자로 넘김(최초 1회, 그 후로는 rdi 사용)
    dec rdi
.progress:
    inc rdi
    xor rcx, rcx
    call parse              ; return: rax = 파싱된 수

    cmp eax, dword [least]
    jae .is_over
    mov dword [least], eax

.is_over:
    mov bl, byte [rdi]
    cmp bl, 0xa
    jne .progress

    lea rdi, [buffer]
    mov esi, dword [least]
    call print
    jmp _exit

.change_least:
    jmp .progress

_exit:
    mov rax, 60
    xor rdi, rdi
    syscall

parse:
    mov ax, word [rdi]
    sub al, 0x30            ; 수로 변경

    add cl, al             ; temp에 수 더함

    cmp ah, 0xa             ; 다음 바이트가 라인피드면 파싱 종료
    je .ret
    cmp ah, 0x20            ; 다음 바이트가 공백이면 파싱 종료
    je .ret

    xor rdx, rdx
    mov eax, ecx
    mov ebx, 10
    mul ebx                  ; x10

    mov ecx, eax             ; temp에 저장

    inc rdi
    jmp parse

.ret:
    mov rax, rcx
    inc rdi
    ret


print:
    ;rdi = buffer
    ;rsi = least
    push 0xa
    mov rax, rsi

.push_loop:
    xor rdx, rdx
    mov rbx, 10

    div ebx ; 4바이트 나눗셈
    
    add rdx, 0x30
    push rdx

    test rax, rax
    jz .before_pop_loop
    jmp .push_loop

.before_pop_loop:
    xor rcx, rcx

.pop_loop:
    pop rbx
    mov byte [rdi], bl
    inc rcx
    inc rdi
    cmp rbx, 0xa
    je .real_print

    jmp .pop_loop

.real_print:
    mov rax, 1
    mov rdi, 1
    mov rsi, buffer
    mov rdx, rcx
    syscall

    ret
