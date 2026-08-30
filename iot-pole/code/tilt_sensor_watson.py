"""기울기 센서 상태를 IBM Watson IoT로 전송한 코드의 공개 정리본."""

from __future__ import annotations

import os
import time
from typing import Any

import RPi.GPIO as GPIO
import wiotp.sdk


GPIO_PIN = 2
PUBLISH_INTERVAL_SECONDS = 2


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"환경변수 {name}가 필요합니다.")
    return value


def build_device_options() -> dict[str, Any]:
    return {
        "identity": {
            "orgId": required_env("WIOTP_ORG_ID"),
            "typeId": os.getenv("WIOTP_DEVICE_TYPE", "sensor"),
            "deviceId": required_env("WIOTP_TILT_DEVICE_ID"),
        },
        "auth": {"token": required_env("WIOTP_TILT_TOKEN")},
    }


def read_inclination() -> dict[str, dict[str, int]]:
    """원본 대시보드 표현에 맞춰 정상 0, 기울어짐 30으로 변환한다."""
    inclination = 30 if GPIO.input(GPIO_PIN) == GPIO.HIGH else 0
    return {"d": {"inclination": inclination}}


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    client = wiotp.sdk.device.DeviceClient(build_device_options())
    client.connect()
    try:
        while True:
            client.publishEvent("status", "json", read_inclination(), qos=0)
            time.sleep(PUBLISH_INTERVAL_SECONDS)
    finally:
        client.disconnect()
        GPIO.cleanup(GPIO_PIN)


if __name__ == "__main__":
    main()
