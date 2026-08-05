import machine
import time

# Pin configuration
ENABLE_PIN = 10   # Active LOW on A4988 — pull LOW to enable motor
STEP_PIN   = 11
DIR_PIN    = 12
LED_PIN    = "LED"

# Motor configuration
# A4988 microstepping (set MS1/MS2/MS3 pins or jumpers on the board):
#   Full step   → 200 steps/rev
#   Half step   → 400 steps/rev
#   Quarter     → 800 steps/rev
#   Eighth      → 1600 steps/rev
#   Sixteenth   → 3200 steps/rev
STEPS_PER_REV = 400   # Assumes half-step mode on A4988 !!DON'T CHANGE!!
DUTY_CYCLE    = 0.25  # 25%

# Setup pins
step   = machine.Pin(STEP_PIN,   machine.Pin.OUT)
dirpin = machine.Pin(DIR_PIN,    machine.Pin.OUT)
enable = machine.Pin(ENABLE_PIN, machine.Pin.OUT)
led    = machine.Pin(LED_PIN,    machine.Pin.OUT)

# Enable the driver (active LOW)
enable.off()

def blink_led(times, gap):
    """Blink onboard LED a given number of times with a gap (in seconds)."""
    for _ in range(times):
        led.on()
        time.sleep(1)
        led.off()
        time.sleep(gap)

def pulse_step(freq_hz=1000):
    """
    Send a single step pulse at 25% duty cycle.
    A4988 minimum pulse width: 1µs HIGH, 1µs LOW — well within these timings.
    """
    period_us   = int(1_000_000 / freq_hz)
    on_time_us  = int(period_us * DUTY_CYCLE)
    off_time_us = period_us - on_time_us

    step.on()
    time.sleep_us(on_time_us)
    step.off()
    time.sleep_us(off_time_us)

def rotate(revolutions, dir_val, freq_hz=1000, pause_every=None, pause_duration_s=0):
    """
    Rotate the motor for a given number of revolutions.
    """
    dirpin.value(dir_val)
    total_steps = revolutions * STEPS_PER_REV

    for s in range(1, total_steps + 1):
        pulse_step(freq_hz)
        if pause_every is not None:
            if s % (pause_every * STEPS_PER_REV) == 0:
                time.sleep(pause_duration_s)

def shutdown():
    """Disable driver to reduce heat when idle."""
    enable.on()  # Active LOW, so HIGH = disabled

# ── MAIN SEQUENCE ────────────────────────────────────────────────

blink_led(times=3, gap=1)

print("Phase 1: Rotating 323 revs, direction = 0")
rotate(revolutions=323, dir_val=0)

print("Phase 2: Rotating 323 revs, direction = 1, pause every 10 revs")
rotate(revolutions=323, dir_val=1, pause_every=10, pause_duration_s=1)

shutdown()
print("Done!")