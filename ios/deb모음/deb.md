# deb 모음 

## dpkg 사용할 수 없을 때 수동으로 풀기


```base
hacker@blackfalconui-MacBookAir wget_cus % ls -ltr
total 392
-rw-r--r--@ 1 hacker  staff  199810  3 19 08:09 wget_1.19.5-2_iphoneos-arm.deb
```

### ar 명령을 사용하여 deb 파일을 추출합니다.

* copy command
```
ar -x wget_1.19.5-2_iphoneos-arm.deb
```

* 결과보기
```
hacker@blackfalconui-MacBookAir wget_cus % ls -ltr
total 800
-rw-r--r--@ 1 hacker  staff  199810  3 19 08:09 wget_1.19.5-2_iphoneos-arm.deb
-rw-r--r--  1 hacker  staff       4  3 19 08:29 debian-binary
-rw-r--r--  1 hacker  staff     332  3 19 08:29 control.tar.gz
-rw-r--r--  1 hacker  staff  199285  3 19 08:29 data.tar.lzma
```
```
hacker@blackfalconui-MacBookAir wget_cus % mkdir data
hacker@blackfalconui-MacBookAir wget_cus % mv data.tar.lzma data
hacker@blackfalconui-MacBookAir wget_cus % cd data
hacker@blackfalconui-MacBookAir data % ls -ltr
total 392
-rw-r--r--  1 hacker  staff  199285  3 19 08:29 data.tar.lzma
hacker@blackfalconui-MacBookAir data % pwd
/Users/hacker/Downloads/package/wget_cus/data
```


* 이렇게 하면 debian-binary, control.tar.xz, data.tar.lzma와 같은 파일들이 생성됩니다.
* data.tar.lzm 파일을 tar로 풉니다.

* lzma 파일을 풀려면 다음 명령을 사용할 수 있습니다:
* 이 명령은 data.tar.lzma를 data.tar 파일로 압축 해제합니다.

```
hacker@blackfalconui-MacBookAir data % ls -ltr
total 392
-rw-r--r--  1 hacker  staff  199285  3 19 08:29 data.tar.lzma
```

### lzma 압축 해제
```
lzma -d data.tar.lzma
```
```
hacker@blackfalconui-MacBookAir data % lzma -d data.tar.lzma 
hacker@blackfalconui-MacBookAir data % ls -ltr
total 1104
-rw-r--r--  1 hacker  staff  564736  3 19 08:29 data.tar
```

### 그 다음, tar 명령을 사용하여 data.tar 파일을 추출할 수 있습니다:


```
tar xvf data.tar
```

 결과확인
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
