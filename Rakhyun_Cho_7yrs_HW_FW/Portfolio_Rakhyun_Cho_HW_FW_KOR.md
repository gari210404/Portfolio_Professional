# Rakhyun Cho (조락현)

## Hardware & Firmware Engineer

**7년 이상의 Full-Stack Embedded Systems 개발 경력**

---

## Professional Summary

회로 설계부터 펌웨어 구현까지 완전한 임베디드 시스템 개발 분야에서 7년 이상의 경력을 보유한 다재다능한 하드웨어 및 펌웨어 엔지니어입니다. STM32 마이크로컨트롤러 기반 시스템, 실시간 운영체제, 산업용 통신 프로토콜을 전문으로 하며, 견고한 하드웨어 설계와 효율적인 펌웨어 아키텍처를 결합한 양산 가능한 제품을 제공한 검증된 실적을 보유하고 있습니다.

**핵심 역량:**
- 완전한 임베디드 시스템 개발 (Hardware + Firmware + Testing)
- FreeRTOS를 활용한 STM32 펌웨어 개발
- 산업용 통신 프로토콜 (Modbus, RS-232/485, I2C/SPI)
- 제어 알고리즘 (PID, state machine, sensor fusion)
- Hardware-firmware co-design 최적화
- 양산 펌웨어 배포 및 필드 업데이트
- 기술 문서화 및 지식 전달

---

## Technical Skills

### Hardware Design
- **Circuit Design**: Mixed-signal 회로, 센서 인터페이스, 통신 모듈, 전원 관리
- **Microcontroller Systems**: STM32 (F1/F4/F7/H7), 주변장치 통합, 클럭 설정
- **Communication Interfaces**: RS-232/485, I2C, SPI, UART, USB, CAN, Modbus RTU/ASCII
- **PCB Design**: Altium Designer, 4-6 layer board, 부품 배치 최적화
- **Tools**: Altium Designer, LTspice, oscilloscope, logic analyzer

### Firmware Development
- **Languages**: C (Expert), C++ (Proficient), Python (Scripting)
- **Microcontrollers**: STM32 시리즈 (F103, F407, F746, H743)
- **RTOS**: FreeRTOS (Task scheduling, Queue, Semaphore, Mutex, Event Group)
- **HAL/LL**: STM32 HAL, LL driver, Custom peripheral driver
- **Communication**: UART/USART, SPI, I2C, USB CDC/HID, Modbus RTU/ASCII, CANopen
- **Protocols**: Modbus Master/Slave, Custom binary protocol, AT command parser
- **Peripherals**: ADC, DAC, Timer/PWM, DMA, SDIO, RTC, Watchdog

### Development Tools
- **IDE**: STM32CubeIDE, Keil µVision, IAR EWARM, VS Code
- **Debuggers**: ST-Link V2/V3, J-Link, GDB, SWD debugging
- **Build Systems**: Make, CMake, STM32CubeMX code generation
- **Version Control**: Git, GitHub, GitLab, SourceTree
- **Testing**: Logic analyzer, oscilloscope, bus monitor, UART console

### Software Architecture
- **Design Pattern**: State machine, Observer, Command pattern
- **Code Organization**: 계층 구조 (HAL → Driver → Application)
- **Memory Management**: Static allocation, memory pool, DMA buffer
- **Optimization**: 코드 크기 최적화, 실행 시간 프로파일링, 전력 소비
- **Bootloader**: IAP (In-Application Programming), UART/USB/SD card를 통한 펌웨어 업데이트

### Control Systems & Algorithms
- **PID Control**: Classical PID, Anti-windup, Derivative filtering, Auto-tuning algorithm
- **Signal Processing**: Moving average, Kalman filtering, FFT, Digital filter
- **Calibration**: Multi-point calibration, 다항식 회귀, 온도 보상
- **State Machine**: 복잡한 multi-state controller, event-driven architecture

---

## Professional Experience

### ATIK Corp. | Hardware & Firmware Engineer
**2018 - Present (7년 이상)**

#### 주요 프로젝트

### 1. **Sigma-1000 LPC Simulator** (2020-2021)
**역할:** Hardware & Firmware Developer | **양산:** 50대 이상 | **불량률:** 0.5%

