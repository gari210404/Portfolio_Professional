"""
조락현 포트폴리오 노션 자동 생성 스크립트
"""

from notion_client import Client
import json

# Notion API 설정
NOTION_TOKEN = "YOUR_NOTION_TOKEN_HERE"

# 클라이언트 초기화
notion = Client(auth=NOTION_TOKEN)

def search_page(page_name):
    """페이지 검색"""
    try:
        response = notion.search(
            query=page_name,
            filter={"property": "object", "value": "page"}
        )
        if response["results"]:
            for result in response["results"]:
                title = ""
                if "title" in result.get("properties", {}):
                    title_prop = result["properties"]["title"]
                    if title_prop.get("title"):
                        title = title_prop["title"][0]["plain_text"]
                elif "properties" in result:
                    for prop in result["properties"].values():
                        if prop.get("type") == "title" and prop.get("title"):
                            title = prop["title"][0]["plain_text"]
                            break
                
                # child_page인 경우
                if result.get("type") == "child_page":
                    title = result.get("child_page", {}).get("title", "")
                
                print(f"  발견: {title} (ID: {result['id']})")
                if page_name in title or title in page_name:
                    return result["id"]
            
            # 첫 번째 결과 반환
            return response["results"][0]["id"]
        return None
    except Exception as e:
        print(f"검색 오류: {e}")
        return None

