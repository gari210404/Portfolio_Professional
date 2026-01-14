# 조락현 (Rakhyun Cho)
## Senior Embedded Systems Engineer (Hardware & Firmware)

**Email:** 92lock@kakao.com | **Tel:** 010-7311-0402 | **GitHub:** github.com/gari210404 | **Location:** Republic of Korea

---

## 📋 Executive Summary

**9년 경력의 시니어 임베디드 시스템 엔지니어**로, **하드웨어 설계부터 펌웨어 개발까지 Full-Stack Embedded 개발** 전문가입니다. 반도체 공정 장비, 광학 분석 기기, 산업용 제어 시스템의 설계 및 개발에서 검증된 실적을 보유하고 있습니다.

**핵심 강점:**
- 10+ 양산 제품 개발 완료 (Hardware + Firmware)
- STM32 MCU Expert (F1/F4/F7/H7 시리즈)
- FreeRTOS 기반 실시간 시스템 설계
- PID 제어 알고리즘 및 Auto-tuning
- Modbus RTU/ASCII, TCP/IP 산업용 통신
- Hardware-Firmware Co-design 최적화

---

## 💼 Core Competencies

### Technical Expertise
```
Firmware Development   ████████████████████ 95%  (9 years)
STM32 MCU              ████████████████████ 95%  (9 years)
Analog/Digital Circuit ███████████████████  90%  (9 years)
RTOS (FreeRTOS)        ██████████████████   85%  (7 years)
PCB Layout             █████████████████    80%  (9 years)
Control Algorithm      ██████████████████   85%  (6 years)
```

### 개발 영역
| 분야 | 세부 기술 | 프로젝트 수 |
|------|-----------|-------------|
| **Firmware** | STM32, FreeRTOS, HAL/LL Driver, Bootloader | 12+ |
| **Hardware** | Mixed-signal, Sensor Interface, Power Supply | 10+ |
| **Communication** | Modbus RTU/ASCII, TCP/IP, UART, SPI, I2C, CAN | 15+ |
| **Control** | PID, Auto-tuning, State Machine, Kalman Filter | 8+ |
| **HMI** | Nextion, TouchGFX, UART Protocol | 10+ |
| **PCB** | Altium Designer, 4-6 Layer, DFM | 10+ |

---

## 🎯 Major Projects Portfolio

### 1. **L-LPC (H-Sensor) System** ⭐ 대표 프로젝트
**Period:** 2022-2024 | **Scale:** 17.5GB, 2,597 files | **Status:** Production

반도체 저압 챔버 제어 시스템 - **Hardware & Firmware Full-Stack 개발**

**시스템 블록 다이어그램:**
```
[H_sensor System Architecture]

┌─────────────────────────────────────────────────────────────────┐
│                    H-Sensor Control System                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  [STM32H743 MCU] ─────────────────────────────────────────────┐│
│       │                                                        ││
│       ├──→ [FPGA Interface] ←─→ [Xilinx Artix-7]              ││
│       │         │                                              ││
│       │         ├── High-speed ADC Control                     ││
│       │         ├── Digital Signal Processing                  ││
│       │         └── Real-time Data Streaming                   ││
│       │                                                        ││
│       ├──→ [Analog Frontend] ─── [Pressure Sensor Array]       ││
│       │         │                                              ││
│       │         ├── TIA (Trans-Impedance Amplifier)            ││
│       │         ├── Variable Gain Amplifier                    ││
│       │         └── Anti-aliasing Filter                       ││
│       │                                                        ││
│       ├──→ [Power Management]                                  ││
│       │         ├── 24V → ±15V, ±5V, 3.3V, 1.8V               ││
│       │         └── Power Sequencing                           ││
│       │                                                        ││
│       └──→ [Communication]                                     ││
│               ├── Ethernet (TCP/IP, UDP)                       ││
│               ├── RS-485 (Modbus RTU)                          ││
│               └── SPI/I2C (Sensor Bus)                         ││
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

※ 블록 다이어그램: H_sensor_Block_Diagram(analog_frontend).pptx
※ FPGA 아키텍처: H_sensor_Block_Diagram(FPGA)_230914.pptx
```

**하드웨어 설계:**
- **Main Board**: STM32H743 기반 (480MHz, 2MB Flash, 1MB RAM)
- **Analog Frontend**: 고정밀 TIA (Gain: 1M/10M/100MΩ, S/N > 60dB)
- **FPGA Interface**: Xilinx Artix-7 데이터 처리 연동
- **Power**: Multi-rail SMPS (효율 > 90%, Ripple < 30mVpp)

