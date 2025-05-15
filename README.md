# 🧠 얼굴 인식 시스템 (이미지 업로드 + 실시간 인식)

이 프로젝트는 **Streamlit**과 **FastAPI**를 활용하여 구현한 얼굴 인식 웹 애플리케이션입니다.

사용자는 다음 두 가지 방식으로 얼굴 인식을 수행할 수 있습니다:

---

## ✅ 주요 기능

1. **이미지 업로드 기반 얼굴 인식**
   - 사용자가 이미지를 업로드하면, FastAPI 백엔드에서 얼굴을 인식하고 결과를 반환합니다.

2. **실시간 얼굴 인식 (웹캠 기반)**
   - 웹캠을 통해 실시간으로 얼굴을 감지하고, 주기적으로 백엔드에 전송하여 인식 결과를 화면에 표시합니다.

---

## 📁 디렉토리 구조

```
project-root/
├── frontend/
│   └── app.py              # Streamlit 프론트엔드
├── backend/
│   └── main.py             # FastAPI 백엔드
├── requirements.txt        # 전체 의존성 리스트
└── image.png               # 예시로 사용할 업로드 이미지
```


## 🚀 실행 방법

### 1. 프론트엔드 실행 (Streamlit)

```bash
streamlit run frontend/app.py
```
### 2. 백엔드 실행 (FastAPI)
```bash
uvicorn backend.main:app --reload
```
## ⚠️ 로컬 HTTP 환경에서 웹캠 사용 시 문제 해결

Chrome은 보안 정책상, **HTTP 환경에서는 웹캠 접근이 차단**됩니다.
개발 환경에서는 다음 방법으로 우회할 수 있습니다:

🔗 [Chrome: Insecure Origin as Secure (Medium)](https://medium.com/@om_bhandari/how-to-use-chrome-flags-unsafely-treat-insecure-origin-as-secure-for-local-development-0c0591b92f46)

> 예: `chrome://flags/#unsafely-treat-insecure-origin-as-secure`
> 입력창에 `http://localhost:8501`을 추가하세요.

---

## 📌 향후 계획

현재는 테스트 단계로, 얼굴 인식 결과로 고정된 `"테스트용"` 값을 반환하고 있습니다.
앞으로는 다양한 모델 넣어 테스트하면서, 업로드된 이미지나 실시간 영상에서 **실제 사용자의 얼굴을 인식하는 기능**을 추가할 예정입니다.





