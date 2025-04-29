# [  e8 d8 fe ff ff   ]

```
0x555555555183 : call getchar@plt   e8 d8 fe ff ff

; call opcode(1) : [ e8 ] + rel32(4) : [ d8 fe ff ff ]

```

## 

## 📌 용어

rel32 : Relative 32-bit signed offset

rel : relative  상대적인

32 = 4바이트 크기 (32비트)

signed int : 부호있는 정수 ( 앞/뒤 모두 jump 가능 )



## 📌 [+] e8 = call rel32

: call 명령어(opcode)

call rel32 (상대적인 32비트 오프셋으로 점프)

 - near call, rel32 방식으로 점프

e8은 현재명령어의 끝(rip) + rel32주소로 점프

32bit signed offset를 사용한다.


## 📌 [+] d8 fe ff ff  = rel32


현재 rip는 0x555555555183 다  

call getchar@plt(5바이트) 명령이 끝난 후에 주소는


0x555555555183 + 5(call getchar@plt = e8 d8 fe ff ff = 5바이트) = 0x555555555188 가 주소다


명령이 끝난 후 rip는  0x555555555188 다.

```
little-endian 변환

1   2  3 4     4  3  2 1

d8 fe ff ff  -> ff ff fe d8 = 0xffffed8

 
0xFFFFFED8  = 11111111 11111111 11111110 11011000 (32-bit)
0x00000000 ~ 0x7FFFFFFF → 양수
0x80000000 ~ 0xFFFFFFFF → 음수

➡️ 가장 높은 왼쪽 비트 = MSB: Most Significant Bit)가 1이면 → 음수!
➡️ 가장 높은 왼쪽 비트 = MSB: Most Significant Bit)가 0이면 → 양수!

따라서 0xFFFFFED8는 음수

2의  보수 
0x100000000 - 0xFFFFFED8 = 0x128
따라서 음수 0x128 = -0x128

```
따라서 d8 fe ff ff는 0x128이다

그래서 점프할 주소는 0x555555555188  + (-0x128) =  0x555555555060

call 0x555555555060(getchar@plt) 이다

```
rip = 0x555555555183 

rip = 0x555555555188

rip = 0x555555555060 = getchar@plt = <--
```

##  📌 최종적으로 다음와 같다.

call rip -> call  getchar@plt ->  call 0x555555555060 -> e8 d8 fe ff ff


#  📌 c8 cw/cd


📌 용어
```
cw : Code Word	  ; code operand가 32bit 크기

cd : Code Doubleword	 ; code operand가 16bit 크기

e8 cw → "call with 16-bit code operand"  → call rel16

e8 cd → "call with 32-bit code operand" → call rel32
```

✔️ Protected Mode와 Real Mode의 차이

```
모드	             설명

Real Mode(call rel16)	     : 16비트 주소 체계 (옛날 DOS 스타일) → call rel16 사용 

Protected Mode(call rel32) : 64비트	현대 시스템, 기본적으로 call rel32 사용
```

* 32/64bit는 call rel32사용하고 64bit 부터는 rel32만 사용


## 🔹 Real Mode란?

가장 초기의 x86 CPU 모드 (8086 CPU)

→ BIOS나 DOS 같은 시스템에서 사용됨

주소 계산: segment × 16 + offset (총 20비트 → 1MB)

보안 없음, MMU 없음, 페이징 없음

단순하고 빠르지만 위험

📌 사용 예: 부트로더 (ex. MBR), BIOS, 초기 16비트 어셈블리

##  🔹 Protected Mode란?

메모리를 보호하고, 현대 운영체제를 구현하기 위한 CPU 모드

→ 80286 이후부터 등장

32비트 또는 64비트 주소 체계

MMU + 페이징 + Ring-based 권한 분리

각 프로세스별 독립된 주소 공간 제공

📌 사용 예: 현대 리눅스, 윈도우, macOS


### 🔍 Real Mode vs Protected Mode

```
| 항목             | Real Mode         | Protected Mode       
|-----------------------------------------------------------------
| 등장 시기        8086 (1981~)          80286~80386 이후       
| 주소 방식        16bit 세그먼트:오프셋  32/64bit 가상 주소     
| 메모리 제한      1MB                   수 GB~TB               
| 보안 기능        없음                  Ring 0~3, 페이징, MMU 
| OS 가능성        BIOS, DOS             리눅스, 윈도우, macOS  

📌 Real Mode는 초기 부트에 사용되고
📌 Protected Mode는 OS 실행을 위한 모드

```

✅ Protected Mode의 핵심: Ring 구조 (권한 레벨)