정밀 DAC 하드웨어와 실시간 제어 펌웨어를 결합한 플라즈마 교정 시뮬레이터

**하드웨어 기여:**
- STM32F407IGT6 기반 제어 보드 설계
- 16채널 MCP4728 DAC 인터페이스 (I2C)
- RS-232/485 통신 회로
- 전원 공급 분배 네트워크

**펌웨어 아키텍처:**
```
Application Layer
├── Calibration Engine
├── Communication Handler (Modbus RTU/ASCII)
├── Data Logging (SD Card)
└── User Interface (Nextion HMI)

Driver Layer
├── DAC Driver (MCP4728 I2C)
├── ADC Driver (Internal 12-bit)
├── UART Driver (RS-232/485)
└── SD Card Driver (SDIO + FatFS)

HAL Layer
└── STM32 HAL + Custom optimization
```

**주요 펌웨어 기능:**
- **Real-time DAC Control**: 
  - 16채널 @ 1ms 업데이트 속도
  - I2C 통신 400kHz
  - 오류 감지 및 자동 재시도 메커니즘
  - 전압 정확도: ±0.01% FSR

- **Communication Protocol**:
  - Modbus RTU/ASCII master/slave 구현
  - 고속 데이터 전송을 위한 custom binary protocol
  - CRC-16 오류 검사
  - Timeout 및 복구 메커니즘

- **Calibration System**:
  - Multi-point calibration (채널당 최대 20포인트)
  - 다항식 curve fitting (최대 3차)
  - 온도 보상 알고리즘
  - 비휘발성 저장 (Flash에 EEPROM emulation)

- **Data Logging**:
  - SD card 파일 시스템 (FatFS)
  - Circular buffer 구현 (1MB RAM buffer)
  - RTC를 사용한 timestamp
  - 분석이 쉬운 CSV 형식

- **User Interface**:
  - Nextion HMI 통신 (UART)
  - 터치스크린 인터페이스
  - 실시간 그래프 표시
  - 설정 메뉴 시스템

**성능 지표:**
- 펌웨어 크기: 256KB Flash, 64KB RAM 사용
- 부팅 시간: < 2초
- 통신 지연: < 10ms (Modbus)
- Calibration 시간: 5분 (이전 방법 대비 83% 단축)

**펌웨어 품질:**
- 양산에서 치명적 버그 Zero
- IAP bootloader를 통한 필드 펌웨어 업데이트
- 종합적인 오류 로깅 및 진단

---

### 2. **Nu-2000 Optical Analysis System** (2021-2022)
**역할:** Firmware Lead & Hardware Support | **프로젝트 규모:** 33MB 개발 계획

복잡한 다채널 제어 펌웨어가 필요한 고급 광학 흡수 분광 시스템

**하드웨어 기여:**
- 시스템 통합 및 디버깅
- 센서 인터페이스 검증
- 통신 모듈 테스트

**펌웨어 아키텍처:**
```
FreeRTOS Tasks (5개 task, priority 1-5)
├── Task1: LED Driver Control (Priority: 5, Period: 100ms)
├── Task2: Photodiode Data Acquisition (Priority: 4, Period: 50ms)
├── Task3: Temperature Monitoring (Priority: 3, Period: 1s)
├── Task4: Communication Handler (Priority: 2, Event-driven)
└── Task5: Data Processing (Priority: 1, Event-driven)

Queue & Semaphore
├── ADC Data Queue (100 sample depth)
├── UART TX Queue (512 byte)
├── I2C Mutex (공유 버스 접근용)
└── Event Group (시스템 상태 플래그)
```

**주요 펌웨어 기능:**

- **Multi-wavelength LED Control**:
  - 4개 LED 채널 (UV: 254nm, 280nm | IR: 1450nm, 1650nm)
  - Timer 주변장치를 사용한 PWM 생성
  - ADC를 통한 전류 모니터링
  - 열 보상 알고리즘
  - 자동 강도 조절

- **High-speed Data Acquisition**:
  - 4개 Photodiode 채널 @ 250kSPS (AD7682 ADC)
  - DMA 기반 circular buffer (CPU 오버헤드 zero)
  - 실시간 신호 처리 파이프라인
  - 노이즈 분석을 위한 FFT
  - Moving average filter (설정 가능한 window)

