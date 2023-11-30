# ChatGPT-DRF-Project

## 1. 목표와 기능
- 하루 5개 영단어 퀴즈를 꾸준히 하는것
- 랜덤한 단어 추출을 위해 ai기술을 이용할 예정
- 역대 단어 퀴즈를 풀었던 기록을 통해 복습할 수 잇게하기

## 2. 개발 기술 및 환경
### 2.1 개발 기술
#### FE
<div>
    <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white">
    <img src="https://img.shields.io/badge/css3-1572B6?style=for-the-badge&logo=css3&logoColor=white">
    <img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white">
    <img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">
    <img alt="Static Badge" src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
</div>

#### BE
<div>
    <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">
</div>

### 2.2 개발 환경
<div>
    <img src="https://img.shields.io/badge/visualstudio-007ACC?style=for-the-badge&logo=visualstudio&logoColor=white">
    <img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
</div>

## 3. 프로젝트 구조와 개발 일정
### 3.1 프로젝트 Directory 구조

#### FE


#### BE

```
📦ChatGPT
 ┣ 📂accounts
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂main
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜tests.py
 ┃ ┗ 📜views.py
 ┣ 📂project
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜asgi.py
 ┃ ┣ 📜settings.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜wsgi.py
 ┣ 📂quiz
 ┃ ┣ 📂__pycache__
 ┃ ┣ 📂migrations
 ┃ ┣ 📜__init__.py
 ┃ ┣ 📜admin.py
 ┃ ┣ 📜apps.py
 ┃ ┣ 📜models.py
 ┃ ┣ 📜permissions.py
 ┃ ┣ 📜serializers.py
 ┃ ┣ 📜tests.py
 ┃ ┣ 📜urls.py
 ┃ ┗ 📜views.py
 ┣ 📂static
 ┣ 📜.env
 ┣ 📜db.sqlite3
 ┗ 📜manage.py
```

### 3.2 프로젝트 URL 구조

#### FE

|url 주소  |html 파일이름  |
|:-------------|:--------------|
|''|main.html|
|'404/'|404.html|
|'accounts/login/'|login.html|
|'accounts/register/'|register.html|
|'quiz/'|quiz.html|
|'quiz/list/'|quizlist.html|

#### BE

|app: accounts  |View  |Method   |
|:-------------|:--------------|:------------|
|'auth/'|AuthAPIView|POST|
|'auth/'|AuthAPIView|DELETE|
|'register/'|UserCreateAPIView|CREATE|
|'refresh_token/'|token_refresh|POST|
|'verify/'|token_verify|POST|

### 3.3 와이어프레임
    <img src="/img/WireFrame-main.png">
    <img src="/img/WireFrame-login.png">
    <img src="/img/WireFrame-signup.png">
    <img src="/img/WireFrame-quiz.png">
    <img src="/img/WireFrame-quizlist.png">

### 3.4 개발 일정(WBS)
    <img src="/img/WBS.png">

### 3.5 ERD
    <img src="/img/ERD.png">

## 4. UI
    <img src="/img/main.png">
    <img src="/img/register.gif">
    <img src="/img/login.gif">
    <img src="/img/logout.gif">
    <img src="/img/quiz.gif">
    <img src="/img/quizlist.png">

## 5. 기능

- 회원가입 및 로그인 기능
- 하루 5회 랜덤한 영어퀴즈
- 자신의 역대 기록

## 6. 개발 이슈

- DRF를 처음하면서 가장 필요해진부분이 block 템플릿이었다. 헤더나 푸터같은부분은 과도하게 중복되는부분이 많았다.
그래서 html을 include하거나 자주쓰는 자바스크립트를 한데 묶어서 사용하는 방법을 찾아보았다.
```html
<header data-include-file="./include/header.html" class="header-wrap includeJs"></header>
<footer data-include-file="./include/footer.html" class="footer-wrap includeJs"></footer>
<script src="/JavaScript/base.js"></script>
```

