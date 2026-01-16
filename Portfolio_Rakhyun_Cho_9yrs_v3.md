# 조락현 | Senior Embedded Engineer | 9년차

> **HW/FW Full-Stack 개발자**  
> STM32 기반 임베디드 시스템 개발 전문

---

## 📋 핵심 역량

- **임베디드 시스템**: STM32, ARM Cortex-M 기반 펌웨어 개발
- **하드웨어 설계**: 회로 설계 (Altium Designer), PCB Layout
- **실시간 제어**: RTOS (FreeRTOS), PID 제어, 모터 제어
- **통신 프로토콜**: UART, SPI, I2C, Ethernet (LwIP), CAN
- **센서 인터페이스**: ADC (AD7682), DAC, RTD, Thermocouple

---

## 🔬 Psi-1000/3000 정밀 가스제어 시스템

> **진공 게이지로 진공 상태를 모니터링하며 고속 가스 압력 제어**

### 프로젝트 개요
- **제품**: 반도체/디스플레이 공정용 정밀 가스 제어 시스템
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4, 168MHz)

### 핵심 기술
- 진공 게이지(Vacuum Gauge) 인터페이스: Pirani/Capacitance Gauge 연동
- 고속 PID 피드백 제어: 250ms 주기로 압력 정밀 제어
- FreeRTOS 기반 멀티태스킹: 압력제어, 센서읽기, 통신 병렬 처리
- Ethernet (LwIP) TCP/UDP 통신: PC 제어 인터페이스
- PID Auto-Tuning: 최적 제어 파라미터 자동 탐색

### 코드 샘플 - 가스 압력 PID 제어

```c
// PrsCtrl.c - 정밀 가스 압력 제어 알고리즘
// 진공 게이지(P1)를 모니터링하며 고속 피드백 제어 수행

/* 압력 입력 변수 */
INTERNAL float32_t sglPrsCtrlFilteredPressureP1;  // 필터링된 입력 압력 P1 (torr)
INTERNAL float32_t sglPrsCtrlDifferentialPressureP1;  // 미분 압력 (torr/sec)

/* 제어 주기: 250ms로 고속 피드백 */
INTERNAL float32_t sglPrsCtrlControlPeriod = 0.25f;

/* PID 가스 압력 제어 */
void pid_htr_compute(PID_STR *pHTR) {
    float error = pHTR->sp - pHTR->pv;  // 목표압력 - 현재압력
    
    // P (비례) 제어
    pHTR->p_term = pHTR->kp * error;
    
    // I (적분) 제어 - 누적 오차 보정
    pHTR->i_term += pHTR->ki * error;
    if (pHTR->i_term > pHTR->i_max) pHTR->i_term = pHTR->i_max;
    
    // D (미분) 제어 - 급격한 변화 억제
    pHTR->d_term = pHTR->kd * (error - pHTR->prev_error);
    
    // 최종 출력 = PWM 듀티 사이클
    pHTR->co = pHTR->p_term + pHTR->i_term + pHTR->d_term;
}
```

---

## 🧪 MS 질량분석기 (Aston) - DRV Board

> **Drive Board 회로 설계 + 펌웨어 개발 담당**

### 프로젝트 개요
- **제품**: 수질분석용 질량분석기 (Mass Spectrometer)
- **담당 보드**: DRV Board (Drive Board) - 회로 설계 + 펌웨어 개발
- **MCU**: STM32F407 (ARM Cortex-M4)

### DRV Board 핵심 기능
- MFC(Mass Flow Controller) 제어: 4-20mA 전류 루프 인터페이스
- 다채널 ADC (AD7682): 16비트 고정밀 센서 신호 측정
- DAC 출력: 아날로그 제어 신호 생성
- PID 온도 제어: 센서 히터/쿨러 제어
- SD카드 데이터 로깅: FATFS 파일 시스템

### 코드 샘플 - MFC 유량 제어