- **Precision Temperature Control**:
  - 듀얼 RTD 센서 (MCP3427 18-bit ADC, I2C)
  - 0.01°C 해상도
  - 광학 안정성을 위한 PID 온도 제어
  - 열 드리프트 보상

- **Optical Module Integration**:
  - 광학 모듈 특성 분석을 위한 테스트 펌웨어
  - 자동화된 calibration 루틴
  - Wiki Optics 외주 업체 검증을 위한 데이터 로깅
  - 필드 테스트를 위한 Beta 버전 펌웨어

- **Bootloader (IAP)**:
  - UART 기반 펌웨어 업데이트
  - CRC32 무결성 검사
  - Fail-safe 업데이트를 위한 dual-bank Flash
  - 부팅 시 버전 표시
  - 설치 매뉴얼 작성 (V0.2)

**소프트웨어 개발 프로세스:**
- 모듈형 펌웨어 아키텍처
- Git 버전 관리
- 종합적인 테스트 절차 문서화
- Hardware-firmware 통합 테스트
- 필드 beta 테스트 프로그램

**산출물:**
- 펌웨어 구조 개요 프레젠테이션
- 광학 모듈 테스트 펌웨어 사용 매뉴얼
- IAP 설치 및 사용 가이드 (V0.2)
- Calibration 절차 문서
- Hardware-firmware 인터페이스 사양서

---

### 3. **Psi-1000 Pressure Controller** (2019-2022)
**역할:** PID Control Algorithm Developer & Firmware Architect

정교한 PID 알고리즘과 대학 협력이 포함된 고급 압력 제어 시스템

**하드웨어 기여:**
- System block diagram 설계
- IAP 업그레이드 메커니즘
- PCB bring-up 및 디버깅

**펌웨어 아키텍처 - PID Control 중심:**

**PID Algorithm 구현:**
- 여러 PID 공식 연구 (Standard Form vs. Beckhoff Library Form)
- Anti-windup이 포함된 discrete-time PID 구현
- 미분항 low-pass filtering (노이즈 감소)
- 설정 가능한 sampling time (1ms - 1s)
- Modbus를 통한 파라미터 튜닝 인터페이스

**PID Form 비교 연구:**
```c
// Standard Form #1 (구현됨)
U(k) = Kp * [e(k) + (T/Ti) * Σe(j) + (Td/T) * (e(k) - e(k-1))]

// Beckhoff Library Form (분석됨)
U(s)/E(s) = Kp * (1 + 1/(Ti*s) + Td*s)

// Anti-windup을 포함한 Discrete 구현
integral = integral + (T/Ti) * error;
if (integral > integral_max) integral = integral_max;  // Anti-windup
derivative = (Td/T) * (error - error_prev) / (1 + Td/(N*T));  // Filtered
output = Kp * (error + integral + derivative);
```

**고급 제어 기능:**
- **Auto-tuning Algorithm**: 
  - Relay feedback 방법 (Åström-Hägglund)
  - Ziegler-Nichols 튜닝 규칙 구현
  - Step response 분석
  - Bode plot 측정 지원

- **Multiple PID Instance**:
  - Pressure control PID (primary)
  - Temperature control PID (heater)
  - Flow control PID (MFC)
  - Cascade control 기능

- **Control Logic Design** (대학 협력):
  - Rev 01 - 05 control logic 반복 문서화
  - 동아대학교 연구 프로젝트
  - 실험을 통한 파라미터 최적화
  - 테스트 결과 분석 및 보고

**Communication & Interface:**
- **Modbus Protocol**:
  - RTU/ASCII 지원 (Master & Slave)
  - Protocol 사양서 Ver 0.27 - 0.30
  - Function code: 03, 06, 16 (Read/Write register)
  - Custom register map 설계

- **Beckhoff PLC Integration**:
  - 설정 절차 문서화
  - PLC와 auto-tuning 통합
  - 실시간 데이터 교환

