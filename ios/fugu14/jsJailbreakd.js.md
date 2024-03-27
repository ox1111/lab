# Fugu14
## [ Fugu14에 있는 runJailbreakd.js 이야기 ]

```
amfid (Apple Mobile File Integrity Daemon)는 
실행파일의 무결성을 검사한다.

실행파일의 코드 서명을 확인하고 신뢰 가능한지 검사하는데 
만약 인증 하지 않은 실행파일 실행하면 차단된다.

해커는 
jailbreakd라는 실행파일을 안정적으로 실행하고 싶어해.

jailbreakd는 인증되지 않는 친구라서 
인증 된 것 처럼 속여야 실행 할 수 있다.

Fugu14는 5개의 exploit이 연결되어 실행한다.
그중 하나의 이야기다.

Fugu14은 
Fugu14_Setup.ipa과 Fugu14_Pwn.ipa  2개의 앱을 설치한다.

우선 Fugu14_Setup.ipa을 설치한다

이 후 Fugu14_Pwn.ipa을 설치 후 실행하면 

runJailbreakd.js를 리소스에 숨겼다가 
앱와 함께  iPhone 들어가고 다시  /tmp/jailbkreakd.js에 복사한다.
 
그리고 Fugu14_Pwn을 실행하는 순간 
swift에서 runJSFile함수 통해서 /tmp/jailbreakd.js을 실행한다.

이때 이전 과정은 생략했지만 
취약점을 통해  root 상태에서 실행한다.

Jailbreakd.js의 주요 임무는 jailbreakd 데몬을 실행하는데 있다.

여기서 문제가 ..
앞서 언급한 

amfid 이 친구는 
듣보잡인 jailbreak을 무결성 검사에 통과시켜줄 리 만무하다.

시작하기전 알아야 할 것이 있어

take port 개념이 있는데 
만약 take port에 접근 가능하면 
Process 관련 가상메모리 , thread등 접근 권한이 부여되고
해당 process의 메모리 정보를 읽거나 쑬 수 있고 , thread를 생성하거나
종료 할 수 도 있어

아무튼 아주아주 중요해.

해커는 amfid의 pid를 가져와 
그리고  task_for_pid함수로 take port가져와
 
즉
Amfid 의 Take port와 
process가 사용하는 thread의 take port도 전부 가져올 수 있어

그렇게 amfid의 메모리 공간에 침투를 시작해.

이제 다른 용도의 take port을 생성해서 받아
예외 처리할 때 사용할 take port야.

task_set_exception_ports 함수를 통해서 만약에 예외 처리할 상황이 오면
“위 생성한 예외 처리용 take port로 해당 메시지를 전송 하라 “ 라고 만들수 있어.

만약 
Process에서 예기치 않는 문제가 발생 시 
커널통해서 예외 처리기에 연결된 take port로 예외 내용이 전달돼..

이런 저런 내용 때문에 
예외 문제가 발생 되었다고

그때 커널에서 예외 처리기로 보낼때 process도 
보낸 내용에 대해 응답을 받고 싶으니 
대략 3가지 내용을 같이 보내 , 
1. 프로세스가 받을 remote port(take port)
2. Message id
3. Thread 식별자( thread take port ) 

그러면 예외 처리가 “어 뭐 thread보니 이러저러해 “ 라고하면서 
Remote port로 내용을 보내.

해커는 여기서 이런 예외 처리 메커니즘을 이용하기고 했어.

우선 amfid 예외 일으키기전 백업을 하고 싶었어
그리서 메모리에 백업해 두고

Amfid 메모리내에 8바이트에 메모리 read,write,copy 권한을 부여해.

그러곤 뜬금 없이 
posix_spawnattr_setflags이 함수를 메모리에 넣고 실행하게 해.

맞아 에러 유발 시키는 겨

그러곤 예외 처리기인양 태연 스럽게 
앞서 알고 있는 예외 처리용 take port로 
예외 메시지가 올때 까지 기다려

그래서 메시지를 받으면 remote port, message id, thread 식별자(take port)중 

thread take port로 해당 thread의 state를 가져와서
x1레지스트리을 읽어서 amfid메모리에 쓰고 다음 내용으로 + jailbreakd의 CDHash값을 넣어서 우회해.

msg + 32: 검증 결과 (result)
msg + 36: Entitlements 검증 여부 (Ents validated)
msg + 40: 서명 유효성 (Sig valid)
msg + 44: Unrestrict 모드 (Unrestrict)
msg + 48: 서명자 유형 (Signer type)
msg + 52: Apple 서명 여부 (Is aapl)
msg + 56: 개발자 서명 여부 (Is dev)
msg + 60: 비정상 상태 (Anomaly)

그리고 다시 메모리에서 amfid 백업했던걸 복원하고
예외 처리응답 메시지를  처리해.

사실 이야기 할 께 더 있는데 오늘은 여기까지


```

