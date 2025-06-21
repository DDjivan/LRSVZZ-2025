import spidev  # Communication SPI
import time

# --- Initialisation SPI ---
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus SPI 0, périphérique CS0
spi.max_speed_hz = 1000000  # 1 MHz : stable pour MCP3204

# --- Fonction de lecture MCP3204 ---
def read_adc(channel):
    """
    Lit une valeur analogique sur le canal MCP3204 donné (0 à 3).
    Retourne une valeur brute 12 bits (0–4095).
    """
    if not 0 <= channel <= 3:
        raise ValueError("Canal invalide : doit être 0-3")

    # Protocole SPI : 3 octets
    start_bit     = 0b00000110  # Start + single-ended
    command       = (channel & 0b11) << 6
    result = spi.xfer2([start_bit, command, 0x00])

    # Reconstruction des 12 bits depuis les 2 derniers octets
    value = ((result[1] & 0b00001111) << 8) | result[2]
    return value

# --- Boucle de test ---
try:
    while True:
        raw = read_adc(0)  # Lire CH0
        voltage = raw * 3.3 / 4095  # Conversion en volts (résolution 12 bits, 3.3V)
        print(f"Feedback brut : {raw} | Tension : {voltage:.2f} V")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Arrêt manuel.")
    spi.close()
