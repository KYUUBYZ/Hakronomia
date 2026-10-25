import time
import math 
import array
import board
import busio
import digitalio
import rotaryio
import audiobusio
import audiomixer
import synthio
import displayio
import terminalio
import adafruit_mpr121

try:
    import i2cdisplaybus
    I2CBus = i2cdisplaybus.I2CDisplayBus
except ImportError:
    I2CBus = displayio.I2CDisplay


# ============================== CONFIG ========================== #
SAMPLE_RATE = 22050         
NOTE_AMP = 0.25                 # Notes volume
BASE_NOTE = 60                  # Hakronomia first key on the piano (60 = C4)
ENC_DIVISOR = 4
DEBOUNCE_MS = 25
LONG_MS = 800

# I2S to PCM5102A (BCK and LRCK must be consecutive)
PIN_BCK, PIN_LRCK, PIN_DIN = board.GP0, board.GP1, board.GP2
# I2C addresses (MPR121 to 0x5A, Oled to 0x3C)
PIN_SDA, PIN_SCL, = board.GP14, board.GP15

# if your ecnoder is clockwhise, change True/False
ENC_MIX = (board.GP26, board.GP27, board.GP5, False)    # SW1
ENC_VOL = (board.GP12, board.GP13, board.GP6, True)     # SW2
ENC_OCT = (board.GP10, board.GP11, board.GP7, True)     # SW3
PIN_SW4 = board.GP9

NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#" "B"]

# ======================== SOUND WAVES ========================== #
TABLE_SIZE = 512

def make_table(f, level):
    return array.array(
        "h", [int(level * fn(i / TABLE_SIZE)) for i in range (TABLE_SIZE)]
    )

def tri_fn(x):
    if x < 0.25:
        return 4 * x
    if x < 0.75:
        return 2 - 4 * x
    return 4 * x - 4

WAVES = [
    ("SIN", make_table(lambda x: math.sin(2 * math.pi * x), 30000)),
    ("TRI", make_table(tri_fn, 30000)),
    ("SAW", make_table(lambda x: 2 * ((x + 0.5) % 1.0) - 1, 20000))
    ("SQR", make_table(lambda x: 1.0 if x < 0.5 else -1.0, 14000)),
]
STEPS_PER_WAVE = 10
MORPH_MAX = (len(WAVES) - 1) * STEPS_PER_WAVE

def morph_table(step):
    pos = step / STEPS_PER_WAVE
    i = int(pos)
    if i >= len(WAVES) - 1:
        return WAVES[-1][1]
    t = pos - 1
    a, b = WAVES [i][1], WAVES[i + 1][1]
    return array.array("h", [int(x + (y - x) * t) for x, y in zip(a, b)])

def morph_table(step):
    pos = step / STEPS_PER_WAVE
    i = int(pos)
    if i >= len(WAVES) - 1:
        return Waves[-1][0]
    pct = int((pos - i) * 100)
    if pct == 0:
        return WAVES[i][0]
    return "{}>{} {}%".format(WAVES[i][0], WAVES[ i + 1][0]. pct)

# =============================== PRESET ============================= #
PRESETS = [
    ("Organo", synthio.Envelope(attack_time=0.01, decay_time=0.05,
                                 release_time=0.08, attack_level=1.0, 
                                 sustain_level=1.0))

    ("Piano", synthio.Envelope(attack_time=0.005, decay_time=0.7,
                                 release_time=0.4, attack_level=1.0, 
                                 sustain_level=0.2))

    ("pad", synthio.Envelope(attack_time=0.4, decay_time=0.3,
                                 release_time=1.0, attack_level=1.0, 
                                 sustain_level=0.8))

    ("Pizzico", synthio.Envelope(attack_time=0.002, decay_time=0.25,
                                 release_time=0.1, attack_level=1.0, 
                                 sustain_level=0.0))
]

# ============================== AUDIO ===============================
audio = audiobusio.I2SOut(bit_clock=PIN_BCK, word_select=PIN_LRCK, data=PIN_DIN)
mixer = audiomixer.Mixer(voice_count=1, sample_rate=SAMPLE_RATE,
                         channel_count=1, bits_per_sample=16,
                         samples_signed=True, buffer_size=2948)
synth = synthio.Synthesizer(sample_rates=SAMPLE_RATE, channel_count=1)
audio.play(mixer)
mixer.voice[0].play(synth)

# ============================== 12C, KEYS, OLED =====================
displayio.release_displays()
i2c = busio.I2C(scl=PIN_SCL, sda=PIN_SDA, frequency=400_000)

while not i2c.try_lock():
    pass
print("I2C devices:", [hex(a) for a in i2c.scan()])
i2c.unlock()

mpr = adafruit_mpr121.MPR121(i2c)

