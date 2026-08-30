
# MTVS, Lounge Reservation 📖

## 🪑Intro: 서비스 소개
<br/>
<strong>MTVS, Reservation</strong>이란 메타버스 아카데미 학생들을 위한 라운지 예약 시스템으로,<br/>
온라인으로 편하게 예약하여 중복없이 사용할 수 있습니다.<br/>
추가로 메인페이지에 존재하는 게시판에서<br/>
학생들간의 소통이 가능하며, 불편사항 또한 접수받을 수 있는 서비스입니다.

<br/>

### ⭐️ Feat: 주요 기능 소개

#### 1) 라운지 예약 서비스
라운지를 이용하기 위한 예약 서비스를 제공하며 날짜별, 시간대별로 예약할 수 있습니다.
사용자에게 편의성을 제공합니다.

#### 2) 커뮤니티
게시판에서 사용자들끼리 각종 정보와 자유로운 게시글을 통해 자유로이 소통할 수 있으며,
불편게시판에서는 이용에 관한 불편사항을 제시하여 운영진들이 확인 후 피드백할 수 있는 환경을 제공합니다.

#### 3) 마이페이지
나의 정보를 확인할 수 있습니다.

<br/>
📅 <strong>프로젝트 기간</strong> : 2023.06.21 ~ 2023.06.28 (약 8일)


## 🛠 개발 환경

- Language  : Java 11 (OpenJDK 11.0.15.9-1)
- DB : MySQL
- Server : Apache Tomcat
- Front : HTML5, CSS3, JavaScript, jQuery, Bootstrap
- Framework : Spring boot(2.7.12)
- Build Tool : Maven
- IDE : Intellij
- 형상 관리 : Github

<br>



## 🗂 Directory: 디렉토리 구조

```
/src/main
├── board
│   ├── controller
│   ├── domain
│   │    ├── entity
│   │    └── repository
│   ├── dto
│   └── service
├── members
│   └── login
│        ├── application
│        │    ├── controller
│        │    └── dto
│        ├── common
│        │    ├── argumentresolver
│        │    ├── interceptor
│        │    └── session
│        └── domain
│              ├── entity
│              ├── repository
│              └── service
└── reservation
     ├── controller
     ├── dto
     ├── entity
     ├── repository
     └── service

/main/resources
├── static
│   ├── css
│   └── img
└── static
     ├── board
     ├── common
     ├── css
     ├── error
     ├── login
     ├── members
     └── reservation

/src/test
└── test                                   
```

## 테스트
```
1. login - Domain - service의 LoginServiceTest        
2. login - Domain - service의 MemberServiceTest
3. reservation - controller의 reserveServiceTest
``` 

<br/>



## 📔 Architecture: 서비스 아키텍쳐
![image](https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/ac93e883-b8ae-4920-a232-5cdf6e867115)
<br>
<br>
<br>



## 📌 SW유스케이스
위키 - [USECASE](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/USECASE)

![image](https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/eb45c7ef-7718-4aac-8b1b-b525ff4d1b7b)
<br>
<br>
<br>


## 🧾 서비스 흐름도
위키 - [FlowChart](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/Flow-Chart)

![image](https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/a76c1027-3ade-4284-aec0-96be084f5995)
<br>
<br>
<br>

## 📊 E-R Diagram
위키 - [ERD](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/ERD)
![image](https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/ffda4a80-3e67-434f-8924-5cb0d876d20d)

<br>
<br>
<br>

## ✅ 화면 구성

### 메인페이지 / 로그인 / 회원가입
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/4c88d3c4-3700-4640-94de-27fccc16afa5">
<br>
<br>

### 마이페이지 (회원 정보 / 예약 목록)
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/8c71162e-b272-4d9d-84a9-2cb8804cf450">
<br>
<br>
<br>

### 게시판 (리스트 / 글쓰기 / 조회 / 수정)
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/21f19d87-4f9c-4530-8a5b-04613174b40a">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/e673124f-d556-418a-9f32-9db519423979">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/983a1c2c-bc43-4174-9fb8-cb74bda80f1e">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/63f7e3ec-d1ce-443b-963a-98a61b847933">
<br>
<br>
<br>

### 메타버스 스터디 라운지 예약 시스템
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/b8d04a46-5df1-491c-9b46-5a9648b5255f">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/c5d15087-e574-4b17-bf88-fd95250e23f0">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/0282ec9d-8613-4eac-8916-a07f7de3857e">
<img width="960" alt="image" src="https://github.com/MTVS-CodeMagician/MTVS-reserve/assets/136250818/faf48e0c-e2fa-4a96-a4ef-679f919439b5">
<br>
<br>
<br>



## 💻 팀원 소개


| 이름                                                           | 포지션    | 담당 기능 구현                          |
|----------------------------------------------------------------|-----------| ----------------------------------------|
| <a href="https://github.com/jinvvoo" target='_blank'>김진우</a> | `서버개발`| `커뮤니티 게시판 리스트` `조회, 글쓰기, 수정, 삭제` `게시판 디자인` `무한스크롤` `DB`| 
| <a href="https://github.com/taedyv" target='_blank'>김태현</a> | `서버개발`| `로그인 페이지` `회원가입, 로그인 기능` `에러 페이지` `회원 데이터 검증` `DB`| 
| <a href="https://github.com/JeonTaeHyeon" target='_blank'>전태현</a> | `서버개발`| `예약 조회 기능` `예약 삭제 기능` `메인페이지` `예약 기능 테스트` `프론트 엔드 디자인` `DB` | 
| <a href="https://github.com/jeongmino1" target='_blank'>정민호</a> | `서버개발`| `커뮤니티 게시판 리스트` `게시판 조회, 글쓰기, 수정, 삭제` `게시판 기능 테스트` `DB`| 
| <a href="https://github.com/CodeJugller" target='_blank'>진용민</a> | `서버개발`| `예약기능` `특정 조건에 따른 예약 조회 기능` `예약 페이지` `프론트 엔드 디자인` `My Page` `DB`| 



<br>
<br>

# Wiki
### [Home](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki)

### 협업
* [깃플로우](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/%EA%B9%83%ED%94%8C%EB%A1%9C%EC%9A%B0) <br>
* [프로젝트보드](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8%EB%B3%B4%EB%93%9C) <br>

### 프로젝트 세부 사항
* [Notion](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/Notion) <br>
* [Testcode](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/%ED%85%8C%EC%8A%A4%ED%8A%B8%EC%BD%94%EB%93%9C) <br>
* [API](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/API) <br>

### 적용 기술 및 전략
* [USECASE](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/USECASE)
* [ERD](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/ERD)
* [Github-Flow](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/Github-Flow)
* [Flow-Chart](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/Flow-Chart)
* [Figma](https://github.com/MTVS-CodeMagician/MTVS-reserve/wiki/Figma)
