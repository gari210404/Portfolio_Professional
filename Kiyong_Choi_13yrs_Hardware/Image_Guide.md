# 포트폴리오 이미지 삽입 가이드

**작성일:** 2026-01-14  
**대상:** 최기용 Senior Hardware Engineer Portfolio

---

## 📊 변환 완료 요약

### PPT → PNG 이미지 변환 성공!

```
총 8개 PPT 파일 → 46개 PNG 이미지 (16.5MB)

변환된 프로젝트:
✅ MS (Mass Spectrometer)      - 11개 이미지 (2.0MB)
✅ Nu-2000 (Optical Analysis)  - 3개 이미지 (0.5MB)
✅ Psi-1000 (Pressure Control) - 6개 이미지 (1.1MB)
✅ L-Titrator (pH Measurement) - 3개 이미지 (0.7MB)
✅ ATIK JIG (Test Jig)         - 5개 이미지 (2.2MB)
✅ Lux (Optical Sensor)        - 18개 이미지 (10.0MB)
```

---

## 📂 이미지 파일 위치

모든 이미지는 프로젝트별 Images 폴더에 저장되어 있습니다:

```
D:\Portfolio_Professional\Project_Files\
├── 01_MS_Mass_Spectrometer\
│   └── Images\
│       ├── ASTON_block_diagram(250814)_Slide1.png  ← 시스템 개요
│       ├── ASTON_block_diagram(250814)_Slide2.png  ← RF Board
│       ├── ASTON_block_diagram(250814)_Slide3.png  ← Ion Detector
│       ├── ASTON_block_diagram(250814)_Slide4.png  ← Data Acquisition
│       └── ... (총 11개 슬라이드)
│
├── 03_Psi-1000\
│   └── Images\
│       ├── Psi-3000 Board System Block Diagram_Slide1.png
│       ├── Psi-3000 Board System Block Diagram_Slide2.png
│       ├── 06. Psi-1000_Rev0.2_수정사항_Slide1.png  ← 회로 개선
│       ├── 06. Psi-1000_Rev0.2_수정사항_Slide2.png
│       └── ... (총 6개)
│
├── 04_Nu-2000\
│   └── Images\
│       ├── 02. Nu-2000_Main_Block_Diagram_Slide1.png
│       ├── 02. Nu-2000_Main_Block_Diagram_Slide2.png
│       └── 02. Nu-2000_Main_Block_Diagram_Slide3.png
│
├── 06_L-Titrator\
│   └── Images\
│       ├── L-titrator_Simple_Block_Diagram_211019_최기용_Slide1.png
│       ├── Reservoir_Main_Block_diagram_220923_v0.1_Slide1.png
│       └── Reservoir_Main_Block_diagram_220923_v0.1_Slide2.png
│
├── 10_Lux\
│   └── Images\
│       ├── OAS-DSP개발 HW 검토 사항_20210112_Slide1.png
│       ├── OAS-DSP개발 HW 검토 사항_20210112_Slide2.png
│       └── ... (총 18개 - HW 검토 자료)
│
└── 11_ATIK_JIG\
    └── Images\
        ├── Jig_Block_diagram_220413_v0.3_Slide1.png
        ├── Jig_Block_diagram_220413_v0.3_Slide2.png
        └── ... (총 5개)
```

---

## 🖼️ Word 문서에 이미지 삽입 방법

### 방법 1: 수동 삽입 (권장)

1. **Word 문서 열기**
   ```
   D:\Portfolio_Professional\Kiyong_Choi_13yrs_Hardware\
   최기용_Senior_Hardware_Engineer_Professional_v2.docx
   ```

2. **프로젝트 섹션으로 이동**
   - 예: "1. MS (Mass Spectrometer) System" 섹션 찾기

3. **이미지 삽입 위치 선택**
   - "시스템 블록 다이어그램:" 다음 줄에 커서 위치

4. **이미지 삽입**
   ```
   Insert → Pictures → This Device
   
   파일 선택:
   D:\Portfolio_Professional\Project_Files\
   01_MS_Mass_Spectrometer\Images\
   ASTON_block_diagram(250814)_Slide1.png
   ```

5. **이미지 크기 조정**
   - 이미지 클릭
   - Layout Options → "In Line with Text"
   - 너비: 15cm (A4 페이지에 맞게)
   - 높이: 자동 조정

