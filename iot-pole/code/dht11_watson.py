"""DHT11 값을 IBM Watson IoT Platform으로 전송한 코드의 공개 정리본.

실제 조직 ID, 장치 ID, 토큰은 저장소에 두지 않고 환경변수에서 읽는다.
"""

from __future__ import annotations

import os
import time
from typing import Any

import Adafruit_DHT
import wiotp.sdk


SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 4
PUBLISH_INTERVAL_SECONDS = 10


def required_env(name: str) -> str:
    """필수 환경변수가 없으면 인증 시도 전에 명확히 중단한다."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"환경변수 {name}가 필요합니다.")
    return value


def build_device_options() -> dict[str, Any]:
    """IBM Watson IoT 장치 설정을 공개 가능한 환경변수로 구성한다."""
    return {
        "identity": {
            "orgId": required_env("WIOTP_ORG_ID"),
            "typeId": os.getenv("WIOTP_DEVICE_TYPE", "sensor"),
            "deviceId": required_env("WIOTP_DHT11_DEVICE_ID"),
        },
        "auth": {"token": required_env("WIOTP_DHT11_TOKEN")},
    }


def read_measurement() -> dict[str, dict[str, float]]:
    """DHT11을 읽고 당시 대시보드에서 사용한 temp/humi JSON으로 만든다."""
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)
    if humidity is None or temperature is None:
        raise RuntimeError("DHT11 값을 읽지 못했습니다.")

    return {
        "d": {
            "temp": round(float(temperature), 1),
            "humi": round(float(humidity), 1),
        }
    }


def main() -> None:
    client = wiotp.sdk.device.DeviceClient(build_device_options())
    client.connect()
    try:
        while True:
            try:
                payload = read_measurement()
                client.publishEvent("status", "json", payload, qos=0)
            except RuntimeError as error:
                print(error)
            time.sleep(PUBLISH_INTERVAL_SECONDS)
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