**펌웨어 아키텍처:**
```c
/* FreeRTOS Task Structure */
┌─────────────────────────────────────────────────────────────────┐
│  FreeRTOS Tasks (Priority: 1-7)                                 │
├─────────────────────────────────────────────────────────────────┤
│  Main_Task      │ Priority: 7  │ Stack: 2KB │ Core Processing   │
│  ADC_Task       │ Priority: 6  │ Stack: 1KB │ Data Acquisition  │
│  FPGA_Task      │ Priority: 5  │ Stack: 1KB │ FPGA Communication│
│  TCP_Task       │ Priority: 4  │ Stack: 2KB │ Ethernet Handler  │
│  UDP_Task       │ Priority: 4  │ Stack: 2KB │ UDP Data Stream   │
│  Term_Task      │ Priority: 3  │ Stack: 1KB │ Debug Console     │
│  SD_Task        │ Priority: 2  │ Stack: 1KB │ Data Logging      │
└─────────────────────────────────────────────────────────────────┘

/* IPC (Inter-Process Communication) */
├── Queue: ADC_DataQueue (1000 samples, DMA double buffer)
├── Queue: UART_TxQueue (512 bytes)
├── Mutex: SPI_Mutex, I2C_Mutex
├── Semaphore: ADC_Complete_Sem
└── EventGroup: System_Status_Flags
```

**주요 펌웨어 코드 (main.c 요약):**
```c
// H-Sensor Main Task Implementation
void Main_Task(void *argument) {
    // Initialization
    HAL_Init();
    SystemClock_Config();  // 480MHz SYSCLK
    
    // Peripheral Init
    MX_ADC1_Init();        // 16-bit ADC @ 2MSPS
    MX_SPI1_Init();        // FPGA Interface @ 50MHz
    MX_LWIP_Init();        // Ethernet TCP/IP Stack
    
    while(1) {
        // 1. Sensor Data Acquisition
        ADC_StartDMA(&hadc1, adc_buffer, ADC_BUFFER_SIZE);
        
        // 2. FPGA Data Processing
        FPGA_SendCommand(FPGA_CMD_START_ACQUISITION);
        FPGA_ReadData(fpga_data, FPGA_DATA_SIZE);
        
        // 3. Digital Signal Processing
        DSP_ApplyFilter(adc_buffer, filtered_data);
        DSP_CalculateRMS(filtered_data, &rms_value);
        
        // 4. PID Control Update
        PID_Update(&pid_controller, setpoint, rms_value);
        DAC_SetOutput(pid_controller.output);
        
        // 5. Communication
        if (tcp_connected) {
            TCP_SendData(measurement_packet);
        }
        
        osDelay(1);  // 1kHz loop rate
    }
}
```

**디버깅 경험:**
- **문제 1**: ADC 노이즈 이슈 (±500mV 스파이크)
  - **원인 분석**: 디지털 신호 간섭 (SPI 클럭 → ADC 입력)
  - **해결책**: PCB 리레이아웃, 가드링 추가, 샘플링 타이밍 조정
  - **결과**: 노이즈 ±5mV로 100배 개선

- **문제 2**: FreeRTOS 데드락 발생
  - **원인 분석**: SPI Mutex 순환 대기
  - **해결책**: Mutex 획득 순서 통일, Timeout 추가
  - **결과**: 시스템 안정성 100% 달성

**성과:**
- 개발 기간: 18개월 (Hardware 6개월 + Firmware 12개월)
- 양산 수량: 100+ units
- 필드 불량률: < 0.2%

**첨부 파일:**
```
📁 Project_Files\02_L-LPC\
   ├── PCB\ (3개 .pcb 파일)
   │   ├── LPC_PD_POWER(rev_0.1)_221026.pcb
   │   ├── ATS9114_P_L_L_MAIN_V0_1.pcb (메인보드)
   │   └── ATS8754_P_H-SENSOR_MAIN_BOARD_REV1_0-230508.pcb (센서보드)
   ├── PDF\ (13개 PDF 파일)
   │   ├── 회로도 PDF 11개
   │   ├── H_sensor__Block_Diagram(analog_frontend).pptx ⭐
   │   └── H_sensor_Block_Diagram(FPGA)_230914.pptx ⭐
   └── Images\ (14개 PNG 이미지)
       ├── H_sensor_Analog_Frontend_Slide1~5.png (Analog 설계)
       └── H_sensor_FPGA_Slide1~9.png (FPGA 아키텍처)
```

---

### 2. **Psi-1000/3000 Pressure Controller** ⭐ PID 제어 전문
**Period:** 2019-2023 | **Scale:** 3.0GB, 399 files | **Production:** 50+ units

정밀 진공 압력 제어 시스템 - **PID 알고리즘 개발 및 최적화**