6. **캡션 추가**
   ```
   이미지 우클릭 → Insert Caption
   
   Caption: Figure 1: MS System Architecture
   Position: Below selected item
   ```

---

### 방법 2: 드래그 앤 드롭

1. Windows 탐색기에서 Images 폴더 열기
2. PNG 파일 선택
3. Word 문서로 드래그 앤 드롭
4. 크기 및 위치 조정

---

## 📝 프로젝트별 추천 이미지

### 1. MS (Mass Spectrometer)

**필수 이미지:**
```
Slide1.png - System Overview (전체 시스템 구조)
Slide2.png - RF Board Architecture
Slide3.png - Ion Detector Block Diagram
Slide4.png - Data Acquisition System
```

**삽입 위치:**
```
포트폴리오 문서:
"### 1. MS (Mass Spectrometer) System"
"시스템 블록 다이어그램:" 섹션 아래
```

**캡션 예시:**
```
[Figure 1] MS System Architecture - ASTON Reverse Engineering
[Figure 2] RF Board - Quadrupole Mass Spectrometer Control
[Figure 3] Ion Detector - High-Voltage Signal Conditioning
[Figure 4] Data Acquisition - 18-bit ADC System
```

---

### 2. Nu-2000 (Optical Analysis)

**필수 이미지:**
```
Slide1.png - Main System Block Diagram
Slide2.png - LED Driver & Photodiode TIA
Slide3.png - Detailed Circuit Explanation
```

**삽입 위치:**
```
"### 4. Nu-2000 (OAS-DSP) Optical Analysis"
"시스템 블록 다이어그램:" 섹션 아래
```

**캡션 예시:**
```
[Figure 5] Nu-2000 Main System Architecture
[Figure 6] LED Driver & Photodiode TIA Circuit
[Figure 7] RTD Temperature Measurement System
```

---

### 3. Psi-1000 (Pressure Control)

**필수 이미지:**
```
Psi-3000 Board System Block Diagram_Slide1.png - System Overview
Psi-3000 Board System Block Diagram_Slide2.png - Detailed Block
06. Psi-1000_Rev0.2_수정사항_Slide1.png - Circuit Improvements
```

**삽입 위치:**
```
"### 3. Psi-1000 Pressure Controller"
"시스템 블록 다이어그램:" 섹션 아래
```

**캡션 예시:**
```
[Figure 8] Psi-1000 Pressure Control System Architecture
[Figure 9] PID Controller & MFC Interface
[Figure 10] Rev 0.2 Circuit Improvements & Optimizations
```

---

### 4. L-Titrator (pH Measurement)

**필수 이미지:**
```
L-titrator_Simple_Block_Diagram_Slide1.png - Simple Overview
Reservoir_Main_Block_diagram_Slide1.png - Main System
Reservoir_Main_Block_diagram_Slide2.png - Detailed Circuit
```

**삽입 위치:**
```
"### 7. 추가 프로젝트 요약"
"L-Titrator" 항목 아래
```

---

### 5. ATIK JIG (Test Jig)

**필수 이미지:**
```
Jig_Block_diagram_Slide1.png - JIG System Overview
Jig_Block_diagram_Slide2.png - MCU Module
Jig_Block_diagram_Slide3.png - I/O Interface
```

**삽입 위치:**
```
"### 7. 추가 프로젝트 요약"
"ATIK JIG" 항목 아래
```

---

### 6. Lux (Optical Sensor) - HW 검토 자료

**필수 이미지 (선별):**
```
OAS-DSP개발 HW 검토 사항_Slide1.png - 개요
OAS-DSP개발 HW 검토 사항_Slide3.png - 회로 설계 검토
OAS-DSP개발 HW 검토 사항_Slide5.png - PCB 레이아웃 검토
OAS-DSP개발 HW 검토 사항_Slide10.png - 테스트 결과
```

**참고:**
- 18개 슬라이드 중 주요 내용만 선별 (4-5개)
- 기술 검토, 회로 분석, 개선 제안 내용 중심

---

## 🎨 이미지 포맷팅 가이드

### 레이아웃 옵션

