✅ 1. LOCK prefix의 의미

LOCK은 다중 CPU 환경(= 멀티코어 시스템)에서 공유 메모리 값을 안전하게 조작하려고 사용됩니다.

🔐 “락을 건다”는 건?

여러 CPU가 동시에 같은 메모리 주소를 조작하려 할 때,

하나의 CPU가 작업 중이면 다른 CPU는 그 메모리에 접근 못하게 막는 것

📌 즉, 메모리 연산의 원자성(atomicity) 보장

→ 중간에 다른 CPU가 끼어들 수 없도록 막음

💡 락을 걸 수 있는 “메모리를 변경하는 연산”이란?

INC, DEC (증감)

XCHG (교환)

ADD, SUB (연산)

OR, AND, XOR

MOV은 제외! (메모리에 단순히 쓰는 것만으론 무조건 LOCK 못 씀)

조건: 대상이 반드시 [메모리 주소] 이어야 함!

✅ 유효한 LOCK 예제

예 1: LOCK INC DWORD PTR [RAX]

```
f0 ff 00       ; LOCK + INC [RAX]

```

바이트	설명

f0	: LOCK prefix

ff	: 그룹 opcode

00	: ModR/M: Mod=00, Reg=000 (/0 = INC), R/M=000 (RAX)

👉 DWORD PTR [RAX] = RAX가 가리키는 메모리 값을 증가시키는 연산

👉 LOCK을 통해 다른 CPU가 동시에 [RAX]를 수정 못 하게 막음


✅ 1. FF는 INC인가요?

✔️ 답: 부분적으로는 맞습니다.

FF는 그룹 opcode입니다.

단독으로 의미가 정해지는 게 아니라, 
**뒤에 오는 ModR/M의 Reg 필드(/n)**에 따라 명령어가 달라져요.

🔍 예: FF /n → 의미는 /n 값으로 결정

/n (Reg 필드) ;	명령어의미

/0 = 000	; INC r/m

/1 = 001	; DEC r/m

/2 = 010	; CALL r/m

/3 = 011	; CALLF m16:16/32

/4 = 100	; JMP r/m

/5 = 101	; JMPF m16:16/32

/6 = 110	; PUSH r/m

✅ 그래서 FF 00에서:

FF = 그룹 opcode

Reg = 000 (== /0) → INC

Mod = 00, R/M = 000 → [RAX]

→ 즉 INC DWORD PTR [RAX]

✅ 2. 00이 왜 RAX인가요?

→ 00은 ModR/M 바이트입니다.

 
비트구성	       필드         값	   ; 의미

7~6	           Mod	       00	   ; 메모리 모드, disp 없음

5~3	           Reg(/n)	   000	 ; /0 = INC

2~0	           R/M	       000	 ; RAX (또는 [RAX])



📌 Mod=00 & R/M=000 = [RAX] 메모리 주소
(레지스터 RAX를 메모리 주소처럼 사용)


✅ 1. 왜 R/M = 000이면 RAX가 아니라 **[RAX]**인가?

✔️ 답: Mod 필드가 결정합니다.


Mod값	  의미

00    	메모리 접근, disp 없음

01    	메모리 접근, disp8 있음

10	    메모리 접근, disp32 있음

11    	레지스터 직접 지정 ✅

🔍 예시 비교:


바이트	   의미	             해석

FF 00	   Mod=00, R/M=000	; [RAX]

FF C0	   Mod=11, R/M=000	; RAX

즉, Mod=00~10은 메모리,

Mod=11이면 레지스터를 의미합니다.

✅ 2. 그럼 왜 DWORD PTR [RAX] 이렇게 표현해요?

메모리를 접근할 땐, CPU는 반드시 **접근할 데이터 크기(비트 수)**를 알아야 합니다.

📌 이유: [RAX]는 주소일 뿐, 몇 비트를 읽거나 쓸지는 명확하지 않기 때문이에요!

🔎 그래서 붙는 접두사들:

크기	표기 예

8비트	BYTE PTR [RAX]

16비트	WORD PTR [RAX]

32비트	DWORD PTR [RAX]

64비트	QWORD PTR [RAX]



🔄 예제 비교

명령어	의미	              해석

INC RAX	                 레지스터	RAX 값 1 증가

INC [RAX]	               메모리	RAX가 가리키는 주소의 값 1 증가

INC DWORD PTR [RAX]	     메모리 + 크기 지정	RAX가 가리키는 4바이트 값 증가


