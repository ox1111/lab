SKT에 사용된 악성코드

[ BPF 악성코드에 대한 정보 ]

bpf는(Berkeley Packet Filter) 는 네트워크 패킷 필터링입니다.


BPF 백도어는  Berkeley Packet Filter를 
악용하여 리눅스 시스템을 감염시키는 백도어 악성코드입니다.

일반 백도어와 달리 C2 연결을 먼저 시도하지 않고, 
오히려 특정 ‘매직 패킷’을 대기하며 잠복합니다.

공격자는 특정 포트를 열지 않아도 되므로 
탐지가 매우 어렵습니다.



[ BPF 악성코드에 대한 탐지 ]

아래와 같은 방법으로 기존 시스템에 
악성코드 감염 여부를 확인가능합니다.
```
hacker@hacker:/opt/lampp/htdocs/gnuboard/5.5.15/a$ ip link show dev ens33
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 xdpgeneric qdisc fq_codel state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:62:c5:a4 brd ff:ff:ff:ff:ff:ff
    prog/xdp id 533 
    altname enp2s1

hacker@hacker:/opt/lampp/htdocs/gnuboard/5.5.15/a$ sudo bpftool prog dump xlated id 533
int xdp_filter(struct xdp_md * ctx):
; return XDP_PASS;
   0: (b7) r0 = 2
   1: (95) exit
```   
[ BPF 악성코드에 대한 방어 전략 ]

1. 주기적으로 침해사고 대응 전략

- 주기적으로 침해사고 대응훈련
- 서버 침투 테스트

2. 주기적으로 백도어 체크 

- /dev/shm 디렉토리에 의심가능 파일 체크
- bpf 설치여부 확인

3. splunk,edr등르로 비정상 패킷및 프로세스 감시
