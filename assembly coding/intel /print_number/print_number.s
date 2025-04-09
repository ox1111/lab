section .data
	now_number: dd 1
	size: db 4
	digit: db 3
section .bss
	input: resb 4	
	buffer: resb 4
	target_number: resd 1

section .text
	global _start

_start:
	xor rax, rax
	xor rdi, rdi
	mov rsi, input
	mov rdx, size
	syscall

	mov rcx, digit
	mov rdi, input
	mov rsi, target_number

	call set_target
	call before_itoa_push_loop
_exit:
	mov rax, 60
	xor rdi, rdi
	syscall



set_target:
	dec ecx
	
	sub byte [rdi], 0x30
	movzx eax, byte [rdi]

	add dword [rsi], eax

	test ecx, ecx
	jz .ret

	inc rdi
	cmp byte [rdi], 0xa
	je .ret

	xor rdx, rdx
	mov ebx, 10
	mov eax, dword [rsi]
	mul ebx

	mov dword [rsi], eax
	jmp set_target
.ret:
	ret




before_itoa_push_loop:
	mov rcx, digit
	inc rcx
	xor rax, rax
	mov eax, dword [now_number]
	cmp eax, dword [target_number]
	ja .ret
	push 0xa

.itoa_push_loop:
	dec ecx
	test ecx, ecx
	jz .before_itoa_pop_loop
	
	xor rdx, rdx
	mov bx, 10
	div bx

	add dx, 0x30
	push rdx
	
	test ax, ax
	jz .before_itoa_pop_loop

	jmp .itoa_push_loop

.before_itoa_pop_loop:
	mov rcx, digit
	inc rcx
	mov rdi, buffer

.itoa_pop_loop:
	dec ecx
	pop rbx
	mov byte [rdi], bl
	inc rdi

	cmp rbx, 0xa
	jne .itoa_pop_loop
	
	mov rax, 1
	mov rdi, 1
	mov rsi, buffer
	mov rdx, digit
	inc rdx
	sub rdx, rcx
	syscall

	inc dword [now_number]
	jmp before_itoa_push_loop

.ret:
	ret
