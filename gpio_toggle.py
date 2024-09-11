import os
import time

# GPIO 핀 번호 (사용할 핀 번호 설정)
GPIO_PIN = 112  # 원하는 GPIO 핀 번호로 변경 가능

# GPIO 초기화 함수
def gpio_setup(pin):
    # GPIO 핀이 이미 export되어 있는지 확인
    if not os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/export", "w") as f:
            f.write(str(pin))

    # 핀 모드 설정 (출력 모드)
    with open(f"/sys/class/gpio/gpio{pin}/direction", "w") as f:
        f.write("out")

# GPIO 상태 쓰기 함수 (0: 끄기, 1: 켜기)
def gpio_write(pin, value):
    with open(f"/sys/class/gpio/gpio{pin}/value", "w") as f:
        f.write(str(value))

# GPIO 해제 함수
def gpio_cleanup(pin):
    if os.path.exists(f"/sys/class/gpio/gpio{pin}"):
        with open("/sys/class/gpio/unexport", "w") as f:
            f.write(str(pin))

try:
    # GPIO 핀 초기화
    gpio_setup(GPIO_PIN)

    # GPIO 핀 토글 반복
    while True:
        # GPIO 켜기
        gpio_write(GPIO_PIN, 1)
        print(f"GPIO {GPIO_PIN} 켜짐")
        time.sleep(1)  # 1초 대기

        # GPIO 끄기
        gpio_write(GPIO_PIN, 0)
        print(f"GPIO {GPIO_PIN} 꺼짐")
        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:
    print("프로그램 종료")

finally:
    # GPIO 핀 해제
    gpio_cleanup(GPIO_PIN)