**개발된 소프트웨어 도구:**
- PID Loop Simulator (Excel VBA)
- 파라미터 튜닝을 위한 PID Scrollbar GUI (Excel)
- Auto-tune 테스트 스크립트
- Step response analyzer

**펌웨어 개발 산출물:**
- Control logic 설계 문서 (Rev 01-05)
- Software 설계 사양서 (Rev 01-03)
- PID 파라미터 변경 절차
- 테스트 결과 분석 프레젠테이션
- Software 매뉴얼 (Ver 0.3)

**Testing & Validation:**
- Heater PID 테스트 데이터 수집
- Z-N 튜닝 방법 검증
- IMC (Internal Model Control) 테스트
- Auto-tune 성능 검증
- Step test 특성 분석

**달성 성과:**
- ±0.1% 압력 제어 정확도 달성
- < 2초 정착 시간 (step response)
- 0.001 - 1000 Torr 범위에서 안정적 동작
- 대학 기술 이전 성공

---

### 4. **L-Titrator (Automatic Titrator)** (2018-2020)
**역할:** Embedded Systems Developer

화학 분석 기기 펌웨어 개발

**펌웨어 기능:**
- 스테퍼 모터 제어 (burette 위치 결정)
- pH 센서 데이터 수집 및 처리
- 온도 보상 알고리즘
- 자동 calibration 루틴
- PC 소프트웨어를 위한 USB 통신
- 데이터 로깅 및 결과 저장

---

## 추가 기술 기여

### Bootloader Development (IAP)
- **IAP_ATIK Project**: 독립형 bootloader 프레임워크
- 기능: UART/USB 펌웨어 업데이트, CRC 무결성 검사, dual-bank Flash
- 여러 프로젝트에 재사용 가능
- 각 제품별 사용자 매뉴얼 작성

### HMI Development
- **Nextion HMI**: 터치스크린 인터페이스 설계
- MCU-HMI 통신을 위한 custom protocol
- 실시간 그래프 표시 최적화
- 사용자 친화적인 설정 메뉴

### Testing & Debugging Tools
- 디버깅을 위한 custom UART console 명령
- 내장 진단 및 자체 테스트 루틴
- Memory dump 및 register 검사
- 성능 프로파일링 도구

---

## 펌웨어 개발 방법론

### 1. **구조화된 설계 프로세스**
- 요구사항 분석 및 사양 정의
- 펌웨어 아키텍처 설계 (block diagram, task diagram)
- 모듈 인터페이스 정의
- 코드 리뷰와 함께 구현
- Unit test 및 통합 테스트
- 시스템 검증 및 필드 테스트

### 2. **코드 품질 표준**
- 명확한 인터페이스를 가진 모듈형 설계
- 일관된 네이밍 규칙
- 종합적인 inline 주석
- 모든 계층에서 에러 처리
- 메모리 누수 방지
- 정적 코드 분석

### 3. **버전 관리 및 문서화**
- Git 브랜칭 전략 (feature/develop/master)
- 이슈 추적이 포함된 commit 메시지
- 각 모듈의 README 파일
- API 문서
- 최종 사용자를 위한 사용자 매뉴얼

---

## 주요 기술 성과

### 펌웨어 프로젝트
- **8개 이상 양산 펌웨어** 배포
- **치명적 버그 Zero** 양산 시스템
- **256KB+ Flash** 일반적인 펌웨어 크기 (최적화)
- **< 2초** 부팅 시간 표준

### 알고리즘 개발
- **PID Control Library**: 프로젝트 전반에 재사용 가능
- **Calibration Engine**: Multi-point, 다항식 fitting
- **Communication Stack**: Modbus RTU/ASCII 구현
- **Data Logger**: FatFS 기반 SD card 시스템

### 기술 문서화
- **15개 이상 사용자 매뉴얼** 작성 (IAP, calibration, testing)
- **8개 이상 기술 프레젠테이션** (회로 검토, PID 연구)
- **460개 이상 문서** 모든 프로젝트 (하드웨어 팀과 함께)
- **종합적인 테스트 절차** 모든 제품

---

## PID Control 전문성 (상세)

### 연구 및 학습
- PID 알고리즘 심층 연구 (프레젠테이션으로 문서화)
- 여러 PID 공식 비교
- Beckhoff PLC PID 라이브러리 분석
- Auto-tuning 방법 문헌 검토

