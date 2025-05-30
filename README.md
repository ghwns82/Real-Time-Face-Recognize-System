# 🧠 얼굴 인식 시스템

이 프로젝트는 **Streamlit + FastAPI** 기반 얼굴 인식 시스템입니다.  
현재는 **ResNet18** 모델로 이미지 분류 결과를 반환하며,  
향후 **실시간 얼굴 인식 기능**으로 확장할 예정입니다.

---

## 📄 상세 기술 문서

- 🔍 [docs/2025_05_21.md](docs/2025_05_21.md): 현재 버전 전체 설명 및 실행 가이드
- 🕓 [CHANGELOG.md](CHANGELOG.md): 업데이트 이력 (버전별 변경사항 기록)

---

## ✅ 현재 구현된 기능

- [x] 업로드된 이미지 분류 (ResNet18, ViT, Swin-T, ConvNeXt-Tiny)
- [x] FastAPI `/predict` 엔드포인트 구현
- [x] `requirements.txt` 및 `.gitignore` 정리
- [x] 디렉토리 구조 개선 (`code/` 중심)
- [x] 실시간 웹캠 기반 분류


## 🔜 향후 계획
- [ ] 얼굴 인식 모델 적용 (e.g. face_recognition, dlib)
- [ ] 실시간 웹캠 기반 얼굴 인식 경량화
- [ ] 여러 모델 테스트 및 비교 (기본 모델 / 특화 모델 / 연구실 모델)
- [ ] https 적용