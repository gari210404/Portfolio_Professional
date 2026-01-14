# 최기용 (Kiyong Choi)

**Senior Hardware Design Engineer**

13 Years Experience | 19+ Products | 99.5% Yield

---

> 💡 **About Me**
> 
> 13년 경력의 시니어 하드웨어 설계 엔지니어입니다. 반도체 공정 장비 및 산업용 분석 기기를 위한 **고정밀 아날로그/디지털 회로 설계, 전원 시스템, PCB 레이아웃**을 전문으로 합니다.

---

## 🎯 Core Strengths

- ✅ **19+ 제품 개발 완료** (양산 8개, 200+ units)
- ✅ **99.5%+ 양산 수율** 달성 (필드 불량률 < 0.5%)
- ✅ **고정밀 측정 회로** (16-bit DAC, 18-bit ADC, TIA)
- ✅ **FPGA 시스템 설계** (Xilinx Zynq, Arty Z7, 5.9GB 프로젝트)
- ✅ **Signal Integrity & EMI/EMC** 설계 및 문제 해결
- ✅ **비용 절감 70%** (외산 제품 대비 국산화)

---

## 📊 Career Highlights

| 항목 | 수치 |
| --- | --- |
| **경력** | 13년 |
| **완료 프로젝트** | 19개 |
| **양산 제품** | 8개 |
| **생산 수량** | 200+ units |
| **평균 수율** | 99.5%+ |
| **현장 불량률** | < 0.5% |
| **비용 절감** | 평균 70% (외산 대비) |
| **개발 기간 단축** | 평균 30% |

---

## 🛠️ Technical Skills

### ⚡ Circuit Design Expertise

**Analog Design** ⭐⭐⭐⭐⭐
- Precision Op-Amp circuits (offset < 100µV)
- Instrumentation Amplifier (CMRR > 100dB)
- Trans-Impedance Amplifier (1nA ~ 10µA)
- Active Filter (Butterworth, Chebyshev)
- Voltage Reference (< 2ppm/°C drift)

**Power Supply Design** ⭐⭐⭐⭐⭐
- Buck/Boost Converter (90%+ efficiency)
- LDO Regulator (PSRR > 70dB)
- Multi-rail Sequencing & Hot-swap
- Battery Management System

**Sensor Interface** ⭐⭐⭐⭐⭐
- RTD (4-wire, ±0.05°C accuracy)
- Thermocouple (cold-junction compensation)
- Photodiode TIA (S/N > 60dB)
- Pressure Transducer (±0.1% FSR)

**FPGA Design** ⭐⭐⭐⭐
- Xilinx Zynq-7000 SoC
- Verilog/VHDL
- Vivado/Vitis Development
- High-speed data acquisition (100MSPS)

---

### 🔨 EDA & Tools

| Tool | Proficiency | Years |
| --- | --- | --- |
| **Altium Designer** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **PADS Layout** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **LTspice** | ⭐⭐⭐⭐⭐ Expert | 13년 |
| **OrCAD** | ⭐⭐⭐⭐ Advanced | 10년 |
| **HyperLynx** | ⭐⭐⭐⭐ Advanced | 8년 |
| **Vivado/Vitis** | ⭐⭐⭐ Intermediate | 5년 |
| **MATLAB** | ⭐⭐⭐ Intermediate | 8년 |

---

# 💼 Projects

---

## 1. MS (Mass Spectrometer) System ⭐ NEW

### 📋 Overview

**Period:** 2024-2025 (진행 중)
**Role:** Lead Hardware Engineer
**Status:** 🟡 Alpha 단계, PCB Rev 1.2 설계 완료

반도체 공정 가스 분석을 위한 Mass Spectrometer 시스템 개발

### 🎯 Objectives

- 반도체 공정 실시간 가스 분석
- Aston 장비 역설계 기반 설계
- 국산화를 통한 비용 절감 (목표 60%)

### 🔧 Technical Specs

| Component | Specification |
| --- | --- |
| **Control Board** | STM32H7 기반 메인 제어 보드 |
| **Sensor Interface** | Mass detector signal conditioning |
| **Communication** | USB 3.0 / Gigabit Ethernet |
| **Power Supply** | Multi-stage (±15V, ±5V, 3.3V, 500W) |
| **QMS Interface** | Quadrupole Mass Spectrometer |

### 💡 Key Features

**1. CB (Control Board) PCB 설계**
- STM32H7 메인 컨트롤러 (480MHz)
- 고속 ADC 인터페이스 (18-bit, 1MSPS)
- USB/Ethernet 듀얼 통신

**2. Block Diagram 최적화**
- Rev 01 → Rev 03 개선
- 시스템 아키텍처 최적화
- 모듈화 설계로 유지보수성 향상

**3. High-Voltage Switching**
- Quadrupole 전극 구동회로
- HV Amplifier (±200V)
- Isolation 설계 (2.5kV)

