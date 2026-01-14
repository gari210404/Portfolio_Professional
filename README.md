# 📁 Professional Portfolio

조락현 & 최기용 전문 포트폴리오 프로젝트

## 📋 프로젝트 구조

```
Portfolio_Professional/
├── Kiyong_Choi_13yrs_Hardware/          # 최기용 13년차 하드웨어 엔지니어
├── Rakhyun_Cho_7yrs_HW_FW/              # 조락현 9년차 임베디드 엔지니어
├── Project_Files/                        # 프로젝트 파일 (회로도, PCB, 블록 다이어그램)
├── create_notion_portfolio.py           # 노션 자동 생성 스크립트
└── search_all_pages.py                  # 노션 페이지 검색 스크립트
```

## 👨‍💼 최기용 - Senior Hardware Engineer (13년차)

**전문 분야:**
- 반도체 분석 장비 하드웨어 설계
- 고정밀 아날로그 회로 설계
- PCB 설계 (PADS, Altium Designer)

**주요 문서:**
- `최기용_Senior_Hardware_Engineer_Professional_v3.docx`
- `Portfolio_Choi_Professional_KOR_v2.md`

## 👨‍💻 조락현 - Senior Embedded Systems Engineer (9년차)

**전문 분야:**
- 하드웨어 & 펌웨어 Full-Stack 개발
- STM32 MCU 기반 임베디드 시스템
- FreeRTOS, PID 제어 알고리즘

**주요 문서:**
- `조락현_Senior_Embedded_Engineer_9년차_v1.docx`
- `경력이력서_조락현_9년차_updated.docx`
- `Portfolio_Rakhyun_Cho_9yrs_Professional_KOR.md`

**노션 포트폴리오:**
- https://notion.so/2e8f07469821811aa8d9dba0b5307682

## 🗂️ 프로젝트 파일 (Project_Files/)

총 **118개 파일**, **98.4MB**

### 프로젝트 목록
1. **MS (Mass Spectrometer)** - 최신 프로젝트
2. **L-LPC (H-Sensor System)** - 대표 프로젝트 (14개 블록 다이어그램)
3. **Psi-1000/3000** - PID 압력 제어
4. **Nu-2000** - 광학 분석
5. **L-Titrator** - 적정 분석
6. **LE_Laser (Mantis SSC)** - 레이저 제어
7. **Lux** - 조도 센서
8. **ATIK_JIG** - 테스트 장비

### 파일 유형
- 📐 **SCH 파일**: 10개
- 🔲 **PCB 파일**: 20개
- 📄 **PDF 문서**: 30개
- 🖼️ **PNG 이미지**: 60개 (블록 다이어그램)

## 🛠️ 기술 스택

### Hardware
- STM32F4/F7 MCU
- Analog Circuit Design (ADC, DAC, OP-Amp, TIA)
- Power Supply (Switching/Linear Regulator)
- PCB Design Tools: PADS, Altium Designer, KiCad

### Firmware
- C/C++
- FreeRTOS
- PID Control Algorithm
- Ethernet (TCP/UDP)
- UART, SPI, I2C
- IAP Bootloader (Y-modem)

### Tools
- STM32CubeIDE
- Source Insight
- Visual Studio
- Pandoc (Markdown → Word)
- Python (Notion API)

## 📝 노션 API 연동

`create_notion_portfolio.py` 스크립트를 사용하여 포트폴리오를 자동으로 노션에 생성할 수 있습니다.

```bash
python create_notion_portfolio.py
```

## 📅 업데이트 내역

- **2026.01.14**: 조락현 경력이력서 9년차 업데이트
- **2026.01.14**: 노션 API 연동 및 자동 포트폴리오 생성
- **2026.01**: 조락현 포트폴리오 9년차 업데이트 (펌웨어+회로 Full-Stack)
- **2026.01**: L-LPC 블록 다이어그램 14개 추가
- **2026.01**: 프로젝트 파일 정리 (118개 파일)
- **2026.01**: 최기용 포트폴리오 v3 제작

## 📞 Contact

- **조락현**: 92lock@kakao.com / 010-7311-0402
- **최기용**: k.y.choi@example.com

---

© 2026 Professional Portfolio Project
