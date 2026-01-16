# 노션 포트폴리오 블록 다이어그램 업로드 가이드

## 📌 개요

향상된 노션 포트폴리오가 생성되었습니다! 이제 블록 다이어그램 이미지를 업로드하여 더욱 전문적으로 만들어보세요.

**새 포트폴리오 URL:** https://notion.so/2e8f0746982181858cf1ea19a1fc6239

---

## 🖼️ 업로드할 블록 다이어그램

### 1. L-LPC (H-Sensor) System
**폴더:** `Project_Files/02_L-LPC/Images/`

**업로드할 이미지 (14개):**

#### FPGA 시스템 (9개)
```
H_sensor_FPGA_Slide1.png  - 전체 시스템 아키텍처
H_sensor_FPGA_Slide2.png  - SPI 통신 인터페이스
H_sensor_FPGA_Slide3.png  - 데이터 버퍼링 구조
H_sensor_FPGA_Slide4.png  - 타이밍 다이어그램
H_sensor_FPGA_Slide5.png  - ADC 인터페이스
H_sensor_FPGA_Slide6.png  - 제어 로직
H_sensor_FPGA_Slide7.png  - 파워 시퀀스
H_sensor_FPGA_Slide8.png  - 에러 핸들링
H_sensor_FPGA_Slide9.png  - 전체 플로우차트
```

#### Analog Frontend (5개)
```
H_sensor_Analog_Frontend_Slide1.png  - TIA 회로
H_sensor_Analog_Frontend_Slide2.png  - Inst-Amp 구성
H_sensor_Analog_Frontend_Slide3.png  - Filter 설계
H_sensor_Analog_Frontend_Slide4.png  - ADC 인터페이스
H_sensor_Analog_Frontend_Slide5.png  - 전원 공급 회로
```

**업로드 위치:** 노션 페이지 > "1️⃣ L-LPC" 토글 > "📐 System Block Diagram" 섹션

---

### 2. Psi-1000/3000 Pressure Controller
**폴더:** `Project_Files/03_Psi-1000/Images/`

**업로드할 이미지 (6개):**
```
06. Psi-1000_Rev0.2_수정사항_Slide1.png  - 시스템 개요
06. Psi-1000_Rev0.2_수정사항_Slide2.png  - PID 제어 블록
06. Psi-1000_Rev0.2_수정사항_Slide3.png  - 통신 구조
06. Psi-1000_Rev0.2_수정사항_Slide4.png  - 하드웨어 구성
Psi-3000 Board System Block Diagram_20210412_Slide1.png  - 3000 시스템
Psi-3000 Board System Block Diagram_20210412_Slide2.png  - 3000 회로
```

**업로드 위치:** 노션 페이지 > "2️⃣ Psi-1000/3000" 토글 > "🎛️ PID Control Algorithm" 섹션

---

### 3. MS (Mass Spectrometer)
**폴더:** `Project_Files/01_MS_Mass_Spectrometer/Images/`

**업로드할 이미지 (11개):**
```
ASTON_block_diagram(250814)_Slide1.png   - 전체 시스템
ASTON_block_diagram(250814)_Slide2.png   - RF 제어
ASTON_block_diagram(250814)_Slide3.png   - 데이터 수집
ASTON_block_diagram(250814)_Slide4.png   - 통신 구조
ASTON_block_diagram(250814)_Slide5.png   - 타이밍
ASTON_block_diagram(250814)_Slide6.png   - 전원 시스템
ASTON_block_diagram(250814)_Slide7.png   - 센서 인터페이스
ASTON_block_diagram(250814)_Slide8.png   - 제어 로직
ASTON_block_diagram(250814)_Slide9.png   - 에러 처리
ASTON_block_diagram(250814)_Slide10.png  - 플로우차트
ASTON_block_diagram(250814)_Slide11.png  - 종합
```

**업로드 위치:** 노션 페이지 > "4️⃣ MS" 토글 내부

---

## 📝 이미지 업로드 방법

### 방법 1: 드래그 앤 드롭 (추천)
1. Windows 탐색기에서 이미지 폴더 열기
2. 노션 페이지의 해당 섹션으로 이동
3. 이미지를 드래그하여 노션 페이지에 드롭
4. 이미지 크기 조정: 클릭 후 모서리 드래그

### 방법 2: 업로드 버튼
1. 노션에서 `/image` 입력
2. "Upload" 선택
3. 파일 선택하여 업로드

### 방법 3: 외부 URL (현재는 로컬 파일만)
- GitHub에 이미지 푸시 후 raw URL 사용
- 예: `https://raw.githubusercontent.com/gari210404/Portfolio_Professional/master/Project_Files/...`

---

## 🎨 이미지 레이아웃 추천

### L-LPC 프로젝트
```
📐 System Block Diagram
├── 전체 시스템 아키텍처 (Slide1) - Full width
├── FPGA Interface 상세
│   ├── Slide2, Slide3 (나란히 2개)
│   └── Slide4, Slide5 (나란히 2개)
├── Analog Frontend
│   ├── Slide1, Slide2 (나란히 2개)
│   └── Slide3 (Full width)
```

### Psi-1000/3000 프로젝트
```
🎛️ PID Control Algorithm
├── 시스템 개요 (수정사항 Slide1) - Full width
├── PID 블록 (수정사항 Slide2) - Full width
└── Psi-3000 Board (Slide1, Slide2 나란히)
```

---

## 💡 이미지 설명 추가 (Caption)

각 이미지 아래에 설명 추가:

```
🖼️ [이미지]
📝 설명: H-Sensor FPGA 전체 시스템 아키텍처
- Xilinx Artix-7 FPGA
- SPI 인터페이스 (20MHz)
- 데이터 버퍼: 2048 samples
```

---

## 🚀 추가 개선 사항

### 1. 칼럼 레이아웃 사용
노션에서 `/column` 입력하여 이미지를 나란히 배치

### 2. 토글 사용
너무 많은 이미지는 토글로 숨기기:
```
▶ 상세 블록 다이어그램 (클릭하여 펼치기)
  [이미지들...]
```

### 3. 캡션에 주석 추가
```
📌 주요 포인트:
- TIA 증폭 회로: OPA657 (1GHz GBW)
- S/N 비율: > 60dB
- 다이나믹 레인지: 16-bit
```

---

## 📊 업로드 후 확인 사항

✅ 모든 이미지가 선명하게 표시되는지 확인
✅ 이미지 순서가 논리적으로 배치되었는지 확인
✅ 설명(Caption)이 각 이미지에 추가되었는지 확인
✅ 모바일에서도 보기 좋은지 확인

---

## 🎯 최종 결과

블록 다이어그램 업로드 후:
- **L-LPC 프로젝트**: 14개 이미지
- **Psi-1000/3000**: 6개 이미지
- **MS (Mass Spectrometer)**: 11개 이미지
- **총 31개의 전문적인 블록 다이어그램**

이렇게 하면 포트폴리오가 훨씬 더 전문적이고 기술적으로 보일 것입니다! 🚀

---

## 📞 문의

이미지 업로드 중 문제가 발생하면:
- 노션 페이지: https://notion.so/2e8f0746982181858cf1ea19a1fc6239
- GitHub 레포: https://github.com/gari210404/Portfolio_Professional