```
Ring   권한       용도

0      최고권한   커널 모드
3      최저권한   유저 모드

📌 x86에서는 Ring 0 ~ Ring 3이 있고,
일반 프로그램은 Ring 3, 커널은 Ring 0에서 실행됩니다.
```


✅ 2. User와 Kernel의 구별: 권한 레벨 + 주소 공간 분리

```
구분	            User Mode	         Kernel Mode

Ring	            Ring 3	            Ring 0
주소 공간	        0x00000000~...	        0xC0000000~ or 높은 영역
권한	            제한됨	             모든 메모리 접근 가능
syscall	        가능 ❌직접 X	       가능 ✅


→ 유저 모드에서 커널 함수 호출 시

int 0x80, syscall 등을 통해 컨트롤 진입해야 합니다.

직접 jump나 call로 넘어가면 #GP 예외로 강제 종료됩니다.

```

✅  GS 레지스터의 값은 "세그먼트 셀렉터"이다

세그먼트 레지스터 (GS, FS, DS 등)에 저장되는 값은:

"세그먼트 셀렉터(Segment Selector)" 라고 부릅니다.


GS = 0x2B 같은 값은 단순한 주소가 아니라,

→ GDT/LDT 테이블에서 세그먼트를 참조할 수 있는 

인덱스 구조이기 때문입니다.



📦 세그먼트 셀렉터(Segment Selector)의 구조 (16bit)

```
15       3  2    1   0
+-----------+----+----+
| Index     | TI | RPL|
+-----------+----+----+

15 ───────────────3  2  1  0
[ Index (13 bits) ] TI RPL



필드	크기	설명

Index	 : 13비트	GDT/LDT에서 디스크립터 위치 ( 	GDT 또는 LDT에서 사용할 디스크립터 슬롯 번호 )

TI (Table Indicator)    :	1비트	0 = GDT, 1 = LDT

RPL (Requestor Privilege Level)	   : 2비트	Requestor Privilege Level : 현재 접근 권한 (Ring 0~3)


- GDT (Global Descriptor Table): 시스템 전체 공용

- LDT (Local Descriptor Table): 각 프로세스 개별 가능

- TI (Table Indicator): 0 = GDT, 1 = LDT

```

즉, GS에 들어가는 값은 = **세그먼트를 선택할 수 있는 번호(Selector)**입니다.

그래서 "GS는 세그먼트 셀렉터다"라고 부르는 거예요.

### 🔍 GS는 왜 세그먼트 셀렉터인가?

- GS는 Segment Register 중 하나 (General Segment)
- GS 레지스터의 값은 단순 숫자가 아니라 → "Segment Selector"
- Selector는 GDT/LDT 테이블에서 어떤 세그먼트를 참조할지 지정하는 포인터
- 16비트 구조: [Index | TI | RPL]

📌 그래서 GS는 "세그먼트 셀렉터 역할을 하는 레지스터"다.
📌 FS/GS는 특히 Thread Local Storage (TLS), 커널 컨텍스트에서 많이 사용됨


📌 용어
```
RPL | Requestor Privilege Level | 세그먼트 셀렉터의 하위 2비트, 현재 코드 실행자의 권한

CPL | Current Privilege Level | CS 세그먼트 셀렉터의 RPL과 동일 (실행 중인 코드의 Ring)

DPL | Descriptor Privilege Level | 세그먼트 디스크립터 안에 저장된 권한 값 (해당 메모리 영역의 보호 수준)

```



✅ GS 레지스터의 셀렉터에서 RPL 필드 확인

GS 레지스터 값 구조 (16비트 세그먼트 셀렉터):

```
15       3 2 1 0
+-----------+---+
| Index     |TI |RPL|
+-----------+---+
```

RPL = 하위 2비트 (비트 0~1)

00 → Ring 0

11 → Ring 3



✅ 예시 1: gs = 0x0020

Ring 0 상태에서 gs = 0x20 → RPL = 00 (Ring 0)

```
0x0020 = 0000 0000 0010 0000
                          ^^
                          RPL = 00
```



✅ 예시 2: gs = 0x002B

Ring 3 상태에서 gs = 0x2B → RPL = 11 (Ring 3)

```
0x002B = 0000 0000 0010 1011
                          ^^
                          RPL = 11

```


### 🔍 세그먼트 셀렉터 0x2B 해석 

- 0x2B = 0010 1011 (16bit)
- RPL = 11 = Ring 3
- TI = 0 → GDT (Global Descriptor Table)
- Index = bits 15:3 = 0000000000101 = 5

📌  0x2B는 GDT의 5번 디스크립터를 Ring 3 권한으로 참조함



✅ GDT란? (Global Descriptor Table)

GDT는 보호 모드(Protected Mode)에서 

