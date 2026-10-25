# Hakronomia

<!--START_SECTION:BOM-TABLE-->
| Item | Qty | Supplier | Cost/item | Total Cost | link |
| --- | --- | --- | --- | --- | --- |
| MPR121QR2 | 1 | Unikeyic | $1.60 | $1.60 | [Link](https://www.unikeyic.com/products/other-interface/mpr121qr2/11118659.html?sku=1003001027325782) |
| PCM5102APWR | 1 | Unikeyic | $1.31 | $1.31 | [Link](https://www.unikeyic.com/products/adc-dac-specialized/pcm5102apwr/33225117.html?sku=1003001444976630) |
| rp2040-zero | 1 | Futura net | $6.51 | $6.51 | [Link](https://futuranet.it/prodotto/scheda-di-sviluppo-mini-basata-su-rp2040/) |
| 0.91 OLED SCREEN | 1 | Futura net | $6.62 | $6.62 | [Link](https://futuranet.it/prodotto/display-oled-i2c-091-128x32-pixel/) |
| 3,5mm jack | 1 | Futura net | $0.34 | $0.34 | [Link](https://futuranet.it/prodotto/presa-jack-stereo-35-mm-da-circuito-stampato/) |
| EC11E15244G1 | 3 | Unikeyic | $2.00 | $6.00 | [Link](https://www.unikeyic.com/products/encoders-and-decoders/ec11e15244g1/24342867.html?sku=1003001012811431) |
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


 