### 📊 Progress

```
Progress: ████████░░ 80%

✅ Requirements Analysis
✅ Block Diagram (Rev 03)
✅ Schematic Design (Rev 1.2)
✅ PCB Layout (Rev 1.2)
🟡 Prototype Assembly
⏳ System Integration Test
⏳ Field Trial
```

### 📁 Deliverables

- Basic 사양서 (Rev 1.0-1.2)
- Block diagram (v01-v03)
- Schematic (MASS_DRB_v0_1_20250909A.sch)
- PCB Layout (4개 버전)
- QMS 교육 자료 (110MB)

### 📂 Files

```
Project_Files/01_MS_Mass_Spectrometer/
├── Schematics/
│   └── MASS_DRB_v0_1_20250909A.sch
├── PCB/
│   ├── MASS_DRB_v0_1_250904-017.pcb
│   ├── MASS_DRB_v0_1_250909-018.pcb
│   ├── MASS_DRB_v0_1_250909-019.pcb
│   └── MASS_DRB_v0_1_250910-021.pcb
└── PDF/
    └── (추출 예정)
```

---

## 2. L-LPC (Low Pressure Chamber) ⭐ 최대 규모

### 📋 Overview

**Period:** 2020-2023 (3년)
**Role:** Lead Hardware Engineer
**Team:** 3 HW + 5 FW engineers
**Status:** ✅ Production (100+ units deployed)

반도체 저압 챔버 제어 시스템 - **경력 중 최대 규모 프로젝트 (17.5GB)**

### 🎯 System Architecture

**Application:** 반도체 공정 챔버 압력/온도/가스 제어
**Scale:** Multi-board system, 10+ PCB 설계
**Production:** 100+ units, 5개 반도체 fab 설치

### 🔧 Hardware Specs

| Component | Specification | Quantity |
| --- | --- | --- |
| **MCU** | STM32H7 (480MHz, 2MB Flash) | 1 |
| **Power Input** | 24VDC ±10%, 500W max | 1 |
| **Pressure Sensors** | MKS Baratron (1mTorr ~ 1000 Torr) | 10채널 |
| **Temperature Sensors** | RTD PT100 (0-200°C) | 20채널 |
| **Flow Controllers** | McMillan MFC (0-100 SCCM) | 5채널 |
| **Communication** | Ethernet, RS-485, CAN bus | - |

### 🎨 PCB Design Highlights

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
- Via stitching (0.5mm pitch) for EMI reduction
- Copper pour for thermal management (200W+ dissipation)
- Star-point grounding for analog section

### 📈 Performance Results

| Parameter | Target | Measured | Status |
| --- | --- | --- | --- |
| **Pressure Accuracy** | ±0.1% FSR | ±0.08% | ✅ |
| **Temperature Accuracy** | ±0.05°C | ±0.03°C | ✅ |
| **Flow Accuracy** | ±0.5% FSR | ±0.4% | ✅ |
| **Response Time** | < 1 sec | 0.7 sec | ✅ |
| **MTBF** | > 10,000 hrs | 12,500 hrs | ✅ |

### 🏆 Achievements

| Metric | Target | Achieved |
| --- | --- | --- |
| **개발 기간** | 24개월 | **18개월** ✅ |
| **양산 수량** | - | **100+ units** |
| **필드 불량률** | < 1% | **0.2%** ✅ |
| **비용 절감** | 50% | **65%** ✅ |
| **수율** | 95% | **99.2%** ✅ |

**Awards:**
- 🏆 사내 우수 프로젝트상 (2023)
- 📜 특허 출원 1건 (Multi-sensor Interface)

### 📂 Files

```
Project_Files/02_L-LPC/
├── PCB/
│   └── LPC_PD_POWER(rev_0.1)_221026.pcb
└── PDF/ (9개 파일)
    ├── LPC_Board_SamplePCB.pdf
    ├── LPC_PWR_Board.pdf
    ├── LPC_PD_Board.pdf
    └── 기타 6개 문서
```

---

## 3. Psi-1000 (Pressure Controller)

### 📋 Overview

**Period:** 2019-2022 (3년)
**Role:** Lead Hardware Engineer
**Collaboration:** 동아대학교 산학협력
**Status:** ✅ Production (20+ units)

정밀 진공 압력 제어 시스템

### 🎯 Objectives

- 고정밀 압력 제어 (±0.1% FSR)
- PID 알고리즘 최적화
- Modbus 통신 구현

### 🔧 Circuit Highlights

**Pressure Sensor Interface:**
```
MKS Baratron (0-10V) 
  → Op-Amp Buffer (OPA140) 
  → 2nd-order LPF (fc=10Hz) 
  → 16-bit ADC (ADS1115)

Resolution: 153µV/LSB
Noise: < 50µVrms
SNR: 106 dB
```

