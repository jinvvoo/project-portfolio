"""클라우드 명령으로 GPIO 전원 상태를 제어한 코드의 공개 정리본."""

from __future__ import annotations

import os
import time
from typing import Any

import RPi.GPIO as GPIO
import wiotp.sdk


GPIO_PIN = 27
STATUS_INTERVAL_SECONDS = 4


def required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"환경변수 {name}가 필요합니다.")
    return value


def build_device_options() -> dict[str, Any]:
    return {
        "identity": {
            "orgId": required_env("WIOTP_ORG_ID"),
            "typeId": os.getenv("WIOTP_DEVICE_TYPE", "actuator"),
            "deviceId": required_env("WIOTP_POWER_DEVICE_ID"),
        },
        "auth": {"token": required_env("WIOTP_POWER_TOKEN")},
    }


class PowerController:
    def __init__(self, client: Any) -> None:
        self.client = client
        self.switch_state = "off"

    def publish_state(self) -> None:
        payload = {"d": {"switch_state": self.switch_state}}
        self.client.publishEvent("status", "json", payload, qos=0)

    def handle_command(self, command: Any) -> None:
        """switch_state가 on/off일 때만 GPIO를 바꾸고 처리 결과를 전송한다."""
        requested = command.data.get("d", {}).get("switch_state")
        if requested not in {"on", "off"}:
            return

        self.switch_state = requested
        GPIO.output(GPIO_PIN, requested == "on")
        self.publish_state()


def main() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT, initial=GPIO.LOW)

    client = wiotp.sdk.device.DeviceClient(build_device_options())
    controller = PowerController(client)
    client.commandCallback = controller.handle_command
    client.connect()
    try:
        while True:
            controller.publish_state()
            time.sleep(STATUS_INTERVAL_SECONDS)
    finally:
        client.disconnect()
        GPIO.cleanup(GPIO_PIN)


if __name__ == "__main__":
    main()
