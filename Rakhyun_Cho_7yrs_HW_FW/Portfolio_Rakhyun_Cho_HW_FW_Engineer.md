# Rakhyun Cho

## Hardware & Firmware Engineer

**7+ Years of Full-Stack Embedded Systems Development**

---

## Professional Summary

Versatile Hardware and Firmware Engineer with 7+ years of experience in complete embedded system development from circuit design to firmware implementation. Specialized in STM32 microcontroller-based systems, real-time operating systems, and industrial communication protocols. Proven track record of delivering production-ready products combining robust hardware design with efficient firmware architecture.

**Core Competencies:**
- Complete embedded system development (Hardware + Firmware + Testing)
- STM32 firmware development with FreeRTOS
- Industrial communication protocols (Modbus, RS-232/485, I2C/SPI)
- Control algorithms (PID, state machines, sensor fusion)
- Hardware-firmware co-design optimization
- Production firmware deployment & field updates
- Technical documentation & knowledge transfer

---

## Technical Skills

### Hardware Design
- **Circuit Design**: Mixed-signal circuits, sensor interfaces, communication modules, power management
- **Microcontroller Systems**: STM32 (F1/F4/F7/H7), peripheral integration, clock configuration
- **Communication Interfaces**: RS-232/485, I2C, SPI, UART, USB, CAN, Modbus RTU/ASCII
- **PCB Design**: Altium Designer, 4-6 layer boards, component placement optimization
- **Tools**: Altium Designer, LTspice, oscilloscope, logic analyzer

### Firmware Development
- **Languages**: C (Expert), C++ (Proficient), Python (Scripting)
- **Microcontrollers**: STM32 series (F103, F407, F746, H743)
- **RTOS**: FreeRTOS (Task scheduling, Queue, Semaphore, Mutex, Event Groups)
- **HAL/LL**: STM32 HAL, LL drivers, Custom peripheral drivers
- **Communication**: UART/USART, SPI, I2C, USB CDC/HID, Modbus RTU/ASCII, CANopen
- **Protocols**: Modbus Master/Slave, Custom binary protocols, AT command parsers
- **Peripherals**: ADC, DAC, Timer/PWM, DMA, SDIO, RTC, Watchdog

### Development Tools
- **IDE**: STM32CubeIDE, Keil µVision, IAR EWARM, VS Code
- **Debuggers**: ST-Link V2/V3, J-Link, GDB, SWD debugging
- **Build Systems**: Make, CMake, STM32CubeMX code generation
- **Version Control**: Git, GitHub, GitLab, SourceTree
- **Testing**: Logic analyzer, oscilloscope, bus monitor, UART console

### Software Architecture
- **Design Patterns**: State machines, Observer, Command pattern
- **Code Organization**: Layered architecture (HAL → Driver → Application)
- **Memory Management**: Static allocation, memory pools, DMA buffers
- **Optimization**: Code size optimization, execution time profiling, power consumption
- **Bootloader**: IAP (In-Application Programming), firmware update via UART/USB/SD card

### Control Systems & Algorithms
- **PID Control**: Classical PID, Anti-windup, Derivative filtering, Auto-tuning algorithms
- **Signal Processing**: Moving average, Kalman filtering, FFT, Digital filters
- **Calibration**: Multi-point calibration, polynomial regression, temperature compensation
- **State Machines**: Complex multi-state controllers, event-driven architectures

---

## Professional Experience

### ATIK Corp. | Hardware & Firmware Engineer
**2018 - Present (7+ years)**

#### Major Projects

### 1. **Sigma-1000 LPC Simulator** (2020-2021)
**Role:** Hardware & Firmware Developer | **Production:** 50+ units | **Defect Rate:** 0.5%

Plasma calibration simulator combining precision DAC hardware with real-time control firmware.

**Hardware Contributions:**
- STM32F407IGT6-based control board design
- 16-channel MCP4728 DAC interface (I2C)
- RS-232/485 communication circuits
- Power supply distribution network

