# Kiyong Choi

## Senior Hardware Design Engineer

**13년 이상의 Analog/Digital 회로 설계 전문 경력**

---

## Professional Summary

반도체 공정 장비 및 산업용 분석 기기를 위한 고정밀 아날로그 회로 설계, 전원 시스템 아키텍처, PCB 레이아웃 분야에서 13년 이상의 전문 경력을 보유한 시니어 하드웨어 설계 엔지니어입니다. 엄격한 신호 무결성, 저노이즈 요구사항, EMI/EMC 규정을 만족하는 복잡한 Mixed-Signal 시스템 설계에 검증된 전문성을 보유하고 있습니다.

**핵심 전문 분야:**
- 고정밀 Analog Circuit Design (Op-Amp, Instrumentation Amplifier, ADC/DAC)
- Power Supply Architecture (Multi-rail SMPS, LDO, Sequencing, Hot-swap)
- Signal Integrity & EMI/EMC Design
- PCB Layout (4-8 Layer, High-speed Digital, RF)
- Sensor Interface Design (RTD, Thermocouple, Photodiode, Pressure Transducer)
- Isolation & Protection Circuits
- Design for Manufacturing (DFM) & Design for Test (DFT)

---

## Technical Skills

### Circuit Design
- **Analog Design**: Precision Op-Amp 회로, Instrumentation amplifier, Active/Passive filter, Trans-impedance amplifier (TIA), Current sensing, Voltage reference 회로
- **Power Design**: Buck/Boost converter, LDO regulator, Multi-rail sequencing, Power-good monitoring, Soft-start 회로, Over-voltage/current protection
- **Sensor Interface**: RTD (PT100/PT1000) 4-wire 측정, Thermocouple cold-junction compensation, Photodiode TIA (1nA~10µA), Pressure sensor conditioning
- **Communication**: RS-232/RS-485 isolation, I2C/SPI bus design, CAN transceiver, Modbus RTU
- **Protection**: ESD protection, Over-voltage clamp, Reverse polarity, Inrush current limiting

### PCB Design
- **Tools**: Altium Designer (Expert level), OrCAD Capture/Layout
- **설계 역량**: 
  - 4-8 Layer stackup 설계
  - High-speed signal routing (100MHz+)
  - Mixed-signal ground/power plane splitting
  - Controlled impedance (50Ω, 100Ω differential)
  - Via stitching, shielding, guard ring
  - 열 관리 (copper pour, thermal via)
  - DFM 규칙 (track/space, annular ring, solder mask)

### Simulation & Analysis
- **Circuit Simulation**: LTspice, TINA-TI, PSpice
- **Signal Integrity**: HyperLynx SI/PI analysis
- **Thermal Analysis**: 열저항 계산, junction temperature 예측
- **SPICE Modeling**: 커스텀 component model, worst-case analysis

### Test & Measurement
- **장비**: Oscilloscope (Tektronix MSO64, Keysight DSOX3024T), Spectrum Analyzer, Network Analyzer, LCR Meter, Source Measure Unit (SMU)
- **측정 방법**: Bode plot 측정, THD+N 분석, PSRR 측정, Step response 특성화, EMI 사전 적합성 시험

---

## Professional Experience

### ATIK Corp. | Senior Hardware Design Engineer
**2012 - Present (13년 이상)**

#### 주요 프로젝트

### 1. **Sigma-1000 LPC Simulator** (2020-2021)
**역할:** Lead Hardware Designer | **기간:** 14개월 | **양산:** 50대 이상

반도체 CVD/Etch 공정 장비용 고정밀 플라즈마 교정 시뮬레이터

**기술 주요 사항:**
- **16-bit DAC System**: MCP4728 quad DAC와 precision OPA4140 buffer를 사용한 시스템 설계
  - 출력 범위: 0-10V, 해상도: 153µV
  - 선형성: ±0.01% FSR (INL < ±1.6 LSB)
  - 노이즈: < 10µVrms (10Hz-10kHz)
  - 온도 드리프트: < 5ppm/°C
  
- **Multi-channel Analog Output**:
  - 16개 독립 DAC 채널
  - 채널별 current/voltage mode 선택
  - 채널당 전류 모니터링 (0-20mA)
  - 절연: 2.5kV (채널 간)

- **Power Supply Design**:
  - Primary: LM2596 (24V → 5V, 3A)
  - Analog supply: LM317 linear regulator (5V → 3.3V, 500mA)
  - Noise rejection: PSRR > 80dB @ 100Hz
  - Ripple: < 10mVpp (ADC VREF에서 측정)

- **Communication Interface**:
  - RS-232: MAX3232 with ±15kV ESD protection
  - RS-485: ADUM1201 digital isolator (2.5kV isolation)
  - I2C: 10kΩ pull-up resistor (400kHz 최적화)