### 🔍 ModR/M에서 [RAX]인지 RAX인지 어떻게 구분하나요?

- Mod 필드가 핵심!
  - Mod=11 → 레지스터
  - Mod=00~10 → 메모리 접근
- R/M=000 → RAX (레지스터 or 주소 역할)

📌 FF 00 = INC DWORD PTR [RAX]
- FF = 그룹 opcode
- /0 = INC
- Mod=00 → 메모리 접근
- R/M=000 → [RAX]
- 메모리 접근이므로 크기 지정 필요 → DWORD PTR


✅ 1. INC [RAX] vs INC DWORD PTR [RAX] vs INC RAX

📌 용어 차이부터!

표현	              뜻 (요약)

INC RAX	            ; RAX 레지스터 값 자체를 1 증가시킴 (레지스터 연산)

INC [RAX]	          ; RAX가 가리키는 주소의 메모리 값을 1 증가시키는데, 어떤 크기인지 명확하지 않음

INC DWORD PTR [RAX]	; [RAX] 주소에 있는 **4바이트 메모리 값(DWORD)**을 1 증가시킴 (정확한 크기 명시)

❓그럼 INC [RAX]도 되잖아요?

네, 되긴 하지만 어셈블러 수준에서는 ambiguous (모호) 합니다.

메모리를 읽어야 하는데, 8비트인지 16비트인지 32비트인지 64비트인지 알 수 없기 때문이에요.

그래서 NASM 같은 어셈블러는 컴파일 오류 내거나 기본값(DWORD)을 정해버립니다.

그래서 명확하게 BYTE, WORD, DWORD, QWORD를 붙여주는 게 규칙입니다.


✅ 2. 그럼 왜 64비트인데 DWORD PTR인가요? → QWORD 아니고?

정답은: 명령어가 32비트 연산이기 때문입니다.

레지스터 이름도 EAX, EBX, r8d 이런 식이면 = 32비트 연산입니다.

🔎 해석: F0 FF 00 = LOCK INC DWORD PTR [RAX]

바이트	   의미

F0	    ; LOCK prefix (멀티코어 보호)

FF	    ; 그룹 opcode (/0 = INC)

00	    ; Mod=00, Reg=/0, R/M=000 → [RAX]


메모리 대상이고, 연산 크기는 따로 정하지 않았기 때문에 기본은 DWORD = 32비트입니다.


📌 어셈블러가 판단해서 "이건 DWORD 접근이야" 라고 자동 해석하거나, 우리가 DWORD PTR 명시함


✅ 언제 QWORD PTR을 써야 하나요?

INC QWORD PTR [RAX] → 메모리 주소 [RAX]의 8바이트 정수 값을 증가시킬 때

즉, 64비트 정수 데이터를 다룰 땐 명확하게 QWORD를 지정해야 합니다


### 🔍 INC [RAX], INC DWORD PTR [RAX], INC RAX 차이

- INC RAX: 64비트 레지스터 자체 값을 증가
- INC [RAX]: RAX가 가리키는 메모리 값 증가 → 크기 불분명
- INC DWORD PTR [RAX]: RAX가 가리키는 메모리의 4바이트 값 증가 (명확히 32비트)

📌 어셈블러는 메모리 연산 시 명확한 크기 정보(BYTE/WORD/DWORD/QWORD)가 필요함

### 🔍 왜 64비트인데 DWORD인가?

- 레지스터 이름이 `EAX`, `EBX`, `r8d`이면 = 32비트 연산
- 메모리 접근도 기본은 `DWORD`
- 64비트로 하고 싶다면: `INC QWORD PTR [RAX]`



🔍 핵심 개념 먼저 비교

표현	                  설명

INC RAX	                ; RAX라는 레지스터에 저장된 값을 1 증가

INC [RAX]	              ; RAX에 저장된 주소에 있는 메모리 값을 1 증가

INC DWORD PTR [RAX]	    ; RAX가 가리키는 주소의 4바이트 메모리 값을 1 증가 (크기 명확히)

INC QWORD PTR [RAX]	    ; RAX가 가리키는 주소의 8바이트 메모리 값을 1 증가 (64비트)

예시 상황:

✅ 예시로 그림처럼 설명해볼게요


```
mov rax, 0x601000        ; RAX = 0x601000
mov dword [rax], 123     ; [0x601000] = 123 (4바이트 저장)
inc dword ptr [rax]      ; [0x601000] 값을 1 증가시킴 → 124

```

