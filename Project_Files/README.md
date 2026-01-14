# 포트폴리오 프로젝트 파일 정리

**작성일:** 2026-01-13  
**대상:** 최기용 (13년차 Senior Hardware Engineer)

---

## 📋 개요

포트폴리오 문서와 함께 제공되는 실제 설계 파일들입니다.  
D 드라이브의 원본 프로젝트에서 주요 파일들을 프로젝트별로 분류하여 정리했습니다.

---

## 📂 폴더 구조

```
Project_Files\
├── 01_MS_Mass_Spectrometer\    ⭐ 최신 프로젝트 (2024-2025)
├── 02_L-LPC\                   ⭐ 최대 규모 (원본 17.5GB)
├── 03_Psi-1000\                ⭐ 동아대 협력
├── 04_Nu-2000\
├── 05_Sigma-1000\
├── 06_L-Titrator\
├── 07_FPGA_Zynq\               ⭐ FPGA 설계 (원본 5.9GB)
├── 08_LE_Laser\
├── 09_BLDC_Motor\
├── 10_Lux\
└── 11_ATIK_JIG\
```

각 프로젝트 폴더 내부:
```
프로젝트명\
├── Schematics\   → 회로도 (.sch 파일)
├── PCB\          → PCB 레이아웃 (.pcb 파일)
├── PDF\          → PDF 문서 (회로도, 스펙)
└── Code\         → 펌웨어 소스 코드 (예정)
```

---

## 📊 파일 통계

| 프로젝트 | Schematics | PCB | PDF/PPT | Code | 합계 | 상태 |
|----------|-----------|-----|---------|------|------|------|
| 01_MS_Mass_Spectrometer | 1 | 4 | 1 | 0 | **6** | ✅ 완료 (+Block Diagram) |
| 02_L-LPC | 0 | 1 | 9 | 0 | **10** | ✅ 완료 |
| 03_Psi-1000 | 0 | 0 | 1 | 0 | **1** | ✅ Block Diagram 추가 |
| 04_Nu-2000 | 1 | 1 | 11 | 0 | **13** | ✅ 완료 (+회로도 PDF) |
| 05_Sigma-1000 | 1 | 1 | 0 | 0 | **2** | ✅ 완료 |
| 06_L-Titrator | 1 | 2 | 1 | 0 | **4** | ✅ 완료 (+Block Diagram) |
| 07_FPGA_Zynq | 0 | 0 | 0 | 0 | **0** | ⏳ Vivado 추출 예정 |
| 08_LE_Laser | 0 | 0 | 0 | 0 | **0** | ⏳ 원본 탐색 중 |
| 09_BLDC_Motor | 0 | 0 | 0 | 0 | **0** | ⏳ 원본 탐색 중 |
| 10_Lux | 3 | 3 | 0 | 0 | **6** | ✅ 완료 |
| 11_ATIK_JIG | 1 | 6 | 1 | 0 | **8** | ✅ 완료 (+Block Diagram) |
| **합계** | **8** | **18** | **24** | **0** | **50** | - |

---

## 🗂️ 프로젝트별 상세 정보

### 1. MS (Mass Spectrometer) ⭐ NEW

**원본 위치:** `D:\00_Project\2025\01_MASS\`  
**프로젝트 기간:** 2024-2025 (진행 중)  
**프로젝트 규모:** 1.14GB, 345 files

**복사된 파일:**
```
Schematics\
  └── MASS_DRB_v0_1_20250909A.sch (497KB)

PCB\
  ├── MASS_DRB_v0_1_250904-017(PCB).pcb (2.6MB)
  ├── MASS_DRB_v0_1_250909-018(PCB).pcb (2.6MB)
  ├── MASS_DRB_v0_1_250909-019(PCB).pcb (2.6MB)
  └── MASS_DRB_v0_1_250910-021(PCB).pcb (2.8MB)
```

**추가 예정:**
- [ ] MASS_RFDB, MASS_IDBB 회로도
- [ ] 블록 다이어그램 PDF
- [ ] QMS 교육 자료 요약

---

### 2. L-LPC (Low Pressure Chamber) ⭐ 최대 규모

**원본 위치:** `D:\100_Git_HW\02_L_LPC\`  
**프로젝트 기간:** 2020-2023  
**프로젝트 규모:** 17.5GB, 2,597 files

**복사된 파일:**
```
PCB\
  └── LPC_PD_POWER(rev_0.1)_221026.pcb (2.6MB)

PDF\ (9개 파일)
  ├── LPC_Board_SamplePCB.pdf
  ├── LPC_PWR_Board_eleparts.pdf
  ├── LPC_PD_Board_eleparts.pdf
  ├── lpc_pd_power(rev_0.1).pdf
  ├── lpc_pd_power(rev_01)_16_2.pdf
  └── 기타 4개 PDF 파일