**시스템 블록 다이어그램:**
```
[Psi-1000 Control System Architecture]

┌────────────────────────────────────────────────────────────────┐
│              Psi-1000 Pressure Control System                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  [STM32F407IGT6 MCU] ──────────────────────────────────────┐  │
│       │                                                     │  │
│       ├──→ [Pressure Sensor Interface]                     │  │
│       │      │                                              │  │
│       │      ├── MKS Baratron (0-10V)                      │  │
│       │      ├── ADS1115 16-bit ADC (I2C)                  │  │
│       │      └── 2nd-order LPF (fc=10Hz)                   │  │
│       │                                                     │  │
│       ├──→ [PID Controller]                                │  │
│       │      │                                              │  │
│       │      ├── Kp, Ki, Kd Auto-tuning                    │  │
│       │      ├── Anti-windup                               │  │
│       │      └── Derivative Filter (N=100)                 │  │
│       │            ↓                                        │  │
│       │      [LTC2630 12-bit DAC] → [V/I Converter]        │  │
│       │                                   ↓                 │  │
│       │                              [MFC 0-20mA Output]    │  │
│       │                                                     │  │
│       ├──→ [Heater Control]                                │  │
│       │      ├── SSR Driver (500W max)                     │  │
│       │      └── ACS712 Current Sensing                    │  │
│       │                                                     │  │
│       ├──→ [Communication]                                 │  │
│       │      ├── RS-485 (Modbus RTU/ASCII)                 │  │
│       │      ├── Ethernet (Modbus TCP)                     │  │
│       │      └── USB (Debug Console)                       │  │
│       │                                                     │  │
│       └──→ [HMI Interface]                                 │  │
│              └── Nextion Display (UART)                    │  │
│                                                            │  │
└────────────────────────────────────────────────────────────────┘

※ 블록 다이어그램: Psi-3000 Board System Block Diagram.pptx (1.2MB)
```

**PID 제어 알고리즘 구현:**
```c
/* PID Controller Implementation (main.c에서 발췌) */

// PID 구조체 정의
typedef struct {
    float Kp, Ki, Kd;           // PID Gains
    float Ti, Td;               // Integral/Derivative Time Constants
    float N;                    // Derivative Filter Coefficient
    float integral;             // Integral Accumulator
    float prev_error;           // Previous Error
    float prev_derivative;      // Previous Derivative (filtered)
    float output_min, output_max;  // Output Limits
    float integral_max;         // Anti-windup Limit
} PID_Controller_t;

// PID 업데이트 함수
float PID_Update(PID_Controller_t* pid, float setpoint, float measurement) {
    float error = setpoint - measurement;
    float dt = 0.001f;  // 1ms sampling time
    
    // Proportional Term
    float P = pid->Kp * error;
    
    // Integral Term with Anti-windup
    pid->integral += (pid->Ki * dt) * error;
    if (pid->integral > pid->integral_max) 
        pid->integral = pid->integral_max;
    if (pid->integral < -pid->integral_max) 
        pid->integral = -pid->integral_max;
    float I = pid->integral;
    
    // Derivative Term with Low-pass Filter
    float derivative = (error - pid->prev_error) / dt;
    float alpha = dt / (dt + 1.0f / (pid->N * pid->Kd / pid->Kp));
    pid->prev_derivative = alpha * derivative + (1 - alpha) * pid->prev_derivative;
    float D = pid->Kd * pid->prev_derivative;
    
    // Output with Saturation
    float output = P + I + D;
    if (output > pid->output_max) output = pid->output_max;
    if (output < pid->output_min) output = pid->output_min;
    
    pid->prev_error = error;
    return output;
}

// Auto-tuning (Relay Feedback Method)
void PID_AutoTune(PID_Controller_t* pid, float setpoint) {
    float relay_amplitude = 10.0f;  // ±10% output
    float oscillation_period, oscillation_amplitude;
    
    // Step 1: Relay Feedback Test
    for (int i = 0; i < AUTO_TUNE_CYCLES; i++) {
        if (measurement > setpoint) {
            DAC_SetOutput(setpoint - relay_amplitude);
        } else {
            DAC_SetOutput(setpoint + relay_amplitude);
        }
        osDelay(10);
    }
    
    // Step 2: Calculate Ultimate Gain & Period
    float Ku = (4 * relay_amplitude) / (PI * oscillation_amplitude);
    float Tu = oscillation_period;
    
    // Step 3: Ziegler-Nichols Tuning
    pid->Kp = 0.6f * Ku;
    pid->Ki = 1.2f * Ku / Tu;
    pid->Kd = 0.075f * Ku * Tu;
}
```

**FreeRTOS Task 구성 (main.c):**
```c
/* Psi-1000 Task Structure */
osThreadId_t Main_TaskHandle;     // Priority: High, Stack: 2KB
osThreadId_t Term_TaskHandle;     // Priority: Normal, Stack: 2KB
osThreadId_t TCP_TaskHandle;      // Priority: Normal, Stack: 2KB
osThreadId_t UDP_TaskHandle;      // Priority: High, Stack: 2KB

// Main Task - PID Control Loop
void Main_Task(void *argument) {
    // Initialize PID Controllers
    PID_Init(&pPID_HTR, 2.5f, 0.1f, 0.5f);   // Heater PID
    PID_Init(&pPID_ALD, 1.0f, 0.05f, 0.2f);  // Pressure PID
    
    while(1) {
        // Read Sensors
        float pressure = ADC_ReadPressure(&hadc1);
        float temperature = RTD_ReadTemperature(&hi2c3);
        
        // PID Control
        float heater_output = PID_Update(&pPID_HTR, temp_setpoint, temperature);
        float valve_output = PID_Update(&pPID_ALD, prs_setpoint, pressure);
        
        // Output
        PWM_SetDuty(&htim10, heater_output);
        DAC_SetOutput(&hdac, valve_output);
        
        // Watchdog
        HAL_IWDG_Refresh(&hiwdg);
        
        osDelay(1);  // 1kHz control loop
    }
}
```

