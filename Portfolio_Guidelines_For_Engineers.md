# 경력직 엔지니어를 위한 포트폴리오 작성 가이드

## 📚 목차
1. [포트폴리오 구조](#포트폴리오-구조)
2. [회로도 첨부 방법](#회로도-첨부-방법)
3. [코드 샘플 작성법](#코드-샘플-작성법)
4. [이미지 및 그래프](#이미지-및-그래프)
5. [실전 예제](#실전-예제)

---

## 포트폴리오 구조

### 경력직 표준 구조 (15-20 pages)

```
┌─────────────────────────────────────┐
│ 1. Executive Summary (1 page)       │
│    - 핵심 역량 3-5개 bullet points  │
│    - 주요 성과 수치                 │
│    - Contact Information            │
├─────────────────────────────────────┤
│ 2. Core Competencies (1 page)       │
│    - Technical Skills Matrix        │
│    - 프로그레스 바 또는 표          │
├─────────────────────────────────────┤
│ 3. Major Projects (10-12 pages)     │
│    - 프로젝트당 2-3 pages           │
│    - Overview → Technical → Results │
│    - 회로도/코드 첨부               │
├─────────────────────────────────────┤
│ 4. Additional Projects (2 pages)    │
│    - 간략 요약 (프로젝트당 4-6줄)  │
├─────────────────────────────────────┤
│ 5. Skills & Tools (1 page)          │
│    - EDA Tools, 시뮬레이션 툴       │
│    - 프로그래밍 언어                │
├─────────────────────────────────────┤
│ 6. Achievements & Metrics (1 page)  │
│    - 정량적 성과                    │
│    - 특허, 논문, 수상               │
└─────────────────────────────────────┘

┌─────────────────────────────────────┐
│ Appendix A: Schematics (5-10 pages) │
│ Appendix B: Code Samples            │
│ Appendix C: Test Results            │
│ Appendix D: Certifications          │
└─────────────────────────────────────┘
```

---

## 회로도 첨부 방법

### 방법 1: Word 문서 내 이미지 삽입 (권장)

**장점:**
- 한 문서로 관리 용이
- 설명과 회로도가 인접
- 인쇄 시 일관성 유지

**작성법:**
```markdown
### 3.1 Precision DAC System

**Overview:**
Sigma-1000 프로젝트의 16채널 DAC 시스템입니다.

**Circuit Architecture:**

[Figure 1: DAC System Block Diagram]
┌─────────────────────────────────────────┐
│  여기에 회로도 이미지 삽입               │
│  (Altium에서 Export한 PNG/PDF)          │
│  권장 크기: 1600x1200 px                │
└─────────────────────────────────────────┘

**Key Features:**
- 12-bit resolution (MCP4728)
- I2C interface
- Low-noise buffer (OPA4140)

**Design Highlights:**
[빨간색 박스로 주요 부분 강조]
```

### 방법 2: PDF Appendix 첨부

**장점:**
- 고해상도 회로도 유지
- 여러 페이지 schematic 가능
- 원본 파일 관리 용이

**작성법:**

1. **Altium Designer에서 PDF 추출:**
```
File → Smart PDF
  ✓ Include: Schematics only
  ✓ Color: Color
  ✓ Resolution: 600 DPI
  ✓ Size: A4
  
Output:
  Sigma_1000_Power_Supply.pdf (1-2 pages)
  Nu_2000_TIA_Circuit.pdf (1 page)
  Psi_1000_Sensor_Interface.pdf (2 pages)
```

2. **포트폴리오에서 참조:**
```markdown
### 3.2 Power Supply Design

전원 회로는 24V 입력을 5V (Digital)과 3.3V (Analog)로 변환합니다.

**상세 회로도:** [Appendix A, Page 3]

**주요 사양:**
- Input: 24VDC ±10%
- Output: 5V @ 3A, 3.3V @ 500mA
- Efficiency: > 85%
```

### 방법 3: 핵심 회로만 발췌 (Best Practice)

**선택 기준:**
- 프로젝트당 1-2개 핵심 회로만
- A4 크기에 맞게 조정
- 텍스트 가독성 확보 (최소 8pt)

**발췌 예시:**

```
[선택하는 회로]
✓ 특별한 기술이 적용된 회로 (예: 고정밀 TIA)
✓ 문제 해결 사례 (예: 오실레이션 제거)
✓ 성능 향상 회로 (예: 노이즈 50% 개선)
✓ 독창적인 설계 (예: 특허 출원)

[선택하지 않는 회로]
✗ 범용 IC의 표준 회로 (예: LM7805)
✗ 간단한 LED 회로
✗ 커넥터만 있는 페이지
```

### 회로도 주석 작성법

**Before (주석 없음):**
```
[단순 회로도 이미지만]
```

**After (주석 추가):**
```
[Figure 2: High-Precision TIA Circuit]

┌─────────────────────────────────────┐
│  [회로도 이미지]                    │
│                                     │
│  [빨간 박스1] OPA140 TIA            │
│  [빨간 박스2] Switchable Gain       │
│  [빨간 박스3] Low-pass Filter       │
└─────────────────────────────────────┘

**Design Innovations:**
1. Variable gain (1M/10M/100MΩ) by analog switch
2. Guard ring layout for low leakage current
3. Input bias current compensation
```

---

## 코드 샘플 작성법

### 방법 1: GitHub Repository (권장)

**장점:**
- 전체 소스코드 공개 가능
- 버전 관리 이력 공개
- Recruiter가 직접 확인 가능

**작성법:**
```markdown
### Firmware Architecture

**Repository:** https://github.com/username/sigma-1000-firmware

**Main Features:**
- FreeRTOS task management
- Modbus RTU/ASCII protocol
- IAP bootloader
- PID control algorithm

**Code Highlights:**
주요 코드는 GitHub repository에서 확인 가능합니다.
```

### 방법 2: 핵심 알고리즘 발췌

**선택 기준:**
- 독창적인 알고리즘 (PID tuning, Calibration)
- 문제 해결 코드 (버그 수정, 최적화)
- 성능 개선 코드 (속도 2배, 메모리 50% 절감)

**발췌 예시:**

```markdown
### PID Control Algorithm

**Implementation:**

```c
/**
 * @brief   Adaptive PID controller with anti-windup
 * @param   target: Setpoint value
 * @param   current: Current measured value
 * @return  Control output (0-100%)
 */
float pid_control(float target, float current) {
    static float integral = 0.0f;
    static float prev_error = 0.0f;
    
    float error = target - current;
    
    // Proportional term
    float p_term = pid.kp * error;
    
    // Integral term with anti-windup
    integral += error * pid.dt;
    if (integral > pid.i_max) integral = pid.i_max;
    if (integral < pid.i_min) integral = pid.i_min;
    float i_term = pid.ki * integral;
    
    // Derivative term with low-pass filter
    float derivative = (error - prev_error) / pid.dt;
    derivative = pid.alpha * derivative + (1 - pid.alpha) * prev_derivative;
    float d_term = pid.kd * derivative;
    
    prev_error = error;
    prev_derivative = derivative;
    
    // Calculate output
    float output = p_term + i_term + d_term;
    
    // Limit output
    if (output > 100.0f) output = 100.0f;
    if (output < 0.0f) output = 0.0f;
    
    return output;
}
```

**Performance:**
- Settling time: 2.5 seconds (vs. 5.0s baseline)
- Overshoot: < 5% (vs. 15% baseline)
- Steady-state error: < 0.1%

**Key Improvements:**
1. Anti-windup: Integral term clamping
2. Derivative filtering: Alpha=0.7 for noise reduction
3. Adaptive gain: Kp/Ki/Kd auto-tuning
```

### 방법 3: 코드 메트릭스 표시

```markdown
### Code Quality Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Lines of Code | 12,450 | - | - |
| Functions | 185 | - | - |
| Cyclomatic Complexity | 8.2 avg | < 10 | ✅ |
| Code Coverage (Unit Test) | 78% | > 70% | ✅ |
| MISRA C Compliance | 98% | > 95% | ✅ |
| Static Analysis Warnings | 3 | < 10 | ✅ |
| Memory Usage (Flash) | 85% | < 90% | ✅ |
| Memory Usage (RAM) | 62% | < 80% | ✅ |

**Code Review Process:**
- Peer review: 2 reviewers per commit
- Static analysis: PC-lint, Cppcheck
- Unit testing: 78% coverage
- Integration testing: 100% scenarios
```

---

## 이미지 및 그래프

### PCB 레이아웃 이미지

**촬영 방법:**
```
Altium Designer:
  View → 3D View
  ↓
  Camera Angle: 45° top-right
  ↓
  Export Image: PNG (1920x1080)
  ↓
  Photoshop: Brightness +20%, Contrast +10%
```

**첨부 예시:**
```markdown
[Figure 3: Sigma-1000 Main Board PCB Layout]

┌─────────────────────────────────────┐
│  [3D PCB 이미지]                    │
│  - 8-Layer stackup                  │
│  - Size: 150x100mm                  │
│  - Components: 320+ parts           │
└─────────────────────────────────────┘

**Layout Features:**
- Analog/Digital ground split (red line)
- Controlled impedance traces (50Ω)
- Via stitching for thermal management
- Component placement optimization
```

### 테스트 결과 그래프

**그래프 종류:**
```
✓ Bode Plot (AC analysis)
✓ Step Response (transient)
✓ FFT (frequency analysis)
✓ Temperature vs. Output (stability)
✓ Load Regulation (power supply)
```

**예시:**
```markdown
[Figure 4: Power Supply Load Regulation]

┌─────────────────────────────────────┐
│  [Load vs. Output Voltage Graph]    │
│                                     │
│  Y-axis: Output Voltage (V)        │
│  X-axis: Load Current (mA)         │
│                                     │
│  Target: 5.00V ±1%                 │
│  Measured: 5.00V ±0.3%             │
└─────────────────────────────────────┘

**Test Conditions:**
- Input: 24VDC ±10%
- Load: 0 ~ 3A (0 ~ 100%)
- Temperature: 25°C
- Measurement: 6.5 digit DMM

**Results:**
✅ Regulation: ±0.3% (spec: ±1%)
✅ Ripple: 35mVpp (spec: < 50mVpp)
✅ Efficiency: 87% @ 50% load
```

---

## 실전 예제

### 예제 1: 프로젝트 페이지 (회로 설계자)

```markdown
## 3. Psi-1000 Pressure Controller

### 3.1 Project Overview

**Period:** 2019-2022 (3 years)
**Role:** Lead Hardware Engineer
**Team:** 2 HW + 3 FW engineers
**Budget:** $150K
**Status:** Production (20+ units deployed)

**Objective:**
반도체 공정용 정밀 진공 압력 제어 시스템 개발

### 3.2 System Architecture

[Figure 1: System Block Diagram]

┌─────────────────────────────────────────────────────┐
│                                                     │
│  [MCU] ─→ [DAC] ─→ [V/I] ─→ [MFC] ─→ [Chamber]   │
│    ↑                                      │         │
│    └──────── [ADC] ←─ [Baratron] ←───────┘        │
│                                                     │
└─────────────────────────────────────────────────────┘

**Key Components:**
- MCU: STM32F407 (168MHz)
- DAC: LTC2630 (12-bit, I2C)
- ADC: ADS1115 (16-bit, I2C)
- Pressure Sensor: MKS Baratron 627D
- MFC: McMillan U803 (0-100 SCCM)

### 3.3 Circuit Design Highlights

#### 3.3.1 Pressure Sensor Interface

[Figure 2: Baratron Interface Circuit]

┌─────────────────────────────────────────────────────┐
│  [회로도 이미지]                                    │
│                                                     │
│  Baratron (0-10V) → Op-Amp Buffer → LPF → ADC     │
│                                                     │
│  [주석]                                            │
│  - Input impedance: 10MΩ (to prevent loading)     │
│  - Buffer: OPA140 (low offset, low noise)         │
│  - LPF: fc=10Hz (2nd-order Butterworth)           │
│  - ADC: ADS1115 (16-bit, 860 SPS)                 │
└─────────────────────────────────────────────────────┘

**Design Parameters:**

| Parameter | Value | Calculation |
|-----------|-------|-------------|
| Input Range | 0-10V | Baratron output |
| Resolution | 153µV/LSB | 10V / 2^16 |
| Noise Floor | < 50µVrms | Op-amp + ADC noise |
| Bandwidth | 10Hz | fc = 1 / (2π×R×C) |
| Update Rate | 100Hz | 860 SPS / 8 avg |

**Noise Analysis:**
```
Total Input-Referred Noise:
  Vnoise = √(Vn_opamp² + Vn_adc²)
         = √(10µV² + 48µV²)
         = 49.0 µVrms

SNR = 20×log10(Vsignal / Vnoise)
    = 20×log10(10V / 49µV)
    = 106 dB
```

#### 3.3.2 MFC Control Loop

[Figure 3: V/I Converter for MFC]

┌─────────────────────────────────────────────────────┐
│  [회로도 이미지]                                    │
│                                                     │
│  DAC (0-5V) → V/I Converter → 0-20mA → MFC        │
│                                                     │
│  [주석]                                            │
│  - DAC: LTC2630-12 (I2C)                           │
│  - V/I: LM334 + Op-amp                             │
│  - Current sense: 0.1Ω shunt + INA139             │
│  - Protection: TVS diode, series resistor          │
└─────────────────────────────────────────────────────┘

**V/I Converter Equation:**
```
Iout = (Vin / R1) × (R2 / R3)
     = (0-5V / 250Ω) × (1kΩ / 1kΩ)
     = 0-20mA

Resolution:
  ILSB = (20mA - 0mA) / 2^12
       = 4.88 µA/LSB
       
Control Range:
  Flow = Iout × MFC_gain
       = (0-20mA) × 5 SCCM/mA
       = 0-100 SCCM
```

### 3.4 PCB Layout

[Figure 4: Psi-1000 Main Board]

┌─────────────────────────────────────────────────────┐
│  [PCB 3D 이미지]                                    │
│                                                     │
│  - Size: 120×80mm                                  │
│  - Layers: 4 (Signal-GND-Power-Signal)            │
│  - Components: 180 parts                           │
└─────────────────────────────────────────────────────┘

**Layout Strategy:**
```
Layer 1 (Top):    Component placement, signal routing
Layer 2 (GND):    Solid ground plane
Layer 3 (Power):  Power rails (+5V, +3.3V, +15V, -15V)
Layer 4 (Bottom): Signal routing, component placement

Critical Traces:
  ✓ Analog signal traces: 0.3mm width, 10mm length
  ✓ Guard ring around TIA (GND trace)
  ✓ Kelvin sensing for current measurement
  ✓ Star-point grounding for analog
```

### 3.5 Test Results

#### 3.5.1 Pressure Control Performance

[Figure 5: Step Response Test]

┌─────────────────────────────────────────────────────┐
│  [Graph: Pressure vs. Time]                         │
│                                                     │
│  Setpoint: 100 mTorr → 500 mTorr (step)           │
│  Rise time: 2.3 seconds                            │
│  Overshoot: 4.2%                                   │
│  Settling time: 4.8 seconds (±1%)                  │
└─────────────────────────────────────────────────────┘

**PID Parameters:**
```
Kp = 2.5
Ki = 0.8
Kd = 0.15

Tuning Method: Ziegler-Nichols
Optimization: Manual fine-tuning
```

#### 3.5.2 Accuracy & Stability

| Test Condition | Target | Measured | Status |
|----------------|--------|----------|--------|
| Accuracy (100 mTorr) | ±0.1% FSR | ±0.08% | ✅ |
| Repeatability | < 0.05% | 0.03% | ✅ |
| Temperature drift | < 0.01%/°C | 0.008%/°C | ✅ |
| Long-term stability (24h) | < 0.1% | 0.06% | ✅ |

### 3.6 Collaboration & External Partnership

**동아대학교 산학협력:**
- 기간: 2020-2022 (2년)
- 협력 내용: PID 알고리즘 공동 개발
- 역할: 하드웨어 설계 및 제공, 펌웨어 인터페이스 정의
- 성과: 
  * Control logic Rev 05까지 반복 개선
  * 논문 1편 공동 저자
  * 특허 1건 공동 출원

**기술 문서:**
- Modbus Protocol Ver 0.27-0.30
- PID Tuning Guide (Rev 2.1)
- User Manual (Korean/English)

### 3.7 Production & Field Performance

**양산 현황:**
```
Production Start:    2022-Q3
Units Produced:      20+ units
Deployment Sites:    5 semiconductor fabs
Field Failure Rate:  0% (no returns)
Uptime:              99.8% (24/7 operation)
```

**비용 분석:**
```
Development Cost:    $150K
Unit Cost:           $4,500
Competitor Price:    $12,000
Cost Savings:        62.5% per unit
```

### 3.8 Lessons Learned

**Technical Challenges:**
1. **Issue:** ADC 노이즈가 스펙 초과 (100µVrms vs. 50µV target)
   - **Root Cause:** PCB layout, power supply ripple
   - **Solution:** LDO 추가 (5V → 3.3V analog), guard ring
   - **Result:** 노이즈 48µVrms로 개선 (52% reduction)

2. **Issue:** MFC 제어 오버슈트 15%
   - **Root Cause:** PID 게인 과다
   - **Solution:** Ziegler-Nichols + manual tuning
   - **Result:** 오버슈트 4.2%로 개선

**Key Takeaways:**
- Analog/Digital ground 분리의 중요성
- PID 파라미터 자동 튜닝 알고리즘 필요
- 산학협력을 통한 기술 향상
```

---

### 예제 2: 프로젝트 페이지 (펌웨어 설계자)

```markdown
## 4. Nu-2000 Firmware Development

### 4.1 Project Overview

**Period:** 2021-2022 (1.5 years)
**Role:** Lead Firmware Engineer
**Team:** 1 HW + 2 FW engineers
**Platform:** STM32F407 + FreeRTOS
**Status:** Production (30+ units)

### 4.2 Software Architecture

[Figure 1: FreeRTOS Task Diagram]

┌─────────────────────────────────────────────────────┐
│  Priority  Task Name           Stack  Period       │
│  ────────  ─────────────────   ─────  ────────     │
│     5      LED_Control         256B   10ms         │
│     4      Sensor_Acquisition   512B   50ms         │
│     3      PID_Control          512B   100ms        │
│     2      Modbus_Handler      1024B   Event        │
│     1      Data_Logger          512B   1000ms       │
│     0      Idle_Task            128B   -           │
└─────────────────────────────────────────────────────┘

**Memory Usage:**
```
Flash:  245 KB / 512 KB (48%)
RAM:     92 KB / 128 KB (72%)
Stack:   14 KB (Task + ISR)
Heap:    20 KB (FreeRTOS)
```

### 4.3 Key Algorithm: Adaptive PID Control

**Algorithm Overview:**
```
┌─────────────────────────────────────────┐
│  Setpoint ──→ [PID] ──→ Output         │
│                ↑                        │
│                │                        │
│  Feedback ─────┘                        │
│                                         │
│  [Features]                             │
│  - Anti-windup                          │
│  - Derivative filtering                 │
│  - Gain scheduling                      │
└─────────────────────────────────────────┘
```

**Implementation (C Code):**

```c
/**
 * @file    pid_control.c
 * @brief   Adaptive PID controller with anti-windup
 * @author  Rakhyun Cho
 * @date    2022-03-15
 * @version 2.1
 */

#include "pid_control.h"
#include <math.h>

// PID controller structure
typedef struct {
    float kp;              // Proportional gain
    float ki;              // Integral gain
    float kd;              // Derivative gain
    float dt;              // Sample time (seconds)
    float i_max;           // Integral max (anti-windup)
    float i_min;           // Integral min (anti-windup)
    float alpha;           // Derivative filter coefficient
} PID_TypeDef;

// Global PID instance
static PID_TypeDef pid = {
    .kp = 2.5f,
    .ki = 0.8f,
    .kd = 0.15f,
    .dt = 0.1f,            // 100ms
    .i_max = 50.0f,
    .i_min = -50.0f,
    .alpha = 0.7f          // Low-pass filter
};

/**
 * @brief   PID control calculation
 * @param   target: Setpoint value
 * @param   current: Current measured value
 * @return  Control output (0-100%)
 */
float PID_Control(float target, float current) {
    static float integral = 0.0f;
    static float prev_error = 0.0f;
    static float prev_derivative = 0.0f;
    
    // Calculate error
    float error = target - current;
    
    // Proportional term
    float p_term = pid.kp * error;
    
    // Integral term with anti-windup
    integral += error * pid.dt;
    if (integral > pid.i_max) integral = pid.i_max;
    if (integral < pid.i_min) integral = pid.i_min;
    float i_term = pid.ki * integral;
    
    // Derivative term with low-pass filter
    float derivative = (error - prev_error) / pid.dt;
    derivative = pid.alpha * derivative + 
                 (1.0f - pid.alpha) * prev_derivative;
    float d_term = pid.kd * derivative;
    
    // Save for next iteration
    prev_error = error;
    prev_derivative = derivative;
    
    // Calculate output
    float output = p_term + i_term + d_term;
    
    // Limit output (0-100%)
    if (output > 100.0f) output = 100.0f;
    if (output < 0.0f) output = 0.0f;
    
    return output;
}

/**
 * @brief   Reset PID controller
 */
void PID_Reset(void) {
    // Reset internal states
    integral = 0.0f;
    prev_error = 0.0f;
    prev_derivative = 0.0f;
}

/**
 * @brief   Update PID parameters (Modbus command)
 * @param   params: New PID parameters
 */
void PID_UpdateParams(PID_Params_t* params) {
    pid.kp = params->kp;
    pid.ki = params->ki;
    pid.kd = params->kd;
    
    // Reset controller after parameter change
    PID_Reset();
}
```

**Performance Comparison:**

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Settling Time | 5.0 sec | 2.5 sec | **50%** ↓ |
| Overshoot | 15% | 4.8% | **68%** ↓ |
| Steady-state Error | 0.5% | 0.08% | **84%** ↓ |
| CPU Usage | 12% | 8% | **33%** ↓ |

### 4.4 Modbus Protocol Implementation

**Supported Functions:**
```
0x03: Read Holding Registers
0x04: Read Input Registers
0x06: Write Single Register
0x10: Write Multiple Registers
0x17: Read/Write Multiple Registers
```

**Register Map (Partial):**

| Address | Name | Type | Unit | Access |
|---------|------|------|------|--------|
| 0x0000 | Device ID | uint16 | - | R |
| 0x0001 | Firmware Ver | uint16 | - | R |
| 0x0010 | Setpoint | float | mTorr | R/W |
| 0x0012 | Current Value | float | mTorr | R |
| 0x0020 | PID Kp | float | - | R/W |
| 0x0022 | PID Ki | float | - | R/W |
| 0x0024 | PID Kd | float | - | R/W |

**Code Snippet:**

```c
/**
 * @brief   Modbus request handler
 * @param   request: Received Modbus frame
 * @param   response: Response buffer
 * @return  Response length
 */
uint16_t Modbus_Handler(uint8_t* request, uint8_t* response) {
    uint8_t function = request[1];
    uint16_t addr = (request[2] << 8) | request[3];
    
    switch (function) {
        case 0x03:  // Read Holding Registers
            return Modbus_ReadHoldingRegs(addr, response);
            
        case 0x06:  // Write Single Register
            return Modbus_WriteSingleReg(addr, request[4], request[5]);
            
        // ... other functions
        
        default:
            return Modbus_Error(MB_EX_ILLEGAL_FUNCTION, response);
    }
}
```

### 4.5 Code Quality & Testing

**Static Analysis:**
```
Tool: PC-lint Plus
Rules: MISRA C:2012

Results:
  ✅ No critical errors
  ✅ 5 warnings (all justified)
  ✅ 98% MISRA compliance
```

**Unit Testing:**
```
Framework: Unity + CMock
Coverage: 78% (target: > 70%)

Test Results:
  ✅ 142 tests passed
  ✅ 0 tests failed
  ✅ Execution time: 2.3 seconds
```

**Integration Testing:**
```
Scenarios Tested:
  ✅ Power-up sequence
  ✅ Sensor failure handling
  ✅ Communication timeout
  ✅ Parameter out-of-range
  ✅ Firmware update (IAP)
  ✅ 24-hour stability test
```

### 4.6 Achievements

**Performance:**
- Zero critical bugs in production
- 99.9% uptime (24/7 operation)
- < 1 second boot time
- 8% CPU usage average

**Development:**
- 12,450 lines of code
- 185 functions
- 15 FreeRTOS tasks
- 8 interrupt handlers

**Documentation:**
- API reference (Doxygen, 200+ pages)
- User manual (Korean/English)
- Modbus protocol specification
- Test procedures (20+ scenarios)
```

---

## ✅ 체크리스트

포트폴리오 제출 전 확인사항:

### 문서 품질
- [ ] 오타/문법 오류 확인 (Grammarly 사용)
- [ ] 일관된 용어 사용 (DAC vs. D/A converter)
- [ ] 페이지 번호 삽입
- [ ] 목차 업데이트 (Word: 참조 → 목차 업데이트)

### 기술 내용
- [ ] 회로도: 가독성 확인 (텍스트 크기 > 8pt)
- [ ] 코드: 주석 포함, 들여쓰기 일관성
- [ ] 이미지: 고해상도 (> 1200px width)
- [ ] 그래프: 축 레이블, 단위 표시

### 정량적 성과
- [ ] 숫자로 표현 (예: "성능 개선" → "성능 50% 개선")
- [ ] 비교 기준 명시 (vs. baseline, vs. competitor)
- [ ] 측정 방법 기재 (DMM 6.5 digit, oscilloscope)

### 기밀 정보
- [ ] 회사 기밀 정보 제거
- [ ] 고객사 이름 익명화 (필요 시)
- [ ] 급여, 계약 금액 제거

### 파일 관리
- [ ] PDF로 저장 (폰트 임베드)
- [ ] 파일명: `Lastname_Firstname_Portfolio_2026.pdf`
- [ ] 파일 크기: < 10MB (이미지 압축)

---

## 📚 참고 자료

**포트폴리오 샘플:**
- IEEE Spectrum: Engineering Portfolio Examples
- LinkedIn: Featured Projects Section
- GitHub: README.md examples

**도구:**
- **Grammarly**: 영문 교정
- **Canva**: 그래픽 디자인
- **Draw.io**: Block diagram
- **PlantUML**: Software architecture diagram

---

**Last Updated:** 2026-01-13
**Version:** 1.0
