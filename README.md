# 🧠 Real-Time Face Recognize System

실시간 얼굴 인식 기반 출석 체크 시스템입니다.
프론트엔드와 백엔드, 두 개의 독립된 실행 환경으로 구성되어 있으며
각 모듈은 서로 API 통신을 통해 동작합니다.

---

## 🏗️ 프로젝트 구조

| 구성 요소                    | 기술 스택                | 배포 위치     | 역할                    |
| ------------------------ | -------------------- | --------- | --------------------- |
| **Frontend (Streamlit)** | Python, Streamlit    | **배포 환경** | 실시간 영상 입력 및 결과 시각화    |
| **Backend (FastAPI)**    | Python, FastAPI      | **로컬 서버** | 얼굴 임베딩 추출 및 출석 로직 처리  |
| **출석 DB**                | SQLite               | **로컬**    | 출석 내역 저장 및 조회         |
| **얼굴 DB**                | Pinecone (Vector DB) | **배포 환경** | 얼굴 임베딩 벡터 저장 및 유사도 검색 |

---

## 🚀 실행 방법

두 서버를 각각 실행해야 합니다.
두 `main.py`는 서로 다른 파일입니다.

### 1️⃣ Streamlit (Frontend)

```bash
streamlit run main.py [필요한 옵션]
```

### 2️⃣ FastAPI (Backend)

```bash
nohup uvicorn main:app [필요한 옵션] &
```

> 예: `nohup uvicorn main:app --host 0.0.0.0 --port 8888 &`

---

## 💾 데이터베이스 구성

### 🗂️ attendance.db (SQLite)

* 로컬에 저장되는 출석 기록 DB
* 주요 컬럼:

  * `student_id`
  * `student_name`
  * `timestamp`

### 🧬 Pinecone Vector DB

* 얼굴 임베딩 벡터를 저장하고 유사도 기반으로 검색
* 각 벡터는 사용자 ID와 연결됨

---

## 🔄 시스템 흐름 요약

1. Streamlit 앱에서 실시간으로 얼굴 이미지를 촬영
2. 이미지가 FastAPI 서버로 전송됨
3. FastAPI가 얼굴 임베딩을 추출 후 Pinecone에 질의
4. 일치하는 인물이 있으면 SQLite에 출석 로그를 기록
5. Streamlit 화면에 결과(이름) 표시

---


## 🧩 추가 개발 예정

* Milvus로 얼굴 DB 전환 테스트
* Streamlit 사용자/관리자 분리 기능 추가


