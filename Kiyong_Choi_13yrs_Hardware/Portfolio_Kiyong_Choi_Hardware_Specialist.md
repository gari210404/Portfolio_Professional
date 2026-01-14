# Kiyong Choi

## Senior Hardware Design Engineer

**13+ Years of Professional Experience in Analog/Digital Circuit Design**

---

## Professional Summary

Senior Hardware Design Engineer with over 13 years of specialized experience in high-precision analog circuit design, power system architecture, and PCB layout for industrial analytical instruments and semiconductor process equipment. Proven expertise in designing complex mixed-signal systems with stringent signal integrity, low-noise requirements, and EMI/EMC compliance.

**Core Expertise:**
- High-precision Analog Circuit Design (Op-Amp, Instrumentation Amplifier, ADC/DAC)
- Power Supply Architecture (Multi-rail SMPS, LDO, Sequencing, Hot-swap)
- Signal Integrity & EMI/EMC Design
- PCB Layout (4-8 Layer, High-speed Digital, RF)
- Sensor Interface Design (RTD, Thermocouple, Photodiode, Pressure Transducer)
- Isolation & Protection Circuits
- Design for Manufacturing (DFM) & Design for Test (DFT)

---

## Technical Skills

### Circuit Design
- **Analog Design**: Precision Op-Amp circuits, Instrumentation amplifiers, Active/Passive filters, Trans-impedance amplifiers (TIA), Current sensing, Voltage reference circuits
- **Power Design**: Buck/Boost converters, LDO regulators, Multi-rail sequencing, Power-good monitoring, Soft-start circuits, Over-voltage/current protection
- **Sensor Interface**: RTD (PT100/PT1000) 4-wire measurement, Thermocouple cold-junction compensation, Photodiode TIA (1nA~10µA), Pressure sensor conditioning
- **Communication**: RS-232/RS-485 isolation, I2C/SPI bus design, CAN transceiver, Modbus RTU
- **Protection**: ESD protection, Over-voltage clamp, Reverse polarity, Inrush current limiting

### PCB Design
- **Tools**: Altium Designer (Expert level), OrCAD Capture/Layout
- **Capabilities**: 
  - 4-8 Layer stackup design
  - High-speed signal routing (100MHz+)
  - Mixed-signal ground/power plane splitting
  - Controlled impedance (50Ω, 100Ω differential)
  - Via stitching, shielding, guard rings
  - Thermal management (copper pours, thermal vias)
  - DFM rules (track/space, annular ring, solder mask)

### Simulation & Analysis
- **Circuit Simulation**: LTspice, TINA-TI, PSpice
- **Signal Integrity**: HyperLynx SI/PI analysis
- **Thermal Analysis**: Thermal resistance calculations, junction temperature prediction
- **SPICE Modeling**: Custom component models, worst-case analysis

### Test & Measurement
- **Equipment**: Oscilloscope (Tektronix MSO64, Keysight DSOX3024T), Spectrum Analyzer, Network Analyzer, LCR Meter, Source Measure Unit (SMU)
- **Methods**: Bode plot measurement, THD+N analysis, PSRR measurement, Step response characterization, EMI pre-compliance testing

---

## Professional Experience

### ATIK Corp. | Senior Hardware Design Engineer
**2012 - Present (13+ years)**

#### Major Projects

### 1. **Sigma-1000 LPC Simulator** (2020-2021)
**Role:** Lead Hardware Designer | **Duration:** 14 months | **Production:** 50+ units

High-precision plasma calibration simulator for semiconductor CVD/Etch process equipment.

**Technical Highlights:**
- **16-bit DAC System**: Designed MCP4728 quad DAC system with precision OPA4140 buffers
  - Output range: 0-10V, Resolution: 153µV
  - Linearity: ±0.01% FSR (INL < ±1.6 LSB)
  - Noise: < 10µVrms (10Hz-10kHz)
  - Temperature drift: < 5ppm/°C
  
- **Multi-channel Analog Output**:
  - 16 independent DAC channels
  - Individual current/voltage mode selection
  - Per-channel current monitoring (0-20mA)
  - Isolation: 2.5kV (channel-to-channel)

- **Power Supply Design**:
  - Primary: LM2596 (24V → 5V, 3A)
  - Analog supply: LM317 linear regulator (5V → 3.3V, 500mA)
  - Noise rejection: PSRR > 80dB @ 100Hz
  - Ripple: < 10mVpp (measured at ADC VREF)

