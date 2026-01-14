"""
조락현 포트폴리오 노션 생성 스크립트
"""
from notion_client import Client

NOTION_TOKEN = "YOUR_NOTION_TOKEN_HERE"
PARENT_ID = "2e8f0746-9821-809c-9331-e34ae2d5e03e"

notion = Client(auth=NOTION_TOKEN)

print("=" * 60)
print("?? 조락현 포트폴리오 노션 자동 생성")
print("=" * 60)

# 1. 메인 페이지 생성
print("\n?? 메인 페이지 생성 중...")

page = notion.pages.create(
    parent={"page_id": PARENT_ID},
    icon={"type": "emoji", "emoji": "?????"},
    cover={
        "type": "external",
        "external": {"url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200"}
    },
    properties={
        "title": {"title": [{"text": {"content": "조락현 | Senior Embedded Systems Engineer (9년)"}}]}
    },
    children=[
        # 헤더 Callout
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "??"},
                "color": "blue_background",
                "rich_text": [{"type": "text", "text": {"content": "9년 경력 | Hardware & Firmware Full-Stack 개발 | STM32 Expert | FreeRTOS | PID Control"}}]
            }
        },
        # 연락처
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": "?? 92lock@kakao.com  |  ?? 010-7311-0402  |  "}, "annotations": {"color": "gray"}},
                    {"type": "text", "text": {"content": "?? GitHub", "link": {"url": "https://github.com/gari210404"}}, "annotations": {"color": "blue"}}
                ]
            }
        },
        {"object": "block", "type": "divider", "divider": {}},
    ]
)

page_id = page["id"]
print(f"  ? 메인 페이지 생성: {page_id}")

# 2. Executive Summary
print("\n?? Executive Summary 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Executive Summary"}}]}},
        {
            "object": "block",
            "type": "quote",
            "quote": {
                "rich_text": [{"type": "text", "text": {"content": "9년 경력의 시니어 임베디드 시스템 엔지니어로, 하드웨어 설계부터 펌웨어 개발까지 Full-Stack Embedded 개발 전문가입니다. 반도체 공정 장비, 광학 분석 기기, 산업용 제어 시스템의 설계 및 개발에서 검증된 실적을 보유하고 있습니다."}}]
            }
        },
        {"object": "block", "type": "divider", "divider": {}},
    ]
)

# 3. Core Competencies
print("?? Core Competencies 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Core Competencies"}}]}},
        {
            "object": "block",
            "type": "table",
            "table": {
                "table_width": 3,
                "has_column_header": True,
                "has_row_header": False,
                "children": [
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "분야"}}], [{"type": "text", "text": {"content": "기술"}}], [{"type": "text", "text": {"content": "경력"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "?? Firmware"}}], [{"type": "text", "text": {"content": "STM32, FreeRTOS, HAL/LL, Bootloader"}}], [{"type": "text", "text": {"content": "9년"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "? Hardware"}}], [{"type": "text", "text": {"content": "Analog/Digital Circuit, PCB Layout"}}], [{"type": "text", "text": {"content": "9년"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "?? Communication"}}], [{"type": "text", "text": {"content": "Modbus RTU/ASCII/TCP, UART, SPI, I2C, CAN"}}], [{"type": "text", "text": {"content": "8년"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "??? Control"}}], [{"type": "text", "text": {"content": "PID, Auto-tuning, State Machine, Kalman"}}], [{"type": "text", "text": {"content": "6년"}}]]}},
                ]
            }
        },
        {"object": "block", "type": "divider", "divider": {}},
    ]
)

# 4. Projects
print("?? Major Projects 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Major Projects"}}]}},
    ]
)

# Project 1: L-LPC
toggle1 = notion.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"type": "text", "text": {"content": "1?? L-LPC (H-Sensor) System | 2022-2024 | ? 대표 프로젝트"}, "annotations": {"bold": True}}],
                "color": "blue_background"
            }
        }
    ]
)

