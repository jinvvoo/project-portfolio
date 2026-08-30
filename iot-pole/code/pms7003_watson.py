"""PMS7003 미세먼지 값을 IBM Watson IoT로 전송한 코드의 공개 정리본.

프레임 검증과 PM 값 추출은 PMS7003의 32바이트 직렬 프로토콜을 따른다.
실제 조직 ID, 장치 ID, 토큰은 환경변수에서 읽는다.
"""

from __future__ import annotations

import os
import struct
import time
from dataclasses import dataclass
from typing import Any

import serial
import wiotp.sdk


FRAME_SIZE = 32
HEADER = b"\x42\x4d"
SERIAL_PORT = os.getenv("PMS7003_SERIAL_PORT", "/dev/ttyUSB0")
BAUD_RATE = 9600
PUBLISH_INTERVAL_SECONDS = 2


@dataclass(frozen=True)
class DustMeasurement:
    pm1: int
    pm2_5: int
    pm10: int

    def as_event(self) -> dict[str, dict[str, int]]:
        return {"d": {"pm1": self.pm1, "pm2_5": self.pm2_5, "pm10": self.pm10}}


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
            "deviceId": required_env("WIOTP_PMS7003_DEVICE_ID"),
        },
        "auth": {"token": required_env("WIOTP_PMS7003_TOKEN")},
    }


def read_frame(port: serial.Serial) -> bytes:
    """0x42 0x4d 헤더를 찾은 뒤 한 프레임을 읽는다."""
    while True:
        if port.read(1) != HEADER[:1]:
            continue
        if port.read(1) == HEADER[1:]:
            return HEADER + port.read(FRAME_SIZE - len(HEADER))


def parse_frame(frame: bytes) -> DustMeasurement:
    """길이·헤더·체크섬을 확인하고 CF=1 기준 PM 값을 추출한다."""
    if len(frame) != FRAME_SIZE:
        raise ValueError(f"PMS7003 프레임 길이 오류: {len(frame)}")
    if not frame.startswith(HEADER):
        raise ValueError("PMS7003 프레임 헤더 오류")

    expected_checksum = int.from_bytes(frame[-2:], byteorder="big")
    if sum(frame[:-2]) != expected_checksum:
        raise ValueError("PMS7003 프레임 체크섬 오류")

    unpacked = struct.unpack(">2B13H2BH", frame)
    return DustMeasurement(
        pm1=unpacked[3],
        pm2_5=unpacked[4],
        pm10=unpacked[5],
    )


def main() -> None:
    client = wiotp.sdk.device.DeviceClient(build_device_options())
    client.connect()
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as port:
            while True:
                try:
                    measurement = parse_frame(read_frame(port))
                    client.publishEvent("status", "json", measurement.as_event(), qos=0)
                except ValueError as error:
                    print(error)
                time.sleep(PUBLISH_INTERVAL_SECONDS)
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()
