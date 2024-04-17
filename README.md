# 🔡Spartamarket
스파르타 AI 6기 조별 프로젝트 + 공부 공유 커뮤니티
# 📝프로젝트 소개
각자 작성한 TIL을 공유, 작성 횟수에 따른 리더보드 내 순위 나열
# 📅개발 기간
* 2024.04.01일 - 2024.04.05일
## 🖥️개발 환경
* HTML
* CSS
* python : Django
* DB : SQLite

# ✅주요 기능
**로그인**  📎[Wiki](https://github.com/luna-negra/csi_group_project/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Login))
  * DB값 검증
  * 로그인 시 세션(Session) 생성
  * 회원가입창으로 이동

**회원가입**  📎[Wiki](https://github.com/luna-negra/csi_group_project/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Register))
  * ID,PW 규칙(길이제한, 영문,숫자,특수문자 포함) 체크
  * ID 중복 체크
  * PW 암호화(SHA-256)

**네이게이션 바**  📎[Wiki](https://github.com/luna-negra/csi_group_project/wiki/%EC%A3%BC%EC%9A%94-%EA%B8%B0%EB%8A%A5-%EC%86%8C%EA%B0%9C(Nav-bar))
  * Home(Main)으로 이동
  * TIL 전체 리스트 조회
  * Leaderboard 이동
  
**메인**  📎[Wiki](https://github.com/luna-negra/csi_group_project/wiki/Main-%ED%99%94%EB%A9%B4-%EA%B5%AC%EC%84%B1)
  * 가장 최신 TIL 3개 표시
  * TIL box 애니메이션 효과(CSS)
    * 앞면 - 썸네일, 제목
    * 뒷면 - 작성자,좋아요 수, 작성일자, 게시물 링크