display = none
try:
    from adafruit_display_text import label
    import adafruit_displayio_ssd1306
    bus = I2CBus(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(bus, width=128, height=32)
    group = displayio.Group()
    lbl_note = label.Label(terminalio.FONT, text="---", scale=2, x=2, y=16)
    lbl_1 = label.Label(terminalio.FONT, text="", x=46, y=5)
    lbl_2 = label.Label(terminalio.FONT, text="", x=46, y=16)
    lbl_3 = label.Label(terminalio.FONT, text="", x=46, y=27)
    for lbl in (lbl_note, lbl_1, lbl_2, lbl_3):
        group_append(lbl)
    display.root_group = group
except Exception as e:
    print("OLED unavailable", e)
    display = None

# ================================= ENCODER AND BUTTON ===========================
def make_encoder(cfg):
    return rotaryio.IncrementalEncoder(cfg[0], cfg[1], divisor=ENC_DIVISOR)

ENC_MIX, ENC_VOL, ENC_OCT = make_encoder(ENC_MIX), make_encoder(ENC_VOL), make_encoder(ENC_OCT)
laast_pos = {"mix": 0, "vol": 0, "oct": 0}

def read_delta(name, enc, cfg):
    pos = enc.position
    d = pos - last_pos[name]
    last_pos[name] = pos
    return -d if cfg[3] else d

class Button:
    def __init__(self, pin):
        self.io = digitalio.DigitalInOut(pin)
        self.io.switch_to_input(pull=digitalio.Pull.UP)
        self.down = False
        self.raw_prev = False
        self.t_edge = 0
        self.t_down = 0

    def update(self, now):
        """Restituisce None, 'short' o 'long' al rilascio del pulsante."""
        raw = not self.io.value            # pressed = low level
        if raw != self.raw_prev:
            self.raw_prev = raw
            self.t_edge = now
        if raw != self.down and now - self.t_edge >= DEBOUNCE_MS:
            self.down = raw
            if raw:
                self.t_down = now
            else:
                return "long" if now - self.t_down >= LONG_MS else "short"
        return None

btn_mix, btn_vol = Button(ENC_MIX[2]), Button(ENC_VOL[2])
btn_oct, btn_sw4 = Button(ENC_OCT[2]), Button(PIN_SW4)

# ================== STATO ==================
st = {
    "oct": 0, "preset": 1, "morph": 0, "vol": 40,
    "mute": False, "hold": False, "last": "---",
    "wave": morph_table(0),
}
active = {}      # tasto -> Note (toccato oppure tenuto dall'hold)
held = set()     # tasti rilasciati ma tenuti dall'hold
dirty = True
shown = None

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def now_ms():
    return time.monotonic_ns() // 1_000_000

def apply_volume():
    level = 0.0 if st["mute"] else 0.9 * (st["vol"] / 100) ** 2
    mixer.voice[0].level = level

def note_name(midi):
    return "{}{}".format(NOTE_NAMES[midi % 12], midi // 12 - 1)

def press_pad(pad):
    old = active.pop(pad, None)
    if old is not None:
        synth.release(old)
    held.discard(pad)
    midi = clamp(BASE_NOTE + 12 * st["oct"] + pad, 0, 127)
    note = synthio.Note(
        frequency=synthio.midi_to_hz(midi),
        waveform=st["wave"],
        envelope=PRESETS[st["preset"]][1],
        amplitude=NOTE_AMP,
    )
    active[pad] = note
    try:
        synth.press(note)
    except Exception as e:           # too many notes together
        print("press:", e)
    st["last"] = note_name(midi)

def release_pad(pad):
    if st["hold"]:
        held.add(pad)
        return
    note = active.pop(pad, None)
    if note is not None:
        synth.release(note)

def set_hold(on):
    st["hold"] = on
    if not on:
        for pad in list(held):
            note = active.pop(pad, None)
            if note is not None:
                synth.release(note)
            held.clear()

def panic():
    synth.release_all()
    active.clear()
    held.clear()
    st["hold"] = False

def refresh_display():
    global shown
    if display is None: 
        return
    vol_txt = "MUTE" if st["mute"] else "V{}".format(st["vol"])
    texts = (
        st["last"],
        PRESETS[st["preset"]][0],
        morph_name(st["morph"]),
        "{} 0{:+d}{}".format(vol_txt, st["oct"], " H" if st["hold"] else ""),

    )
    if texts == shown:
        return
    shown = texts
    lbl_note.text, lbl_1.text, lbl_2.text, lbl_3.text = texts

# ======================= START UP ===============================
apply_volume()
refresh_display()

# small test
test_notes = []
for m in (60, 64, 67):
    n = synthio.Note(frequency=synthio.midi_to_hz(m), waveform=st["wave"],
                     envelope=PRESETS[1][1], amplitude=NOTE_AMP)
    synth.press(n)
    test_notes.append(n)
time.sleep(0.6)
for n in test_notes:
    synth.release(n)

# ================== MAIN LOOP ==================
last_touched = 0
while True:
    now = now_ms()

    # --- keys (MPR121: bit 0 = Touch1 = Do ... bit 11 = Touch12 = Si)
    touched = mpr.touched()
    if touched != last_touched:
        changed = touched ^ last_touched
        for pad in range(12):
            bit = 1 << pad
            if changed & bit:
                if touched & bit:
                    press_pad(pad)
                else:
                    release_pad(pad)
        last_touched = touched
        dirty = True

    # --- SW1: wave's morph
    d = read_delta("mix", enc_mix, ENC_MIX)
    if d:
        st["morph"] = clamp(st["morph"] + d, 0, MORPH_MAX)
        st["wave"] = morph_table(st["morph"])
        dirty = True
    r = btn_mix.update(now)
    if r:
        st["preset"] = (st["preset"] + 1) % len(PRESETS)
        dirty = True

    # --- SW2: volume
    d = read_delta("vol", enc_vol, ENC_VOL)
    if d:
        st["vol"] = clamp(st["vol"] + 3 * d, 0, 100)
        st["mute"] = False
        apply_volume()
        dirty = True
    r = btn_vol.update(now)
    if r:
        st["mute"] = not st["mute"]
        apply_volume()
        dirty = True

    # --- SW3: ottava
    d = read_delta("oct", enc_oct, ENC_OCT)
    if d:
        st["oct"] = clamp(st["oct"] + d, -3, 3)
        dirty = True
    r = btn_oct.update(now)
    if r:
        st["oct"] = 0
        dirty = True

    # --- SW4: hold (short) / ferma tutto (long)
    r = btn_sw4.update(now)
    if r == "short":
        set_hold(not st["hold"])
        dirty = True

    elif r == "long":
        panic()
        dirty = True

    if dirty:
        refresh_display()
        dirty = False