def create_portfolio_content(parent_id):
    """포트폴리오 콘텐츠 생성"""
    
    # 메인 페이지 생성
    print("\n?? 포트폴리오 페이지 생성 중...")
    
    portfolio_page = notion.pages.create(
        parent={"page_id": parent_id},
        icon={"type": "emoji", "emoji": "?????"},
        cover={
            "type": "external",
            "external": {"url": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200"}
        },
        properties={
            "title": {
                "title": [{"text": {"content": "조락현 | Senior Embedded Systems Engineer"}}]
            }
        },
        children=[
            # 헤더 섹션
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
                        {"type": "text", "text": {"content": "?? 92lock@kakao.com | ?? 010-7311-0402 | "}, "annotations": {"color": "gray"}},
                        {"type": "text", "text": {"content": "GitHub", "link": {"url": "https://github.com/gari210404"}}, "annotations": {"color": "blue"}}
                    ]
                }
            },
            {"object": "block", "type": "divider", "divider": {}},
            
            # Executive Summary
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Executive Summary"}}]}
            },
            {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": "9년 경력의 시니어 임베디드 시스템 엔지니어로, 하드웨어 설계부터 펌웨어 개발까지 Full-Stack Embedded 개발 전문가입니다. 반도체 공정 장비, 광학 분석 기기, 산업용 제어 시스템의 설계 및 개발에서 검증된 실적을 보유하고 있습니다."}}]
                }
            },
            {"object": "block", "type": "divider", "divider": {}},
            
            # Core Competencies
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Core Competencies"}}]}
            },
            {
                "object": "block",
                "type": "column_list",
                "column_list": {"children": []}
            },
        ]
    )
    
    page_id = portfolio_page["id"]
    print(f"  ? 메인 페이지 생성 완료: {page_id}")
    
    # 핵심 역량 테이블 추가
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "table",
                "table": {
                    "table_width": 3,
                    "has_column_header": True,
                    "has_row_header": False,
                    "children": [
                        {
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "분야"}}],
                                    [{"type": "text", "text": {"content": "기술"}}],
                                    [{"type": "text", "text": {"content": "경력"}}]
                                ]
                            }
                        },
                        {
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Firmware"}}],
                                    [{"type": "text", "text": {"content": "STM32, FreeRTOS, HAL/LL, Bootloader"}}],
                                    [{"type": "text", "text": {"content": "9년"}}]
                                ]
                            }
                        },
                        {
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Hardware"}}],
                                    [{"type": "text", "text": {"content": "Analog/Digital Circuit, PCB Layout"}}],
                                    [{"type": "text", "text": {"content": "9년"}}]
                                ]
                            }
                        },
                        {
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Communication"}}],
                                    [{"type": "text", "text": {"content": "Modbus RTU/ASCII, TCP/IP, CAN"}}],
                                    [{"type": "text", "text": {"content": "8년"}}]
                                ]
                            }
                        },
                        {
                            "type": "table_row",
                            "table_row": {
                                "cells": [
                                    [{"type": "text", "text": {"content": "Control"}}],
                                    [{"type": "text", "text": {"content": "PID, Auto-tuning, State Machine"}}],
                                    [{"type": "text", "text": {"content": "6년"}}]
                                ]
                            }
                        }
                    ]
                }
            }
        ]
    )
    
    # 프로젝트 섹션
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {"object": "block", "type": "divider", "divider": {}},
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Major Projects"}}]}
            }
        ]
    )
    
    # 프로젝트 1: L-LPC
    create_project_toggle(page_id, 
        "1?? L-LPC (H-Sensor) System | 2022-2024 | ? 대표 프로젝트",
        [
            "반도체 저압 챔버 제어 시스템 - Hardware & Firmware Full-Stack 개발",
            "",
            "?? 하드웨어 설계:",
            "? Main Board: STM32H743 (480MHz, 2MB Flash)",
            "? Analog Frontend: 고정밀 TIA (S/N > 60dB)",
            "? FPGA Interface: Xilinx Artix-7 연동",
            "? Power: Multi-rail SMPS (효율 > 90%)",
            "",
            "?? 펌웨어 개발:",
            "? FreeRTOS 기반 멀티태스크 구조 (7개 Task)",
            "? DMA 기반 고속 ADC 데이터 수집",
            "? TCP/IP, Modbus RTU 통신 구현",
            "",
            "?? 디버깅 경험:",
            "? ADC 노이즈 이슈: ±500mV → ±5mV (100배 개선)",
            "? FreeRTOS 데드락 해결: Mutex 순서 통일",
            "",
            "?? 성과: 양산 100+ units, 필드 불량률 < 0.2%"
        ]
    )
    
    # 프로젝트 2: Psi-1000
    create_project_toggle(page_id,
        "2?? Psi-1000/3000 Pressure Controller | 2019-2023 | ? PID 전문",
        [
            "정밀 진공 압력 제어 시스템 - PID 알고리즘 개발 및 최적화",
            "",
            "?? PID 제어 알고리즘:",
            "? Anti-windup, Derivative filtering 구현",
            "? Auto-tuning (Relay Feedback, Z-N Method)",
            "? Cascade control (Pressure + Temperature)",
            "",
            "?? 통신 프로토콜:",
            "? Modbus RTU/ASCII Master/Slave",
            "? Ethernet (Modbus TCP)",
            "? Beckhoff PLC 연동",
            "",
            "?? 성과:",
            "? ±0.1% 압력 제어 정확도 달성",
            "? < 2초 정착 시간 (Step Response)",
            "? 동아대학교 연구 협력"
        ]
    )
    
    # 프로젝트 3: Nu-2000
    create_project_toggle(page_id,
        "3?? Nu-2000 Optical Analysis System | 2021-2022",
        [
            "광학 흡수 분광 시스템 - Multi-channel 펌웨어 개발",
            "",
            "?? 펌웨어 특징:",
            "? FreeRTOS 5개 Task 구조",
            "? 4채널 LED Driver PWM 제어",
            "? 4채널 Photodiode 고속 ADC (250kSPS)",
            "? IAP Bootloader 개발 (UART/USB)",
            "",
            "?? 하드웨어 지원:",
            "? 광학 모듈 Wiki Optics 외주 관리",
            "? Alpha/Beta 버전 수락 시험"
        ]
    )
    
    # 프로젝트 4: MS
    create_project_toggle(page_id,
        "4?? MS (Mass Spectrometer) System | 2024-2025 | ?? 최신",
        [
            "반도체 공정 가스 분석 Mass Spectrometer - 시스템 펌웨어 개발",
            "",
            "? 데이터 수집 펌웨어 개발",
            "? RF 제어 인터페이스",
            "? 통신 프로토콜 구현",
            "? 현재 개발 진행 중"
        ]
    )
    
    # 프로젝트 5: LE_Laser
    create_project_toggle(page_id,
        "5?? LE_Laser (Mantis SSC) | 2025 | ?? 최신",
        [
            "레이저 기반 정밀 센서 시스템",
            "",
            "? STM32G071RB (최신 Cortex-M0+)",
            "? 22-bit ADC 고분해능 측정",
            "? Compact 2-board design",
            "? Low-power operation"
        ]
    )
    
    # 코드 샘플 섹션
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {"object": "block", "type": "divider", "divider": {}},
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Code Samples"}}]}
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": "PID Controller Implementation"}}]}
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "language": "c",
                    "rich_text": [{"type": "text", "text": {"content": """// PID Update Function
float PID_Update(PID_Controller_t* pid, float setpoint, float measurement) {
    float error = setpoint - measurement;
    float dt = 0.001f;  // 1ms sampling
    
    // Proportional
    float P = pid->Kp * error;
    
    // Integral with Anti-windup
    pid->integral += (pid->Ki * dt) * error;
    pid->integral = CLAMP(pid->integral, -pid->integral_max, pid->integral_max);
    
    // Derivative with Low-pass Filter
    float derivative = (error - pid->prev_error) / dt;
    pid->prev_derivative = 0.1f * derivative + 0.9f * pid->prev_derivative;
    float D = pid->Kd * pid->prev_derivative;
    
    pid->prev_error = error;
    return CLAMP(P + pid->integral + D, pid->output_min, pid->output_max);
}"""}}]
                }
            },
            {
                "object": "block",
                "type": "heading_3",
                "heading_3": {"rich_text": [{"type": "text", "text": {"content": "FreeRTOS Task with Queue"}}]}
            },
            {
                "object": "block",
                "type": "code",
                "code": {
                    "language": "c",
                    "rich_text": [{"type": "text", "text": {"content": """// ADC Data Acquisition Task
void ADC_Task(void *argument) {
    uint16_t adc_data[4];
    
    while(1) {
        // DMA 기반 ADC 변환
        HAL_ADC_Start_DMA(&hadc1, (uint32_t*)adc_data, 4);
        
        // 완료 대기
        if (xSemaphoreTake(ADC_Sem, pdMS_TO_TICKS(100)) == pdTRUE) {
            // Queue로 데이터 전송
            xQueueSend(ADC_DataQueue, &adc_data, 0);
        }
        
        osDelay(10);  // 100Hz
    }
}"""}}]
                }
            }
        ]
    )
    
    # 기술 스킬 섹션
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {"object": "block", "type": "divider", "divider": {}},
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "??? Technical Skills"}}]}
            },
            {
                "object": "block",
                "type": "column_list",
                "column_list": {"children": []}
            }
        ]
    )
    
    # 스킬 테이블
    notion.blocks.children.append(
        block_id=page_id,
        children=[
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
                        {"type": "table_row", "table_row": {"cells": [[{"type": "text", "text": {"content": "Control"}}], [{"type": "text", "text": {"content": "PID, Auto-tuning, Kalman Filter, State Machine"}}]]}}
                    ]
                }
            }
        ]
    )
    
    # 성과 섹션
    notion.blocks.children.append(
        block_id=page_id,
        children=[
            {"object": "block", "type": "divider", "divider": {}},
            {
                "object": "block",
                "type": "heading_1",
                "heading_1": {"rich_text": [{"type": "text", "text": {"content": "?? Key Achievements"}}]}
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "12+ 양산 펌웨어 배포, 치명적 버그 Zero"}}]}
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "99.8%+ 시스템 가동률 달성"}}]}
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "PID 라이브러리, IAP Bootloader - 프로젝트 전반 재사용"}}]}
            },
            {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": "20+ 기술 문서, 15+ 사용자 매뉴얼 작성"}}]}
            }
        ]
    )
    
    print(f"\n? 포트폴리오 생성 완료!")
    print(f"?? 페이지 URL: https://notion.so/{page_id.replace('-', '')}")
    
    return page_id


