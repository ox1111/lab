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

- Mod (Mode): 주소 모드 지정 (메모리 or 레지스터)
  - 00 = 메모리, 디스플 없음
  - 01 = 메모리, 디스플 1바이트
  - 10 = 메모리, 디스플 4바이트
  - 11 = 레지스터 모드

- Reg: 연산에 사용될 레지스터 or opcode 확장
  - 예: /0 = INC, /5 = SUB, /7 = CMP 등

- R/M: 실제 오퍼랜드 레지스터 또는 메모리 주소
  - Mod=11일 경우 → 일반 레지스터
  - Mod≠11일 경우 → 메모리로 해석

 💡 참고
/0 = INC 이란?

일부 opcode는 Reg 필드가 "이 명령의 서브타입"을 결정해요.

예: FF /0 = INC, FF /1 = DEC