# runJailbreakd.js 출력 Log

```
[+]    
[+]    
[+] runJailbreakd.js executed
[+]    
[+]    
[+]    
[+] modify by SPeeDr00t
[+]    
[+]    
[+]    
[+]    

[+] [ runJailbreakd.js::main() ] The path to the jailbreakd file to be executed. 
[ JAILBREAKD_PATH = 0x000000016b957df2 ]

[+] [ runJailbreakd.js::main() ] The arguments for jailbreakd. 
[ JAILBREAKD_ARG = 0x000000016b957e11 ]

[+] [ runJailbreakd.js::main() ] The CDHash of jailbreakd. 
[ JAILBREAKD_CDHASH = a8a86653aa54b4efab1e137dd0ddc2aee10bf54e ]

[+] [ runJailbreakd.js::main() ] My UID is  = 0x0000000000000000
[+] [ runJailbreakd.js::main() ] I'm root! 
[+] [ runJailbreakd.js::main() -> launchJailbreakd() ] Force launching jailbrekd

[+] [ runJailbreakd.js::launchJailbreakd() ] called 
[+] [ runJailbreakd.js::launchJailbreakd() ] Spawning binary 
[+] [ runJailbreakd.js::launchJailbreakd() ] 0x000000016b957df2
[+] [ runJailbreakd.js::launchJailbreakd() ] 0x0000000000000000
[+] [ runJailbreakd.js::launchJailbreakd() ] Assign 8 bytes to the variable pid. 
[+] [ runJailbreakd.js::launchJailbreakd() ] Assign 24 bytes to the variable argvBuf. 
[+] [ runJailbreakd.js::launchJailbreakd() ] Copy the value of target_path to argvBuf
[+] [ runJailbreakd.js::launchJailbreakd() ] Copy the value of target_arg to the second element of the argvBuf array at the memory location obtained by adding 8 bytes
[+] [ runJailbreakd.js::launchJailbreakd() ] This line means that the value 0 is being written to the memory location obtained by adding 16 bytes to the argvBuf array.
[+] [ runJailbreakd.js::launchJailbr end ] Spawn returned: [ 85 ]
[+] [ runJailbreakd.js::main() -> findAmfi() ]  Retrieve the task port of amfid. 

[+] [ runJailbreakd.js::findAmfi() ] called 
[+] The process /usr/libexec/amfid is responsible for validating code signatures on iOS, 
[+] ensuring that they meet Apple's requirements for security and integrity.
[+] [ runJailbreakd.js::findAmfi() ]  Searching for amfid...
[+] [ runJailbreakd.js::findAmfi() ] Found /usr/libexec/amfid PID: 407
[+] [ runJailbreakd.js::findAmfi() ] Attempting to get task port...
[+] [ runJailbreakd.js::findAmfi() ] Got task port for /usr/libexec/amfid  amfi.tp : 0x0000000000001707
[+] [ runJailbreakd.js::findAmfi() ] Getting threads

[+] [ runJailbreakd.js::class Thread -> constructor(tp) ]  

[+] [ runJailbreakd.js::class Thread -> constructor(tp) ]  

[+] [ runJailbreakd.js::class Thread -> constructor(tp) ]  

[+] [ runJailbreakd.js::class Thread -> constructor(tp) ]  
[+] [ runJailbreakd.js::findAmfi() ] Thread 0: task port threads[i].tp 0x0000000000001803
[+] [ runJailbreakd.js::findAmfi() ] Thread 1: task port threads[i].tp 0x0000000000002703
[+] [ runJailbreakd.js::findAmfi() ] Thread 2: task port threads[i].tp 0x0000000000002603
[+] [ runJailbreakd.js::findAmfi() ] Thread 3: task port threads[i].tp 0x0000000000001903

      


[+] [ runJailbreakd.js::findAmfi() ] Thread 0: task port threads[t].tp 0x0000000000001803

[+] [ runJailbreakd.js::class Thread -> getState() ]  

[+] [ runJailbreakd.js::class ThreadState -> constructor(buf) ]  this.bur = 0x00000001046aa810

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ]  
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016db46fc0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016db47040
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000000190008ff
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016db46fc0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016db46fc0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000000000019a
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016db47000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000018b9153b8
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.fp 0x002ce7816db46fa0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.lr 0xea1633018b8ef6ec
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.sp 0x001938816db46f90
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.pc 0xff014181b9cb8d10
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.flagsCPSR 0x0000000101010100
TH0 x0 -> 0x0000000000000000
TH0 x1 -> 0x0000000000000000
TH0 x2 -> 0x0000000000000000
TH0 x3 -> 0x000000016db46fc0
TH0 x4 -> 0x000000016db47040
TH0 x5 -> 0x00000000190008ff
TH0 x6 -> 0x0000000000000000
TH0 x7 -> 0x0000000000000000
TH0 x8 -> 0x000000016db46fc0
TH0 x9 -> 0x000000016db46fc0
TH0 x10 -> 0x0000000000000000
TH0 x11 -> 0x0000000000000000
TH0 x12 -> 0x0000000000000000
TH0 x13 -> 0x0000000000000000
TH0 x14 -> 0x0000000000000000
TH0 x15 -> 0x0000000000000000
TH0 x16 -> 0x000000000000019a
TH0 x17 -> 0x000000016db47000
TH0 x18 -> 0x0000000000000000
TH0 x19 -> 0x000000018b9153b8
TH0 x20 -> 0x0000000000000000
TH0 x21 -> 0x0000000000000000
TH0 x22 -> 0x0000000000000000
TH0 x23 -> 0x0000000000000000
TH0 x24 -> 0x0000000000000000
TH0 x25 -> 0x0000000000000000
TH0 x26 -> 0x0000000000000000
TH0 x27 -> 0x0000000000000000
TH0 x28 -> 0x0000000000000000

TH0 fp -> 0x002ce7816db46fa0
TH0 lr -> 0xea1633018b8ef6ec
TH0 sp -> 0x001938816db46f90
TH0 pc -> 0xff014181b9cb8d10
TH0 flagsCPSR -> 0x0000000101010100


[+] [ runJailbreakd.js::findAmfi() ] Thread 1: task port threads[t].tp 0x0000000000002703

[+] [ runJailbreakd.js::class Thread -> getState() ]  

[+] [ runJailbreakd.js::class ThreadState -> constructor(buf) ]  this.bur = 0x00000001046aa810

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ]  
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000040
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd2b80
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000030
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014bf04c40
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000004
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000023
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014e00a038
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000003fff
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014bf00000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000011ea2846
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000011ea283e
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000833
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000170
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000010101010
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd3000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd30a0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd3098
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.fp 0x004af9816dbd2b60
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.lr 0x383cc781d7815860
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.sp 0x001f8e816dbd2b40
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.pc 0x432afe01b9cb9184
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.flagsCPSR 0x0000000040000000
TH0 x0 -> 0x0000000000000040
TH0 x1 -> 0x000000016dbd2b80
TH0 x2 -> 0x0000000000000000
TH0 x3 -> 0x0000000000000000
TH0 x4 -> 0x0000000000000030
TH0 x5 -> 0x000000014bf04c40
TH0 x6 -> 0x0000000000000004
TH0 x7 -> 0x0000000000000023
TH0 x8 -> 0x0000000000000000
TH0 x9 -> 0x0000000000000000
TH0 x10 -> 0x000000014e00a038
TH0 x11 -> 0x0000000000003fff
TH0 x12 -> 0x000000014bf00000
TH0 x13 -> 0x0000000011ea2846
TH0 x14 -> 0x0000000011ea283e
TH0 x15 -> 0x0000000000000833
TH0 x16 -> 0x0000000000000170
TH0 x17 -> 0x0000000010101010
TH0 x18 -> 0x0000000000000000
TH0 x19 -> 0x000000016dbd3000
TH0 x20 -> 0x0000000000000001
TH0 x21 -> 0x000000016dbd30a0
TH0 x22 -> 0x000000016dbd3098
TH0 x23 -> 0x0000000000000000
TH0 x24 -> 0x0000000000000000
TH0 x25 -> 0x0000000000000000
TH0 x26 -> 0x0000000000000000
TH0 x27 -> 0x0000000000000000
TH0 x28 -> 0x0000000000000000

TH0 fp -> 0x004af9816dbd2b60
TH0 lr -> 0x383cc781d7815860
TH0 sp -> 0x001f8e816dbd2b40
TH0 pc -> 0x432afe01b9cb9184
TH0 flagsCPSR -> 0x0000000040000000


[+] [ runJailbreakd.js::findAmfi() ] Thread 2: task port threads[t].tp 0x0000000000002603

[+] [ runJailbreakd.js::class Thread -> getState() ]  

[+] [ runJailbreakd.js::class ThreadState -> constructor(buf) ]  this.bur = 0x00000001046aa810

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ]  
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000100
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dabab80
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000040
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014be0b810
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000018
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000020401
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014be0c4c1
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dabab80
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014be0c4f8
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000007
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000048
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000170
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000001eb763d78
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dabb000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dabb0a0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dabb098
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.fp 0x00699a816dabab50
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.lr 0x383cc781d7815860
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.sp 0x000b40816dabab30
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.pc 0x432afe01b9cb9184
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.flagsCPSR 0x0000000000000000
TH0 x0 -> 0x0000000000000100
TH0 x1 -> 0x000000016dabab80
TH0 x2 -> 0x0000000000000001
TH0 x3 -> 0x0000000000000000
TH0 x4 -> 0x0000000000000040
TH0 x5 -> 0x000000014be0b810
TH0 x6 -> 0x0000000000000018
TH0 x7 -> 0x0000000000020401
TH0 x8 -> 0x000000014be0c4c1
TH0 x9 -> 0x000000016dabab80
TH0 x10 -> 0x0000000000000001
TH0 x11 -> 0x000000014be0c4f8
TH0 x12 -> 0x0000000000000000
TH0 x13 -> 0x0000000000000007
TH0 x14 -> 0x0000000000000001
TH0 x15 -> 0x0000000000000048
TH0 x16 -> 0x0000000000000170
TH0 x17 -> 0x00000001eb763d78
TH0 x18 -> 0x0000000000000000
TH0 x19 -> 0x000000016dabb000
TH0 x20 -> 0x0000000000000001
TH0 x21 -> 0x000000016dabb0a0
TH0 x22 -> 0x000000016dabb098
TH0 x23 -> 0x0000000000000000
TH0 x24 -> 0x0000000000000000
TH0 x25 -> 0x0000000000000000
TH0 x26 -> 0x0000000000000000
TH0 x27 -> 0x0000000000000000
TH0 x28 -> 0x0000000000000000

TH0 fp -> 0x00699a816dabab50
TH0 lr -> 0x383cc781d7815860
TH0 sp -> 0x000b40816dabab30
TH0 pc -> 0x432afe01b9cb9184
TH0 flagsCPSR -> 0x0000000000000000


[+] [ runJailbreakd.js::findAmfi() ] Thread 3: task port threads[t].tp 0x0000000000001903

[+] [ runJailbreakd.js::class Thread -> getState() ]  

[+] [ runJailbreakd.js::class ThreadState -> constructor(buf) ]  this.bur = 0x00000001046aa810

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ]  
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.fp 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.lr 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.sp 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.pc 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.flagsCPSR 0x0000000000000000
TH0 x0 -> 0x0000000000000000
TH0 x1 -> 0x0000000000000000
TH0 x2 -> 0x0000000000000000
TH0 x3 -> 0x0000000000000000
TH0 x4 -> 0x0000000000000000
TH0 x5 -> 0x0000000000000000
TH0 x6 -> 0x0000000000000000
TH0 x7 -> 0x0000000000000000
TH0 x8 -> 0x0000000000000000
TH0 x9 -> 0x0000000000000000
TH0 x10 -> 0x0000000000000000
TH0 x11 -> 0x0000000000000000
TH0 x12 -> 0x0000000000000000
TH0 x13 -> 0x0000000000000000
TH0 x14 -> 0x0000000000000000
TH0 x15 -> 0x0000000000000000
TH0 x16 -> 0x0000000000000000
TH0 x17 -> 0x0000000000000000
TH0 x18 -> 0x0000000000000000
TH0 x19 -> 0x0000000000000000
TH0 x20 -> 0x0000000000000000
TH0 x21 -> 0x0000000000000000
TH0 x22 -> 0x0000000000000000
TH0 x23 -> 0x0000000000000000
TH0 x24 -> 0x0000000000000000
TH0 x25 -> 0x0000000000000000
TH0 x26 -> 0x0000000000000000
TH0 x27 -> 0x0000000000000000
TH0 x28 -> 0x0000000000000000

TH0 fp -> 0x0000000000000000
TH0 lr -> 0x0000000000000000
TH0 sp -> 0x0000000000000000
TH0 pc -> 0x0000000000000000
TH0 flagsCPSR -> 0x0000000000000000

      
[+] [ runJailbreakd.js::main() -> getMachPort() ] 

[+] [ runJailbreakd.js::getMachPort() ] called 

[+] [ runJailbreakd.js::getMachPort() ] port = 0x0000000000002503
[+] [ runJailbreakd.js::main() ] Setting exception port : excPort = 0x0000000000002503
[+] [ runJailbreakd.js::main() ] 'task_set_exception_ports' sets up exception handling for bad access cases.
[+] [ runJailbreakd.js::main() ] amfi of Image Base :  0x00000001023cc000
[+] [ runJailbreakd.js::main() ] amfi_func_entry_off : 50568
[+] [ runJailbreakd.js::main() ] Target =  base + amfi_func_entry_off : 0x00000001023d8588
[+] [ runJailbreakd.js::main() ] Back up the 'amfi' process to 'targetBackup'.
[+] [ runJailbreakd.js::main() ] Changed target 

[+] [ runJailbreakd.js::launchJailbreakd() ] called 

[+] [ runJailbreakd.js::handleExc() ] called 
[+] [ runJailbreakd.js::launchJailbreakd() ] Spawning binary 
[+] [ runJailbreakd.js::handleExc() ] Waiting for exception message...
[+] [ runJailbreakd.js::launchJailbreakd() ] 0x000000016b957df2
[+] [ runJailbreakd.js::launchJailbreakd() ] 0x0000000000000000
[+] [ runJailbreakd.js::launchJailbreakd() ] Assign 8 bytes to the variable pid. 
[+] [ runJailbreakd.js::launchJailbreakd() ] Assign 24 bytes to the variable argvBuf. 
[+] [ runJailbreakd.js::launchJailbreakd() ] Copy the value of target_path to argvBuf
[+] [ runJailbreakd.js::launchJailbreakd() ] Copy the value of target_arg to the second element of the argvBuf array at the memory location obtained by adding 8 bytes
[+] [ runJailbreakd.js::launchJailbreakd() ] This line means that the value 0 is being written to the memory location obtained by adding 16 bytes to the argvBuf array.
[+] [ runJailbreakd.js::handleExc() ] Received exception message!
[+] [ runJailbreakd.js::handleExc() ] Patching amfid...

[+] [ runJailbreakd.js::class Thread -> constructor(tp) ]  
       
       

[+] [ runJailbreakd.js::patchAMFI() ] called 
       
       
       
[+] [ runJailbreakd.js::patchAMFI()->th.getState() ] Get crash state thread -> th.getState()

[+] [ runJailbreakd.js::class Thread -> getState() ]  

[+] [ runJailbreakd.js::class ThreadState -> constructor(buf) ]  this.bur = 0x00000001046aa810

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ]  
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd16d0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000000000010a0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000f07
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000c480001112
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000001023d8560
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000028
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000001
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000101
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000000000000bc
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000833
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0xffffffffffffffe1
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000001023d8258
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd0630
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014c804840
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000000000010a0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd16d0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000000000000
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000014c804690
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x000000016dbd30e0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x00000000000003e7
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] 0x0000000007000902

[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.fp 0x003e9a016dbd0620
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.lr 0xcb149381023d2fd0
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.sp 0x002c28816dbd0620
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.pc 0x83252481b9c96b84
[+] [ runJailbreakd.js::class ThreadState -> reloadState() ] this.flagsCPSR 0x0000000080000000
[+] [ runJailbreakd.js::patchAMFI() let st = th.getState(); st.pc ] PC : 0x83252481b9c96b84
[+] [ runJailbreakd.js::patchAMFI() let st = th.getState(); st.x8 ] X8 : 0x000000c480001112
[+] [ runJailbreakd.js::patchAMFI() let st = th.getState(); st.x1 ] X1 : 0x000000016dbd16d0
[+] [ runJailbreakd.js::patchAMFI() ] Getting out message  : msg = st.x1 -> 0x000000016dbd16d0
[+] [ runJailbreakd.js::patchAMFI() ] Write changes
[+] [ runJailbreakd.js::patchAMFI() ] msg address = 0x000000016dbd16d0 Write 0 to the address obtained by adding 32 to the address of msg.
[+] [ runJailbreakd.js::patchAMFI() ] Wrote bits
[+] [ runJailbreakd.js::patchAMFI() ] Wrote unsatisfied ents
[+] [ runJailbreakd.js::patchAMFI() ] Writing jailbreakd's target_CDHash to memory.
[+] [ runJailbreakd.js::patchAMFI() ] Message length
[+] [ runJailbreakd.js::patchAMFI() ] Wrote message length
[+] [ runJailbreakd.js::patchAMFI() ] NDR = 0x0000000100000000
[+] [ runJailbreakd.js::patchAMFI() ] Wrote NDR
[+] [ runJailbreakd.js::patchAMFI() ] Now update thread state
[+] [ runJailbreakd.js::patchAMFI() ] Created buffer

[+] [ runJailbreakd.js::class Thread -> setState() ]  
[+] [ runJailbreakd.js::patchAMFI() ] Updated thread state
[+] [ runJailbreakd.js::handleExc() ] Sent reply!
[+] [ runJailbreakd.js::launchJailbr end ] Spawn returned: [ 0 ]
[+] [ runJailbreakd.js::main() ] jailbreakd.js done!
Blackfalcon:/private/var/tmp> 
```
