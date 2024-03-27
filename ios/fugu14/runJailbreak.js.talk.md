# [ Fugu14에 있는 runJailbreakd.js 이야기 ]


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
그래서 메모리에 백업해 두고

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