def create_project_toggle(page_id, title, content_lines):
    """프로젝트 토글 블록 생성"""
    # Toggle 블록 생성
    toggle_block = notion.blocks.children.append(
        block_id=page_id,
        children=[
            {
                "object": "block",
                "type": "toggle",
                "toggle": {
                    "rich_text": [{"type": "text", "text": {"content": title}, "annotations": {"bold": True}}],
                    "color": "default",
                    "children": []
                }
            }
        ]
    )
    
    # Toggle 내부에 콘텐츠 추가
    toggle_id = toggle_block["results"][0]["id"]
    
    children = []
    for line in content_lines:
        if line.startswith("?"):
            children.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {"rich_text": [{"type": "text", "text": {"content": line[2:]}}]}
            })
        elif line.startswith("??") or line.startswith("??") or line.startswith("??") or line.startswith("??") or line.startswith("??"):
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": line}, "annotations": {"bold": True}}]}
            })
        elif line == "":
            continue
        else:
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {"rich_text": [{"type": "text", "text": {"content": line}}]}
            })
    
    if children:
        notion.blocks.children.append(block_id=toggle_id, children=children)


def main():
    print("=" * 50)
    print("?? 조락현 포트폴리오 노션 자동 생성")
    print("=" * 50)
    
    # 페이지 검색
    print("\n?? '새 페이지' 검색 중...")
    parent_id = search_page("새 페이지")
    
    if parent_id:
        print(f"  ? 페이지 발견: {parent_id}")
        
        # 포트폴리오 생성
        create_portfolio_content(parent_id)
    else:
        print("  ? '새 페이지'를 찾을 수 없습니다.")
        print("\n?? 해결 방법:")
        print("  1. 노션에서 '새 페이지' 열기")
        print("  2. 우측 상단 '...' → 'Connections' → Integration 추가")
        print("  3. 스크립트 다시 실행")


if __name__ == "__main__":
    main()
