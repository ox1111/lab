🧠 x86-64 명령어 구성 순서 및 각 요소 상세 설명

x86-64 명령어는 다음 구성 순서로 이루어져 있으며, 각 항목은 필요에 따라 생략되거나 붙을 수 있다.

[Prefix] → [REX] → [Opcode] → [ModR/M] → [SIB] → [Disp] → [Imm]

각 항목은 CPU가 명령어를 디코딩하는 순서대로 처리된다.

1️⃣ Prefix (접두사)

📘 용어 설명:

Prefix는 명령어의 특성을 수정하거나 확장하는 선택적 바이트이다.

최대 4개까지 연속적으로 붙을 수 있으며, 순서가 정해져 있다.

🧱 구조 및 종류:

그룹    예시 Prefix    설명

1    F0, F2, F3                LOCK, REP, REPE/REPNE

2    2E, 36, 3E, 26, 64, 65    세그먼트 오버라이드

3    66                        오퍼랜드 크기 오버라이드

4    67                       주소 크기 오버라이드

➡️ CPU는 명령어 시작 시 prefix인지 검사하고 4개까지 읽어 저장한다.

💡 예시 (Prefix 전체 조합 예시 및 LOCK/REP/REPE 예제)

아래는 Prefix를 1~4개 조합하여 사용하는 실제 예시입니다. (정해진 순서: Group 1 → Group 2 → Group 3 → Group 4)

f3 90                ; REP + NOP (REP = group1, opcode only)

f0 90                ; LOCK + NOP

66 b8 2a 00 00 00    ; Operand Size Override + MOV AX, 42 (16비트)

67 a1 78 56 34 12    ; Address Size Override + MOV EAX, [imm32]

2e a1 78 56 34 12    ; Segment override (CS) + MOV EAX, [imm32]

64 a1 78 56 34 12    ; Segment override (FS) + MOV EAX, [imm32]


; 모든 그룹 prefix가 동시에 붙은 예 (올바른 순서)

f3 64 66 67 a5       ; REP + FS + Operand Size + Address Size + MOVS

f0 2e 66 67 a1 34 12 00 00 ; LOCK + CS + Operand/Address override + MOV EAX, [imm32]


📌 참고:

F0: LOCK (group 1)

F3: REP/REPE (group 1)

2E, 64: 세그먼트 오버라이드 (group 2)

66: 오퍼랜드 크기 변경 (group 3)

67: 주소 크기 변경 (group 4)

CPU는 prefix를 그룹별 순서에 맞게 1~4개까지 허용하며, 순서를 지켜야 정상적으로 해석합니다.

🔁 그룹 1~4 순서 전체 Prefix 조합 예제


; 올바른 순서: 그룹1 → 그룹2 → 그룹3 → 그룹4 → opcode

f0 2e 66 67 a1 34 12 00 00    ; LOCK + CS + Operand + Address + MOV EAX, [imm32]

f3 64 66 67 a5                ; REP + FS + Operand + Address + MOVS

f2 2e 66 67 a6                ; REPNE + CS + Operand + Address + CMPS

f0 64 66 67 ff 08             ; LOCK + FS + Operand + Address + DEC DWORD PTR [RAX]


📌 설명:

F0 = LOCK (그룹 1)

F2/F3 = REPNE/REPE (그룹 1)

2E, 64 = 세그먼트 오버라이드 (그룹 2)

66 = 오퍼랜드 크기 (16비트 등) (그룹 3)

67 = 주소 크기 (32비트 등) (그룹 4)

A1, A5, A6 등은 실제 opcode

⚠️ 이 순서를 지키지 않으면 CPU가 prefix를 무시하거나 예외를 발생시킬 수 있음

🔐 LOCK / REP / REPE / REPNE 예시들

f0 ff 08                ; LOCK DEC DWORD PTR [RAX]

f0 01 18                ; LOCK ADD DWORD PTR [RAX], EBX

