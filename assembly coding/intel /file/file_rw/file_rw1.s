section .data
    guide: db "type a filename in this directory(max 32character): "
    guide_len: equ $ - guide

section .bss
    filename: resb 0x20
    file_content: resb 0x101

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, guide
    mov rdx, guide_len
    syscall             ; 사용 가이드 출력

    xor rax, rax
    xor rdi, rdi
    mov rsi, filename
    mov rdx, 0x100
    syscall             ; 파일 이름 읽기

    mov rdi, filename
    call have_linefeed

    mov rax, 257        ; openat
    mov rdi, -100       ; 현재 디렉토리에서
    xor rdx, rdx        ; 읽기 전용
    syscall

    mov r12, rax        ; 결과 fd 저장

    xor rax, rax
    mov rdi, r12        ; 열었던(fd를 얻은) 파일을 읽기
    mov rsi, file_content
    mov rdx, 0x100
    syscall             

    mov r12, rax        ; 읽은 바이트 저장

    mov rax, 1
    mov rdi, 1
    mov rsi, file_content
    mov rdx, r12
    syscall

    mov rax, 60
    xor rdi, rdi
    syscall


; rdi = buffer
; rax = 총 바이트 반환
have_linefeed:
    push rcx
    
.loop:
    movzx rax, byte [rdi]
    cmp al, 0xa
    je .ret

    inc rcx
    inc rdi
    jmp .loop

.ret:
    mov byte [rdi], 0x0
    mov rax, rcx
    pop rcx
    ret
