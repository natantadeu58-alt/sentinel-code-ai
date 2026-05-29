import re

def detector_phishing(url):
    # Lista de padrões suspeitos comuns em URLs de phishing
    padroes = (r"login", r"secure", r"account", r"update", r"verify")
    for padrao in padroes:
        if re.search(padrao, url, re.IGNORECASE):
            return True
    return False

def verificar_ip(ip):
    """Verifica se o IP está na lista de BLACKLIST."""
    # Nota: No código da imagem, a variável IPS_SUSPEITOS não está definida.
    # Exemplo de lista para o código funcionar:
    IPS_SUSPEITOS = ["10.0.0.5", "192.168.1.100"]
    return ip in IPS_SUSPEITOS

# --- INTERFACE ---
print("-" * 40)
print("Detector de Phishing v2.0")
print("-" * 40)

url = input("Digite a URL: ").strip()
ip_input = input("Digite o IP: ").strip()

print("\n--- Analisando ---")

if detector_phishing(url):
    print(f"X ALERTA: URL \"{url}\" SUSPEITA!")
else:
    print(f"URL OK.")

if verificar_ip(ip_input):
    print(f"X ALERTA: IP \"{ip_input}\" BLOQUEADO!")
else:
    print(f"IP OK.")