```

**추가 예정:**
- [ ] 메인 보드 회로도 (.sch)
- [ ] Multi-board 시스템 블록 다이어그램
- [ ] 전체 시스템 사양서

---

### 3. Psi-1000 (Pressure Controller)

**원본 위치:** `D:\100_Git_HW\02_Psi_1000\` (Git 레포지토리)  
**프로젝트 기간:** 2019-2022  
**프로젝트 규모:** 3.0GB, 399 files

**현재 상태:** 파일 없음 (Git에서 추출 필요)

**추가 예정:**
- [ ] Git에서 최종 버전 체크아웃
- [ ] 회로도 (.sch) 추출
- [ ] PCB (.pcb) 추출
- [ ] PDF 변환

---

### 4. Nu-2000 (Optical Analysis System)

**원본 위치:** `D:\100_Git_HW\00_Nu_2000\`  
**프로젝트 기간:** 2021-2022  
**프로젝트 규모:** 387MB, 447 files

**복사된 파일:**
```
Schematics\
  └── Total_Board_ATIK_V1.2.sch (700KB)

PCB\
  └── Total_Board_ATIK_V1.2.pcb (4.2MB)

PDF\ (8개 파일)
  ├── Total_Board_ATIK_V1.2.pdf
  ├── H_Bridge_Rev0.2_3D.pdf
  ├── PD_AMP_V2.0.pdf
  ├── FET_Board_V1.0.pdf
  └── 기타 4개 PDF 파일
```

---

### 5. Sigma-1000 (LPC Simulator)

**원본 위치:** `D:\100_Git_HW\02_시그마\`  
**프로젝트 기간:** 2020-2021  
**프로젝트 규모:** 23MB, 22 files

**복사된 파일:**
```
Schematics\
  └── ATIK_JIG_BOARD(V01)_220510A_V16_2.sch (497KB)

PCB\
  └── ATS8009_P_ATIK_JIG_BOARD_V0.1_220511_F.pcb (2.8MB)
```

**참고:** Sigma-4000도 동일 JIG 보드 사용

---

### 6. L-Titrator (pH Measurement System)

**원본 위치:** `D:\100_Git_HW\00_L_titrator\`  
**프로젝트 기간:** 2018-2020  
**프로젝트 규모:** 309MB, 134 files

**복사된 파일:**
```
Schematics\
  └── L_TITRATOR_MCU_MODULE(V0.1)_20211217A.sch

PCB\
  ├── ATS7704_1_P_L_TITRATOR_MCU_MODULE(V0.1)수정_220427_F.pcb
  └── ATS8051_P_L_TITRATOR_MAIN(V0_2).pcb
```

---

### 7. FPGA Zynq ⭐ FPGA 설계

**원본 위치:** `D:\03_FPGA\Zynq\`  
**프로젝트 기간:** 2024  
**프로젝트 규모:** 5.9GB, 43,474 files

**현재 상태:** 파일 없음 (Vivado 프로젝트 추출 필요)

**추가 예정:**
- [ ] Vivado 블록 다이어그램 PDF
- [ ] Verilog/VHDL 소스 코드 샘플
- [ ] Arty Z7 보드 회로도
- [ ] FPGA 핀 배치도

---

### 10. Lux (Optical Sensor)

**원본 위치:** `D:\100_Git_HW\01_Lux\`  
**프로젝트 기간:** 2023-2024  
**프로젝트 규모:** 250MB

**복사된 파일:**
```
Schematics\
  ├── PD_Board_rev01_240203.sch
  ├── PD_Board_rev01_240220.sch
  └── LD_Board_rev01_240203.sch

PCB\
  ├── PD_Board_rev01_240203.pcb
  ├── PD_Board_rev01_240220.pcb
  └── LD_Board_rev01_240203.pcb
```

---

### 11. ATIK JIG (Test Jig Board)

**원본 위치:** `D:\100_Git_HW\00_ATIK_JIG\`  
**프로젝트 기간:** 2022  
**프로젝트 규모:** 15MB

**복사된 파일:**
```
Schematics\
  └── ATIK_JIG_BOARD(V01)_220510A_V16_2.sch

PCB\ (6개 버전별 파일)
  ├── ATS8009_P_ATIK_JIG_BOARD_V0.1_220503_4.pcb
  ├── ATS8009_P_ATIK_JIG_BOARD_V0.1_220506_10.pcb
  ├── ATS8009_P_ATIK_JIG_BOARD_V0.1_220510_11.pcb
  ├── ATS8009_P_ATIK_JIG_BOARD_V0.1_220510_12.pcb
  ├── ATS8009_P_ATIK_JIG_BOARD_V0.1_220510_13.pcb
  └── ATS8009_P_ATIK_JIG_BOARD_V0.1_220511_F.pcb (최종)
