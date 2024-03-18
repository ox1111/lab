# deb 모음 

## dpkg 사용할 수 없을 때 수동으로 풀기



### ar 명령을 사용하여 deb 파일을 추출합니다.

```
ar -x wget_1.19.5-2_iphoneos-arm.deb
```

### lzma 압축 해제
```
lzma -d data.tar.lzma
```

### tar 명령을 사용하여 data.tar 파일을 추출할

```
tar xvf data.tar
```

#### 결과확인
```
hacker@blackfalconui-MacBookAir data % tar xvf data.tar 
x .
x ./usr
x ./usr/bin
x ./usr/bin/wget
x ./usr/etc
x ./usr/etc/wgetrc
```

이렇게 하면 deb 패키지의 실제 컨텐츠가 현재 디렉토리에 추출됩니다.


## dpkg 사용할 수 있을 때
```
sudo dpkg -i wget_1.19.5-2_iphoneos-arm.deb
```

## deb

https://apt.bingner.com/debs/1200.00/

http://ftp.tku.edu.tw/Linux/ArchLinux-arm/aarch64/extra/

https://www.procurs.us/pool/main/iphoneos-arm64-rootless/1900/shell-cmds/

https://strap.palera.in/pool/main/iphoneos-arm64/2000/