```
Word에서 이미지 클릭 → Layout Options

권장 설정:
✅ In Line with Text (기본)
   - 장점: 텍스트와 함께 이동
   - 용도: 본문 설명과 함께 표시

대안:
○ Square
   - 장점: 텍스트가 이미지 주변 감싸기
   - 용도: 넓은 다이어그램

○ Tight
   - 장점: 텍스트가 이미지 윤곽 따라감
   - 용도: 불규칙한 형태 이미지
```

### 크기 조정

```
권장 크기:
- 너비: 15cm (A4 페이지 여백 내)
- 높이: 자동 (비율 유지)

작은 이미지 (다이어그램):
- 너비: 12cm
- 중앙 정렬

큰 이미지 (전체 시스템):
- 너비: 16cm (페이지 거의 전체)
- 중앙 정렬
```

### 이미지 정렬

```
이미지 클릭 → Layout → Position

권장:
✅ Center (중앙 정렬)
   - 가장 전문적
   - 가독성 좋음

대안:
○ Left (왼쪽 정렬)
   - 설명과 함께 배치 시
```

---

## 📋 캡션 작성 가이드

### 캡션 형식

```
권장 형식:
[Figure X] 제목 - 부제목

예시:
[Figure 1] MS System Architecture - ASTON Reverse Engineering
[Figure 2] Nu-2000 Block Diagram - LED Driver & Photodiode TIA
[Figure 3] Psi-1000 PID Controller - Pressure Control Loop
```

### 캡션 자동 번호

```
Word에서:
References → Insert Caption

설정:
- Label: Figure
- Position: Below selected item
- Numbering: 1, 2, 3, ...

자동 생성 예시:
Figure 1: MS System Architecture
Figure 2: RF Board Block Diagram
...
```

### 캡션 스타일

```
캡션 선택 → Home → Styles → Caption

권장 포맷:
- 폰트: Arial 9pt
- 색상: 회색 (Gray 50%)
- 정렬: 중앙
- 간격: 위 6pt, 아래 12pt
```

---

## 🔧 실전 삽입 예시

### 예제 1: MS 프로젝트

**1단계: 위치 찾기**
```
Word 문서에서:
Ctrl+F → "MS (Mass Spectrometer) System" 검색
"시스템 블록 다이어그램:" 섹션으로 이동
```

**2단계: 이미지 삽입**
```
커서를 아래와 같이 위치:

시스템 블록 다이어그램:

[커서 위치] ← 여기

```mermaid
...
```

Insert → Pictures → 
D:\Portfolio_Professional\Project_Files\01_MS_Mass_Spectrometer\Images\
ASTON_block_diagram(250814)_Slide1.png
```

**3단계: 크기 조정**
```
이미지 클릭
Picture Format → Size
Width: 15 cm (높이 자동)
```

**4단계: 캡션 추가**
```
이미지 우클릭 → Insert Caption
Caption: Figure 1: MS System Architecture
```

**최종 결과:**
```
시스템 블록 다이어그램:

[MS 시스템 아키텍처 이미지]
Figure 1: MS System Architecture

**기술 사양:**
- System Architecture: ASTON Reverse Engineering 기반 설계
...
```

---

### 예제 2: 여러 이미지 연속 삽입

**Psi-1000 프로젝트:**

```
[이미지 1]
Figure 8: Psi-1000 System Block Diagram

[이미지 2]
Figure 9: PID Controller & MFC Interface

[이미지 3]
Figure 10: Rev 0.2 Circuit Improvements

**주요 개선사항:**
- 출력 오실레이션 제거
- ADC 노이즈 50% 감소
...
```

---

## ✅ 삽입 완료 체크리스트

### 프로젝트별 체크

- [ ] **MS (Mass Spectrometer)**
  - [ ] System Overview (Slide1)
  - [ ] RF Board (Slide2)
  - [ ] Ion Detector (Slide3)
  - [ ] Data Acquisition (Slide4)

- [ ] **Nu-2000 (Optical)**
  - [ ] Main Block Diagram (Slide1)
  - [ ] LED Driver & TIA (Slide2)
  - [ ] Circuit Details (Slide3)

- [ ] **Psi-1000 (Pressure)**
  - [ ] System Block Diagram (Slide1)
  - [ ] Detailed Block (Slide2)
  - [ ] Rev 0.2 Improvements (수정사항 Slide1-4)