**회로 설계 성과:**
- 10Ω damping resistor + 100nF snubber 추가로 출력 오실레이션 문제 해결
- ADC 노이즈 성능 50% 개선 (C32: 20pF → 0.1µF bypass capacitor)
- I2C rise time 800ns → 150ns 최적화 (R33-40: 100kΩ → 10kΩ pull-up)
- RS-485 termination resistor 최적화 구현 (오류율: 10% → 0.01%)

**양산 결과:**
- Calibration 시간 단축: 83% (30분 → 5분)
- 생산 수율: 99.5% (50대, 현장 불량 0건)
- 비용 절감: 이전 외부 calibrator 대비 80%

**설계 문서:**
- 완전한 schematic review 프레젠테이션 (Rev 3.6)
- PCB layout 가이드라인 (4-layer stackup)
- BOM 최적화 (5개 revision 추적)
- 제조 테스트 절차서

---

### 2. **Nu-2000 Optical Analysis System** (2021-2022)
**역할:** Hardware Design Lead | **기간:** 16개월 | **외주 관리:** Wiki Optics

반도체 공정 가스 분석을 위한 고급 광학 흡수 분광(OAS) 시스템

**기술 주요 사항:**

- **Multi-wavelength LED Driver**:
  - UV LED driver: 254nm, 280nm (10-500mA, PWM 제어)
  - IR LED driver: 1450nm, 1650nm (10-500mA, PWM 제어)
  - 전류 조절: ±2% 정확도 (0-60°C 범위)
  - 열 보상 알고리즘 구현
  
- **Photodiode Trans-Impedance Amplifier (TIA)**:
  - 입력 전류 범위: 1nA ~ 10µA
  - 게인 선택: 1MΩ, 10MΩ, 100MΩ (소프트웨어 전환)
  - 대역폭: DC ~ 1kHz
  - S/N ratio: > 60dB @ 1nA input
  - 개선 설계 (Rev 0.2): 가변 PD bias (-3V ~ -10V) → S/N 20% 향상

- **Precision Temperature Measurement**:
  - RTD sensor: PT100 (α=0.00385), 4-wire 측정
  - ADC: MCP3427 (18-bit, I2C)
  - 해상도: 0.01°C
  - 정확도: ±0.05°C (0-100°C 범위)
  - 여기 전류: 1mA (precision current source)

- **High-Resolution ADC**:
  - AD7682 16-bit SAR ADC
  - Throughput: 250kSPS
  - SNR: 91.5dB typical
  - Reference: ADR4540 (4.096V, ±0.02% initial accuracy, 2ppm/°C drift)

**회로 최적화:**
- LED driver 회로 재설계 (5회 반복 문서화)
- 듀얼 채널 지원을 위한 PD 회로 수정
- RTD sensor interface 회로 설계 검토
- UV/IR PD 회로 개선

**외주 협력:**
- Wiki Optics 광학 모듈 개발 관리
- 기술 사양 정의
- Alpha/Beta 버전 검증
- 최종 인수 시험 (광 출력 안정도: ±1%, 목표: ±2%)

**설계 문서:**
- System block diagram (종합)
- 15개 기술 문서 작성 (01-10 시리즈 번호 체계)
- 8개 회로 검토 프레젠테이션
- Hardware 교육 자료

---

### 3. **Psi-1000 Pressure Controller** (2019-2022)
**역할:** Hardware Design Consultant | **대학 협력:** 동아대학교

반도체 공정 챔버용 정밀 진공 압력 제어 시스템

**기술 주요 사항:**

- **Pressure Sensor Interface**:
  - Sensor: MKS Baratron capacitance manometer
  - 측정 범위: 1 mTorr ~ 1000 Torr
  - Interface: 0-10V analog output
  - ADC: 16-bit (ADS1115), I2C
  - 정확도: ±0.1% of reading

- **Mass Flow Controller (MFC) Interface**:
  - McMillan U803 MFC
  - 제어: LTC2630 12-bit DAC (I2C)
  - 출력: 0-20mA current loop
  - 해상도: 4.88µA per LSB

- **Heater Control**:
  - 전력: 500W max
  - 제어: SSR (Solid State Relay)
  - 전류 센싱: ACS712 Hall-effect sensor
  - 보호: Over-current, over-temperature

- **Communication**:
  - Modbus RTU/ASCII (RS-485)
  - 프로토콜 사양서: 0.27 ~ 0.30 (문서화)
  - Baud rate: 115200 bps
  - Error checking: CRC-16

**하드웨어 진화:**
- Rev 0.1: 초기 프로토타입
- Rev 0.2: 하드웨어 수정 (2021년 11월)
- Rev 0.25-0.27: 사양 업데이트 (2022년 1-3월)

**회로 문서:**
- System block diagram (Ver 1.0)
- Wiring diagram (종합)
- PCB 조립 및 테스트 절차
- Calibration 절차

