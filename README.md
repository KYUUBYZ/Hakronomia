# Hakronomia

<!--START_SECTION:BOM-TABLE-->
| Item | Qty | Supplier | Cost/item | Total Cost | link |
| --- | --- | --- | --- | --- | --- |
| 0.1uF | 6 | Unikeyic | $0.08 | $0.48 | [Link](https://www.unikeyic.com/products/ceramic-capacitors/gcd21br72a104ka01l/10036938.html?sku=1003001027405269) |
| 2.2nF | 2 | Unikeyic | $0.05 | $0.10 | [Link](https://www.unikeyic.com/products/ceramic-capacitors/gcm2165c2a222ja16d/5775567.html?sku=1003001445194783) |
| 10nF | 6 | Unikeyic | $0.01 | $0.06 | [Link](https://www.unikeyic.com/products/ceramic-capacitors/cc0805jrx7r9bb103/17962920.html?sku=1003001445184833) |
| 2.2uF | 2 | Unikeyic | $0.05 | $0.10 | [Link](https://www.unikeyic.com/products/ceramic-capacitors/cga4j3x7r1c225kt0y0n/8873476.html?sku=1003001017784221) |
| 10uF | 4 | Unikeyic | $0.08 | $0.32 | [Link](https://www.unikeyic.com/products/ceramic-capacitors/c2012x7r0j106k125ab/17422021.html?sku=1003001013214412) |
| AudioJack5 | 1 | Futuranet | $0.30 | $0.30 | [Link](https://futuranet.it/prodotto/presa-jack-stereo-35-mm-da-circuito-stampato/) |
| 330R | 12 | Unikeyic | $0.01 | $0.12 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/rc0805fr-07330rl/4454264.html?sku=1003001443534963) |
| 4.7k | 2 | Unikeyic | $0.01 | $0.02 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/rc0805fr-7w4k7l/3329266.html?sku=1003001021096266) |
| 75k | 1 | Unikeyic | $0.00 | $0.00 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/wr08x753-jtl/28917829.html?sku=1003001442043903) |
| 10k | 2 | Unikeyic | $0.00 | $0.00 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/0805w8f1002t5e/33861683.html?sku=1003001012328856) |
| 470R | 2 | Unikeyic | $0.00 | $0.00 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/0805w8f4700t5e/27378691.html?sku=1003001012328951) |
| 0R | 1 | Unikeyic | $0.01 | $0.01 | [Link](https://www.unikeyic.com/products/surface-mount-resistors/rtt050000ftp/30082103.html?sku=1003001013772933) |
| RP2040-Zero | 1 | Futuranet | $6.61 | $6.61 | [Link](https://futuranet.it/prodotto/scheda-di-sviluppo-mini-basata-su-rp2040/) |
| RotaryEncoder_Switch_MP | 3 | Unikeyic | $1.49 | $4.47 | [Link](https://www.unikeyic.com/products/encoders-and-decoders/ec11e15244g1/24342867.html?sku=1003001012811431) |
| ER_OLEDM0.91_1x-I2C | 1 | Futuranet | $0.00 | $0.00 | [Link](https://futuranet.it/prodotto/display-oled-i2c-091-128x32-pixel/) |
| MPR121QR2 | 1 | Unikeyic | $0.00 | $0.00 | [Link](https://www.unikeyic.com/products/other-interface/mpr121qr2/11118659.html?sku=1003001027325782) |
| PCM5102A | 1 | Unikeyic | $0.00 | $0.00 | [Link](https://www.unikeyic.com/products/adc-dac-specialized/pcm5102apwr/33225117.html?sku=1003001444976630) |
| Estimated total shipping | 1 |  |  | $5.00 |  |
<!--END_SECTION:BOM-TABLE-->
# HOW TO INSTALL THE FIRMWARE (Hakronomia.py):

1)    Connect your RP2040-ZERO to your PC using a data transfer cable while pressing BOOT 

2)    Install/Copy the "adafruit-ciruitpython-waveshare" file i put in this folder ON the RP2040-ZERO.

3)    you should see file be downloaded on your microcontroller.

4)    From CircuitPython libraries bundle, copy "adafruit_mpr121, adafruit_displayio_ssd1306, adafruit_display_text, adafruit_bus_device" on the rp2040-zero.

5)    Copy Hakronomia.py on the rp2040-zero

# What is Hakronomia?
Hakronomia, Midi keyboard, it's a Piano style keyboard an it has 12 exposed copper plates keys, plus 3 rotary encoder, a 0.91 inch screen, a switch and a 3.5mm AudioJack.
It uses a MPR121QR2 ( The MPR121QR2 is a Capacitive Touch Sensor Controller )  and the PCM5102A ( DAC Chip (Digital-to-Analog Converter ).

<img width="1034" height="900" alt="image" src="https://github.com/user-attachments/assets/b32604f4-7dbe-4195-bde2-0b71a842cef6" />

<img width="935" height="846" alt="image" src="https://github.com/user-attachments/assets/26af54c9-22df-4bdb-8102-4b393dc6ff8d" />


 
