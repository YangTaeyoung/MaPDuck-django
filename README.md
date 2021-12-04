# MAPDUCK
마프덕의 크롤링 서비스를 위해 백그라운드에서 동작하는 Django Server입니다.  
<hr/>

### 해당 API에서는 다음과 같은 기능을 수행합니다.

1. **네이버 구매목록 크롤링**   
- 실제 구현은 naver/services/naver_service.py, naver/services/naver_selenium_crawling.py에 정의되어 있습니다.   
- 네이버 자동 로그인을 가능하게 하기 위해 사용되었습니다.   
   
2. **다나와 쇼핑 검색목록 크롤링**   
- 모델명을 검색하기 위해 사용자로부터 keyword를 받아 실질적으로 검색하는 역할을 수행합니다.   
- 상품과 관련된 모든 키워드를 분석하며 분석 모듈은 danawa/services/danawa_separator.py,   
- 크롤링 모듈은 danawa/services/crawling.py에 정의되어 있습니다. 

<hr/>
자세한 API는 [MaPDuck-spring Repository](https://github.com/YangTaeyoung/MaPDuck-spring/)
에서 확인할 수 있습니다.

