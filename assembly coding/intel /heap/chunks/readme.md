🔍 실전 예제: 함수 프롤로그 & 에필로그 분석 (각 바이트 및 ModR/M 구성 설명 포함)

```
0x55555555516d:  55                  ; push rbp
0x55555555516e:  48 89 e5           ; mov rbp, rsp
0x555555555171:  48 83 ec 10        ; sub rsp, 0x10
0x555555555175:  bf 20 00 00 00     ; mov edi, 0x20
0x55555555517a:  e8 f1 fe ff ff     ; call malloc@plt (rel32)
0x55555555517f:  48 89 45 f8        ; mov QWORD PTR [rbp-0x8], rax
0x555555555183:  e8 d8 fe ff ff     ; call getchar@plt
0x555555555188:  b8 00 00 00 00     ; mov eax, 0
0x55555555518d:  c9                 ; leave
0x55555555518e:  c3                 ; ret
```

명령어                                   바이트 (HEX)    ;설명

push rbp                                55              ; opcode(1): 64비트 기본 레지스터 단축 opcode

mov rbp, rsp                            48 89 e5        ; REX(1) + opcode(1) + ModR/M(1)

sub rsp, 0x10                           48 83 ec 10     ; REX + opcode + ModR/M + imm8

mov edi, 0x20                           bf 20 00 00 00  ; opcode for mov reg, imm32 (bf = mov edi, imm32)

call malloc@plt                         e8 f1 fe ff ff  ; call opcode(1) + rel32(4)

mov [rbp-0x8], rax                      48 89 45 f8     ; REX + opcode + ModR/M + disp8 (f8 = -8)

call getchar@plt                        e8 d8 fe ff ff  ; call opcode(1) + rel32(4)

mov eax, 0                              b8 00 00 00 00  ; opcode for mov eax, imm32

leave                                   c9              ; 단일 opcode

ret                                     c3              ; 단일 opcode


📌 추가 분석:

mov QWORD PTR [rbp-0x8], rax = 48 89 45 f8

48: REX.W = 1 (64비트 연산)

89: opcode = mov r/m64, r64

45: ModR/M

Mod = 01 (메모리 + disp8)

Reg = 000 (rax)

R/M = 101 (rbp)

f8: disp8 = -8 (2's complement)

sub rsp, 0x10 = 48 83 ec 10

48: REX.W

83: opcode for SUB with imm8

ec: ModR/M

Mod = 11 (레지스터)

Reg = 101 (SUB)

R/M = 100 (rsp)

10: imm8 = 16

mov rbp, rsp = 48 89 e5

48: REX.W

89: opcode (mov r/m64, r64)

e5: ModR/M

Mod = 11 (레지스터)

Reg = 100 (rsp)

R/M = 101 (rbp)

📌 참고:

REX(48)는 64비트 레지스터 사용 (예: mov rbp, rsp)

ModR/M은 레지스터/메모리 위치 지정용 1바이트

disp8, rel32, imm32는 추가 상수 값

각 명령어와 레지스터 조합에 대해 실제 인코딩 바이트 수와 구조를 정리하며, 각 명령어 카테고리마다 예제 형식으로 설명을 추가합니다.

예: mov eax, 42 → b8 2a 00 00 00 → 5바이트 → opcode(1) + imm32(4)