**디버깅 경험:**
- **문제**: PID 오버슈트 40% 발생
  - **원인 분석**: Derivative kick (setpoint 급변 시)
  - **해결책**: Derivative-on-measurement 방식 적용
  - **결과**: 오버슈트 5% 이내로 개선

- **문제**: Modbus 통신 간헐적 실패
  - **원인 분석**: RS-485 Transceiver 방향 전환 타이밍
  - **해결책**: DE/RE 신호 타이밍 조정 (100µs delay 추가)
  - **결과**: 통신 성공률 100% 달성

**성과:**
- ±0.1% 압력 제어 정확도 달성
- < 2초 정착 시간 (Step Response)
- 동아대학교 연구 협력 (PID 알고리즘 공동 개발)

**첨부 파일:**
```
📁 Project_Files\03_Psi-1000\
   ├── PDF\ (PPT 파일)
   │   ├── Psi-3000 Board System Block Diagram.pptx (1.2MB)
   │   └── Psi-1000_Rev0.2_수정사항.pptx (1.6MB)
   └── Images\ (6개 PNG 이미지)
       ├── Psi-3000_Board_System_Block_Diagram_Slide1~2.png
       └── Psi-1000_Rev0.2_수정사항_Slide1~4.png

📁 Code_Samples\
   └── Psi-1000_main.c (1,552 lines, PID 제어 로직)
```

---

### 3. **Nu-2000 (OAS-DSP) Optical Analysis System**
**Period:** 2021-2022 | **Scale:** 387MB, 447 files | **Status:** Production

광학 흡수 분광 시스템 - **Multi-channel 펌웨어 개발**

**시스템 블록 다이어그램:**
```
[Nu-2000 System Architecture]

┌────────────────────────────────────────────────────────────────┐
│               Nu-2000 Optical Analysis System                   │
├────────────────────────────────────────────────────────────────┤
│                                                                │
│  [STM32F407 MCU] ──────────────────────────────────────────┐  │
│       │                                                     │  │
│       ├──→ [LED Driver (4ch)]                              │  │
│       │      │                                              │  │
│       │      ├── UV LED: 254nm, 280nm                      │  │
│       │      ├── IR LED: 1450nm, 1650nm                    │  │
│       │      ├── PWM Control (10kHz)                       │  │
│       │      └── Current Monitor (INA139)                  │  │
│       │                        ↓                            │  │
│       │                   [Sample Cell]                     │  │
│       │                        ↓                            │  │
│       ├──→ [Photodiode TIA (4ch)]                          │  │
│       │      │                                              │  │
│       │      ├── OPA140 TIA (1M/10M/100MΩ)                 │  │
│       │      ├── AD7682 16-bit ADC @ 250kSPS               │  │
│       │      └── DMA Circular Buffer                       │  │
│       │                                                     │  │
│       ├──→ [Temperature Control]                           │  │
│       │      ├── PT100 RTD (MCP3427 18-bit ADC)           │  │
│       │      ├── PID Heater Control                        │  │
│       │      └── ±0.05°C Accuracy                          │  │
│       │                                                     │  │
│       └──→ [Communication]                                 │  │
│              ├── RS-485 (Modbus RTU)                       │  │
│              └── USB CDC (Debug/Update)                    │  │
│                                                            │  │
└────────────────────────────────────────────────────────────────┘
```

**FreeRTOS 멀티태스크 구조:**
```c
/* Nu-2000 Task Architecture */
FreeRTOS Tasks (5개 task, priority 1-5)
├── Task1: LED_DriverTask (Priority: 5, Period: 100ms)
│   - 4채널 LED PWM 제어
│   - 전류 모니터링 및 피드백
│   - 열 보상 알고리즘
│
├── Task2: ADC_AcquisitionTask (Priority: 4, Period: 50ms)
│   - 4채널 Photodiode 데이터 수집
│   - DMA 기반 고속 샘플링 (250kSPS)
│   - Moving average filter (8-tap)
│
├── Task3: TempControlTask (Priority: 3, Period: 1s)
│   - RTD 온도 측정 (18-bit)
│   - PID 히터 제어
│   - 광학 안정성 보장
│
├── Task4: CommHandlerTask (Priority: 2, Event-driven)
│   - Modbus RTU/ASCII 처리
│   - USB CDC 명령 처리
│   - Register Read/Write
│
└── Task5: DataProcessTask (Priority: 1, Event-driven)
    - Signal processing (FFT, Filter)
    - Calibration 계산
    - 결과 저장

/* Queue & Semaphore */
├── ADC_DataQueue (100 sample depth)
├── UART_TxQueue (512 bytes)
├── I2C_Mutex (공유 버스 보호)
└── EventGroup (시스템 상태 플래그)
```

