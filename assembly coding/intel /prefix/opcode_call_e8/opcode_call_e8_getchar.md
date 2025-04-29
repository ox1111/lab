[  e8 d8 fe ff ff   ]

```
0x555555555183 : call getchar@plt   e8 d8 fe ff ff

; call opcode(1) : [ e8 ] + rel32(4) : [ d8 fe ff ff ]

```

📌 [+] e8 = call rel32

: call 명령어(opcode)

call rel32 (상대적인 32비트 오프셋으로 점프)

 - near call, rel32 방식으로 점프

e8은 현재명령어의 끝(rip) + rel32주소로 점프

32bit signed offset를 사용한다.


📌 [+] d8 fe ff ff  = rel32


현재 rip는 0x555555555183 다  call getchar@plt(5바이트) 명령이 끝난 후에 주소는


0x555555555183 + 5(call getchar@plt = e8 d8 fe ff ff = 5바이트) = 0x555555555188 가 주소다


명령이 끝난 후 rip는  0x555555555188 다.

```
little-endian 변환

1   2  3 4     4  3  2 1

d8 fe ff ff  -> ff ff fe d8 = 0xffffed8


2의  보수 

0x100000000 - 0xFFFFFED8 = -0x128

```
따라서 d8 fe ff ff는 0x128이다

그래서 점프할 주소는 0x555555555188  + (-0x128) =  0x555555555060

call 0x555555555060(getchar@plt) 이다

```
rip = 0x555555555183 

rip = 0x555555555188

rip = 0x555555555060 = getchar@plt = <--
```

 최종적으로 다음와 같다.

call rip 는 call 0x555555555060  = call  getchar@plt  = e8 d8 fe ff ff  

