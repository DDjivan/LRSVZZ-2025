import spidev
import time

# --- Initialisation SPI ---
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus SPI 0, périphérique CS0
spi.max_speed_hz = 1000000  # Fréquence adaptée au MCP3204 (jusqu'à 1.6 MHz)

# --- Fonction de lecture MCP3204 ---
def read_adc(channel):
    if not 0 <= channel <= 3:
        raise ValueError("Canal invalide : 0 à 3 uniquement")

    # Construction de la commande :
    # Byte 1 : 00000110 pour start bit + mode single-ended
    # Ajouter le bit D2 du canal (bit 2) au bit 0 du premier octet
    start = 0b00000110 | ((channel & 0b100) >> 2)
    # Byte 2 : bits D1 et D0 du canal décalés à gauche
    msb = (channel & 0b011) << 6
    result = spi.xfer2([start, msb, 0x00])

    # Conversion du résultat (12 bits) : 4 bits bas du 2e octet + 8 bits du 3e
    value = ((result[1] & 0x0F) << 8) | result[2]
    return value

# --- Conversion en degrés ---
def adc_to_degrees(raw_value):
    """
    Convertit la valeur ADC brute en angle en degrés.
    Hypothèse : 0 V = 0°, 3.3 V = 360°
    """
    voltage = raw_value * 3.3 / 4095  # 12 bits -> max = 4095
    angle = (voltage / 3.3) * 360     # Proportion linéaire
    return angle

# --- Retourne les valeurs d'angles ---
def getAngles():
    return tuple(adc_to_degrees(read_adc(ch)) for ch in (0, 1))

# --- Boucle de test ---
if __name__ == "__main__":
    try:
        while True:
            for ch in range(2):
                raw = read_adc(ch)
                angle = adc_to_degrees(raw)
                voltage = (angle / 360) * 3.3
                print(f"Canal {ch} : Valeur ADC = {raw} | Angle = {angle:.1f}° | Tension = {voltage:.2f} V")
            print("----------------------------------------------------")
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Arrêt par l'utilisateur.")

    finally:
        spi.close()