notion.blocks.children.append(
    block_id=toggle1["results"][0]["id"],
    children=[
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "반도체 저압 챔버 제어 시스템 - Hardware & Firmware Full-Stack 개발"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "?? 하드웨어 설계:"}, "annotations": {"bold": True, "color": "blue"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Main Board: STM32H743 (480MHz, 2MB Flash, 1MB RAM)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Analog Frontend: 고정밀 TIA (S/N > 60dB)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "FPGA Interface: Xilinx Artix-7 연동"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Power: Multi-rail SMPS (효율 > 90%, Ripple < 30mVpp)"}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "?? 펌웨어 개발:"}, "annotations": {"bold": True, "color": "purple"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "FreeRTOS 기반 멀티태스크 구조 (7개 Task)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "DMA 기반 고속 ADC 데이터 수집 (2MSPS)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "TCP/IP (lwIP), Modbus RTU 통신 구현"}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "?? 디버깅 경험:"}, "annotations": {"bold": True, "color": "red"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "ADC 노이즈 이슈: ±500mV → ±5mV (100배 개선)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "FreeRTOS 데드락 해결: Mutex 획득 순서 통일"}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "callout", "callout": {"icon": {"type": "emoji", "emoji": "??"}, "color": "green_background", "rich_text": [{"type": "text", "text": {"content": "성과: 양산 100+ units, 필드 불량률 < 0.2%"}}]}},
    ]
)

# Project 2: Psi-1000
toggle2 = notion.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"type": "text", "text": {"content": "2?? Psi-1000/3000 Pressure Controller | 2019-2023 | ? PID 전문"}, "annotations": {"bold": True}}],
                "color": "purple_background"
            }
        }
    ]
)

notion.blocks.children.append(
    block_id=toggle2["results"][0]["id"],
    children=[
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "정밀 진공 압력 제어 시스템 - PID 알고리즘 개발 및 최적화"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "??? PID 제어 알고리즘:"}, "annotations": {"bold": True, "color": "purple"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Anti-windup, Derivative filtering 구현"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Auto-tuning (Relay Feedback, Z-N Method)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Cascade control (Pressure + Temperature)"}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "?? 통신 프로토콜:"}, "annotations": {"bold": True, "color": "blue"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Modbus RTU/ASCII Master/Slave 구현"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Ethernet (Modbus TCP)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Beckhoff PLC 연동"}}]}},
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": ""}}]}},
        {"object": "block", "type": "callout", "callout": {"icon": {"type": "emoji", "emoji": "??"}, "color": "green_background", "rich_text": [{"type": "text", "text": {"content": "성과: ±0.1% 압력 정확도, < 2초 정착시간, 동아대 연구 협력"}}]}},
    ]
)

# Project 3: Nu-2000
toggle3 = notion.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"type": "text", "text": {"content": "3?? Nu-2000 Optical Analysis System | 2021-2022"}, "annotations": {"bold": True}}],
                "color": "yellow_background"
            }
        }
    ]
)

notion.blocks.children.append(
    block_id=toggle3["results"][0]["id"],
    children=[
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "광학 흡수 분광 시스템 - Multi-channel 펌웨어 개발"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "FreeRTOS 5개 Task 구조"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "4채널 LED Driver PWM 제어"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "4채널 Photodiode 고속 ADC (250kSPS)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "IAP Bootloader 개발 (UART/USB)"}}]}},
    ]
)

# Project 4: MS
toggle4 = notion.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"type": "text", "text": {"content": "4?? MS (Mass Spectrometer) | 2024-2025 | ?? 최신"}, "annotations": {"bold": True}}],
                "color": "green_background"
            }
        }
    ]
)

notion.blocks.children.append(
    block_id=toggle4["results"][0]["id"],
    children=[
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "반도체 공정 가스 분석 Mass Spectrometer"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "데이터 수집 펌웨어 개발"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "RF 제어 인터페이스"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "통신 프로토콜 구현"}}]}},
    ]
)

# Project 5: LE_Laser
toggle5 = notion.blocks.children.append(
    block_id=page_id,
    children=[
        {
            "object": "block",
            "type": "toggle",
            "toggle": {
                "rich_text": [{"type": "text", "text": {"content": "5?? LE_Laser (Mantis SSC) | 2025 | ?? 최신"}, "annotations": {"bold": True}}],
                "color": "orange_background"
            }
        }
    ]
)

notion.blocks.children.append(
    block_id=toggle5["results"][0]["id"],
    children=[
        {"object": "block", "type": "paragraph", "paragraph": {"rich_text": [{"type": "text", "text": {"content": "레이저 기반 정밀 센서 시스템"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "STM32G071RB (최신 Cortex-M0+)"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "22-bit ADC 고분해능 측정"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "Compact 2-board design"}}]}},
    ]
)