**광학 신호 처리 코드:**
```c
/* Photodiode Signal Processing */
void ADC_AcquisitionTask(void *argument) {
    uint16_t adc_raw[4];
    float absorbance[4];
    
    while(1) {
        // DMA 기반 ADC 읽기 (4채널 동시)
        HAL_ADC_Start_DMA(&hadc1, adc_buffer, 4);
        xSemaphoreTake(ADC_Complete_Sem, portMAX_DELAY);
        
        // Moving Average Filter
        for (int ch = 0; ch < 4; ch++) {
            adc_filtered[ch] = MovingAverage_Update(&ma_filter[ch], adc_raw[ch]);
        }
        
        // Absorbance Calculation (Beer-Lambert Law)
        // A = -log10(I/I0)
        for (int ch = 0; ch < 4; ch++) {
            float intensity = (float)adc_filtered[ch] / 65535.0f;
            float reference = calibration_data[ch].I0;
            absorbance[ch] = -log10f(intensity / reference);
        }
        
        // Queue로 결과 전송
        xQueueSend(DataQueue, &absorbance, 0);
        
        osDelay(50);  // 20Hz 샘플링
    }
}
```

**IAP Bootloader 개발:**
```c
/* IAP (In-Application Programming) Bootloader */

// Bootloader 진입 조건 체크
void Bootloader_CheckEntry(void) {
    // 1. Button 체크 (부팅 시 버튼 3초 이상 누름)
    if (HAL_GPIO_ReadPin(BOOT_BTN_GPIO_Port, BOOT_BTN_Pin) == GPIO_PIN_RESET) {
        HAL_Delay(3000);
        if (HAL_GPIO_ReadPin(BOOT_BTN_GPIO_Port, BOOT_BTN_Pin) == GPIO_PIN_RESET) {
            goto_bootloader = 1;
        }
    }
    
    // 2. Flash Flag 체크 (펌웨어 업데이트 요청)
    if (*(uint32_t*)BOOT_FLAG_ADDR == BOOT_FLAG_VALUE) {
        goto_bootloader = 1;
    }
    
    // 3. Application 유효성 체크
    uint32_t app_stack_pointer = *(uint32_t*)APP_START_ADDR;
    if (app_stack_pointer < SRAM_START || app_stack_pointer > SRAM_END) {
        goto_bootloader = 1;  // Invalid application
    }
}

// UART 기반 펌웨어 업데이트
void Bootloader_UART_Update(void) {
    uint8_t packet[256];
    uint32_t flash_addr = APP_START_ADDR;
    
    // 1. Handshake
    UART_SendString("BOOT_READY\r\n");
    
    // 2. Receive & Flash
    while(1) {
        // Packet 수신 (Header + Data + CRC32)
        UART_ReceivePacket(packet, &packet_len);
        
        // CRC32 검증
        if (CRC32_Verify(packet, packet_len) != CRC_OK) {
            UART_SendString("CRC_ERROR\r\n");
            continue;
        }
        
        // Flash 프로그래밍
        HAL_FLASH_Unlock();
        for (int i = 0; i < packet_len - 4; i += 4) {
            HAL_FLASH_Program(FLASH_TYPEPROGRAM_WORD, flash_addr, *(uint32_t*)(packet + i));
            flash_addr += 4;
        }
        HAL_FLASH_Lock();
        
        UART_SendString("ACK\r\n");
        
        // End of File 체크
        if (packet[0] == EOF_MARKER) break;
    }
    
    // 3. Application으로 점프
    JumpToApplication(APP_START_ADDR);
}
```

**첨부 파일:**
```
📁 Project_Files\04_Nu-2000\
   ├── Schematics\ (2개 .sch 파일)
   │   ├── ATIK_LED_Board_rev01_220517.sch
   │   └── ATIK_PD_Board_rev01_240203.sch
   ├── PDF\ (11개 PDF/PPT 파일)
   │   ├── Total_Board_ATIK_V1.2.pdf
   │   ├── Nu-2000_Main_Block_Diagram.pptx
   │   ├── PD_AMP_V2.0.pdf
   │   └── LED/PD 상세 회로도
   └── Images\ (3개 PNG 이미지)
       └── Nu-2000_Main_Block_Diagram_Slide1~3.png
```

---

### 4. **MS (Mass Spectrometer) System** ⭐ 최신 프로젝트
**Period:** 2024-2025 | **Scale:** 1,140MB, 345 files | **Status:** Development

반도체 공정 가스 분석 Mass Spectrometer - **시스템 펌웨어 개발**

