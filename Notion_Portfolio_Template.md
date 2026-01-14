# 노션 포트폴리오 제작 가이드

## 📋 노션 포트폴리오 구조

```
📄 Cover Page (커버 페이지)
├── 🏠 Home (프로필 요약)
├── 💼 Projects (프로젝트 갤러리)
│   ├── 📁 MS (Mass Spectrometer)
│   ├── 📁 L-LPC
│   ├── 📁 Psi-1000
│   ├── 📁 Nu-2000
│   ├── 📁 Sigma-1000
│   └── ... (기타 프로젝트)
├── 🛠️ Skills & Tools (기술 스택)
├── 📊 Achievements (성과)
└── 📞 Contact (연락처)
```

---

## 🎯 Step 1: 노션 계정 생성

1. https://notion.so 접속
2. 계정 생성 (무료 플랜 사용 가능)
3. 새 페이지 생성: "최기용 - Hardware Engineer Portfolio"

---

## 🎨 Step 2: 커버 페이지 설정

### 커버 이미지 추가
1. 페이지 상단 "Add cover" 클릭
2. 옵션:
   - Unsplash: "circuit board", "electronics", "technology"
   - 또는 자신의 PCB 사진 업로드

### 아이콘 추가
1. 제목 옆 아이콘 클릭
2. 이모지 선택: ⚡ 또는 🔧

### 제목 작성
```
최기용 (Kiyong Choi)
Senior Hardware Design Engineer
13 Years Experience | 19+ Products | 99.5% Yield
```

---

## 📝 Step 3: 홈 페이지 (Profile Summary)

**노션에서 작업:**
1. 페이지 내에 `/callout` 입력 → Callout 블록 생성
2. 아이콘: 💡
3. 아래 내용 복사-붙여넣기:

---

### 💼 About Me

13년 경력의 시니어 하드웨어 설계 엔지니어입니다. 반도체 공정 장비 및 산업용 분석 기기를 위한 **고정밀 아날로그/디지털 회로 설계, 전원 시스템, PCB 레이아웃**을 전문으로 합니다.

**핵심 강점:**
- ✅ 19+ 제품 개발 완료
- ✅ 99.5%+ 양산 수율 달성
- ✅ 고정밀 측정 회로 (16-bit DAC, 18-bit ADC, TIA)
- ✅ FPGA 기반 시스템 설계 (Xilinx Zynq, Arty Z7)
- ✅ Signal Integrity & EMI/EMC 설계

---

### 📊 Career Highlights

| 항목 | 수치 |
|------|------|
| 경력 | 13년 |
| 완료 프로젝트 | 19개 |
| 양산 제품 | 8개 |
| 생산 수량 | 200+ units |
| 평균 수율 | 99.5%+ |
| 현장 불량률 | < 0.5% |
| 비용 절감 | 평균 70% (외산 대비) |

---

### 🎓 Education & Certification

- **학력:** [대학교명] [전공] (졸업년도)
- **자격증:**
  - 전자기기기능사 / 전자기기산업기사
  - Altium Designer Certified
  - EMC Design Professional

---

## 🛠️ Step 4: Skills & Tools 페이지

**노션에서 작업:**
1. `/toggle` 입력 → Toggle 리스트 생성
2. 각 카테고리별로 아래 내용 복사:

---

### 🔧 Technical Skills

#### ⚡ Analog Circuit Design
- Precision Op-Amp circuits (offset < 100µV)
- Instrumentation Amplifier (CMRR > 100dB)
- Trans-Impedance Amplifier (1nA ~ 10µA input)
- Active Filter (Butterworth, Chebyshev, Bessel)
- Voltage Reference (< 2ppm/°C drift)

**숙련도:** ⭐⭐⭐⭐⭐ Expert (13 years)

#### 🔋 Power Supply Design
- Buck/Boost Converter (90%+ efficiency)
- LDO Regulator (PSRR > 70dB)
- Multi-rail Sequencing
- Hot-swap Controller
- Battery Management

**숙련도:** ⭐⭐⭐⭐⭐ Expert (13 years)

#### 📡 Sensor Interface
- RTD (4-wire, ±0.05°C accuracy)
- Thermocouple (cold-junction compensation)
- Photodiode TIA (S/N > 60dB)
- Pressure Transducer (±0.1% FSR)

**숙련도:** ⭐⭐⭐⭐⭐ Expert (13 years)

#### 💻 FPGA Design
- Xilinx Zynq-7000 SoC
- Verilog/VHDL
- Vivado/Vitis Development
- High-speed data acquisition

