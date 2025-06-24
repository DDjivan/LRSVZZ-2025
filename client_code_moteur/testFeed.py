import spidev
import time

# --- Initialisation SPI ---
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus SPI 0, périphérique CS0
spi.max_speed_hz = 1000000  # Fréquence adaptée au MCP3204

# --- Fonction de lecture MCP3204 ---
def read_adc(channel):
    if not 0 <= channel <= 3:
        raise ValueError("Canal invalide : 0 à 3 uniquement")
    start_bit = 0b00000110
    command = (channel & 0b11) << 6
    result = spi.xfer2([start_bit, command, 0x00])
    value = ((result[1] & 0b00001111) << 8) | result[2]
    return value

# --- Conversion en degrés ---
def adc_to_degrees(raw_value):
    """
    Convertit la valeur ADC brute en angle en degrés.
    Hypothèse : 0 V = 0°, 3.3 V = 180°
    """
    voltage = raw_value * 3.3 / 4095  # Convertir en volts
    angle = (voltage / 3.3) * 360     # Proportion linéaire
    return angle

# --- Boucle de test ---
try:
    while True:
        raw = read_adc(0)  # Lecture sur canal CH0
        angle = adc_to_degrees(raw)
        print(f"Valeur ADC : {raw} | 2e Angle estimé : {angle:.1f}°")
        raw = read_adc(1)  # Lecture sur canal CH0
        angle = adc_to_degrees(raw)
        print(f"Valeur ADC : {raw} | 2e Angle estimé : {angle:.1f}°")
        print("----------------------------------------------------")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Arrêt par l'utilisateur.")
    spi.close()