**시스템 구성:**
```
[MS System Architecture]

┌─────────────────────────────────────────────────────────────┐
│                MS (Mass Spectrometer) System                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Host PC] ←─ USB 3.0/Ethernet ─→ [Main Control Board]     │
│                                      │                      │
│                                      ├─→ [RF Board (RFDB)]  │
│                                      │   - RF Generator     │
│                                      │   - Matching Network │
│                                      │   - Quadrupole Drive │
│                                      │                      │
│                                      ├─→ [Ion Detector]     │
│                                      │   - Electron Mult.   │
│                                      │   - High-voltage PS  │
│                                      │   - Signal Amp       │
│                                      │                      │
│                                      └─→ [Data Acq. (DRB)]  │
│                                          - 18-bit ADC       │
│                                          - FPGA Processing  │
│                                          - Real-time DSP    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**펌웨어 역할:**
- 시스템 통합 및 디버깅
- 데이터 수집 펌웨어 개발
- RF 제어 인터페이스
- 통신 프로토콜 구현

**첨부 파일:**
```
📁 Project_Files\01_MS_Mass_Spectrometer\
   ├── Schematics\ (1개 .sch 파일)
   ├── PCB\ (4개 .pcb 파일)
   ├── PDF\ (2개 파일)
   │   ├── ASTON_block_diagram(250814).pptx
   │   └── MS_Blockdiagram.pdf
   └── Images\ (11개 PNG 이미지)
       └── ASTON_block_diagram_Slide1~11.png
```

---

### 5. **LE_Laser (Mantis SSC) Sensor System** ⭐ 최신 프로젝트
**Period:** 2025 | **Scale:** 35MB, 32 files | **Status:** Development

레이저 기반 정밀 센서 시스템

**시스템 구성:**
```
[LE_Laser System Architecture]

┌────────────────────────────────────────────────────────────┐
│              LE_Laser (Mantis SSC) System                   │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  [STM32G071RB MCU] ────────────────────────────────────┐  │
│       │                                                 │  │
│       ├──→ [Sensor Board]                              │  │
│       │      ├── Chipsense130 Pressure Sensor          │  │
│       │      ├── SHT3X Temp/Humidity (I2C)             │  │
│       │      └── MCP3550 22-bit ADC (SPI)              │  │
│       │                                                 │  │
│       ├──→ [Laser Module Interface]                    │  │
│       │      ├── Laser Driver Control                  │  │
│       │      └── Safety Interlock                      │  │
│       │                                                 │  │
│       └──→ [Communication]                             │  │
│              ├── USB Type-C (CDC)                      │  │
│              └── I2C/SPI (Sensor Bus)                  │  │
│                                                        │  │
└────────────────────────────────────────────────────────────┘
```

**설계 특징:**
- Compact 2-board design (Main + Sensor)
- STM32G0 시리즈 (최신 Cortex-M0+)
- 22-bit ADC로 고분해능 측정
- Low-power operation (< 100mA)

**첨부 파일:**
```
📁 Project_Files\08_LE_Laser\
   ├── Schematics\ (2개 .sch 파일)
   │   ├── ATiK_SSC_main_v0.1_20250429_modify.sch
   │   └── ATiK_SSC_v0.1_250316F_sensorBD.sch
   └── PCB\ (2개 .pcb 파일)
       ├── ATiK_SSC_main_v0.1_20250429_modify.pcb
       └── ATiK_SSC_V0.1_250316F_sensorBD.pcb
```

---

### 6. **Sigma-1000 LPC Simulator**
**Period:** 2020-2021 | **Scale:** 50+ units | **Status:** Production

플라즈마 교정 시뮬레이터 - **16채널 DAC 제어 펌웨어**

**펌웨어 구조:**
```c
/* Sigma-1000 Firmware Architecture */

Application Layer
├── Calibration Engine (Multi-point, Polynomial fitting)
├── Communication Handler (Modbus RTU/ASCII)
├── Data Logging (SD Card, FatFS)
└── User Interface (Nextion HMI)

Driver Layer
├── DAC Driver (MCP4728 I2C, 16채널)
├── ADC Driver (Internal 12-bit)
├── UART Driver (RS-232/485)
└── SD Card Driver (SDIO + FatFS)