**숙련도:** ⭐⭐⭐⭐ Advanced (5 years)

---

### 🔨 EDA & Simulation Tools

| Tool | Proficiency | Years |
|------|-------------|-------|
| **Altium Designer** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **PADS Layout** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **LTspice** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **OrCAD** | ⭐⭐⭐⭐ Advanced | 10년 |
| **HyperLynx** | ⭐⭐⭐⭐ Advanced | 8년 |
| **Vivado** | ⭐⭐⭐ Intermediate | 5년 |
| **MATLAB** | ⭐⭐⭐ Intermediate | 8년 |

---

## 💼 Step 5: Projects 페이지 (갤러리 뷰)

**노션에서 작업:**
1. `/database` 입력 → "Gallery" 선택
2. 데이터베이스 이름: "Projects"
3. 속성 추가:
   - **Status** (Select): 완료, 진행중
   - **Period** (Date): 시작일~종료일
   - **Tech** (Multi-select): Analog, Power, Sensor, FPGA
   - **Scale** (Text): 프로젝트 규모

### 프로젝트 카드 추가

각 프로젝트마다 새 카드를 만들고 아래 정보를 입력하세요:

---

#### 📌 Card 1: MS (Mass Spectrometer)

**Cover Image:** PCB 사진 또는 제품 사진 업로드

**Properties:**
- Status: 진행중
- Period: 2024.01 ~ 2025.12
- Tech: Analog, Power, Sensor
- Scale: 1.14GB, 345 files

**카드 내용:**

---

# MS (Mass Spectrometer) System

> 반도체 공정 가스 분석을 위한 Mass Spectrometer 시스템 개발

## 📋 Project Overview

**Period:** 2024-2025 (진행 중)  
**Role:** Lead Hardware Engineer  
**Status:** Alpha 단계, PCB Rev 1.2 설계 완료

## 🎯 Objectives

- 반도체 공정 실시간 가스 분석
- Aston 장비 역설계 기반 설계
- 국산화를 통한 비용 절감

## 🔧 Technical Specifications

| 항목 | 사양 |
|------|------|
| **System Architecture** | ASTON Reverse Engineering |
| **Control Board** | STM32 기반 메인 제어 보드 |
| **Sensor Interface** | Mass detector signal conditioning |
| **Communication** | USB/Ethernet interface |
| **Power Design** | Multi-stage (±15V, ±5V, 3.3V) |

## 💡 Key Features

### 주요 설계 내용

1. **CB (Control Board) PCB 설계**
   - STM32H7 메인 컨트롤러
   - 고속 ADC 인터페이스
   - USB/Ethernet 통신

2. **Block Diagram 설계**
   - Rev 01-03 추적 관리
   - 시스템 아키텍처 최적화

3. **QMS Interface**
   - Quadrupole Mass Spectrometer 인터페이스
   - High-voltage switching 회로

## 📊 Project Status

```
Progress: ████████░░ 80%

✅ Block Diagram (Rev 03)
✅ Schematic Design (Rev 1.2)
✅ PCB Layout (Rev 1.2)
⏳ Prototype Assembly
⏳ System Integration Test
```

## 📁 Technical Documents

- Basic 사양서 (Rev 1.0-1.2)
- Block diagram (v01-v03)
- PCB 변경사항 추적
- Back to the basics (QMS) 교육 자료 110MB

## 🖼️ Images

[여기에 PCB 이미지, 블록 다이어그램 이미지 추가]

---

#### 📌 Card 2: L-LPC (Low Pressure Chamber)

**Cover Image:** L-LPC 시스템 사진

**Properties:**
- Status: 완료
- Period: 2020.01 ~ 2023.12
- Tech: Analog, Power, Sensor, Multi-board
- Scale: 17.5GB, 2,597 files

**카드 내용:**

---

# L-LPC (Low Pressure Chamber)

> 반도체 저압 챔버 제어 시스템 - **경력 중 최대 규모 프로젝트**

## 📋 Project Overview

**Period:** 2020-2023 (3년)  
**Role:** Lead Hardware Engineer  
**Team:** 3 HW + 5 FW engineers  
**Status:** ✅ Production (100+ units deployed)

## 🎯 System Architecture

**Application:** 반도체 공정 챔버 압력/온도 제어  
**Scale:** Multi-board system, 10+ PCB 설계  
**Production:** 100+ units deployed

### 주요 보드 구성

```
┌─────────────────────────────────────┐
│  Main Control Board (STM32H7)      │
├─────────────────────────────────────┤
│  Power Distribution Board          │
├─────────────────────────────────────┤
│  Sensor Interface Board (×3)        │
├─────────────────────────────────────┤
│  MFC Controller Board (×5)          │
└─────────────────────────────────────┘
```

