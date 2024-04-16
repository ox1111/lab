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

Packages

7-zip (POSIX) - 4.57-3p
Action Menu - 1.2.14
Activator - 1.8.4~rc1
AdBlocker - 1.60
adv-cmds - 119-5
AlwaysClear - 0.1
Apex 2 (iOS 7) - 1.0.9
AppInfo - 1.6.2
Apple File Conduit "2" - 1.0
AppList - 1.5.8
AppSync Unified - 4.4-1
APR (/usr/lib) - 1.3.3-2
APT 0.6 Transitional - 1:0-23
APT 0.7 (apt-key) - 0.7.25.3-3
APT 0.7 Strict - 0.7.25.3-8
APT 0.7 Strict (lib) - 0.7.25.3-13
AptBackup - 1.1-9
Asphaleia - 1.0.4-31
Auxo 2 (iOS 7) - 1.2.3
Avenir Font iOS 7 - 1.0
Background Manager - 0.9-26
Base Structure - 1-4
basic-cmds - 48-2p
Berkeley DB - 4.6.21-4p
BigBoss Icon Set - 1.0
biteSMS - 8.3.6
Boover - 2.1-5
Bourne-Again SHell - 4.0.17-13
BytaFont 2 - 2.1.4
bzip2 - 1.0.5-7
Circlet - 1.2.2-1
Core Utilities - 8.12-12p
Core Utilities (/bin) - 8.12-7p
Cycript - 0.9.501
Cydia Installer - 1.1.12
Cydia Substrate - 0.9.5001
Cydia Translations - 1.1.12
Darwin Tools - 1-4
Debian Packager - 1.14.25-9
Debian Utilities - 3.3.3ubuntu1-1p
Diff Utilities - 2.8.1-6
diskdev-cmds - 421.7-4
DockShift - 1.5
Eclipse - 1.3-2
Erica Utilities - 1:0.4.2
f.lux - 0.990
f.lux Flipswitch - 0.2-1
file-cmds - 220.7-3
Find Utilities - 4.2.33-6
FlipControlCenter - 1.0.1~beta1
Flipswitch - 1.0.4~beta3
Gawk - 3.1.6-2p
grep - 2.5.4-3
guilty - 1.8
gzip - 1.6-7
hAcx Daemon - 1.0-17
HomescreenDesigner - 1.0.19
iBlacklist - 7.0-5
iBlank - 4.3
iCleaner Pro - 7.2.0
IconSupport - 1.9.4-1
iFile - 2.0.1-1
iOS Firmware - 7.1.2
iPhone Firmware (/sbin) - 0-1
iTouchSecure - 2.0.1.3
libobjcipc - 1.0.0-17
libstatusbar - 1:0.9.7.1.2
libsymbolicate - 1.0.1-1
LockInfo7 - 7.0.7-28
LockPages - 1.3.1-22
LZMA Utils - 4.32.7-4
Messages Customiser - 2.4.3
MobileTerminal - 520-3
network-cmds - 307.0.1-6
New Curses - 5.7-13
No Percent Sign - 1.5-1
NoAnnoyance - 0.2.0~beta5-1
NoSlowAnimations - 3.1.1
NoVoiceMail - 1.0-32
OneByOne Contacts - 2.1
PAM (Apple) - 32.1-3
PAM Modules - 36.1-4
Pangu 7.1-7.1.x Untether - 0.2
pcre - 8.30-5p
PebbleSiri - 0.6-5
Phantom for Snapchat - 3.1.6-6
Photo Info - 2.0.2
PhotoAlbums+ for iOS 7 and iPhone/iPod - 1.0.0.5
PkgBackup - 7.0.4
PreferenceLoader - 2.2.2
Profile Directory - 0-2
readline - 6.0-7
RocketBootstrap - 1.0.2
Safe Mode Flipswitch - 0.9
ScreenDimmer - 1.82
sed - 4.1.5-7
shell-cmds - 118-6
Smartwatch+ - 1.500.2
Source Saver - 1.1
Springtomize 3 - iOS 7 - 1.1.2-2
Substrate Safe Mode - 0.9.4000
Sudo - 1.6.9p12-4p
Super Recorder - 1.59
SwipeExpander - 0.2-1
symbolicate - 1.4.0-1
system-cmds - 433.4-12
Tape Archive - 1.19-8
TetherMe - 3.0-3
TinyBar - 0.0.5-2
UIKit Tools - 1.1.8
unrar - 3.6.8-2p
unzip - 5.52-5p
Zeppelin - 2.0.2-13
zip - 2.32-5p


