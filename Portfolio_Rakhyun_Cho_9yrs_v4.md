# 조락현 | Senior Embedded Engineer | 9년차

> **HW/FW Full-Stack 개발자**  
> STM32 기반 임베디드 시스템 개발 전문

---

## 📋 핵심 역량

- **임베디드 시스템**: STM32 (F1, F4, H7), ARM Cortex-M 기반 펌웨어 개발
- **하드웨어 설계**: Altium Designer 기반 회로 설계 및 PCB Layout
- **실시간 제어**: FreeRTOS, PID 제어, 모터 제어 (Stepper, BLDC)
- **광학 시스템**: UV/IR LED, Photo Diode Array, 레이저 광학계 인터페이스
- **통신 프로토콜**: UART, SPI, I2C, Ethernet (LwIP), USB

---

## 💧 Nu-2000 (Lux) - UV+IR 용액 농도 분석기

> **UV+IR 광학을 이용한 용액 농도 분석 장비**

### 프로젝트 개요
- **제품**: UV+IR(광학)를 이용한 용액 농도 분석 장비
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4, 168MHz)

### 시스템 블록 다이어그램
> 📊 [Nu-2000 블록 다이어그램 삽입]

### 핵심 기술
- UV/IR LED 광학 측정: 흡광도 기반 농도 분석
- A3977 스테핑 모터: 시린지 펌프 마이크로스텝 제어 (1/8 스텝)
- 다채널 ADC (AD7682): 16비트 고정밀 광센서 신호 측정
- Nextion HMI LCD: 터치스크린 UI
- Ethernet/USB 통신: PC 연동 및 데이터 전송

### 코드 샘플 - 스테핑 모터 제어

```c
// motor.c - A3977 스테핑 모터 드라이버 제어
// 시린지 펌프용 마이크로 스텝 정밀 제어

#define STEP_MOTOR_GPIO     GPIOI
#define PIN_STEP            GPIO_PIN_3   // 스텝 펄스
#define PIN_DIR             GPIO_PIN_4   // 방향 제어
#define PIN_ENABLE          GPIO_PIN_5   // 출력 활성화

/* 마이크로 스텝 모드 */
#define A3977_FULL_STEP     0   // 전체 스텝
#define A3977_HALF_STEP     1   // 1/2 스텝
#define A3977_QUARTER_STEP  2   // 1/4 스텝
#define A3977_EIGHTH_STEP   3   // 1/8 스텝

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

## 🧪 L-Titrator - 적정식 용액 농도 분석기

> **적정(Titration) 방식을 활용한 용액 농도 분석 장비**

### 프로젝트 개요
- **제품**: 적정 방식을 활용한 용액 농도 분석 장비
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [L-Titrator 블록 다이어그램 삽입]

### 핵심 기술
- 시린지 펌프 제어: BLDC/스테핑 모터 정밀 토출 제어
- pH/전도도 센서: 적정 종말점 검출
- 배터리 관리 시스템: 휴대용 기기 충방전 관리
- 저전력 설계: 현장 휴대용 최적화
- 터치스크린 UI: Nextion HMI LCD

---

## 🔬 Psi-1000/3000 - 정밀 가스 제어 시스템

> **진공 게이지 모니터링 기반 정밀 가스 제어 시스템**

### 프로젝트 개요
- **제품**: 정밀 가스 제어 시스템 (반도체/디스플레이 공정용)
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4, 168MHz)

### 시스템 블록 다이어그램
> 📊 [Psi 블록 다이어그램 삽입]

### 핵심 기술
- 진공 게이지 인터페이스: Pirani/Capacitance Gauge 연동
- 고속 PID 피드백 제어: 250ms 주기 압력 제어
- FreeRTOS 멀티태스킹: 압력제어, 센서, 통신 병렬 처리
- Ethernet (LwIP): TCP/UDP PC 제어 인터페이스
- PID Auto-Tuning: 최적 파라미터 자동 탐색

### 코드 샘플 - 가스 압력 PID 제어

```c
// PrsCtrl.c - 정밀 가스 압력 제어 알고리즘
// 진공 게이지 모니터링 + 고속 PID 피드백 제어

/* 압력 제어 변수 */
INTERNAL float32_t sglPrsCtrlFilteredPressureP1;  // 입력 압력 (torr)
INTERNAL float32_t sglPrsCtrlControlPeriod = 0.25f;  // 250ms 제어 주기

