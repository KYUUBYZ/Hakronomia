# Hakronomia

<!--START_SECTION:BOM-TABLE-->
| Item | Qty | Supplier | Cost/item | Total Cost | link |
| --- | --- | --- | --- | --- | --- |
| CGA0805X7R104K500KT | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C7503486.html) |
| CGA0805X7R222K500KT | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C5254797.html) |
| TCC0805X7R103K251DT | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C282726.html) |
| CC0805ZRY5V6BB225 | 20 | LCSC | $0.03 | $0.60 | [Link](https://www.lcsc.com/product-detail/C520072.html) |
| GRM21BR61C106KE15L | 20 | LCSC | $0.04 | $0.80 | [Link](https://www.lcsc.com/product-detail/C77075.html) |
| FRC0805F3300TS | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C2930157.html) |
| FRC0805F4701TS | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C2907264.html) |
| 0805 ±5% 75K | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C2889622.html) |
| RT0805BRD0710KL | 20 | LCSC | $0.04 | $0.80 | [Link](https://www.lcsc.com/product-detail/C110775.html) |
| FRC0805F4700TS | 100 | LCSC | $0.01 | $1.00 | [Link](https://www.lcsc.com/product-detail/C2907267.html) |
| MPR121QR2 | 1 | LCSC | $2.61 | $2.61 | [Link](https://www.lcsc.com/product-detail/C91322.html) |
| PCM5102APWR | 1 | LCSC | $1.51 | $1.51 | [Link](https://www.lcsc.com/product-detail/C107671.html) |
| PCB | 1 | JLPCB | $6.20 | $6.20 |  |
| Estimated total shipping | 1 |  |  | $0.00 |  |
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

## Physical view:
<img width="1034" height="900" alt="image" src="https://github.com/KYUUBYZ/Hakronomia/blob/main/Images/Hakronomia-view.png" />

## PCB view:
<img width="935" height="846" alt="image" src="https://github.com/KYUUBYZ/Hakronomia/blob/main/Images/Hakronomia-PCB.png" />

## Schematic view:
<img width="1101" height="735" alt="image" src="https://github.com/KYUUBYZ/Hakronomia/blob/main/Images/Hakronomia-Schematic.png" />

 