```c
// mfc.c - Mass Flow Controller 4-20mA 인터페이스
// MS DRV Board에서 MFC를 통해 가스 유량을 정밀 제어

/*
 * McMillan U803 MFC 사양:
 * - 유량 범위: 10mL/min ~ 50mL/min
 * - 인터페이스: 4-20mA 전류 루프
 * 
 * 수식: Flow Rate = 3.125 × Current(mA) - 12.5
 */

void mfc_out_svc(void) {
    // 1. MFC 활성화 상태 확인
    if (bd.env.working[OUT_420_EN] & (0x01 << 2))
        mfc.onoff = 1;
    else
        mfc.onoff = 0;
    
    // 2. 목표 유량 계산 (mL/min)
    mfc.out_ml = x2_float(bd.env.working[MASS_FLOW_SPEED]);
    
    // 3. 액체 보정 계수 적용
    if (bd.env.working[MASS_FLOW_FACTOR] == 0)
        mfc.liq_factor = 1.7;  // 기본 DSP 액체 계수
    else
        mfc.liq_factor = x2_float(bd.env.working[MASS_FLOW_FACTOR]);
    
    mfc.out_ml_factor = mfc.out_ml * mfc.liq_factor;
    if (mfc.out_ml_factor > 50.0) mfc.out_ml_factor = 50.0;  // MFC 최대 한계
    
    // 4. 유량 → 전류(mA) 변환
    mfc.out_cur = (mfc.out_ml_factor + 12.5) / 3.125;
    
    // 5. 전류 → DAC 값 변환 (교정값 적용)
    mfc.out_dac = (bd.env.working[CAL_420_OUT2_20m] - bd.env.working[CAL_420_OUT2_4m]) 
                  / 16 * mfc.out_cur;
}
```

---

## 🔧 JIG Board (자동화 테스트 시스템)

> **다중 제품 품질 검증용 자동화 테스트 장비 개발**

### 프로젝트 개요
- **제품**: 생산라인 품질검증용 JIG (Test Fixture)
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 핵심 기술
- 다중 제품 지원: L-Titrator, Nu-2000, Sigma, Psi 시리즈 등
- 멀티 UART 핸들링: 여러 포트 동시 통신
- ADC/DAC 자동 테스트: 아날로그 회로 검증
- 릴레이/MUX 제어: 테스트 포인트 선택
- 상태 머신 기반 테스트 시퀀스: 자동화된 테스트 절차

### 코드 샘플 - 멀티 제품 테스트 시스템

```c
// ATIK_JIG_main.c - 다중 제품 자동화 테스트 시스템

/* 지원 제품 목록 */
const char hw_model_str[16][30] = {
    "1.L-Titrator",
    "2.Nu-2000",
    "3.Sigma-3000/4000",
    "4.Psi-3000",
    "5.Psi-1000",
    // ...
    "15.ATIK_JIG"
};

/* 초기화 제어 - 릴레이/MUX 제어 */
void init_enable_ctrl(void) {
    uint16_t wr_buf_16;
    
    wr_buf_16 = GPIOF->ODR;
    wr_buf_16 &= ~0xff;
    GPIOF->ODR = wr_buf_16;
    
    // MUX 비활성화
    HAL_GPIO_WritePin(MUX_ENB_GPIO_Port, MUX_ENB_Pin, 0);
    
    // TC&RTD 릴레이 OFF
    HAL_GPIO_WritePin(TC_CTRL_ENB_GPIO_Port, TC_CTRL_ENB_Pin, 0);
    HAL_GPIO_WritePin(TC_CTRL_CLK_GPIO_Port, TC_CTRL_CLK_Pin, 1);
    asm("nop"); asm("nop"); asm("nop");
    HAL_GPIO_WritePin(TC_CTRL_CLK_GPIO_Port, TC_CTRL_CLK_Pin, 0);
    
    // 24V 출력 OFF
    HAL_GPIO_WritePin(OUT1_24V_ENB_GPIO_Port, OUT1_24V_ENB_Pin, 0);
}
```

---

## 💧 Nu-2000 (Lux) 자동적정 시스템

> **수질분석용 자동적정장치 - 시린지 펌프 정밀 제어**

### 프로젝트 개요
- **제품**: 수질/식품 분석용 자동적정장치
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 핵심 기술
- A3977 스테핑 모터 드라이버: 마이크로스텝 제어 (1/8 스텝)
- 시린지 펌프 정밀 제어: 0.1μL 단위 토출량 제어
- 다채널 ADC: pH, 전도도, 온도 센서 동시 측정
- Nextion HMI LCD: 터치스크린 UI 구현
- Ethernet/USB 통신: PC 연동 및 데이터 전송

