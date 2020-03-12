# deploy
deploy

# 셋팅 절차
 - 1. git에 새로운 저장소 생성
 -    https://github.com/ohchangsuk/deploy.git
 - 2. 로컬 pc에서 aws 폴더를 vscode에 오픈
 - 3. terminal 오픈
 - 4. $ git clone https://github.com/ohchangsuk/deploy.git
 - 5. cd deploy
# 파일 세팅(~/aws/deploy)
 - 1. fabfile.py, deploy.json 파일을 위치(deploy에)
 - 2. 서버파일 생성
 - 3. wsgi.py(엔트리포인트), run.py 생성
 - 4. 코드 작성
 - 5. 배포 관련 환경변수 파일 수정(deploy.json)
 - 6. git 주소, 서버의 Ip, 도메인은 향후 IP와 연결( 호스팅쪽 ) 리눅스 접속 계정 ID등을 설정
 - requirements.txt : 본서비스를 구동하기위해 사용된 모든 파이썬 패키지를 기술한다.

 # 구동
 - python3 버전 기반으로 수행
 - 운영체계 및 서버 세팅 및 배포, 업데이트 관리 등등을 자동화 하는 모듈 => fabric3
 - $ pip install fabric3
 - git에 최종소스 반영
 - fab new_server
 - 중간에 y, git로그인등등이 나올수 있다.
 - 브라우저 가동
 - 54.180.82.140
 - 접속로그 확인 (리눅스에서 진행)
 - $ tail -f /var/apache2/access.log