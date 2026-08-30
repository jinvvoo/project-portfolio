# 프로젝트 코드 안내

2021년 전신주 최종 프로젝트에 사용한 코드 5개를 센서와 역할이 바로 드러나도록 정리했습니다.

| 파일 | 기능 |
|---|---|
| `dht11_watson.py` | DHT11 온도·습도 수집 → IBM Watson IoT 이벤트 전송 |
| `pms7003_watson.py` | PMS7003 프레임 검증·PM 값 추출 → IBM Watson IoT 이벤트 전송 |
| `tilt_sensor_watson.py` | 기울기 상태 수집 → IBM Watson IoT 이벤트 전송 |
| `impact_sensor_watson.py` | 충격 상태 수집 → IBM Watson IoT 이벤트 전송 |
| `power_control_watson.py` | 클라우드 명령 수신 → GPIO 전원 상태 변경·결과 전송 |

조직·장치·인증 정보는 환경변수로 분리했습니다. 실행하려면 각 파일에 적힌 환경변수와 Raspberry Pi 하드웨어용 라이브러리가 필요합니다.

센서 데이터 수집, IBM Watson IoT 전송, 기울기·충격 감지와 전원 제어 흐름을 코드에서 확인할 수 있습니다.

## 파일명 정리

| 원본 | 공개 정리본 |
|---|---|
| `dht11.py` | `dht11_watson.py` |
| `PMS7003.py` | `pms7003_watson.py` |
| `cldoudTiltS.py` | `tilt_sensor_watson.py` |
| `crashCloudS.py` | `impact_sensor_watson.py` |
| `led5.py` | `power_control_watson.py` |

센서와 역할이 바로 드러나도록 파일명을 정리하고, 인증 정보는 환경변수로 분리했습니다. 예외 처리와 종료 시 연결·GPIO 정리도 함께 보완했습니다.