/* PID 압력 제어 */
void pid_pressure_compute(PID_STR *pPID) {
    float error = pPID->sp - pPID->pv;  // 목표압력 - 현재압력
    
    pPID->p_term = pPID->kp * error;           // 비례
    pPID->i_term += pPID->ki * error;          // 적분
    pPID->d_term = pPID->kd * (error - pPID->prev_error);  // 미분
    
    // 최종 출력 (밸브 PWM)
    pPID->co = pPID->p_term + pPID->i_term + pPID->d_term;
}
```

---

## 🔴 LPC - 레이저 파티클 분석기

> **레이저(광학)를 이용한 슬러리 파티클 분석 장비**

### 프로젝트 개요
- **제품**: 레이저 광학 기반 슬러리 파티클 카운터
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [LPC 블록 다이어그램 삽입]

### 핵심 기술
- 레이저 광학계: 산란광 검출 기반 파티클 계수
- 고속 ADC 샘플링: 실시간 파티클 신호 검출
- 신호 처리: 디지털 필터링 및 피크 검출
- 데이터 로깅: SD카드 측정 결과 저장

---

## 📊 SSC - Photo Diode Array 슬러리 분석기

> **Photo Diode Array를 사용한 광학식 슬러리 분석 장비**

### 프로젝트 개요
- **제품**: PDA(Photo Diode Array) 기반 광학식 슬러리 분석기
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [SSC 블록 다이어그램 삽입]

### 핵심 기술
- Photo Diode Array: 다채널 동시 광학 측정
- 분광 분석: 파장별 흡광도 측정
- 고속 데이터 수집: 멀티채널 ADC 동기화
- 실시간 분석: 슬러리 농도/입도 분석

---

## 🧪 MS (Aston) - 질량분석기 DRV Board

> **질량분석기 Drive Board - 펌프, 센서 등 장비 제어**

### 프로젝트 개요
- **제품**: 수질분석용 질량분석기 (Mass Spectrometer)
- **담당**: DRV Board (Drive Board) 회로 설계 + 펌웨어 개발
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [MS DRV Board 블록 다이어그램 삽입]

### DRV Board 핵심 기능
- MFC(Mass Flow Controller) 제어: 4-20mA 전류 루프
- 펌프 제어: 시료/시약 주입 펌프 구동
- 센서 인터페이스: 다채널 ADC 센서 신호 측정
- PID 온도 제어: 센서 히터/쿨러 제어
- SD카드 로깅: FATFS 데이터 저장

### 코드 샘플 - MFC 유량 제어

```c
// mfc.c - Mass Flow Controller 4-20mA 인터페이스
// DRV Board에서 펌프/센서 장비 제어

/* McMillan U803 MFC: 10~50 mL/min, 4-20mA */
void mfc_out_svc(void) {
    // 1. MFC 활성화 상태 확인
    if (bd.env.working[OUT_420_EN] & (0x01 << 2))
        mfc.onoff = 1;
    
    // 2. 목표 유량 (mL/min)
    mfc.out_ml = x2_float(bd.env.working[MASS_FLOW_SPEED]);
    
    // 3. 액체 보정 계수 적용
    mfc.liq_factor = x2_float(bd.env.working[MASS_FLOW_FACTOR]);
    mfc.out_ml_factor = mfc.out_ml * mfc.liq_factor;
    if (mfc.out_ml_factor > 50.0) mfc.out_ml_factor = 50.0;
    
    // 4. 유량 → 전류(mA) → DAC 변환
    mfc.out_cur = (mfc.out_ml_factor + 12.5) / 3.125;
    mfc.out_dac = (bd.env.working[CAL_420_OUT2_20m] - bd.env.working[CAL_420_OUT2_4m]) 
                  / 16 * mfc.out_cur;
}
```

---

## 🔧 ATIK JIG Board - 보드 입고 테스트 장비

> **보드 입고 테스트를 위한 자동화 테스트 장비**

### 프로젝트 개요
- **제품**: 생산라인 보드 입고 테스트용 JIG
- **역할**: 회로 설계 + 펌웨어 개발 (100%)
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [JIG Board 블록 다이어그램 삽입]

### 핵심 기술
- 다중 제품 지원: L-Titrator, Nu-2000, Sigma, Psi 등
- 자동화 테스트: ADC/DAC, 통신, GPIO 자동 검증
- 멀티 UART 핸들링: 타겟 보드 통신 테스트
- 릴레이/MUX 제어: 테스트 포인트 자동 선택
- 테스트 결과 리포트: PASS/FAIL 판정 및 로깅

### 코드 샘플 - 멀티 제품 테스트

```c
// ATIK_JIG_main.c - 보드 입고 테스트 시스템
// 다중 제품 보드 자동화 테스트 지원

const char hw_model_str[16][30] = {
    "1.L-Titrator",
    "2.Nu-2000",
    "3.Sigma-3000/4000",
    "4.Psi-3000",
    "5.Psi-1000",
    "15.ATIK_JIG"
};

void init_enable_ctrl(void) {
    // MUX 비활성화
    HAL_GPIO_WritePin(MUX_ENB_GPIO_Port, MUX_ENB_Pin, 0);
    
    // TC&RTD 릴레이 OFF
    HAL_GPIO_WritePin(TC_CTRL_ENB_GPIO_Port, TC_CTRL_ENB_Pin, 0);
    
    // 24V 출력 OFF
    HAL_GPIO_WritePin(OUT1_24V_ENB_GPIO_Port, OUT1_24V_ENB_Pin, 0);
}
```

---

## ⚗️ Sigma-1000/3000/4000 - COD 분석 시스템

> **COD/BOD/TOC 수질분석 전용 장비**

### 프로젝트 개요
- **제품**: COD(화학적 산소요구량) 자동분석 시스템
- **역할**: 회로 설계 + 펌웨어 개발
- **MCU**: STM32F407 (ARM Cortex-M4)

### 시스템 블록 다이어그램
> 📊 [Sigma 블록 다이어그램 삽입]

### 핵심 기술
- UV-IR LED 광학 측정: 흡광도 기반 농도 측정
- 다중 채널 시린지 펌프: 시약/샘플 자동 주입
- 반응조 온도 제어: PID 기반 정밀 온도 제어
- SD카드 데이터 로깅: 측정 결과 저장

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