## 🔧 Technical Specifications

### Hardware Specs

| Component | Specification |
|-----------|--------------|
| **MCU** | STM32H7 (480MHz, 2MB Flash) |
| **Power** | 24V → Multi-rail (±15V, 12V, 5V, 3.3V) |
| **Pressure Sensors** | MKS Baratron (10채널) |
| **Temperature Sensors** | RTD PT100 (20채널) |
| **Flow Controllers** | MFC (5채널) |
| **Communication** | Ethernet, RS-485, CAN bus |

### Performance

| Parameter | Specification | Measured |
|-----------|--------------|----------|
| **Pressure Accuracy** | ±0.1% FSR | ±0.08% |
| **Temperature Accuracy** | ±0.05°C | ±0.03°C |
| **Flow Accuracy** | ±0.5% FSR | ±0.4% |
| **Response Time** | < 1 sec | 0.7 sec |

## 🎨 PCB Design

**Layer Stackup:** 8-Layer
```
Layer 1: Signal (Top)
Layer 2: Ground Plane
Layer 3: Power Plane (+5V, +3.3V)
Layer 4: Signal
Layer 5: Signal
Layer 6: Power Plane (±15V, +12V)
Layer 7: Ground Plane
Layer 8: Signal (Bottom)
```

**Key Features:**
- Controlled impedance: 50Ω single-ended, 100Ω differential
- Via stitching (0.5mm pitch) for GND plane
- Copper pour for thermal management (200W+ dissipation)

## 📈 Results & Achievements

### Quantitative Results

| Metric | Target | Achieved |
|--------|--------|----------|
| 개발 기간 | 24개월 | 18개월 ✅ |
| 양산 수량 | - | 100+ units |
| 필드 불량률 | < 1% | 0.2% ✅ |
| 비용 절감 | 50% | 65% ✅ |

### Awards & Recognition

- 🏆 사내 우수 프로젝트상 (2023)
- 📜 특허 출원 1건 (Multi-sensor Interface)

## 🖼️ Gallery

[여기에 이미지 추가]
- PCB 3D View
- 조립 완료 사진
- 테스트 결과 그래프
- 필드 설치 사진

---

#### 📌 Card 3-11: 나머지 프로젝트들

동일한 형식으로 다음 프로젝트 카드들을 생성하세요:

3. **Psi-1000** (Pressure Controller)
4. **Nu-2000** (Optical Analysis System)
5. **Sigma-1000** (LPC Simulator)
6. **L-Titrator** (pH Measurement)
7. **FPGA Zynq** (Zynq-7000 SoC)
8. **Lux** (Optical Sensor)
9. **LE** (Laser Equipment)
10. **BLDC Motor** (Motor Controller)
11. **ATIK JIG** (Test Jig)

---

## 📊 Step 6: Achievements 페이지

**노션에서 작업:**
1. `/column` 입력 → 2열 레이아웃 생성
2. 왼쪽 열: 정량적 성과
3. 오른쪽 열: 기술 문서

---

### 📈 Quantitative Achievements

#### 프로젝트 실적

| Metric | Value |
|--------|-------|
| 프로젝트 완료 | **19개** (13년) |
| 양산 제품 | **8개** |
| 양산 수량 | **200+ units** |
| 평균 수율 | **99.5%+** |
| 현장 불량률 | **< 0.5%** |
| 비용 절감 | 평균 **70%** (외산 대비) |
| 개발 기간 단축 | 평균 **30%** |

#### 기술 문서 작성

| 문서 유형 | 수량 |
|----------|------|
| 기술 문서 | 460+ 건 |
| Schematic Review | 50+ 프레젠테이션 |
| BOM 관리 | 100+ Rev |
| 설계 변경 이력 | 200+ ECO |
| 교육 자료 | 20+ 건 |

---

### 🏆 Awards & Patents

#### 특허 & 논문

1. **특허 출원:** "Multi-channel Sensor Interface Circuit" (2023)
2. **공동 논문:** "Precision Pressure Control Algorithm" w/ 동아대 (2022)

#### 수상 이력

- 🥇 우수 개발 프로젝트상 (2023) - L-LPC 프로젝트
- 🥈 품질 우수상 (2021) - Sigma-1000 (수율 99.5%)
- 🥉 기술 혁신상 (2020) - Nu-2000 (비용 절감 80%)

---

## 📞 Step 7: Contact 페이지