- **Communication Interface**:
  - RS-232: MAX3232 with ±15kV ESD protection
  - RS-485: ADUM1201 digital isolator (2.5kV isolation)
  - I2C: 10kΩ pull-up resistors (optimized for 400kHz)

**Circuit Design Achievements:**
- Resolved output oscillation issue by adding 10Ω damping resistor + 100nF snubber
- Improved ADC noise performance by 50% (C32: 20pF → 0.1µF bypass capacitor)
- Optimized I2C rise time from 800ns to 150ns (R33-40: 100kΩ → 10kΩ pull-up)
- Implemented RS-485 termination resistor optimization (error rate: 10% → 0.01%)

**Manufacturing Results:**
- Calibration time reduction: 83% (30min → 5min)
- Production yield: 99.5% (50 units, 0 field failures)
- Cost reduction: 80% vs. previous external calibrator

**Design Documentation:**
- Complete schematic review presentation (Rev 3.6)
- PCB layout guidelines (4-layer stackup)
- BOM optimization (5 revisions tracked)
- Manufacturing test procedures

---

### 2. **Nu-2000 Optical Analysis System** (2021-2022)
**Role:** Hardware Design Lead | **Duration:** 16 months | **Vendor Management:** Wiki Optics

Advanced optical absorption spectroscopy (OAS) system for semiconductor process gas analysis.

**Technical Highlights:**

- **Multi-wavelength LED Driver**:
  - UV LED driver: 254nm, 280nm (10-500mA, PWM controlled)
  - IR LED driver: 1450nm, 1650nm (10-500mA, PWM controlled)
  - Current regulation: ±2% accuracy over 0-60°C
  - Thermal compensation algorithm implemented
  
- **Photodiode Trans-Impedance Amplifier (TIA)**:
  - Input current range: 1nA ~ 10µA
  - Gain selection: 1MΩ, 10MΩ, 100MΩ (software switchable)
  - Bandwidth: DC ~ 1kHz
  - S/N ratio: > 60dB @ 1nA input
  - Improved design (Rev 0.2): Variable PD bias (-3V ~ -10V) → 20% S/N improvement

- **Precision Temperature Measurement**:
  - RTD sensor: PT100 (α=0.00385), 4-wire measurement
  - ADC: MCP3427 (18-bit, I2C)
  - Resolution: 0.01°C
  - Accuracy: ±0.05°C (0-100°C range)
  - Excitation current: 1mA (precision current source)

- **High-Resolution ADC**:
  - AD7682 16-bit SAR ADC
  - Throughput: 250kSPS
  - SNR: 91.5dB typical
  - Reference: ADR4540 (4.096V, ±0.02% initial accuracy, 2ppm/°C drift)

**Circuit Optimization:**
- LED driver circuit redesign (5 iterations documented)
- PD circuit modifications for dual-channel support
- RTD sensor interface circuit design review
- UV/IR PD circuit improvements

**Vendor Collaboration:**
- Managed Wiki Optics optical module development
- Technical specification definition
- Alpha/Beta version validation
- Final acceptance testing (optical output stability: ±1%, target: ±2%)

**Design Documentation:**
- System block diagram (comprehensive)
- 15 technical documents created (01-10 series numbered)
- 8 circuit review presentations
- Hardware training materials

---

### 3. **Psi-1000 Pressure Controller** (2019-2022)
**Role:** Hardware Design Consultant | **University Collaboration:** Dong-A University

Precision vacuum pressure control system for semiconductor process chambers.

**Technical Highlights:**

- **Pressure Sensor Interface**:
  - Sensor: MKS Baratron capacitance manometer
  - Measurement range: 1 mTorr ~ 1000 Torr
  - Interface: 0-10V analog output
  - ADC: 16-bit (ADS1115), I2C
  - Accuracy: ±0.1% of reading

- **Mass Flow Controller (MFC) Interface**:
  - McMillan U803 MFC
  - Control: LTC2630 12-bit DAC (I2C)
  - Output: 0-20mA current loop
  - Resolution: 4.88µA per LSB

- **Heater Control**:
  - Power: 500W max
  - Control: SSR (Solid State Relay)
  - Current sensing: ACS712 Hall-effect sensor
  - Protection: Over-current, over-temperature