```javascript
// include.js
(function () {
    function includeHtml() {
        const includeTarget = document.querySelectorAll(".includeJs");
        includeTarget.forEach(function (el, idx) {
            const targetFile = el.dataset.includeFile;
            if (targetFile) {
                let xhttp = new XMLHttpRequest();

                xhttp.onreadystatechange = function () {
                    if (this.readyState === XMLHttpRequest.DONE) {
                        this.status === 200 ? (el.innerHTML = this.responseText) : null;
                        this.status === 404 ? (el.innerHTML = "include not found.") : null;
                    }
                };
                xhttp.open("GET", targetFile, true);
                xhttp.send();
                return;
            }
        });
    }

    includeHtml();
})();
```
```javascript
// base.js
const script1 = document.createElement('script');
script1.src = '/JavaScript/include.js';
document.head.appendChild(script1);

const script2 = document.createElement('script');
script2.src = '/JavaScript/header.js';
document.head.appendChild(script2);

const script3 = document.createElement('script');
script3.src = '/JavaScript/logout.js';
document.head.appendChild(script3);

const script4 = document.createElement('script');
script4.src = '/JavaScript/token.js';
document.head.appendChild(script4);
```

- include로 자바스크립트와 html을 받다보니, 로드되기 전에 html을 읽어오면 헤더의 login logout을 동적으로 조정하지 못하게 되었다.
그래서 settimeout을 이용해서, 실패할떄마다 일정시간 뒤 반복해서 실행하게 하였다.

```javascript
(function updateHeader() {
    const sign = document.querySelector('#sign');
    const register = document.querySelector('#register');
    const access = sessionStorage.getItem('access');
    let temp = 0

    if (sign) {
        if (access) {
            sign.innerHTML = `<button class="nav-link" onclick="logout()"><i class="fa-solid fa-right-from-bracket"></i></button>`;
        } else {
            register.innerHTML = `<a class="nav-link" href="/accounts/register"><i class="fa-solid fa-user-plus"></i></a>`;
            sign.innerHTML = `<a class="nav-link" href="/accounts/login"><i class="fa-solid fa-right-to-bracket"></i></a>`;
        }
    } else {
        temp++
        console.log(temp + '회 실패')
        setTimeout(updateHeader, 100);
    }
})()
```

- 이번에도 역시 비밀번호 해싱 오류가 있었고, 원래는 중간에 뺴와서 set_password를 하려고했었다.
그런데 직렬화 과정에서 해싱을 해주는 방법이 있음을 보고 그 방법으로 해결했다.
```python
def create(self, validated_data):
    '''
    직렬화할떄 비밀번호를 해싱하는작업.
    '''
    user = super().create(validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user
```

- User 커스텀 클래스에서 related_name을 요구하는 버그가 있었다.
```
ERRORS:
accounts.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'accounts.User.groups' clashes with reverse accessor for 'auth.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'accounts.User.groups' or 'auth.User.groups'.
accounts.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'accounts.User.user_permissions' clashes with reverse accessor for 'auth.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'accounts.User.user_permissions' or 'auth.User.user_permissions'.
auth.User.groups: (fields.E304) Reverse accessor 'Group.user_set' for 'auth.User.groups' clashes with reverse accessor for 'accounts.User.groups'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.groups' or 'accounts.User.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor 'Permission.user_set' for 'auth.User.user_permissions' clashes with reverse accessor for 'accounts.User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'auth.User.user_permissions' or 'accounts.User.user_permissions'.
```
해결은 유저 클래스를 기본을 사용해서 해결했지만 settings.py를 수정하지 않았기 떄문인듯싶다.
```python
AUTH_USER_MODEL = 'app.User'
```


## 7. 개발하면서 느낀점

- 처음엔 DRF라고 큰 차이는 없을거라 생각했는데, jwt 지식 부족으로 인증부분에서 며칠을 투자하기도 했고, nginx를 연동하는데도 꼬박 하루가 걸렸던것같다.
하지만 다시 처음부터하라고 하면 두개 합쳐 하루면 충분할거라는 자신감이 붙었다. 시간이 조금 더 있었더라면 공식문서도 파헤쳐보고 연구해볼 수 있었을텐데 조금 아쉬웠다.

- 처음 기획했던건 chatGPT를 교사처럼 사용해서 문제를 받고, 답안을 주면 정답여부를 받고, 다음문제를 호명하면 또 다른 문제를 받고,
총 결과를 호명하면 총 결과를 받고 끝내는 방식으로 대화하듯이 풀어나가려고 기획했었다.
그러나 답변이 튀는건 둘쨰치고 앞부분에 대화햇던것을 기억하지 못하는 대답이 돌아와서 문제와 답을 한번에주고 자바스크립트로 모두 해결해버리는 방식으로 전환하였다.
이 역시 시키는대로 오지않고 가끔 이상한 대답을 하는 것 떄문에 이부분은 조금 더 해결해야할듯한 숙제인 듯 하다.