**세그먼트의 정보(주소, 크기, 권한 등)**를 정의해둔 테이블

CPU는 프로그램이 세그먼트 레지스터(CS, DS, GS 등)를 

사용할 때마다 GDT를 참조

```
세그먼트 레지스터  | 의미         | GDT에서 하는 역할

CS               | 코드 세그먼트 | 명령어 fetch 영역

DS, ES, FS, GS   | 데이터 접근   | 메모리 접근 시 기준

SS               | 스택 세그먼트 | 스택 위치와 크기 정의

```


### 🔍 GDT란?

- GDT = Global Descriptor Table
- 목적: 보호 모드에서 세그먼트(코드, 데이터 등) 정의
- 구성:
  - 각 엔트리 = 8바이트 디스크립터
  - base 주소, 크기, 권한, 타입 포함

📌 세그먼트 레지스터(CS, DS, GS 등)는 GDT index를 참조함

📌 GDT를 통해 메모리 접근 권한과 경계를 제어함

📌 Real Mode와 달리 주소 보호, 권한 분리 가능




## ✅ GDT의 구성

- 배열 구조: 각 엔트리는 8바이트(64비트)

- 각 엔트리 = 하나의 세그먼트 디스크립터

📌 디스크립터 종류:
 * 코드 세그먼트
 * 데이터 세그먼트
 * TSS (Task State Segment)
 * LDT 디스크립터 등



## 📦 GDT는 왜 필요할까?

🔍 Real Mode에서는?

세그먼트:오프셋으로 물리 주소 계산 (ex: 0x1234:0x0002)

🔍 Protected Mode에서는?

📌 세그먼트 자체에:
* Base 주소
* Limit (크기)
* DPL (권한 등급)
* Type/속성 을 정의해서 보호 기능 제공

📌 이걸 모아둔 테이블이 바로 GDT입니다.




## ✅ GDT 디스크립터 구조 (8바이트 = 64비트)



```
| 바이트 위치     | 필드 이름                   | 크기  | 설명                           |
|----------------|--------------------------  |-------|--------------------------------|
| 0~1 (16비트)    | **Limit[15:0]**           | 2B    | 세그먼트 크기의 하위 16비트      |
| 2~3 (16비트)    | **Base[15:0]**            | 2B    | 시작 주소의 하위 16비트          |
| 4 (8비트)       | **Base[23:16]**           | 1B    | 시작 주소의 중간 바이트          |
| 5 (8비트)       | **Access Byte** (Type/DPL)| 1B    | 권한 정보 (DPL, Type 등 포함)   |
| 6 (4+4비트)     | Flags + Limit[19:16]      | 1B    | 상위 Limit + Flags             |
| 7 (8비트)       | **Base[31:24]**           | 1B    | 시작 주소의 상위 바이트         |
```


```
gdt_code:
    dw 0xFFFF          ; Limit[15:0]  → 하위 크기
    dw 0x0000          ; Base[15:0]   → 시작 주소 하위
    db 0x00            ; Base[23:16]  → 중간 바이트
    db 10011010b       ; Access Byte (Type + S + DPL + P)
    db 11001111b       ; Flags(4) + Limit[19:16]
    db 0x00            ; Base[31:24]  → 상위
```


🔍 필드 분석

📌 Base (세그먼트 시작 주소)

Base[15:0] = 0x0000

Base[23:16] = 0x00

Base[31:24] = 0x00

⟶ 전체 Base = 0x00000000

👉 이 세그먼트는 물리 주소 0x00000000부터 시작


📌 Limit (세그먼트 크기)

Limit[15:0] = 0xFFFF

Limit[19:16] = 0xF

⟶ 전체 Limit = 0xFFFFF = 1MB

✅ Granularity(4KB 단위) 플래그가 켜져 있으면:

```
0xFFFFF × 4KB = 4GB - 1B

```


📌 Type + DPL (Access Byte = 10011010b)

```
비트 | 필드 | 설명
7 | P = 1 | Present (사용 가능)
6-5 | DPL = 00 | Descriptor 권한 = Ring 0
4 | S = 1 | Code/Data 구분 (1=일반 세그먼트)
3-0 | Type = 1010 | Code Segment, readable, not conforming
```

📌 Flags (1100)

```
비트 | 의미
G = 1 | Granularity = 4KB 단위
D = 1 | 32-bit segment
0 | AVL = 0 (예약)
L = 0 | 64비트 segment 아님 (for legacy code)
```


