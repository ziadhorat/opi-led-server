# app.py

from flask import Flask, jsonify, request
import os
import time

app = Flask(__name__)

LED_PATH = "/sys/class/leds"
LED_COLORS = ["green_led", "blue_led"]

def set_led_color(color, state):
    """Set LED color state (on/off)."""
    for led in LED_COLORS:
        brightness_path = os.path.join(LED_PATH, led, "brightness")
        trigger_path = os.path.join(LED_PATH, led, "trigger")
        
        if led == color and state == "on":
            # Turn on the specified LED
            with open(trigger_path, 'w') as f:
                f.write("none")
            with open(brightness_path, 'w') as f:
                f.write("1")
        else:
            # Turn off all other LEDs
            with open(trigger_path, 'w') as f:
                f.write("none")
            with open(brightness_path, 'w') as f:
                f.write("0")

@app.route("/led/<color>/on", methods=["POST"])
def turn_on_led(color):
    if color not in LED_COLORS:
        return jsonify({"error": "Invalid color"}), 400
    set_led_color(color, "on")
    return jsonify({"message": f"{color} LED turned on"}), 200

@app.route("/led/<color>/off", methods=["POST"])
def turn_off_led(color):
    if color not in LED_COLORS:
        return jsonify({"error": "Invalid color"}), 400
    set_led_color(color, "off")
    return jsonify({"message": f"{color} LED turned off"}), 200

@app.route("/led/test", methods=["POST"])
def test_led():
    """Cycle through LEDs, turning each on for 5 seconds."""
    for color in LED_COLORS:
        set_led_color(color, "on")
        time.sleep(5)
        set_led_color(color, "off")
    return jsonify({"message": "LED test completed"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