### 구현 경험
- Anti-windup이 포함된 Classical PID
- Manual/auto 전환을 위한 bumpless transfer
- Derivative kick 방지
- Setpoint weighting
- 비선형 시스템을 위한 gain scheduling

### 적용된 튜닝 방법
- Ziegler-Nichols (closed-loop, open-loop)
- Cohen-Coon 방법
- Relay feedback (Åström-Hägglund)
- IMC (Internal Model Control) 튜닝
- Step response 분석을 통한 수동 튜닝

### 실제 적용 사례
- 압력 제어: ±0.1% 정확도, < 2초 정착
- 온도 제어: ±0.05°C 안정성
- 유량 제어: ±2% MFC setpoint 추종

---

## 전문성 개발

### 지속적 학습
- 고급 RTOS 개념 (task priority, scheduling, IPC)
- 신호 처리 알고리즘 (Kalman filter, FFT)
- 제어 이론 (modern control, state-space model)
- 통신 프로토콜 (CANopen, EtherCAT 기초)
- 안전 표준 (IEC 61508, functional safety)

### 기술 스킬 성장
- 시작: 기본 STM32 프로그래밍
- 현재: Expert-level 펌웨어 architect
- 미래: Edge AI/ML, Rust for embedded 탐색

---

## Tools & Technologies

### Development Environment
- **IDE**: STM32CubeIDE (primary), Keil µVision, IAR EWARM
- **Debugger**: ST-Link V2/V3, J-Link, OpenOCD
- **Version Control**: Git, GitHub Desktop, SourceTree
- **Documentation**: Doxygen, Markdown, Microsoft Office

### Testing & Analysis
- **Hardware**: Logic analyzer (Saleae), Oscilloscope (Tektronix)
- **Software**: Bus monitor tool, UART terminal (Tera Term, PuTTY)
- **Profiling**: SystemView (Segger), FreeRTOS trace

### Simulation & Modeling
- **Circuit**: LTspice (하드웨어 검증)
- **Control**: MATLAB/Simulink (PID 튜닝), Excel VBA (PID simulator)
- **Python**: 데이터 분석 스크립트, 자동화 도구

---

## 업무 스타일 및 특성

- **Full-Stack 사고방식**: 하드웨어와 펌웨어 경계를 넘나드는 작업에 능숙
- **문제 해결사**: 하드웨어 신호부터 펌웨어 로직까지 체계적 디버깅
- **세심함**: Edge case 및 에러 처리에 주의 깊은 주의
- **협업**: 하드웨어 팀 및 외주 업체와 효과적인 커뮤니케이션
- **자기 학습**: 새로운 기술과 모범 사례 학습에 적극적
- **실용적**: 양산 가능하고 유지보수 가능한 코드에 집중

---

## Contact Information

**Cho, Rakhyun (조락현)**  
Hardware & Firmware Engineer

- **Email**: 92lock@kakao.com
- **Tel**: 010-7311-0402
- **Location**: Republic of Korea
- **GitHub**: [github.com/gari210404](https://github.com/gari210404)

---

## GitHub Repositories

| Repository | Description | Tech Stack |
|------------|-------------|------------|
| **ATIK-Firmware** | STM32 펌웨어 모음 (85MB) | C, FreeRTOS, STM32 HAL |
| **ATIK-Hardware-Projects** | Schematic & PCB 설계 (759MB) | Altium Designer |
| **ATIK-Software** | PC 소프트웨어 도구 (2.9MB) | C#, Python |
| **ATIK-Nextion-HMI** | HMI 프로젝트 (138MB) | Nextion IDE |
| **Arduino-Libraries** | Custom library (54MB) | C++, Arduino |

---

## References & Code Samples

펌웨어 소스 코드, 설계 문서, 기술 프레젠테이션은 요청 시 또는 GitHub 레포지토리를 통해 제공 가능합니다.

---

*본 포트폴리오는 양산 품질 펌웨어, 제어 알고리즘, hardware-firmware co-design에 강한 초점을 맞춘 7년 이상의 실무 임베디드 시스템 개발 경험을 나타냅니다.*