**Firmware Architecture:**
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
└── STM32 HAL + Custom optimizations
```

**Key Firmware Features:**
- **Real-time DAC Control**: 
  - 16 channels @ 1ms update rate
  - I2C communication at 400kHz
  - Error detection & automatic retry mechanism
  - Voltage accuracy: ±0.01% FSR

- **Communication Protocol**:
  - Modbus RTU/ASCII master/slave implementation
  - Custom binary protocol for high-speed data transfer
  - CRC-16 error checking
  - Timeout & recovery mechanisms

- **Calibration System**:
  - Multi-point calibration (up to 20 points per channel)
  - Polynomial curve fitting (up to 3rd order)
  - Temperature compensation algorithm
  - Non-volatile storage (EEPROM emulation in Flash)

- **Data Logging**:
  - SD card file system (FatFS)
  - Circular buffer implementation (1MB RAM buffer)
  - Timestamp using RTC
  - CSV format for easy analysis

- **User Interface**:
  - Nextion HMI communication (UART)
  - Touch screen interface
  - Real-time graph display
  - Configuration menu system

**Performance Metrics:**
- Firmware size: 256KB Flash, 64KB RAM usage
- Boot time: < 2 seconds
- Communication latency: < 10ms (Modbus)
- Calibration time: 5 minutes (83% reduction vs. previous method)

**Firmware Quality:**
- Zero critical bugs in production
- Field firmware updates via IAP bootloader
- Comprehensive error logging & diagnostics

---

### 2. **Nu-2000 Optical Analysis System** (2021-2022)
**Role:** Firmware Lead & Hardware Support | **Project Scale:** 33MB development plan

Advanced optical absorption spectroscopy system requiring complex multi-channel control firmware.

**Hardware Contributions:**
- System integration & debugging
- Sensor interface validation
- Communication module testing

**Firmware Architecture:**
```
FreeRTOS Tasks (5 tasks, priority 1-5)
├── Task1: LED Driver Control (Priority: 5, Period: 100ms)
├── Task2: Photodiode Data Acquisition (Priority: 4, Period: 50ms)
├── Task3: Temperature Monitoring (Priority: 3, Period: 1s)
├── Task4: Communication Handler (Priority: 2, Event-driven)
└── Task5: Data Processing (Priority: 1, Event-driven)

Queues & Semaphores
├── ADC Data Queue (100 samples depth)
├── UART TX Queue (512 bytes)
├── I2C Mutex (For shared bus access)
└── Event Group (System state flags)
```

**Key Firmware Features:**

- **Multi-wavelength LED Control**:
  - 4 LED channels (UV: 254nm, 280nm | IR: 1450nm, 1650nm)
  - PWM generation using Timer peripherals
  - Current monitoring via ADC
  - Thermal compensation algorithm
  - Automatic intensity adjustment

- **High-speed Data Acquisition**:
  - 4 Photodiode channels @ 250kSPS (AD7682 ADC)
  - DMA-based circular buffer (zero CPU overhead)
  - Real-time signal processing pipeline
  - FFT for noise analysis
  - Moving average filter (configurable window)

- **Precision Temperature Control**:
  - Dual RTD sensors (MCP3427 18-bit ADC, I2C)
  - 0.01°C resolution
  - PID temperature control for optical stability
  - Thermal drift compensation

- **Optical Module Integration**:
  - Test firmware for optical module characterization
  - Automated calibration routines
  - Data logging for Wiki Optics vendor validation
  - Beta version firmware for field testing

- **Bootloader (IAP)**:
  - UART-based firmware update
  - CRC32 integrity checking
  - Dual-bank Flash for fail-safe updates
  - Boot-time version display
  - Installation manual created (V0.2)

**Software Development Process:**
- Modular firmware architecture
- Git version control
- Comprehensive test procedures documented
- Hardware-firmware integration testing
- Field beta testing program

**Documentation Deliverables:**
- Firmware structure overview presentation
- Optical module test firmware user manual
- IAP installation & usage guide (V0.2)
- Calibration procedure documentation
- Hardware-firmware interface specification

---

### 3. **Psi-1000 Pressure Controller** (2019-2022)
**Role:** PID Control Algorithm Developer & Firmware Architect

Advanced pressure control system with sophisticated PID algorithms and university collaboration.

**Hardware Contributions:**
- System block diagram design
- IAP upgrade mechanism
- PCB bring-up & debugging

**Firmware Architecture - PID Control Focus:**

**PID Algorithm Implementation:**
- Studied multiple PID formulations (Standard Form vs. Beckhoff Library Form)
- Implemented discrete-time PID with anti-windup
- Derivative term low-pass filtering (noise reduction)
- Configurable sampling time (1ms - 1s)
- Parameter tuning interface via Modbus

**PID Forms Comparison Research:**
```c
// Standard Form #1 (Implemented)
U(k) = Kp * [e(k) + (T/Ti) * Σe(j) + (Td/T) * (e(k) - e(k-1))]

