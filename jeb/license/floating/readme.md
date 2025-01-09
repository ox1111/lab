# JEB 플로팅 라이선스 시스템

이 문서는 JEB 플로팅 라이선스 시스템의 개요를 제공합니다.

## JEB Controller 구조도

아래는 JEB 컨트롤러의 구조를 나타내는 다이어그램입니다:

![jeb controller 구조도](./jeb-controller-diagram.png)

## 주요 기능

- 플로팅 라이선스 관리
- 안전한 인증 및 라이선싱
- 라이선스 추적을 위한 데이터베이스 스키마

## JEB Controller 설치 방법

### 1) 구매후 jeb 다운로드링크와 암호가 전달된다.
![jeb 링크](./download.PNG)

### 2) JDK 17버전 다운로드하고 설치한다.

![jdk 17 설치](./0.3%20자바설치및%20환경변수%20설정.PNG)



```
sudo apt install alien -y
sudo apt install rpm -y
sudo alien -i jdk-17.0.12_linux-x64_bin.rpm

sudo vi ~/.bashrc
파일의 마지막에 아래 추가

export JAVA_HOME=/usr/lib/jvm/jdk-17.0.12-oracle-x64
export PATH=$JAVA_HOME/bin:$PATH

source  ~/.bashrc
```

![5.7 JEB 클라이언트 설치하기](./버전확인.PNG)

### 3) JEB Controller 실행하기

앞서 이메일로 받은 암호를 넣는다.

```
./jeb_linux.sh -c --controller

```

![1.1 JEB Controller 실행하기](./1.1%20jeb%20controller실행하기.PNG)


### 4 ) Input your license key 입력 받는 대기화면 확인

license data를 복사한다.

![1.2 JEB Controller 실행하기](./1.2%20jeb%20controller실행하기.PNG)


### 5 ) JEB KEY GENERATOR

아래 사이트에 접속해서 

4)에서 복사한 license data와 원하는 key name을 입력한다.

```
pnfsoftware.com/genlk
```

![1.3 JEB Controller 실행하기](./1.3%20jeb%20controller실행하기.PNG)


### 6) 생성한 License key를 확인한다

![1.4 JEB Controller 실행하기](./1.4%20jeb%20controller실행하기.PNG)

### 7) Lincense key 입력한다.

6)에서 생성한 Lincense key를 복사해서 입력한다.

``
Input your license key : key
``


![1.5 JEB Controller 실행하기](./1.5%20jeb%20controller실행하기.PNG)


## JEB client 접속 방법

### 1) JEB client 실행하기

```
./jeb_linux.sh
```


![5.8 JEB 클라이언트 설치하기](./5.8%20jeb%20클라이언트%20설치하기.PNG)


![5.10 JEB 클라이언트 설치하기](./5.10%20jeb%20클라이언트%20설치하기.PNG)

![5.11 JEB 클라이언트 설치하기](./5.11%20jeb%20클라이언트%20설치하기.PNG)