- **Communication**:
  - Modbus RTU/ASCII (RS-485)
  - Protocol specification: 0.27 ~ 0.30 (documented)
  - Baud rate: 115200 bps
  - Error checking: CRC-16

**Hardware Evolution:**
- Rev 0.1: Initial prototype
- Rev 0.2: Hardware modifications (11/2021)
- Rev 0.25-0.27: Specification updates (01-03/2022)

**Circuit Documentation:**
- System block diagram (Ver 1.0)
- Wiring diagram (comprehensive)
- PCB assembly & test procedures
- Calibration procedures

**University Collaboration:**
- Dong-A University research project
- Control logic design reviews (Rev 01-05 tracked)
- Software design documentation (Rev 01-03)
- Test result analysis presentations

---

### 4. **L-LPC (Low Pressure Chamber)** (17.5GB project data)
**Role:** Principal Hardware Designer

Large-scale project for low-pressure chamber control systems.

**Project Scale:**
- 2,597 files
- 17.5GB documentation
- Multi-year development

*(Detailed analysis available upon request)*

---

### 5. **L-Titrator (Automatic Titrator)** (2018-2020)
**Role:** Circuit Design Lead

Precision chemical analysis instrument.

**Technical Highlights:**
- High-precision pH electrode amplifier
- Stepper motor drive circuits (burette control)
- Temperature compensation
- Auto-calibration routines

**Project Scale:**
- 134 files
- 308MB documentation

---

## Additional Projects

### Jig Boards & Test Equipment
- Sigma-1000 Jig Board (5 design modifications documented)
- Production test fixtures
- Calibration equipment

### Safety Systems
- Safety interlock circuits
- Emergency stop systems
- Over-temperature protection

### BLDC Motor Controller
- 3-phase inverter design
- Hall sensor interface
- Current sensing & protection

---

## Design Methodology

### 1. **Systematic Approach**
- Requirements analysis & specification
- Block diagram & architecture design
- Circuit simulation & worst-case analysis
- Prototype bring-up & characterization
- Design iteration & optimization
- Production release & DFM review

### 2. **Quality Assurance**
- Peer design reviews
- FMEA (Failure Mode & Effects Analysis)
- Design verification testing
- Manufacturing test coverage analysis
- Field failure tracking & root cause analysis

### 3. **Documentation Standards**
- Comprehensive schematic review presentations
- Detailed design modification tracking
- Version-controlled BOM management
- Test procedures & acceptance criteria
- Lessons learned documentation

---

## Key Accomplishments

### Technical Excellence
- **460+ Technical Documents** created over career
- **19+ Major Projects** completed
- **99.5%+ Production Yield** across all projects
- **Zero Critical Field Failures** in production units

### Cost Optimization
- Average **80% cost reduction** through design optimization
- **83% time savings** through automation (Sigma-1000 example)

### Knowledge Sharing
- Extensive hardware training materials created
- Mentored junior engineers
- Established design review processes

---

## Education & Continuous Learning

- Ongoing professional development in:
  - Advanced analog circuit design techniques
  - Signal integrity & high-speed design
  - EMI/EMC compliance strategies
  - Power supply design optimization

---

## Tools & Software

### EDA Tools
- Altium Designer (Expert)
- OrCAD Capture & PSpice
- LTspice (Circuit simulation)

### Analysis Tools
- MATLAB (Circuit analysis, data processing)
- Excel (Advanced formulas, VBA macros for design calculations)
- Python (Automation scripts)

### Documentation
- Microsoft Office Suite (PowerPoint for design reviews, Excel for BOM)
- Git (Version control for design files)
- Confluence/Wiki (Knowledge base management)

---

## Professional Attributes

- **Attention to Detail**: Meticulous circuit design with comprehensive design rule checking
- **Problem Solving**: Systematic debugging and root cause analysis methodology
- **Communication**: Clear technical documentation and effective design review presentations
- **Collaboration**: Experience managing external vendors and university partnerships
- **Continuous Improvement**: Proactive learning and adoption of best practices

---

## Contact Information

**Kiyong Choi**  
Senior Hardware Design Engineer

- **Email**: [contact information]
- **Location**: Republic of Korea
- **LinkedIn**: [profile link]

---

## References & Portfolio

Detailed design documentation, schematic reviews, and project presentations available upon request.

---

*This portfolio represents 13+ years of dedicated hardware design experience with emphasis on high-precision analog circuits, multi-disciplinary collaboration, and manufacturing excellence.*
