===================================================================================
**Title:** Domain Name System Bind attack  
**Author:** 유동훈 (Xpl017Elz)  
**E-mail:** [szoahc@hotmail.com](mailto:szoahc@hotmail.com)  
**Home:** [http://x82.i21c.net](http://x82.i21c.net)  
**Date:** 2001/3/06  
===================================================================================  


### 작자주
이 문서는 DNS attack에 대해 공부하는 이들을 위해 제작되었습니다.  
만약, 문서의 내용 중 오류가 있다면 [szoahc@hotmail.com](mailto:szoahc@hotmail.com)으로 메일 주시면 감사하겠습니다.

---

## Domain Name System Bind Attack

**Domain Name System**이란 인터넷 호스트 이름을 IP 주소로 변환하는 시스템을 말한다.  
DNS는 항상 작동해왔다. IP 주소에서 도메인으로 전환하기 위해 리눅스와 유닉스 계열에서는 **Bind (Berkeley Internet Name Domain)** 애플리케이션을 채택해왔다.  
물론 우리는 DNS가 심각한 취약점을 가지고 있는 것을 알아채지 못했다.

얼마 전에야 DNS의 취약점들이 하나씩 밝혀지면서 해커들의 시선을 주목하게 되었다.  
한마디로 DNS는 심각한 보안 문제를 지니고 있었음에도 불구하고 오랜 기간 동안 묻혀왔던 것이다.

현재 도메인과 IP를 전환해주는 서버로 **Bind 네임서버**를 사용하고 있다.  
Version은 9.1.0 최신 버전이다. (아직은 문제점이 발견되지 않았다.)  
그 이전 Version의 Bind들은 모두 심각한 취약점을 지니고 있다.

만약 당신이 취약점을 가지고 있는 서버를 운영 중이라면 업데이트를 권장하는 바이다.  
- **Bind 9.1.0 다운로드:** [ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz](ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz)  
- **PGP Signature for BIND 9.1.0:** [ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz.asc](ftp://ftp.isc.org/isc/bind9/9.1.0/bind-9.1.0.tar.gz.asc)
