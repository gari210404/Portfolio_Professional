# 조락현 포트폴리오 보완 Markdown
# 이 파일을 기반으로 경력이력서 업데이트

## 경력 요약 (9년차)

### ATIK (2016.03 ~ 현재)
- 분석기기 전문 회사
- 직책: Senior Embedded Engineer
- 역할: 하드웨어 설계 + 펌웨어 개발

---

## 주요 프로젝트

### 1. L-LPC (Laser Particle Counter) - 2022.03 ~ 2024.12
**역할:** HW 설계 + FW 개발 전담

**하드웨어:**
- MCU: STM32F407VGT6 (168MHz, ARM Cortex-M4)
- Ethernet PHY: LAN8720
- ADC: ADS1256 (24-bit)
- DAC: DAC8568 (16-bit)
- Interface: RS232, RS485, Ethernet, USB

**펌웨어:**
- FreeRTOS 기반 멀티태스크 설계
- LwIP TCP/IP 스택
- Modbus RTU/TCP 프로토콜
- 실시간 입자 계수 알고리즘

**성과:**
- 양산 적용 및 고객사 납품

---

### 2. L-Titrator (자동 적정기) - 2021.10 ~ 2022.09
**역할:** 회로 설계 + 펌웨어 개발 전담 (신규 개발)

**하드웨어:**
- Main Board: 모터 드라이버, 밸브 제어, 센서 인터페이스
- MCU Module: STM32F407 + Ethernet + SD Card
- Relay Module: 8채널 릴레이, 오토샘플러 제어

**펌웨어:**
- 시린지 펌프 스테핑 모터 정밀 제어
- pH 측정 및 온도 보상
- 자동 적정 알고리즘 (종점 검출)
- FreeRTOS 멀티태스크

**성과:**
- 신규 제품 양산 적용

---

### 3. Nu-2000 / Lux (분광광도계) - 2020.01 ~ 2023.12
**역할:** 펌웨어 개발 및 유지보수

**특징:**
- Lux는 Nu-2000의 후속 버전
- TouchGFX 기반 GUI
- STM32F407

**펌웨어:**
- 광학 시스템 제어 (회절격자 스테핑 모터)
- 스펙트럼 스캔 및 피크 검출
- 실시간 그래프 UI
- USB/SD Card 데이터 내보내기

---

### 4. Psi-1000 / Psi-3000 (항온조) - 2019.06 ~ 2021.12
**역할:** 펌웨어 개발

**특징:**
- ±0.01°C 정밀 온도 제어
- 듀얼 채널 제어

**펌웨어:**
- PID 온도 제어 알고리즘
- PT100 RTD 센서 처리
- PWM Heater + Peltier 제어
- 자동 튜닝 기능

---

### 5. MS (Mass Spectrometer) - Aston 시리즈 - 2019.01 ~ 현재
**역할:** 하드웨어 설계 (다수 모듈 보드)

**개발 보드:**
- Main Board: 시스템 제어
- Interface Board: 외부 장치 연결
- HV Power Board: 고전압 전원 (수 kV)
- Sensor Board: 이온 검출기 인터페이스
- Vacuum Gauge: 진공도 측정

---

### 6. SSC - Mantis (소형 분광계) - 2024.03 ~ 현재
**역할:** 회로 설계 + 펌웨어 개발 (진행 중)

**하드웨어:**
- MCU: STM32G0 시리즈
- Main Board + Sensor Board
- RS485 Modbus 통신

**펌웨어:**
- UART 인터럽트 핸들러
- Modbus RTU 프로토콜
- 저전력 설계

---

### 7. ATIK JIG Board (생산 테스트) - 2022.01 ~ 2022.12
**역할:** JIG 보드 회로 설계

**목적:** 양산 제품 기능 테스트 자동화

**기능:**
- Power Test: 전원 레일 자동 측정
- Communication Test: UART, SPI, I2C 루프백
- GPIO Test: I/O 핀 상태 확인

---

## 기술 스택

### 프로그래밍 언어
- **C/C++** - 임베디드 펌웨어 ★★★★★
- **Python** - 자동화, 테스트 도구 ★★★★☆
- **Assembly** - ARM Cortex-M ★★★☆☆

### MCU & 개발 도구
- **STM32 Series** (F4, F7, G0) ★★★★★
- **STM32CubeMX/IDE** ★★★★★
- **Renesas RA** (e2 studio) ★★★★☆
- **FreeRTOS** ★★★★☆

### 통신 프로토콜
- UART/RS232/RS485 ★★★★★
- SPI/I2C ★★★★★
- Ethernet/TCP/UDP (LwIP) ★★★★☆
- Modbus RTU/TCP ★★★★☆

### 회로 설계
- **OrCAD/Cadence** - 회로도 ★★★★★
- **PADS** - PCB 아트워크 ★★★★★
- 아날로그 회로 (Op-Amp, ADC) ★★★★☆
- 전원 설계 (SMPS, LDO) ★★★★☆

---

## GitHub
- Repository: github.com/gari210404/Portfolio_Professional
- 프로젝트별 회로도, PCB, 블록 다이어그램, 코드 샘플 포함

---

## 연락처
- Email: rakguard@gmail.com
- Phone: 010-3233-5365
