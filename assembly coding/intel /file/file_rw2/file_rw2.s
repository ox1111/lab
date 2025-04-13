section .data
    guide: db "type a filename to read: "
    guide_len: equ $ - guide
    new_filename: db "new_written_file.txt"

section .bss
    filename: resb 0x10
    file_content: resb 0x100

section .text
    global _start

_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, guide
    mov rdx, guide_len
    syscall             ; 가이드 출력

    xor rax, rax
    xor rdi, rdi
    mov rsi, filename
    mov rdx, 0x10
    syscall             ; 파일 이름 입력

    dec rax
    cmp byte [filename + rax], 0xa  ; 가장 마지막 바이트가 줄바꿈인가?
    jne .ok

    mov byte [filename + rax], 0x0  ; 줄바꿈 삭제

.ok:
    mov rax, 0x101
    mov rdi, -100
    mov rsi, filename
    xor rdx, rdx
    syscall             ; 현재 위치에서 이름이 filename과 동일한 파일의 fd 얻기

    mov r12, rax        ; fd 저장

    xor rax, rax
    mov rdi, r12
    mov rsi, file_content
    mov rdx, 0x100
    syscall             ; 파일 읽기

    mov r12, rax

    mov rax, 3
    ;mov rdi, rdi         기존 fd 사용
    syscall             ; fd 닫기(close)

    mov rax, 0x101
    mov rdi, -100
    mov rsi, new_filename
    mov rdx, 0x41       ; O_WRONLY | O_CREAT = 쓰기 전용, 없으면 생성 모드로 파일 열기
    mov r10, 0o644      ; 실행권한: rw-r--r--
    syscall             ; 파일 생성하며 열기

    mov r11, rax        ; fd 저장

    mov rax, 1
    mov rdi, r11
    mov rsi, file_content
    mov rdx, r12        ; 아까 읽은 바이트 수 사용
    syscall             ; 파일에 작성

    mov rax, 3
    ;mov rdi, rdi
    syscall             ; fd 닫기

    mov rax, 0x3c
    xor rdi, rdi
    syscall             ; 종료