이때 메모리 구조 (그림):
```
메모리 주소:       값:
0x601000          0x0000007B   ← 123 (4바이트)
          ↑
         RAX는 이 주소를 가리킴

```

🔁 INC DWORD PTR [RAX] → 위의 값이 124(0x7C) 로 바뀜


❗ 그런데 만약 INC RAX를 했다면?

```
mov rax, 0x601000
inc rax                 ; RAX = 0x601001


```

→ 메모리 내용은 변하지 않음!
단지 RAX 값 자체가 +1 되어 다른 주소를 가리키게 됨


✅ 비유로 설명하면:

코드	                 실제 의미	                           ; 비유

INC RAX	               RAX = RAX + 1	                     ; 손가락이 가리키는 방향이 바뀜

INC [RAX]	             RAX가 가리키는 주소에 있는 값을 +1	   ; 손가락이 가리키는 물건의 숫자 변경

INC DWORD PTR [RAX]	   4바이트 값으로 명확히 +1	             ; 그 물건의 "정확한 크기"를 지정하고 변경


### 🔍 INC RAX vs INC [RAX] vs INC DWORD PTR [RAX]

1. INC RAX
   → RAX 값(숫자 자체)을 1 증가
   → 메모리는 안 건드림

2. INC [RAX]
   → RAX가 가리키는 주소에 있는 메모리 값을 증가
   → 몇 바이트인지는 불분명 → 에러 가능성 있음

3. INC DWORD PTR [RAX]
   → RAX가 가리키는 주소에 있는 4바이트 값을 증가
   → 안전하고 정확한 방식 (보통 이걸 사용)

📌 [RAX]는 '주소', RAX는 '값'
📌 메모리 접근 시에는 BYTE/WORD/DWORD/QWORD 크기 명시 필수



❓ mov rax, 0x601000
이건 RAX에 주소를 넣는 건가요? 값 자체를 넣는 건가요?


✅ 정답:
RAX에 그냥 '값'을 넣는 것이에요.

하지만 그 값이 주소처럼 사용될 수도 있고,
그냥 정수 값으로 연산할 수도 있습니다.


💡 핵심은 → 그 "값을 어떻게 쓰느냐"에 따라 의미가 달라집니다!
📌 예 1: 주소처럼 쓰는 경우

```
mov rax, 0x601000     ; RAX ← 0x601000
mov dword [rax], 123  ; RAX를 '주소'로 해석 → 그 주소의 메모리값에 123 저장
```

→ 여기선 RAX가 주소 역할을 하죠
[RAX] ← 대괄호가 붙었기 때문에 “메모리를 가리킨다”는 의미로 해석


📌 예 2: 그냥 값으로 쓰는 경우
```
mov rax, 0x601000     ; RAX ← 0x601000
add rax, 1            ; 그냥 숫자 +1 → RAX는 0x601001이 됨

```
→ 여기선 단순히 정수 연산에 사용되는 값입니다
“메모리 주소”란 의미는 전혀 없음



🧠 비유로 쉽게 이해하기
mov rax, 0x601000 = “이 숫자를 RAX에 넣는다”

근데 mov [rax], ... 같이 쓰면 → “그 숫자를 주소로 해석한다”

즉, 값인지 주소인지는 '그 이후 문맥'이 결정


### mov rax, 0x601000 의 의미는?

- 그냥 숫자 0x601000을 RAX에 넣는 것
- RAX가 주소냐 값이냐는, 그 값을 **어떻게 쓰느냐에 따라 달라짐**

#### 예:
- mov [rax], 123 → RAX는 주소로 쓰임 (메모리 쓰기)
- add rax, 1     → RAX는 숫자로 쓰임 (연산 대상)

📌 대괄호 [ ] 가 붙으면 = "이건 주소다!"
📌 안 붙으면 = "이건 값 자체다!"


🎯 어셈블리 MOV의 방향 구조

```
mov destination, source
        ←       ←
     (왼쪽으로 복사됨)


```

✅ 예제 1: mov rax, [rbx]

뜻: rbx가 가리키는 메모리 주소에 있는 값을 읽어서 rax에 저장한다


구성	        의미

[rbx]	        rbx에 들어있는 주소의 메모리 값

rax         	값을 저장할 대상 레지스터

전체 의미	    "메모리 → 레지스터" 방향의 복사

```
rbx = 0x601000  
[0x601000] = 12345678

→ mov rax, [rbx]
→ 결과: rax = 12345678

```