**MFC Control Loop:**
```
MCU (I2C) 
  → 12-bit DAC (LTC2630) 
  → V/I Converter (0-20mA) 
  → McMillan MFC

Resolution: 4.88µA/LSB
Control range: 0-100 SCCM
Update rate: 100Hz
```

### 📈 PID Control Performance

| Metric | Before | After | Improvement |
| --- | --- | --- | --- |
| **Settling Time** | 5.0 sec | 2.5 sec | **50%** ↓ |
| **Overshoot** | 15% | 4.2% | **72%** ↓ |
| **Steady-state Error** | 0.5% | 0.08% | **84%** ↓ |

### 🤝 Collaboration

**동아대학교 산학협력 (2020-2022):**
- PID 알고리즘 공동 개발
- Control logic Rev 01 → Rev 05 개선
- 논문 1편 공동 저자
- 특허 1건 공동 출원

### 📁 Deliverables

- Modbus Protocol Spec (Ver 0.27-0.30)
- PID Tuning Guide (Rev 2.1)
- User Manual (Korean/English)

---

## 4. Nu-2000 (OAS-DSP) Optical Analysis

### 📋 Overview

**Period:** 2021-2022 (1.5년)
**Role:** Lead Hardware Engineer
**Vendor:** Wiki Optics (광학 모듈)
**Status:** ✅ Production (30+ units)

광학 흡수 분광 시스템 메인보드 설계

### 🔧 Key Circuits

**1. LED Driver (4 Channels)**
```
MCU PWM 
  → MOSFET Driver (IRF530) 
  → UV/IR LED (10-500mA)
  → Current Sense (0.1Ω + INA139)

Specs:
- Current range: 10-500mA (±2%)
- PWM frequency: 10kHz
- Thermal compensation: NTC sensor
```

**2. Photodiode TIA**
```
Photodiode 
  → Variable Gain TIA (1M/10M/100MΩ) 
  → OPA140 
  → LPF (1kHz)
  → 16-bit ADC (AD7682)

Specs:
- Input current: 1nA ~ 10µA
- S/N ratio: > 60dB @ 1nA
- Rev 0.2: Variable PD bias (-3V ~ -10V)
```

**3. RTD Temperature**
```
PT100 (4-wire)
  → Precision Current Source (1mA)
  → 18-bit ADC (MCP3427)

Resolution: 0.01°C
Accuracy: ±0.05°C
```

### 📊 Vendor Management

**Wiki Optics 협업:**
- 광학 모듈 기술 사양 정의
- Alpha/Beta 버전 검증
- 최종 광 출력 안정도: **±1%** (목표 ±2% 초과 달성)

### 📂 Files

```
Project_Files/04_Nu-2000/
├── Schematics/
│   └── Total_Board_ATIK_V1.2.sch
├── PCB/
│   └── Total_Board_ATIK_V1.2.pcb
└── PDF/ (8개 파일)
    ├── Total_Board_ATIK_V1.2.pdf
    ├── H_Bridge_Rev0.2_3D.pdf
    ├── PD_AMP_V2.0.pdf
    └── 기타 5개 문서
```

---

## 5. Sigma-1000 (LPC Simulator)

### 📋 Overview

**Period:** 2020-2021 (1년)
**Status:** ✅ Production (50+ units)

플라즈마 교정 시뮬레이터 - **Calibration 시간 83% 단축**

### 🔧 16-bit DAC System

```
STM32F407 (I2C)
  → MCP4728 (12-bit DAC)
  → OPA4140 Buffer
  → Output (0-10V, 16 channels)

Specs:
- Resolution: 153µV
- Linearity: ±0.01% FSR (INL < ±1.6 LSB)
- Noise: < 10µVrms (10Hz-10kHz)
- Temp drift: < 5ppm/°C
```

### 🎨 Circuit Optimization

**Issue 1: 출력 오실레이션**
- Root Cause: Capacitive load instability
- Solution: 10Ω damping resistor + 100nF snubber
- Result: ✅ Stable output

**Issue 2: ADC 노이즈 과다 (100µVrms)**
- Root Cause: VREF bypass capacitor 부족
- Solution: C32 (20pF → 0.1µF)
- Result: ✅ 50% 노이즈 감소 (48µVrms)

**Issue 3: RS-485 통신 오류 (10%)**
- Root Cause: Termination resistor 값 부적합
- Solution: R33-40 (100kΩ → 10kΩ)
- Result: ✅ 오류율 0.01%

### 📈 Production Results

| Metric | Value |
| --- | --- |
| **생산 수율** | **99.5%** (50 units) |
| **Calibration 시간** | 30분 → **5분** (83% 단축) |
| **비용 절감** | **80%** vs. 외부 calibrator |
| **필드 불량** | **0건** (24개월 운영) |

---