f3 a4                   ; REP MOVSB

f3 ab                   ; REP STOSD (EAX → [EDI])

f3 a7                   ; REPE CMPS DWORD PTR [RSI], [RDI] (Equal할 때 반복)

f2 a7                   ; REPNE CMPS DWORD PTR [RSI], [RDI] (Not Equal할 때 반복)

f3 90                   ; REP NOP = pause (인텔 최적화용 2바이트 NOP)


📌 참고:

LOCK은 메모리 대상 명령어와 함께만 의미 있음

REP, REPE, REPNE는 주로 MOVS, STOS, LODS, SCAS, CMPS 계열에 사용됨

F3 90은 pause라는 이름으로도 불리며, 반복 루프 최적화 용도로 사용됨

2️⃣ REX (Register Extension Prefix)

📘 용어 설명:

REX는 64비트 모드에서 사용하는 1바이트 확장 접두사이다.

레지스터 확장 및 64비트 오퍼랜드 사용을 지정할 수 있다.

🧱 비트 구조 (1바이트):

0100WRXB

비트    의미

W     1: 64비트 오퍼랜드 사용

R     reg 필드 상위 비트 확장

X     index 필드 상위 비트 확장

B     r/m 또는 base 필드 확장

💡 예시:

48 89 c8    ; mov rax, rcx

; 48 = REX.W (64비트 오퍼랜드)


3️⃣ Opcode (명령어 코드)

📘 용어 설명:

Opcode는 CPU가 어떤 동작을 수행할지를 결정하는 핵심 코드이다.

대부분 1~3바이트이며, 필수 요소이다.

💡 예시:

b8 2a 00 00 00 ; mov eax, 42 (opcode + imm32)

4️⃣ ModR/M 바이트

📘 용어 설명:

ModR/M 바이트는 명령어의 오퍼랜드(레지스터/메모리)를 지정한다.

총 8비트 = 1바이트로 구성

🧱 비트 구조:

| 7-6 | 5-3 | 2-0 |

| Mod | Reg | R/M |


Mod: 주소지정 모드

Reg: opcode에서 사용되는 레지스터

R/M: 오퍼랜드 대상 (레지스터 or 메모리)

💡 예시:

89 d8 ; mov eax, ebx

; 89 = opcode, d8 = Mod=11, Reg=011 (ebx), R/M=000 (eax)


5️⃣ SIB 바이트 (Scale Index Base)

📘 용어 설명:

SIB는 메모리 주소 계산에 사용되는 보조 바이트이다.

ModR/M의 R/M 필드가 100이고 Mod ≠ 11일 때 사용된다.

🧱 비트 구조:

| 7-6 | 5-3  | 2-0  |

| Scale | Index | Base |


Scale: 인덱스 곱셈 계수 (00=1, 01=2, 10=4, 11=8)

Index: 인덱스 레지스터

Base: 기본 주소 레지스터

💡 예시:

mov eax, [rax + rcx*4]

; SIB = scale=10 (4), index=001 (rcx), base=000 (rax)


6️⃣ Disp (Displacement)

📘 용어 설명:

Disp는 메모리 주소 계산에 사용되는 상수 오프셋이다.

Mod 값에 따라 1바이트(disp8), 4바이트(disp32)로 사용됨

💡 예시:

mov eax, [rbp-4] ; disp8 = -4 = fc (2's complement)


7️⃣ Imm (Immediate)

📘 용어 설명:

Imm은 명령어에 포함된 즉시값 상수이다.

명령에 따라 1, 2, 4, 8바이트 크기를 가짐

💡 예시:

b8 2a 00 00 00 ; mov eax, 42

; b8 = opcode, 뒤의 4바이트는 imm32 = 0x2a


각 요소는 CPU가 opcode를 기준으로 필요한 만큼만 읽고 해석함으로써 명령어 경계를 정확히 판단할 수 있도록 설계되어 있다.