HAL Layer
└── STM32 HAL + Custom Optimization
```

**주요 기능:**
- 16채널 DAC 1ms 업데이트
- I2C 400kHz 통신
- ±0.01% FSR 전압 정확도
- SD 카드 데이터 로깅

---

### 7. **추가 프로젝트 요약**

| 프로젝트 | 기간 | 역할 | 주요 내용 | 첨부 파일 |
|----------|------|------|-----------|-----------|
| **L-Titrator** | 2018-2020 | FW Lead | pH 측정, 스테퍼 제어, USB 통신 | 1 SCH, 2 PCB, 3 Images |
| **Lux (Optical)** | 2023-2024 | HW+FW | 광학 센서, PD/LD 설계 | 3 SCH, 3 PCB, 18 Images |
| **ATIK JIG** | 2022 | FW Lead | 테스트 지그, 자동화 | 1 SCH, 6 PCB, 5 Images |
| **IAP Bootloader** | 2019-현재 | Developer | UART/USB 펌웨어 업데이트 | 코드 샘플 |

---

## 🛠️ Technical Skills

### Firmware Development
```
STM32 MCU              ⭐⭐⭐⭐⭐ Expert     9년
FreeRTOS               ⭐⭐⭐⭐⭐ Expert     7년
C/C++ Programming      ⭐⭐⭐⭐⭐ Expert     9년
HAL/LL Driver          ⭐⭐⭐⭐⭐ Expert     9년
Bootloader (IAP)       ⭐⭐⭐⭐  Advanced   6년
USB (CDC/HID)          ⭐⭐⭐⭐  Advanced   5년
```

### Communication Protocols
```
Modbus RTU/ASCII       ⭐⭐⭐⭐⭐ Expert     8년
UART/SPI/I2C           ⭐⭐⭐⭐⭐ Expert     9년
TCP/IP (lwIP)          ⭐⭐⭐⭐  Advanced   5년
CAN Bus                ⭐⭐⭐   Intermediate 3년
```

### Hardware Design
```
Analog Circuit Design  ⭐⭐⭐⭐  Advanced   9년
PCB Layout (Altium)    ⭐⭐⭐⭐  Advanced   9년
Power Supply Design    ⭐⭐⭐⭐  Advanced   7년
Signal Integrity       ⭐⭐⭐   Intermediate 5년
```

### Control Systems
```
PID Algorithm          ⭐⭐⭐⭐⭐ Expert     6년
Auto-tuning            ⭐⭐⭐⭐  Advanced   4년
Kalman Filter          ⭐⭐⭐   Intermediate 3년
State Machine          ⭐⭐⭐⭐⭐ Expert     8년
```

### Development Tools
| Tool | Proficiency | Usage |
|------|-------------|-------|
| STM32CubeIDE | Expert | Primary IDE |
| Keil µVision | Advanced | Legacy projects |
| Altium Designer | Advanced | PCB design |
| Git/GitHub | Expert | Version control |
| Logic Analyzer | Expert | Debugging |
| Oscilloscope | Expert | Signal analysis |

---

## 📊 Firmware Development Methodology

### 1. 아키텍처 설계
```
┌─────────────────────────────────────────────────────────────┐
│                    Firmware Architecture                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Application Layer]                                        │
│    ├── Main Application Logic                               │
│    ├── State Machine                                        │
│    └── User Interface                                       │
│                                                             │
│  [Service Layer]                                            │
│    ├── Communication Service (Modbus, TCP/IP)               │
│    ├── Data Logger Service                                  │
│    ├── Calibration Service                                  │
│    └── Diagnostics Service                                  │
│                                                             │
│  [Driver Layer]                                             │
│    ├── Peripheral Drivers (ADC, DAC, Timer)                 │
│    ├── Sensor Drivers (Temperature, Pressure)               │
│    └── Communication Drivers (UART, SPI, I2C)               │
│                                                             │
│  [HAL Layer]                                                │
│    └── STM32 HAL / LL Drivers                               │
│                                                             │
│  [RTOS Layer]                                               │
│    └── FreeRTOS (Task, Queue, Semaphore, Mutex)             │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 2. 코드 품질 표준
```c
/* Code Quality Standards */

// 1. 명확한 인터페이스 정의
typedef struct {
    // Public interface
    int (*init)(void);
    int (*read)(uint8_t* data, uint16_t len);
    int (*write)(const uint8_t* data, uint16_t len);
    int (*deinit)(void);
} Driver_Interface_t;

// 2. 에러 핸들링
typedef enum {
    ERR_OK = 0,
    ERR_TIMEOUT = -1,
    ERR_INVALID_PARAM = -2,
    ERR_BUSY = -3,
    ERR_HARDWARE = -4
} Error_Code_t;

// 3. 설정 가능한 파라미터 (#define 사용)
#define CONFIG_ADC_SAMPLE_RATE    1000    // Hz
#define CONFIG_UART_BAUDRATE      115200
#define CONFIG_PID_KP             1.0f
```

### 3. 디버깅 프로세스
```
1. 문제 식별
   └── 로그 분석, 재현 조건 확인

2. 원인 분석
   ├── Logic Analyzer로 신호 분석
   ├── Oscilloscope로 타이밍 확인
   ├── Breakpoint 디버깅
   └── Printf 디버깅 (UART Console)

3. 해결책 구현
   ├── 코드 수정
   ├── 하드웨어 수정 (필요시)
   └── 설정 변경

4. 검증
   ├── Unit Test
   ├── Integration Test
   └── Long-term Stability Test
```

---

## 💡 Code Samples

