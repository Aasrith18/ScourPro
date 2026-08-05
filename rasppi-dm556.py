import machine
import time

# Pin configuration
PULSE_PIN = 16
DIR_PIN = 17
LED_PIN = "LED"  # Onboard LED for Pico 2

# Motor configuration
STEPS_PER_REV = 400
DUTY_CYCLE = 0.25  # 25%

# Setup pins
pulse = machine.Pin(PULSE_PIN, machine.Pin.OUT)
direction = machine.Pin(DIR_PIN, machine.Pin.OUT)
led = machine.Pin(LED_PIN, machine.Pin.OUT)

def blink_led(times, gap):
    """Blink onboard LED a given number of times with a millisecond gap."""
    for _ in range(times):
        led.on()
        time.sleep(1)   # LED on duration
        led.off()
        time.sleep(gap)  # Gap between blinks

def pulse_step(freq_hz=1000):
    """
    Send a single step pulse respecting 25% duty cycle.
    At freq_hz, period = 1/freq_hz seconds.
    ON time  = 25% of period
    OFF time = 75% of period
    """
    period_us = int(1_000_000 / freq_hz)
    on_time_us  = int(period_us * DUTY_CYCLE)       # 25%
    off_time_us = period_us - on_time_us             # 75%

    pulse.on()
    time.sleep_us(on_time_us)
    pulse.off()
    time.sleep_us(off_time_us)

def rotate(revolutions, dir_val, freq_hz=1000, pause_every=None, pause_duration_s=0):
    """
    Rotate the motor for a given number of revolutions.
    
    :param revolutions:     Number of full revolutions
    :param dir_val:         Direction pin value (0 or 1)
    :param freq_hz:         Step frequency in Hz
    :param pause_every:     Pause after every N revolutions (None = no pause)
    :param pause_duration_s: Duration of each pause in seconds
    """
    direction.value(dir_val)
    total_steps = revolutions * STEPS_PER_REV

    for step in range(1, total_steps + 1):
        pulse_step(freq_hz)

        # Pause logic: check after completing a full revolution boundary
        if pause_every is not None:
            if step % (pause_every * STEPS_PER_REV) == 0:
                time.sleep(pause_duration_s)

# ── MAIN SEQUENCE ────────────────────────────────────────────────

# Step 1: Blink LED 3 times with 1 ms gap
blink_led(times=3, gap=1)

# Step 2: Rotate 323 revolutions in direction 0 continuously
print("Phase 1: Rotating 323 revs, direction = 0")
rotate(revolutions=323, dir_val=0)

# Step 3 & 4: Change direction to 1, rotate 323 revolutions
#             with a 1-second pause after every 10 revolutions
print("Phase 2: Rotating 323 revs, direction = 1, pause every 10 revs")
rotate(
    revolutions=323,
    dir_val=1,
    pause_every=10,
    pause_duration_s=1
)

print("Done!")