```

---

## 🔧 파일 사용 방법

### 회로도 파일 (.sch)

**프로그램:**
- PADS Logic (Mentor Graphics)
- OrCAD Capture
- 또는 PADS Professional

**PDF 변환:**
```
1. PADS Logic에서 .sch 파일 열기
2. File → Print
3. 프린터: Microsoft Print to PDF
4. 옵션: Color, 600 DPI, A4
5. 저장: PDF\ 폴더에 저장
```

### PCB 파일 (.pcb)

**프로그램:**
- PADS Layout (Mentor Graphics)
- PADS Professional

**3D 뷰 캡처:**
```
1. PADS Layout에서 .pcb 파일 열기
2. View → 3D View
3. 카메라 각도: 45° top-right
4. Tools → Export Image → PNG (1920x1080)
5. 저장: Images\ 폴더에 저장
```

**Gerber 파일 추출:**
```
1. File → CAM
2. CAM Document: 선택 (또는 새로 생성)
3. Generate Files
4. Output: Gerber_Output\ 폴더
```

### PDF 파일

- Adobe Acrobat Reader로 즉시 열람 가능
- 회로도, 블록 다이어그램, 테스트 결과 포함

---

## ✅ 작업 완료 항목

- [x] 프로젝트별 폴더 구조 생성 (11개 프로젝트)
- [x] MS 프로젝트 파일 복사 (5개)
- [x] L-LPC PDF 파일 복사 (10개)
- [x] Nu-2000 파일 복사 (10개)
- [x] Sigma-1000 파일 복사 (2개)
- [x] L-Titrator 파일 복사 (3개)
- [x] Lux 파일 복사 (6개)
- [x] ATIK JIG 파일 복사 (7개)
- [x] 포트폴리오 문서에 파일 위치 표기

---

## ⏳ 향후 작업 예정

### 우선순위 1: PDF 추출
- [ ] MS 프로젝트 회로도 → PDF (3개 보드)
- [ ] L-LPC 회로도 → PDF (메인 보드)
- [ ] Psi-1000 Git에서 추출 → PDF
- [ ] Lux 회로도 → PDF (2개 보드)

### 우선순위 2: Git 레포지토리 추출
- [ ] Psi-1000 최종 버전 체크아웃
- [ ] L-Titrator 최신 버전 확인
- [ ] Epsilon 프로젝트 탐색

### 우선순위 3: FPGA 프로젝트
- [ ] Zynq Vivado 프로젝트 블록 다이어그램
- [ ] Verilog/VHDL 소스 코드 샘플 추출
- [ ] Arty Z7 보드 관련 파일

### 우선순위 4: 코드 샘플
- [ ] GitHub에서 펌웨어 주요 함수 발췌
- [ ] PID 제어 알고리즘 (Nu-2000, Psi-1000)
- [ ] Modbus 프로토콜 구현 (Sigma-1000)
- [ ] IAP Bootloader (L-Titrator)

### 우선순위 5: 이미지 자료
- [ ] PCB 3D 뷰 캡처 (각 프로젝트)
- [ ] 제품 사진 수집
- [ ] 테스트 결과 그래프/차트

---

## 📝 참고 사항

### 파일 크기 관리
- 원본 프로젝트 규모: 총 ~30GB
- 복사된 파일 크기: ~50MB (회로도/PCB만)
- PDF 추가 시 예상: ~150MB
- 코드 샘플 추가 시: ~200MB
- **목표 최종 크기:** < 300MB (포트폴리오 첨부용)

### Backup 파일 제외
복사 시 제외된 파일들:
- `*backup*.pcb` - 백업 파일
- `*modify*.sch` - 수정 중인 파일
- `*temp*.pcb` - 임시 파일

각 프로젝트의 **최종(Final) 버전**만 선별하여 복사했습니다.

### Git 레포지토리
일부 프로젝트는 Git 버전 관리 중:
- `D:\100_Git_HW\` - 하드웨어 Git 레포지토리
- `D:\99_Git\` - 펌웨어 Git 레포지토리

최종 버전 확인이 필요한 경우 Git 히스토리 참조

---

## 🔗 관련 링크

**포트폴리오 문서:**
- `최기용_Senior_Hardware_Engineer_Professional_v2.docx`
- 위치: `D:\Portfolio_Professional\Kiyong_Choi_13yrs_Hardware\`

**원본 프로젝트:**
- `D:\00_Project\` - 연도별 프로젝트
- `D:\100_Git_HW\` - Git 관리 프로젝트
- `D:\03_FPGA\` - FPGA 프로젝트

**GitHub (업로드 완료):**
- ATIK-Hardware-Projects (759MB)
- ATIK-Firmware (85MB)
- FPGA-Projects (120MB)

---

**작성:** 2026-01-13  
**최종 수정:** 2026-01-13  
**버전:** 1.0