✅ 예제 2: mov [rax], rbx

뜻: rbx의 값을 rax가 가리키는 메모리 주소에 저장한다


구성	           의미
rbx	            ; 복사할 값
[rax]	          ; rax가 가리키는 메모리 주소에 저장

전체 의미	"레지스터 → 메모리" 방향의 복사

```
rbx = 0x12345678  
rax = 0x601000

→ mov [rax], rbx
→ 결과: [0x601000] = 0x12345678
```

🔁 정리: 방향성 비교

명령어	              방향	              의미 요약

mov rax, [rbx]	   메모리 → 레지스터	    메모리에서 값을 읽어온다

mov [rax], rbx   	레지스터 → 메모리	    값을 메모리에 저장한다

mov rax, rbx	    레지스터 → 레지스터  	단순한 레지스터 간 복사

### 🔄 mov 방향성 핵심

mov destination, source

- mov rax, [rbx]   → [rbx]의 메모리 값을 rax로 복사
- mov [rax], rbx   → rbx의 값을 [rax] 메모리에 저장

📌 [ ] ← 대괄호가 있으면 '주소(메모리)'라는 의미
📌 왼쪽이 목적지, 오른쪽이 원본!






예 2: LOCK ADD DWORD PTR [RBX], EAX


```
f0 01 03       ; LOCK + ADD [RBX], EAX

```

바이트	설명

f0 :	LOCK

01 :	ADD r/m32, r32

03 :	ModR/M: Mod=00, Reg=000 (EAX), R/M=011 (RBX)


❌ 유효하지 않은 예 (무의미한 LOCK)

```
f0 90    ; LOCK NOP → 의미 없음
f0 c3    ; LOCK RET → 무효

```

CPU는 대부분 이런 경우 LOCK을 무시하고 실행합니다.


### 🔐 LOCK prefix란?

- 다중 CPU 환경에서 메모리 연산의 원자성을 보장하기 위한 prefix

- 반드시 메모리를 **변경**하는 명령 + 메모리 대상이어야 유효

#### ✅ 유효한 예제:

- f0 ff 00 = LOCK INC DWORD PTR [RAX]

- f0 01 03 = LOCK ADD DWORD PTR [RBX], EAX

#### ❌ 무효한 예제:

- f0 90 = LOCK NOP (의미 없음)

- f0 c3 = LOCK RET (의미 없음)


✅ 용어

✅ 전체 구조: ModR/M 바이트란?

ModR/M 바이트는 8비트(1바이트)로, 명령어의 오퍼랜드(레지스터/메모리)를 지정하는 데 사용됩니다.

🧱 구조:

```
| 7 6 | 5 4 3 | 2 1 0 |
| Mod | Reg   | R/M   |

```
🔍 각각의 의미와 약자

필드	비트 위치	약자의미	          설명

Mod	  비트 7~6	Mode            	오퍼랜드가 메모리인지, 레지스터인지, 디스플레이스먼트 포함 여부

Reg	  비트 5~3	Register	        소스 레지스터 또는 opcode 확장 필드

R/M	  비트 2~0	Register/Memory	  대상 오퍼랜드가 어떤 레지스터 또는 메모리 주소인지

🧠 예시 해석: ModR/M = 00 000 000 (== 0x00)

필드	값	  해석

Mod	  00	  메모리 주소 (디스플레이스먼트 없음)

Reg	  000	  연산 대상 = /0, 즉 INC일 때 의미 (또는 레지스터 EAX)

R/M	  000	  [RAX] (메모리 주소로 해석)


→ 명령어: LOCK INC DWORD PTR [RAX]

→ 전체 바이트: f0 ff 00

### 🔍 ModR/M 구성 필드 설명

Mod (Mode): 주소 모드 지정 (메모리 or 레지스터)
  
00 = 메모리, 디스플 없음
  
01 = 메모리, 디스플 1바이트

10 = 메모리, 디스플 4바이트

11 = 레지스터 모드


Reg: 연산에 사용될 레지스터 or opcode 확장

예: /0 = INC, /5 = SUB, /7 = CMP 등

R/M: 실제 오퍼랜드 레지스터 또는 메모리 주소

  - Mod=11일 경우 → 일반 레지스터
  - 
  - Mod≠11일 경우 → 메모리로 해석

 💡 참고
/0 = INC 이란?

일부 opcode는 Reg 필드가 "이 명령의 서브타입"을 결정해요.

예: FF /0 = INC, FF /1 = DEC