**대학 협력:**
- 동아대학교 연구 프로젝트
- Control logic 설계 검토 (Rev 01-05 추적)
- Software 설계 문서화 (Rev 01-03)
- 테스트 결과 분석 프레젠테이션

---

### 4. **L-LPC (Low Pressure Chamber)** (17.5GB 프로젝트 데이터)
**역할:** Principal Hardware Designer

저압 챔버 제어 시스템을 위한 대규모 프로젝트

**프로젝트 규모:**
- 2,597개 파일
- 17.5GB 문서
- 다년간 개발

*(상세 분석은 요청 시 제공)*

---

### 5. **L-Titrator (Automatic Titrator)** (2018-2020)
**역할:** Circuit Design Lead

정밀 화학 분석 기기

**기술 주요 사항:**
- 고정밀 pH 전극 증폭기
- 스테퍼 모터 드라이브 회로 (burette 제어)
- 온도 보상
- 자동 calibration 루틴

**프로젝트 규모:**
- 134개 파일
- 308MB 문서

---

## 추가 프로젝트

### Jig Board & Test Equipment
- Sigma-1000 Jig Board (5개 설계 수정 문서화)
- 생산 테스트 지그
- Calibration 장비

### Safety Systems
- 안전 인터락 회로
- Emergency stop 시스템
- Over-temperature protection

### BLDC Motor Controller
- 3상 인버터 설계
- Hall sensor interface
- 전류 센싱 및 보호

---

## 설계 방법론

### 1. **체계적 접근법**
- 요구사항 분석 및 사양 정의
- Block diagram 및 아키텍처 설계
- 회로 시뮬레이션 및 worst-case 분석
- 프로토타입 bring-up 및 특성 분석
- 설계 반복 및 최적화
- 양산 릴리즈 및 DFM 검토

### 2. **품질 보증**
- 동료 설계 검토
- FMEA (Failure Mode & Effects Analysis)
- 설계 검증 시험
- 제조 테스트 커버리지 분석
- 현장 불량 추적 및 근본 원인 분석

### 3. **문서화 표준**
- 종합적인 schematic review 프레젠테이션
- 상세한 설계 수정 이력 추적
- 버전 관리된 BOM 관리
- 테스트 절차 및 합격 기준
- Lessons learned 문서화

---

## 주요 성과

### 기술적 우수성
- **460+ 기술 문서** 경력 기간 동안 작성
- **19+ 주요 프로젝트** 완료
- **99.5%+ 생산 수율** 모든 프로젝트에서 달성
- **현장 치명 불량 Zero** 양산 제품

### 비용 최적화
- 설계 최적화를 통한 평균 **80% 비용 절감**
- 자동화를 통한 **83% 시간 절감** (Sigma-1000 사례)

### 지식 공유
- 광범위한 하드웨어 교육 자료 작성
- 주니어 엔지니어 멘토링
- 설계 검토 프로세스 확립

---

## 교육 및 지속적 학습

다음 분야의 지속적인 전문성 개발:
- 고급 analog 회로 설계 기법
- Signal integrity & high-speed 설계
- EMI/EMC 적합성 전략
- Power supply 설계 최적화

---

## Tools & Software

### EDA Tools
- Altium Designer (Expert)
- OrCAD Capture & PSpice
- LTspice (Circuit simulation)

### Analysis Tools
- MATLAB (회로 분석, 데이터 처리)
- Excel (고급 수식, VBA macro for 설계 계산)
- Python (자동화 스크립트)

### Documentation
- Microsoft Office Suite (PowerPoint for 설계 검토, Excel for BOM)
- Git (설계 파일 버전 관리)
- Confluence/Wiki (지식 베이스 관리)

---

## 전문적 특성

- **세심함**: 종합적인 설계 규칙 검사를 통한 꼼꼼한 회로 설계
- **문제 해결**: 체계적인 디버깅 및 근본 원인 분석 방법론
- **커뮤니케이션**: 명확한 기술 문서 및 효과적인 설계 검토 프레젠테이션
- **협업**: 외주 업체 및 대학 파트너십 관리 경험
- **지속적 개선**: 적극적인 학습 및 모범 사례 채택

---

## Contact Information

**Choi, Kiyong (최기용)**  
Senior Hardware Design Engineer

- **Email**: [연락처 정보]
- **Location**: Republic of Korea
- **LinkedIn**: [프로필 링크]

---

## References & Portfolio

상세한 설계 문서, schematic review, 프로젝트 프레젠테이션은 요청 시 제공 가능합니다.

---

*본 포트폴리오는 고정밀 아날로그 회로, 다학제 협업, 제조 우수성에 중점을 둔 13년 이상의 전문 하드웨어 설계 경험을 나타냅니다.*
