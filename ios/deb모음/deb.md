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

## Packages

http://cydia.zodttd.com/repo/cydia/dists/stable/Release

http://cydia.zodttd.com/repo/cydia/dists/stable/Release/main/binary-iphoneos-arm/Packages.bz2

http://cydia.zodttd.com/repo/cydia/dists/stable/main/binary-iphoneos-arm/Packages.bz2

http://apt.saurik.com/dists/ios/1240.10/main/binary-iphoneos-arm/Packages.bz2

http://apt.saurik.com/dists/ios/1240.00/main/binary-iphoneos-arm/Packages.bz2



## DebFounder
https://github.com/ox1111/DebFounder.git


## list

Sources

46&2 Beta Repository
http://repo.fortysixandtwo.com/

Alex Zielenski
http://repo.alexzielenski.com/

apt.dba-technologies.combeta
http://apt.dba-technologies.com/beta/

BigBoss
http://apt.thebigboss.org/repofiles/cydia/dists/stable

Blazar
http://ath.ink/

CokePokes
http://cydia.cokepokes.com/

CokePokes - MyRepoSpace.com 
http://cokepokes.myrepospace.com/

CP Digital Darkroom
http://repo.cpdigitaldarkroom.com/

Cydia/Telesphoreo
http://apt.saurik.com/dists/ios/847.27

dbk1ng - MyRepoSpace.com 
http://dbk1ng.myrepospace.com/

Delta
http://getdelta.co/

deVbug Cydia Repo
http://devbug.me/apt/

Exile.90's Beta Repo
http://exile90software.com/cydia/beta/

hAcx Repository
http://hacx.org/repo/

insanj repo
http://repo.insanj.com/

iRepo
http://theirepo.com/

JerryEn's Repo
http://cydia.jerryen.com/

Karen's Pineapple 
http://cydia.angelxwind.net/

kinchan Repository
http://kindadev.com/apt/

kuaidial.googlecode.comsvndeb
http://kuaidial.googlecode.com/svn/deb/

ModMyi.com
http://apt.modmyi.com/dists/stable

pNre Repo 
http://repo.pnre.co/

Q's Beta
http://cydia.qusic.me/

repo.peng-u-in.de
http://repo.peng-u-in.de/

repo666.ultrasn0w.com
http://repo666.ultrasn0w.com/

rpetrich repo
http://rpetri.ch/repo/

Ryan Pendleton 
http://cydia.ryanp.me/

tateu's repo
http://tateu.net/repo/

test-cydia.bitesms.com
http://test-cydia.bitesms.com/

ZodTTD & MacCiti
http://cydia.zodttd.com/repo/cydia/dists/stable

