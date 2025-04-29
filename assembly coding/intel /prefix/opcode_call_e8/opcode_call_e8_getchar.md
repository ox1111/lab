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

call rip -> call  getchar@plt -> e8 d8 fe ff ff  ->  call 0x555555555060


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
구분	        User Mode	         Kernel Mode

Ring	        Ring 3	            Ring 0
주소 공간    0x00000000~...      0xC0000000~ or 높은 영역
권한	        제한됨	             모든 메모리 접근 가능
syscall	가능 ❌ 직접 X	가능 ✅
```








 