**노션에서 작업:**
1. `/callout` 입력
2. 배경색: 파란색
3. 아이콘: 📧

---

### 📧 Get in Touch

**최기용 (Kiyong Choi)**  
Senior Hardware Design Engineer

---

**Email:** your.email@example.com  
**Phone:** 010-XXXX-XXXX  
**Location:** 대한민국

---

**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com)  
**GitHub:** [github.com/yourname](https://github.com)  
**Portfolio (Word):** [다운로드 링크]

---

**Response Time:** 24시간 이내 회신  
**Available for:** 정규직, 프로젝트 자문

---

### 💼 Recruitment Inquiry

```
채용 담당자님께,

포트폴리오를 검토해 주셔서 감사합니다.

13년간 반도체/분석 장비 하드웨어 설계 경험을 바탕으로,
귀사의 제품 개발에 기여하고 싶습니다.

주요 강점:
✅ 고정밀 아날로그 회로 설계
✅ FPGA 기반 시스템 설계
✅ EMI/EMC 문제 해결
✅ 양산 최적화 (99.5% 수율)

연락 주시면 자세한 이야기 나눌 수 있습니다.

감사합니다.
최기용 드림
```

---

## 🎨 Step 8: 디자인 팁

### 1. 컬러 테마 통일

**추천 색상:**
- 🟦 파란색: 프로페셔널, 신뢰
- 🟩 초록색: 완료 항목
- 🟨 노란색: 진행 중
- 🟥 빨간색: 중요 항목

### 2. 아이콘 활용

**섹션별 추천 아이콘:**
- 프로필: 👨‍💼 💼 🎓
- 프로젝트: 🔧 ⚡ 🔬 🖥️
- 기술: 💻 🛠️ ⚙️
- 성과: 📊 📈 🏆
- 연락처: 📞 📧 💬

### 3. 이미지 최적화

**권장 크기:**
- 커버 이미지: 1500×600px
- 프로젝트 썸네일: 800×600px
- 회로도 이미지: 1200×900px

### 4. 모바일 최적화

- 텍스트는 간결하게
- 표는 3열 이내
- 이미지는 적절한 크기로

---

## 📤 Step 9: 공유 설정

### 퍼블릭 공유

1. 페이지 우측 상단 "Share" 클릭
2. "Share to web" 토글 ON
3. "Allow duplicate as template" 선택 (선택사항)
4. 링크 복사

### 커스텀 도메인 (Pro 플랜)

- `portfolio.yourname.com` 같은 커스텀 도메인 연결 가능

### 비밀번호 보호

- 민감한 정보가 있다면 비밀번호 설정

---

## ✅ 체크리스트

포트폴리오 공개 전 확인사항:

### 콘텐츠
- [ ] 프로필 사진 추가
- [ ] 모든 프로젝트 카드 작성 (최소 8개)
- [ ] 각 프로젝트에 이미지 2개 이상
- [ ] 기술 스택 완성
- [ ] 연락처 정보 정확성 확인

### 디자인
- [ ] 커버 이미지 설정
- [ ] 아이콘 통일
- [ ] 컬러 테마 일관성
- [ ] 모바일에서 확인

### 기술 정보
- [ ] 회사 기밀 정보 제거
- [ ] 숫자/성과 검증
- [ ] 오타 확인
- [ ] 링크 작동 확인

### 공유
- [ ] 퍼블릭 공유 설정
- [ ] 링크 복사
- [ ] 이력서에 노션 링크 추가
- [ ] LinkedIn에 링크 게시

---

## 🔗 참고 링크

**노션 템플릿 갤러리:**
- https://notion.so/templates (포트폴리오 템플릿 참고)

**우수 노션 포트폴리오 예시:**
- Engineer Portfolio Template
- Product Designer Portfolio
- Data Analyst Portfolio

**노션 튜토리얼:**
- YouTube: "노션 포트폴리오 만들기"
- Notion Help Center

---

## 💡 Pro Tips

### 1. SEO 최적화
- 페이지 제목에 직무 키워드 포함
- 설명(Description)에 핵심 역량 명시

### 2. 인터랙티브 요소
- Toggle로 상세 내용 숨기기
- 탭(Tab)으로 정보 정리
- Progress bar로 진행도 표시

### 3. 정기 업데이트
- 새 프로젝트 추가
- 기술 스택 업데이트
- 성과 수치 갱신

### 4. 분석 도구
- Notion Analytics로 조회수 확인
- Google Analytics 연동 (Pro 플랜)

---

**작성일:** 2026-01-13  
**버전:** 1.0  
**예상 작업 시간:** 4-6시간
