# iOS/macOS 탈옥을 위한 보안 취약점 분석

이 글은 iOS와 macOS의 보안 취약점을 이용한 탈옥(jailbreak) 과정을 설명하고 있습니다. 주요 내용은 다음과 같이 요약할 수 있습니다:

## 1. dyld closure 취약점
- iOS 앱 실행 속도를 높이기 위해 사용되는 dyld closure 캐시 파일을 조작해 코드를 인젝션할 수 있는 취약점
- 샌드박스 밖에서 실행되는 앱의 바이너리로 교체해 악성 closure를 로딩함으로써 취약점 익스플로잇 

## 2. DriverKit 커널 익스플로잇
- macOS의 커널 확장 대안인 DriverKit 프레임워크의 취약점을 이용해 커널 메모리에 임의 읽기/쓰기 권한 획득
- 초기화되지 않은 변수를 이용해 물리 메모리 전체에 접근할 수 있는 `IOMemoryDescriptor` 객체 생성 가능

## 3. 커널 PAC 바이패스
- 아이폰 XS 이후 모델의 PAC(Pointer Authentication Code) 메커니즘 우회
- 커널 익셉션 핸들러가 유저 스레드 상태를 서명할 때 `cpsr` 레지스터를 변조해 커널 권한 획득

## 4. PPL 바이패스
- `pmap_enter_options_internal` 함수에서 물리 주소 값 검증 부재를 이용해 PPL로 보호된 페이지에 접근

## 5. 탈옥 과정
- dyld closure 취약점을 이용해 샌드박스 탈출, 루트 권한 획득, `amfid` 패치
- DriverKit 익스플로잇으로 커널 메모리 읽기/쓰기
- PAC, PPL 바이패스로 시스템 무결성 검증 해제 
- 루트 파일시스템 쓰기 가능 상태로 마운트 및 지속성 확보  

## 6. dyld closure 취약점 익스플로잇 상세
- `PwnClosure` API를 통해 악성 dyld closure 생성
- Objective-C 메서드 인젝션 및 ROP를 활용한 SLOP 익스플로잇 체인 구성

## 7. DriverKit 익스플로잇 상세 
- Codeless Kernel Extension을 통해 DriverKit 드라이버 등록 및 체크인 토큰 획득
- `IOUserClient`의 취약한 `CreateMemoryDescriptorFromClient` 메서드로 임의 물리 메모리 매핑
- `IODMACommand`로 커널 메모리에 읽기/쓰기 수행

이와 같이 다양한 취약점들을 연계 공격함으로써 iOS와 macOS 기기의 보안 모델을 무력화시키고 탈옥에 성공하는 과정을 보여주고 있습니다.