- [ ] **L-Titrator**
  - [ ] Simple Block Diagram
  - [ ] Reservoir Main (Slide1-2)

- [ ] **ATIK JIG**
  - [ ] JIG System Overview (Slide1)
  - [ ] MCU Module (Slide2-3)
  - [ ] I/O Interface (Slide4-5)

- [ ] **Lux (선택적)**
  - [ ] HW 검토 주요 슬라이드 4-5개

### 포맷팅 체크

- [ ] 모든 이미지 크기 일관성 (15cm 너비)
- [ ] 모든 이미지 중앙 정렬
- [ ] 모든 이미지에 캡션 추가
- [ ] 캡션 번호 연속성 확인 (Figure 1, 2, 3...)
- [ ] 이미지 해상도 확인 (선명도)
- [ ] 페이지 넘김 확인 (이미지가 페이지 중간에 잘리지 않도록)

### 최종 확인

- [ ] 목차 업데이트 (References → Update Table)
- [ ] Figure 리스트 생성 (선택사항)
- [ ] PDF 변환 테스트
- [ ] 파일 크기 확인 (< 10MB 권장)

---

## 📤 PDF 변환 및 배포

### PDF 변환

**방법 1: Word에서 직접**
```
File → Save As → PDF
설정:
✅ Optimize for: Standard (publishing online and printing)
✅ Include: Document properties
✅ PDF/A compliant: 체크 (장기 보관용)
```

**방법 2: 전문 PDF 변환기**
```
Adobe Acrobat DC:
- 고품질 이미지 유지
- 북마크 자동 생성
- 검색 가능한 텍스트

출력 파일:
최기용_Senior_Hardware_Engineer_Professional_v2.pdf
```

### 파일 크기 최적화

```
이미지 압축:
Word → File → Options → Advanced → Image Size and Quality

설정:
- Default resolution: 220 ppi (고품질)
- Do not compress images: 체크 해제

예상 파일 크기:
- Word: 25-30MB (이미지 46개 포함)
- PDF: 15-20MB (압축 후)
```

---

## 🎯 최종 포트폴리오 구성

```
완성된 포트폴리오:

최기용_Senior_Hardware_Engineer_Portfolio (폴더)
├── 최기용_Senior_Hardware_Engineer_Professional_v2.docx (Word)
├── 최기용_Senior_Hardware_Engineer_Professional_v2.pdf (PDF)
├── Project_Files\ (회로도, PCB, 이미지)
│   ├── 01_MS_Mass_Spectrometer\
│   ├── 02_L-LPC\
│   ├── 03_Psi-1000\
│   ├── 04_Nu-2000\
│   └── ... (11개 프로젝트)
└── README.md (파일 설명서)

배포 방법:
1. USB 드라이브에 복사
2. 클라우드 (Google Drive, Dropbox) 링크 공유
3. 이메일 첨부 (PDF만, < 10MB)
4. 노션/GitHub Pages (온라인 버전)
```

---

## 💡 Pro Tips

### 1. 이미지 품질 유지

```
✅ 권장:
- 원본 PNG 파일 사용 (1920x1080)
- Word에서 압축하지 않음
- PDF 변환 시 고품질 설정

❌ 피해야 할 것:
- JPG로 재압축
- 스크린샷 사용
- 저해상도 이미지
```

### 2. 레이아웃 일관성

```
모든 프로젝트에 동일한 형식 적용:

[프로젝트 제목]
[텍스트 설명 3-5줄]
[이미지 1: 시스템 개요]
[이미지 2: 상세 회로]
[기술 사양 표]
[성과 요약]
```

### 3. 인쇄 최적화

```
인쇄용 설정:
- 용지: A4 (210×297mm)
- 여백: 좁게 (2cm 상하좌우)
- 컬러: 풀컬러 (블록 다이어그램 강조)
- 양면 인쇄: 권장

예상 페이지 수:
- 텍스트: 15-20 페이지
- 이미지: 20-25 페이지
- 총: 35-45 페이지
```

---

**작성:** 2026-01-14  
**최종 수정:** 2026-01-14  
**버전:** 1.0

**다음 작업:** Word 문서를 열어서 이미지 삽입 시작! 🚀
