# Hakronomia

<!--START_SECTION:BOM-TABLE-->
| Product name | Producer | Order Qty. | Unit Price(USD) | Ext.Price(USD) | Vendor | Product Link | Valore | Designators | Qty needed |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CGA0805X7R104K500KT | HRE | 100 | 0.0043 | 0.43 | LCSC | [Link](https://www.lcsc.com/product-detail/C7503486.html) | 0.1uF | C1,C9,C10,C12,C18,C20 | 6 |
| CGA0805X7R222K500KT | HRE | 100 | 0.0066 | 0.66 | LCSC | [Link](https://www.lcsc.com/product-detail/C5254797.html) | 2.2nF | C2,C11 | 2 |
| TCC0805X7R103K251DT | CCTC | 100 | 0.0061 | 0.61 | LCSC | [Link](https://www.lcsc.com/product-detail/C282726.html) | 10nF | C3,C4,C5,C6,C7,C8 | 6 |
| CC0805ZRY5V6BB225 | YAGEO | 20 | 0.0345 | 0.69 | LCSC | [Link](https://www.lcsc.com/product-detail/C520072.html) | 2.2uF | C13,C19 | 2 |
| GRM21BR61C106KE15L | muRata | 20 | 0.0375 | 0.75 | LCSC | [Link](https://www.lcsc.com/product-detail/C77075.html) | 10uF | C16,C17,C21,C22 | 4 |
| FRC0805F3300TS | FOJAN | 100 | 0.0025 | 0.25 | LCSC | [Link](https://www.lcsc.com/product-detail/C2930157.html) | 330R | R1,R2,R3,R4,R5,R6,R7,R8,R9,R10,R11,R12 | 12 |
| FRC0805F4701TS | FOJAN | 100 | 0.0022 | 0.22 | LCSC | [Link](https://www.lcsc.com/product-detail/C2907264.html) | 4.7k | R13,R14 | 2 |
| 0805 ±5% 75K | VO | 100 | 0.0031 | 0.31 | LCSC | [Link](https://www.lcsc.com/product-detail/C2889622.html) | 75k | R15 | 1 |
| RT0805BRD0710KL | YAGEO | 20 | 0.0371 | 0.74 | LCSC | [Link](https://www.lcsc.com/product-detail/C110775.html) | 10k | R16,R17 | 2 |
| FRC0805F4700TS | FOJAN | 100 | 0.0022 | 0.22 | LCSC | [Link](https://www.lcsc.com/product-detail/C2907267.html) | 470R | R18,R19 | 2 |
| MPR121QR2 | NXP | 1 | 2.6105 | 2.61 | LCSC | [Link](https://www.lcsc.com/product-detail/C91322.html) | MPR121QR2 | U2 | 1 |
| PCM5102APWR | TI | 1 | 1.5052 | 1.51 | LCSC | [Link](https://www.lcsc.com/product-detail/C107671.html) | PCM5102A | U3 | 1 |
| PCB | JLPCB | 5 | $6.20 | $6.20 | JLPCB |  |  |  |
| Shipping cost |  |  | $6.6 | $6.6 |  |  |
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

 
