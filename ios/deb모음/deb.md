# deb 모음 

## dpkg 사용할 수 없을 때 수동으로 풀기
deb 파일은 ar 아카이브와 tar 아카이브의 조합으로 이루어져 있습니다.

다음 단계를 따라 deb 파일을 수동으로 풀 수 있습니다:

deb 파일을 작업 디렉토리에 복사합니다.


```base
cp dpkg_1.19.7-2_iphoneos-arm.deb ./
```
ar 명령을 사용하여 deb 파일을 추출합니다.

Copy code
```
ar -x dpkg_1.19.7-2_iphoneos-arm.deb
```

이렇게 하면 debian-binary, control.tar.xz, data.tar.lzma와 
같은 파일들이 생성됩니다.
data.tar.lzm 파일을 tar로 풉니다.

lzma 파일을 풀려면 다음 명령을 사용할 수 있습니다:

```
lzma -d data.tar.lzma
```
이 명령은 data.tar.lzma를 data.tar 파일로 압축 해제합니다.

그 다음, tar 명령을 사용하여 data.tar 파일을 추출할 수 있습니다:


```
tar -xvf data.tar
```
이렇게 하면 deb 패키지의 실제 컨텐츠가 현재 디렉토리에 추출됩니다.


Copy code
```
tar -xf data.tar.xz
```
이 명령은 deb 패키지의 실제 컨텐츠를 추출합니다.
이제 추출된 파일들을 적절한 위치로 수동으로 이동시킬 수 있습니다.


## dpkg 사용할 수 있을 때
```
sudo dpkg -i dpkg_1.19.7-2_iphoneos-arm.deb
```

## deb

https://apt.bingner.com/debs/1200.00/

http://ftp.tku.edu.tw/Linux/ArchLinux-arm/aarch64/extra/

https://www.procurs.us/pool/main/iphoneos-arm64-rootless/1900/shell-cmds/

https://strap.palera.in/pool/main/iphoneos-arm64/2000/
