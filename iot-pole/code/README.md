# 공개 코드 안내

이 폴더는 2021년 전신주 최종 프로젝트에 사용한 코드 5개를 포트폴리오에서 읽을 수 있도록 정리한 사본입니다.

| 파일 | 기능 |
|---|---|
| `dht11_watson.py` | DHT11 온도·습도 수집 → IBM Watson IoT 이벤트 전송 |
| `pms7003_watson.py` | PMS7003 프레임 검증·PM 값 추출 → IBM Watson IoT 이벤트 전송 |
| `tilt_sensor_watson.py` | 기울기 상태 수집 → IBM Watson IoT 이벤트 전송 |
| `impact_sensor_watson.py` | 충격 상태 수집 → IBM Watson IoT 이벤트 전송 |
| `power_control_watson.py` | 클라우드 명령 수신 → GPIO 전원 상태 변경·결과 전송 |

원본에 하드코딩돼 있던 조직·장치·인증 정보는 제거했습니다. 실행하려면 각 파일에 적힌 환경변수와 Raspberry Pi 하드웨어용 라이브러리가 필요합니다.

이 코드는 현재 환경의 실행 예제가 아니라 당시 구현 흐름을 설명하는 공개 정리본입니다. 난방 실습·강의 샘플과 중간 실패본은 전신주 최종 프로젝트 코드가 아니므로 포함하지 않았습니다.

## 원본 파일명

| 원본 | 공개 정리본 |
|---|---|
| `dht11.py` | `dht11_watson.py` |
| `PMS7003.py` | `pms7003_watson.py` |
| `cldoudTiltS.py` | `tilt_sensor_watson.py` |
| `crashCloudS.py` | `impact_sensor_watson.py` |
| `led5.py` | `power_control_watson.py` |

파일명은 센서와 역할이 바로 드러나도록 정리했습니다. 원본의 장치 인증값은 환경변수로 바꾸고, 예외 처리와 종료 시 연결·GPIO 정리를 보완했습니다.