### 📊 GDT 디스크립터 구조 (예: 코드 세그먼트)
```
Base:
- Base = Base[15:0] + Base[23:16] + Base[31:24]
- ex) 0x00000000 → 세그먼트 시작 주소

Limit:
- Limit = Limit[15:0] + Limit[19:16]
- Granularity = 4KB 단위면: Limit × 4KB

Access Byte (Type/DPL):
- P = Present (1 = 사용 가능)
- DPL = Descriptor Privilege Level (0~3)
- S = 1 (Code/Data 세그먼트)
- Type = 1010 (Code, readable)

Flags:
- G = 1 (4KB 단위)
- D = 1 (32bit)
- L = 0 (64bit 아님)
```

✅ 실제 메모리 예시: 8바이트 바이트값

```
GDT[5] = FF FF 00 00 00 9A CF 00
         ↑  ↑   ↑  ↑  ↑  ↑  ↑ ↑
        limit base base typ lim flg base

```

이 구조를 기반으로 CPU는:

Base + offset 계산

접근 제한 검사

권한 비교 (DPL vs CPL/RPL)

을 모두 수행합니다.


🔧 GDT 선언 예제 (nasm)

```
gdt_start:
    dq 0                    ; null descriptor
    dw 0xFFFF, 0x0000, 0x9A00, 0x00CF   ; code segment (Ring 0)
    dw 0xFFFF, 0x0000, 0x9200, 0x00CF   ; data segment (Ring 0)
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start


```

🔧 NASM 코드 예제 (완성 흐름)

```
[BITS 16]
org 0x7c00          ; BIOS가 로딩하는 주소

start:
    cli             ; 인터럽트 비활성화
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7c00

    ; GDT 로딩
    lgdt [gdt_descriptor]

    ; 보호 모드 진입 준비: CR0의 PE 비트 설정
    mov eax, cr0
    or eax, 1
    mov cr0, eax

    ; 32비트 Protected Mode 진입 (FAR jump)
    jmp 0x08:protected_mode_start

; GDT 정의
gdt_start:
    dq 0                          ; Null Descriptor
    dw 0xFFFF, 0x0000, 0x9A00, 0x00CF  ; Code Segment (Ring 0)
    dw 0xFFFF, 0x0000, 0x9200, 0x00CF  ; Data Segment (Ring 0)
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start

; 32비트 Protected Mode 코드
[BITS 32]
protected_mode_start:
    mov ax, 0x10       ; data segment selector
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax

    mov esp, 0x90000   ; 스택 초기화

    ; 여기부터 보호 모드에서의 프로그램 실행
    hlt

```


✅ 보호 모드 진입 후에는?

32비트 코드 실행 가능

Ring 0~3 구분 가능

paging 기능 활성화 가능 (추가 설정 필요)

멀티태스킹 지원 기반이 마련됨

```
; 1단계 부트로더 (512바이트 MBR, GRUB 없이 직접 보호 모드 진입)
; stage1.asm
[BITS 16]
[ORG 0x7c00]             ; BIOS는 MBR을 0x7c00에 로딩함

start:
    cli
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x7c00

    ; Stage2 로딩 (0x0000:0x8000 = 0x8000)
    mov si, 0            ; sector = 0
    mov dl, 0x00         ; 부팅 드라이브
    mov bx, 0x8000       ; 로딩 위치
    call load_stage2

    jmp 0x0000:0x8000    ; stage2 시작

load_stage2:
    mov ah, 0x02         ; BIOS read sector
    mov al, 1            ; read 1 sector
    mov ch, 0            ; cylinder 0
    mov cl, 2            ; sector 2 (stage2는 MBR 다음)
    mov dh, 0            ; head 0
    int 0x13
    ret

; 부트 시그니처 (필수!)
times 510 - ($ - $$) db 0
    dw 0xAA55

; ===== stage2.asm: 2단계 부트로더 (Protected Mode 진입) =====
[BITS 16]
[ORG 0x8000]

stage2:
    cli
    lgdt [gdt_descriptor]
    mov eax, cr0
    or eax, 1
    mov cr0, eax
    jmp 0x08:protected_mode

; GDT 정의 (code=0x08, data=0x10)
gdt_start:
    dq 0
    dw 0xFFFF, 0x0000, 0x9A00, 0x00CF  ; code segment
    dw 0xFFFF, 0x0000, 0x9200, 0x00CF  ; data segment
gdt_end:

gdt_descriptor:
    dw gdt_end - gdt_start - 1
    dd gdt_start

; 보호 모드 진입 코드
[BITS 32]
protected_mode:
    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax
    mov ss, ax

    mov esp, 0x90000
    mov ebx, msg
    call print_string
    hlt

print_string:
.next:
    mov al, [ebx]
    test al, al
    jz .done
    mov ah, 0x0E
    int 0x10
    inc ebx
    jmp .next
.done:
    ret

msg db "[✔] Protected Mode 진입 성공!", 0

```