// Beckhoff Library Form (Analyzed)
U(s)/E(s) = Kp * (1 + 1/(Ti*s) + Td*s)

// Discrete Implementation with Anti-windup
integral = integral + (T/Ti) * error;
if (integral > integral_max) integral = integral_max;  // Anti-windup
derivative = (Td/T) * (error - error_prev) / (1 + Td/(N*T));  // Filtered
output = Kp * (error + integral + derivative);
```

**Advanced Control Features:**
- **Auto-tuning Algorithm**: 
  - Relay feedback method (Åström-Hägglund)
  - Ziegler-Nichols tuning rule implementation
  - Step response analysis
  - Bode plot measurement support

- **Multiple PID Instances**:
  - Pressure control PID (primary)
  - Temperature control PID (heater)
  - Flow control PID (MFC)
  - Cascade control capability

- **Control Logic Design** (University Collaboration):
  - Rev 01 - 05 control logic iterations documented
  - Dong-A University research project
  - Parameter optimization through experimentation
  - Test result analysis & reporting

**Communication & Interface:**
- **Modbus Protocol**:
  - RTU/ASCII support (Master & Slave)
  - Protocol specification Ver 0.27 - 0.30
  - Function codes: 03, 06, 16 (Read/Write registers)
  - Custom register map design

- **Beckhoff PLC Integration**:
  - Configuration procedure documentation
  - Auto-tuning integration with PLC
  - Real-time data exchange

**Software Tools Developed:**
- PID Loop Simulator (Excel VBA)
- PID Scrollbar GUI for parameter tuning (Excel)
- Auto-tune test scripts
- Step response analyzer

**Firmware Development Deliverables:**
- Control logic design document (Rev 01-05)
- Software design specification (Rev 01-03)
- PID parameter change procedure
- Test result analysis presentations
- Software manual (Ver 0.3)

**Testing & Validation:**
- Heater PID test data collection
- Z-N tuning method validation
- IMC (Internal Model Control) testing
- Auto-tune performance verification
- Step test characterization

**Achievements:**
- ±0.1% pressure control accuracy achieved
- < 2 second settling time (step response)
- Stable operation over 0.001 - 1000 Torr range
- Successful university technology transfer

---

### 4. **L-Titrator (Automatic Titrator)** (2018-2020)
**Role:** Embedded Systems Developer

Chemical analysis instrument firmware development.

**Firmware Features:**
- Stepper motor control (burette positioning)
- pH sensor data acquisition & processing
- Temperature compensation algorithms
- Auto-calibration routines
- USB communication for PC software
- Data logging & result storage

---

## Additional Technical Contributions

### Bootloader Development (IAP)
- **IAP_ATIK Project**: Standalone bootloader framework
- Features: UART/USB firmware update, CRC integrity check, dual-bank Flash
- Reusable across multiple projects
- User manuals created for each product

### HMI Development
- **Nextion HMI**: Touch screen interface design
- Custom protocols for MCU-HMI communication
- Real-time graph display optimization
- User-friendly configuration menus

### Testing & Debugging Tools
- Custom UART console commands for debugging
- Built-in diagnostics & self-test routines
- Memory dump & register inspection
- Performance profiling tools

---

## Firmware Development Methodology

### 1. **Structured Design Process**
- Requirements analysis & specification
- Firmware architecture design (block diagram, task diagram)
- Module interface definition
- Implementation with code reviews
- Unit testing & integration testing
- System validation & field testing

### 2. **Code Quality Standards**
- Modular design with clear interfaces
- Consistent naming conventions
- Comprehensive inline comments
- Error handling at every layer
- Memory leak prevention
- Static code analysis

### 3. **Version Control & Documentation**
- Git branching strategy (feature/develop/master)
- Commit messages with issue tracking
- README files for each module
- API documentation
- User manuals for end users

---

## Key Technical Achievements

### Firmware Projects
- **8+ Production Firmware** delivered
- **Zero Critical Bugs** in production systems
- **256KB+ Flash** typical firmware size (optimized)
- **< 2 Second** boot time standard

### Algorithm Development
- **PID Control Library**: Reusable across projects
- **Calibration Engine**: Multi-point, polynomial fitting
- **Communication Stack**: Modbus RTU/ASCII implementation
- **Data Logger**: FatFS-based SD card system

### Technical Documentation
- **15+ User Manuals** created (IAP, calibration, testing)
- **8+ Technical Presentations** (circuit reviews, PID study)
- **460+ Documents** across all projects (with hardware team)
- **Comprehensive Test Procedures** for every product

---

## PID Control Expertise (Detailed)

### Research & Study
- In-depth study of PID algorithms (documented in presentations)
- Comparison of multiple PID formulations
- Analysis of Beckhoff PLC PID library
- Literature review of auto-tuning methods

### Implementation Experience
- Classical PID with anti-windup
- Bumpless transfer for manual/auto switching
- Derivative kick prevention
- Setpoint weighting
- Gain scheduling for non-linear systems

### Tuning Methods Applied
- Ziegler-Nichols (closed-loop, open-loop)
- Cohen-Coon method
- Relay feedback (Åström-Hägglund)
- IMC (Internal Model Control) tuning
- Manual tuning with step response analysis

### Practical Applications
- Pressure control: ±0.1% accuracy, < 2s settling
- Temperature control: ±0.05°C stability
- Flow control: ±2% MFC setpoint tracking

---

## Professional Development

### Continuous Learning
- Advanced RTOS concepts (task priorities, scheduling, IPC)
- Signal processing algorithms (Kalman filter, FFT)
- Control theory (modern control, state-space models)
- Communication protocols (CANopen, EtherCAT basics)
- Safety standards (IEC 61508, functional safety)

### Technical Skills Growth
- Started: Basic STM32 programming
- Current: Expert-level firmware architect
- Future: Exploring AI/ML at edge, Rust for embedded

---

## Tools & Technologies

### Development Environment
- **IDE**: STM32CubeIDE (primary), Keil µVision, IAR EWARM
- **Debuggers**: ST-Link V2/V3, J-Link, OpenOCD
- **Version Control**: Git, GitHub Desktop, SourceTree
- **Documentation**: Doxygen, Markdown, Microsoft Office

### Testing & Analysis
- **Hardware**: Logic analyzer (Saleae), Oscilloscope (Tektronix)
- **Software**: Bus monitor tools, UART terminal (Tera Term, PuTTY)
- **Profiling**: SystemView (Segger), FreeRTOS trace

### Simulation & Modeling
- **Circuit**: LTspice (hardware validation)
- **Control**: MATLAB/Simulink (PID tuning), Excel VBA (PID simulator)
- **Python**: Data analysis scripts, automation tools

---

## Work Style & Attributes

- **Full-Stack Mindset**: Comfortable working across hardware and firmware boundaries
- **Problem Solver**: Systematic debugging from hardware signals to firmware logic
- **Detail-Oriented**: Careful attention to edge cases and error handling
- **Collaborative**: Effective communication with hardware team and vendors
- **Self-Learner**: Proactive in studying new technologies and best practices
- **Practical**: Focus on production-ready, maintainable code

---

## Contact Information

**Rakhyun Cho**  
Hardware & Firmware Engineer

- **Email**: 92lock@kakao.com
- **Tel**: 010-7311-0402
- **Location**: Republic of Korea
- **GitHub**: [github.com/gari210404](https://github.com/gari210404)

---

## GitHub Repositories

| Repository | Description | Tech Stack |
|------------|-------------|------------|
| **ATIK-Firmware** | STM32 firmware collection (85MB) | C, FreeRTOS, STM32 HAL |
| **ATIK-Hardware-Projects** | Schematic & PCB designs (759MB) | Altium Designer |
| **ATIK-Software** | PC software tools (2.9MB) | C#, Python |
| **ATIK-Nextion-HMI** | HMI projects (138MB) | Nextion IDE |
| **Arduino-Libraries** | Custom libraries (54MB) | C++, Arduino |

---

## References & Code Samples

Firmware source code, design documents, and technical presentations available upon request or via GitHub repositories.

---

*This portfolio represents 7+ years of hands-on embedded systems development with a strong focus on production-quality firmware, control algorithms, and hardware-firmware co-design.*
