# JEB 플로팅 라이선스 시스템

이 문서는 JEB 플로팅 라이선스 시스템의 개요를 제공합니다.

## JEB Controller 구조도

아래는 JEB 컨트롤러의 구조를 나타내는 다이어그램입니다:

![jeb controller 구조도](./jeb-controller-diagram.png)

## 주요 기능

- 플로팅 라이선스 관리
- 안전한 인증 및 라이선싱
- 라이선스 추적을 위한 데이터베이스 스키마

## 설치 방법

### 1) 구매후 jeb 다운로드링크와 암호가 전달된다.
![jeb 링크](./download.PNG)

### 2) JDK 17버전 다운로드하고 설치한다.

![jdk 17 설치](./0.3 자바설치및 환경변수 설정.PNG)


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