# 5. Code Samples
print("?? Code Samples 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "divider", "divider": {}},
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Code Samples"}}]}},
        {"object": "block", "type": "heading_3", "heading_3": {"rich_text": [{"type": "text", "text": {"content": "PID Controller Implementation"}}]}},
        {
            "object": "block",
            "type": "code",
            "code": {
                "language": "c",
                "rich_text": [{"type": "text", "text": {"content": """// PID Update with Anti-windup
float PID_Update(PID_t* pid, float setpoint, float measurement) {
    float error = setpoint - measurement;
    
    // Proportional
    float P = pid->Kp * error;
    
    // Integral with Anti-windup
    pid->integral += pid->Ki * 0.001f * error;
    pid->integral = CLAMP(pid->integral, -pid->i_max, pid->i_max);
    
    // Derivative with Filter
    float deriv = (error - pid->prev_error) / 0.001f;
    pid->filtered_d = 0.1f * deriv + 0.9f * pid->filtered_d;
    float D = pid->Kd * pid->filtered_d;
    
    pid->prev_error = error;
    return CLAMP(P + pid->integral + D, pid->out_min, pid->out_max);
}"""}}]
            }
        },
        {"object": "block", "type": "heading_3", "heading_3": {"rich_text": [{"type": "text", "text": {"content": "FreeRTOS Task with Queue"}}]}},
        {
            "object": "block",
            "type": "code",
            "code": {
                "language": "c",
                "rich_text": [{"type": "text", "text": {"content": """// ADC Acquisition Task
void ADC_Task(void *arg) {
    uint16_t adc_data[4];
    
    while(1) {
        HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_data, 4);
        
        if (xSemaphoreTake(ADC_Sem, pdMS_TO_TICKS(100)) == pdTRUE) {
            xQueueSend(ADC_Queue, &adc_data, 0);
        }
        osDelay(10);  // 100Hz
    }
}"""}}]
            }
        },
    ]
)

# 6. Technical Skills
print("??? Technical Skills 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "divider", "divider": {}},
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "??? Technical Skills"}}]}},
        {
            "object": "block",
            "type": "table",
            "table": {
                "table_width": 2,
                "has_column_header": True,
                "has_row_header": False,
                "children": [
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Category"}}], [{"type": "text", "text": {"content": "Technologies"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "MCU"}}], [{"type": "text", "text": {"content": "STM32 F1/F4/F7/H7/G0, ARM Cortex-M"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "RTOS"}}], [{"type": "text", "text": {"content": "FreeRTOS (Task, Queue, Semaphore, Mutex)"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Languages"}}], [{"type": "text", "text": {"content": "C (Expert), C++, Python"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Protocols"}}], [{"type": "text", "text": {"content": "Modbus RTU/ASCII/TCP, UART, SPI, I2C, CAN"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Tools"}}], [{"type": "text", "text": {"content": "STM32CubeIDE, Altium Designer, Git, Logic Analyzer"}}]]}},
                    {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Control"}}], [{"type": "text", "text": {"content": "PID, Auto-tuning, Kalman Filter, State Machine"}}]]}},
                ]
            }
        },
    ]
)

# 7. Key Achievements
print("?? Key Achievements 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "divider", "divider": {}},
        {"object": "block", "type": "heading_1", "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Key Achievements"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "12+ 양산 펌웨어 배포, 치명적 버그 Zero"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "99.8%+ 시스템 가동률 달성"}, "annotations": {"bold": True}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "PID 라이브러리, IAP Bootloader - 5개 제품 재사용"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "20+ 기술 문서, 15+ 사용자 매뉴얼 작성"}}]}},
        {"object": "block", "type": "bulleted_list_item", "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "동아대학교 PID 알고리즘 연구 협력"}}]}},
    ]
)

# 8. Footer
print("?? Contact 추가...")
notion.blocks.children.append(
    block_id=page_id,
    children=[
        {"object": "block", "type": "divider", "divider": {}},
        {
            "object": "block",
            "type": "callout",
            "callout": {
                "icon": {"type": "emoji", "emoji": "??"},
                "color": "gray_background",
                "rich_text": [{"type": "text", "text": {"content": "Contact: 92lock@kakao.com | 010-7311-0402 | github.com/gari210404"}}]
            }
        },
    ]
)

print("\n" + "=" * 60)
print("? 포트폴리오 생성 완료!")
print("=" * 60)
print(f"\n?? 페이지 URL: https://notion.so/{page_id.replace('-', '')}")
print("\n노션에서 '새 페이지' 하위에서 확인하세요!")