### Sample 1: FreeRTOS Task with Queue
```c
/* ADC Data Acquisition Task */
void ADC_Task(void *argument) {
    uint16_t adc_data[4];
    
    while(1) {
        // Start ADC conversion
        HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_data, 4);
        
        // Wait for completion
        if (xSemaphoreTake(ADC_Complete_Sem, pdMS_TO_TICKS(100)) == pdTRUE) {
            // Process data
            ADC_Data_t processed = {
                .channel = {adc_data[0], adc_data[1], adc_data[2], adc_data[3]},
                .timestamp = HAL_GetTick()
            };
            
            // Send to processing task via Queue
            xQueueSend(ADC_DataQueue, &processed, 0);
        } else {
            // Timeout handling
            Error_Log("ADC timeout");
        }
        
        osDelay(10);  // 100Hz sampling
    }
}
```

### Sample 2: Modbus RTU Implementation
```c
/* Modbus RTU Slave Handler */
void Modbus_ProcessRequest(uint8_t* request, uint16_t len) {
    uint8_t slave_addr = request[0];
    uint8_t function = request[1];
    uint16_t start_addr = (request[2] << 8) | request[3];
    uint16_t quantity = (request[4] << 8) | request[5];
    
    // CRC Check
    uint16_t crc_received = (request[len-1] << 8) | request[len-2];
    uint16_t crc_calculated = CRC16_Modbus(request, len - 2);
    if (crc_received != crc_calculated) {
        return;  // CRC Error, no response
    }
    
    // Function Code Handler
    switch (function) {
        case 0x03:  // Read Holding Registers
            Modbus_ReadHoldingRegisters(start_addr, quantity);
            break;
        case 0x06:  // Write Single Register
            Modbus_WriteSingleRegister(start_addr, quantity);
            break;
        case 0x10:  // Write Multiple Registers
            Modbus_WriteMultipleRegisters(start_addr, quantity, &request[7]);
            break;
        default:
            Modbus_SendException(function, MODBUS_EXCEPTION_ILLEGAL_FUNCTION);
            break;
    }
}
```

### Sample 3: State Machine Pattern
```c
/* System State Machine */
typedef enum {
    STATE_INIT,
    STATE_IDLE,
    STATE_RUNNING,
    STATE_CALIBRATION,
    STATE_ERROR,
    STATE_SHUTDOWN
} System_State_t;

typedef struct {
    System_State_t current;
    System_State_t next;
    void (*entry_action)(void);
    void (*exit_action)(void);
    void (*during_action)(void);
} State_Machine_t;

void StateMachine_Run(State_Machine_t* sm) {
    // State transition
    if (sm->current != sm->next) {
        if (sm->exit_action) sm->exit_action();
        sm->current = sm->next;
        if (sm->entry_action) sm->entry_action();
    }
    
    // During action
    if (sm->during_action) sm->during_action();
    
    // Event handling
    switch (sm->current) {
        case STATE_IDLE:
            if (event_start_received) sm->next = STATE_RUNNING;
            if (event_calibrate_received) sm->next = STATE_CALIBRATION;
            break;
        case STATE_RUNNING:
            if (event_stop_received) sm->next = STATE_IDLE;
            if (error_detected) sm->next = STATE_ERROR;
            break;
        // ... 기타 상태
    }
}
```

---

## 📈 Key Achievements

### 펌웨어 프로젝트
- **12+ 양산 펌웨어** 배포
- **치명적 버그 Zero** 양산 시스템
- **99.8%+ 가동률** 달성

### 기술 기여
- **PID 라이브러리**: 프로젝트 전반에 재사용
- **IAP Bootloader**: 5개 제품에 적용
- **Modbus Stack**: 표준화된 통신 모듈

### 문서화
- **20+ 기술 문서** 작성
- **15+ 사용자 매뉴얼** 작성
- **코드 리뷰 문화** 정착

---

## 📁 Portfolio Files Summary

| 프로젝트 | SCH | PCB | PDF | Images | 코드 |
|----------|-----|-----|-----|--------|------|
| MS | 1 | 4 | 2 | 11 | - |
| L-LPC | - | 3 | 13 | 14 | main.c |
| Psi-1000 | - | - | 2 | 6 | main.c (PID) |
| Nu-2000 | 2 | - | 11 | 3 | - |
| L-Titrator | 1 | 2 | 1 | 3 | - |
| LE_Laser | 2 | 2 | - | - | - |
| Lux | 3 | 3 | - | 18 | - |
| ATIK_JIG | 1 | 6 | 1 | 5 | - |
| **Total** | **10** | **20** | **30** | **60** | **2** |

---

## Contact Information

**조락현 (Cho, Rakhyun)**  
Senior Embedded Systems Engineer (Hardware & Firmware)

- **Email**: 92lock@kakao.com
- **Tel**: 010-7311-0402
- **Location**: Republic of Korea
- **GitHub**: [github.com/gari210404](https://github.com/gari210404)

---

*본 포트폴리오는 9년간의 하드웨어 및 펌웨어 통합 개발 경험을 나타내며, 반도체 공정 장비, 광학 분석 기기, 산업용 제어 시스템 분야에서의 검증된 실적을 보여줍니다.*