### 코드 샘플 - A3977 스테핑 모터 제어

```c
// motor.c - A3977 스테핑 모터 드라이버 제어
// 마이크로 스텝 모드로 정밀 위치 제어 구현

/* GPIO 핀 정의 - A3977 드라이버 인터페이스 */
#define STEP_MOTOR_GPIO     GPIOI
#define PIN_MODE2           GPIO_PIN_0   // 마이크로스텝 모드[2]
#define PIN_MODE1           GPIO_PIN_1   // 마이크로스텝 모드[1]
#define PIN_MODE0           GPIO_PIN_2   // 마이크로스텝 모드[0]
#define PIN_STEP            GPIO_PIN_3   // 스텝 펄스
#define PIN_DIR             GPIO_PIN_4   // 방향 제어
#define PIN_ENABLE          GPIO_PIN_5   // 출력 활성화

/* 마이크로 스텝 모드 */
#define A3977_FULL_STEP     0   // 전체 스텝
#define A3977_HALF_STEP     1   // 1/2 스텝
#define A3977_QUARTER_STEP  2   // 1/4 스텝
#define A3977_EIGHTH_STEP   3   // 1/8 스텝

/* A3977 초기화 */
void init_A3977() {
    A3977_Reset();
    A3977_Output_Disable();
    A3977_Sleep_Disable();
    
    A3977_Set_Step(micro_step);      // 마이크로 스텝 모드 설정
    A3977_Set_Direction(motor_dir);  // 방향 설정
    A3977_Set_SR(A3977_SR_ACTIVE);   // Slew Rate 활성화
    
    A3977_Step_Off();
    A3977_Output_Enable();
}
```

---

## 🧪 L-Titrator 자동적정 시스템

> **휴대용 현장 수질분석 자동적정장치**

### 프로젝트 개요
- **제품**: 현장용 휴대형 자동적정장치
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 핵심 기술
- 시린지 펌프 제어: BLDC/스테핑 모터 정밀 제어
- 배터리 관리 시스템: 충전/방전 상태 모니터링
- 저전력 설계: 휴대용 기기 최적화
- 터치스크린 UI: Nextion HMI LCD

---

## ⚗️ Sigma-1000/3000/4000 분석 시스템

> **COD/BOD/TOC 수질분석 전용 장비**

### 프로젝트 개요
- **제품**: COD(화학적 산소요구량) 자동분석 시스템
- **역할**: 회로 설계 + 펌웨어 개발
- **MCU**: STM32F407 (ARM Cortex-M4)

### 핵심 기술
- UV-IR LED 광학 측정: 흡광도 기반 농도 측정
- 다중 채널 시린지 펌프: 시약/샘플 자동 주입
- 온도 제어: 반응조 PID 온도 제어
- SD카드 데이터 로깅: 측정 결과 저장

---

## 🌡️ SSC 항온조 온도제어 시스템

> **고정밀 항온조 PID 온도제어 시스템**

### 프로젝트 개요
- **제품**: 실험용 고정밀 항온조 (±0.01°C)
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 핵심 기술
- RTD/Thermocouple 온도 센서: 고정밀 온도 측정
- PID 온도 제어: 히터/쿨러 PWM 제어
- PID Auto-Tuning: Ziegler-Nichols 방식 자동 튜닝
- Ethernet 통신: 원격 모니터링 및 제어

---

## 🛠️ 기술 스택

### 프로그래밍 언어
- C/C++ (Embedded), Python, Verilog

### MCU/프로세서
- STM32 시리즈 (F1, F4, H7), Renesas RA6M4
- Xilinx Zynq (FPGA + ARM)

### 개발 도구
- **IDE**: STM32CubeIDE, VS Code, Keil
- **EDA**: Altium Designer (회로설계/PCB)
- **FPGA**: Vivado, Vitis
- **버전관리**: Git, GitHub

---

## 📞 연락처

- 📧 **Email**: gari210@naver.com
- 🐙 **GitHub**: github.com/gari210404

---

*Thank you for reviewing my portfolio!*
