# ox1111의 iOS 도구 모음

## [dyld-cache-fix-example](https://github.com/ox1111/dyld-cache-fix-example)
- iPhone 6s iOS 14.0에서 가져온 IOSurface 예제

## [SSH Ramdisk Script](https://github.com/ox1111/SSHRD_Script)
- checkm8 장치에서 SSH ramdisk를 생성하고 부팅하는 스크립트

## [trustcache](https://github.com/ox1111/trustcache)
- trustcache 생성 및 상호 작용 도구

## [ldid](https://github.com/ox1111/ldid.git)
- Link Identity Editor: Mach-O 파일에 실제 또는 가짜 서명을 삽입하는 도구
- Mach-O는 Apple의 iOS와 macOS에서 사용되는 실행 파일 형식
- 개발자 인증서 없이도 Mach-O 파일에 서명을 추가할 수 있음
- 탈옥 개발이나 보안 연구 등 특수한 목적으로 사용됨

## [img4tool v2](https://github.com/ox1111/img4tool.git)
- 원본 img4tool을 더 많은 기능과 개선 사항으로 완전히 재작성한 버전
- libimg4tool 라이브러리를 설치하여 프로젝트에 쉽게 포함할 수 있음

## [opainject](https://github.com/ox1111/opainject.git)
- iOS 도구를 사용하여 셸코드와 ROP 방법으로 프로세스에 dylib을 주입
- iOS 14, 15, 16, 17에서 테스트됨 (이론적으로는 11.0 이상에서 작동)
- arm64e 디바이스에서는 dylib가 인젝션되지만 trust cache에 없으면 프로세스가 충돌함

## [ChOma](https://github.com/ox1111/ChOma.git)
- MachO/FAT 파일의 코드 서명을 조작하기 위한 C 라이브러리

## [XNU Patch Finder (based on ChOma)](https://github.com/ox1111/XPF.git)
- ChOma 기반의 XNU 패치 파인더

## [libSandy](https://github.com/ox1111/libSandy.git)
- 탈옥한 iOS에서 애플리케이션 및 시스템 프로세스의 샌드박스를 안전하게 확장할 수 있는 개발자 라이브러리

## [cat /etc/passwd](https://github.com/ox1111/cat-etc-passwd.git)
- UNIX 시스템에서 사용자 계정 정보를 저장하는 /etc/passwd 파일을 읽어오는 도구
- 사용자 이름, UID, GID, 홈 디렉토리, 기본 셸 등의 정보를 확인할 수 있음
- 시스템 관리 및 보안 감사 목적으로 활용됨