## 6-11. Additional Projects

### 6. L-Titrator (pH Measurement)
**Period:** 2018-2020 | **Status:** ✅ Production

**Key Features:**
- pH 전극 증폭기 (High impedance > 10TΩ)
- 스테퍼 모터 제어 (A4988 driver)
- Auto-titration 알고리즘

**Files:** 1 SCH, 2 PCB

---

### 7. FPGA Zynq (Xilinx Zynq-7000)
**Period:** 2024 | **Status:** 🟡 개발 중 | **Scale:** 5.9GB

**Key Features:**
- Dual-core ARM Cortex-A9 @ 866MHz
- FPGA Fabric: 85K logic cells
- Custom IP core (Verilog)
- High-speed data acquisition (100MSPS)

**Projects:**
- Arty Z7 platform
- H_Sensor_TEST (92MB)
- FreeRTOS integration

---

### 8. Lux (Optical Sensor)
**Period:** 2023-2024 | **Status:** ✅ Pilot production

**Key Features:**
- PD Board (Photodiode interface)
- LD Board (Laser diode driver)
- Precision optical measurement

**Files:** 3 SCH, 3 PCB

---

### 9-11. Other Projects

| Project | Period | Scale | Key Features |
| --- | --- | --- | --- |
| **LE (Laser Equipment)** | 2024 | 35MB | 센서 수리 및 개선 |
| **BLDC Motor** | 2022 | 20MB | 3상 인버터, Hall sensor |
| **ATIK JIG** | 2022 | 15MB | 범용 테스트 지그 |

---

# 📊 Achievements

## 🏆 Awards & Recognition

### 수상 이력

- 🥇 **우수 개발 프로젝트상** (2023) - L-LPC 프로젝트
- 🥈 **품질 우수상** (2021) - Sigma-1000 (수율 99.5%)
- 🥉 **기술 혁신상** (2020) - Nu-2000 (비용 절감 80%)

### 특허 & 논문

1. **특허 출원:** "Multi-channel Sensor Interface Circuit" (2023)
2. **공동 논문:** "Precision Pressure Control Algorithm" w/ 동아대 (2022)

---

## 📈 Quantitative Impact

### Career Statistics

```
📊 프로젝트 실적
┌─────────────────────────────┐
│ 완료 프로젝트:     19개      │
│ 양산 제품:         8개       │
│ 생산 수량:         200+ units│
│ 평균 수율:         99.5%+    │
│ 현장 불량률:       < 0.5%    │
│ 비용 절감:         평균 70%  │
│ 개발 기간 단축:    평균 30%  │
└─────────────────────────────┘

📝 기술 문서
┌─────────────────────────────┐
│ 기술 문서:         460+ 건   │
│ Schematic Review:  50+ PPT   │
│ BOM 관리:          100+ Rev  │
│ 설계 변경 이력:    200+ ECO  │
│ 교육 자료:         20+ 건    │
└─────────────────────────────┘
```

---

# 📞 Contact

> 📧 **Get in Touch**
> 
> 포트폴리오를 검토해 주셔서 감사합니다.
> 
> 13년간 반도체/분석 장비 하드웨어 설계 경험을 바탕으로,
> 귀사의 제품 개발에 기여하고 싶습니다.

---

## 📮 Contact Information

**최기용 (Kiyong Choi)**
Senior Hardware Design Engineer

---

**Email:** your.email@example.com
**Phone:** 010-XXXX-XXXX
**Location:** 대한민국

---

**LinkedIn:** [linkedin.com/in/yourprofile](https://linkedin.com)
**GitHub:** [github.com/yourname](https://github.com)

---

**Response Time:** 24시간 이내 회신
**Available for:** 정규직, 프로젝트 자문

---

## 💼 For Recruiters

### 주요 강점

✅ **고정밀 아날로그 회로 설계**
- 16/18-bit ADC/DAC 시스템
- TIA, Instrumentation Amp
- Noise < 10µVrms

✅ **FPGA 기반 시스템 설계**
- Xilinx Zynq-7000 SoC
- 5.9GB 프로젝트 경험
- Verilog/VHDL

✅ **EMI/EMC 문제 해결**
- CISPR 11 Class A 적합
- Signal Integrity 설계
- 실제 인증 경험

✅ **양산 최적화**
- 수율 99.5%+ 달성
- 비용 절감 70% (평균)
- 필드 불량률 < 0.5%

---

### 희망 직무

- **Senior Hardware Engineer**
- **Lead Circuit Designer**
- **Hardware Architect**
- **Technical Consultant**

---

### 희망 연봉

면접 시 협의 (현재 시장가 기준)

---

**연락 주시면 자세한 이야기 나눌 수 있습니다.**

**감사합니다.**
**최기용 드림**

---

*Last Updated: 2026-01-13*
*Portfolio Version: 2.0 (Notion)*
