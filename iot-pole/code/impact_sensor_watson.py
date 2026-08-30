"""충격 센서 상태를 IBM Watson IoT로 전송한 코드의 공개 정리본."""

from __future__ import annotations

import os
import time
from typing import Any

import RPi.GPIO as GPIO
import wiotp.sdk


GPIO_PIN = 3
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
            "deviceId": required_env("WIOTP_IMPACT_DEVICE_ID"),
        },
        "auth": {"token": required_env("WIOTP_IMPACT_TOKEN")},
    }


def read_impact() -> dict[str, dict[str, int]]:
    """원본 대시보드 표현에 맞춰 정상 0, 충격 감지 30으로 변환한다."""
    impact = 0 if GPIO.input(GPIO_PIN) == GPIO.HIGH else 30
    return {"d": {"sense_impact": impact}}


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)
    client = wiotp.sdk.device.DeviceClient(build_device_options())
    client.connect()
    try:
        while True:
            client.publishEvent("status", "json", read_impact(), qos=0)
            time.sleep(PUBLISH_INTERVAL_SECONDS)
    finally:
        client.disconnect()
        GPIO.cleanup(GPIO_PIN)


if __name__ == "__main__":
    main()
