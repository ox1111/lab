# Fugu14
## [ Fugu14에 있는 runJailbreakd.js 이야기 ]

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
