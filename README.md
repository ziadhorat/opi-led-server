# Orange Pi LED Control Container

This Docker container hosts a Flask API to control the onboard LEDs of an Orange Pi. It provides endpoints to turn each LED on or off and to test the LEDs by cycling through colors.

## Requirements
- Docker installed on the Orange Pi.
- LEDs exposed through `/sys/class/leds` (e.g., `green_led`, `blue_led`).

## Setup and Usage

### 1. Mounting LED Directories

The container needs access to the `/sys/class/leds` directory on the Orange Pi to control the LEDs. When starting the container, mount this directory as a volume.

```bash
docker run -d \
  --name orange_pi_led_control \
  -p 5000:5000 \
  --mount type=bind,source=/sys/class/leds,target=/sys/class/leds \
  orangepi/led-control
```
