import re
from pathlib import Path

def rodar_scanner():
    # 1. Configura o diretório de saída de forma segura
    pasta_logs = Path("meus_logs")
    pasta_logs.mkdir(exist_ok=True)
    arquivo_saida = pasta_logs / "resultado.txt"

    texto = """
    IP: 192.168.1.10, Email: teste@gmail.com
    Outro IP: 10.0.0.5, Suporte: ajuda@empresa.com
    """

    # 2. Regex otimizadas
    regra_ip = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    regra_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # 3. Extração dos dados
    ips = re.findall(regra_ip, texto)
    emails = re.findall(regra_email, texto)

    # 4. Escrita formatada no arquivo
    try:
        with open(arquivo_saida, "w", encoding="utf-8") as f:
            f.write("=== RELATÓRIO DE SCANNER ===\n\n")
            
            f.write(f"IPs encontrados ({len(ips)}):\n")
            f.write("\n".join(f"- {ip}" for ip in ips) + "\n\n")
            
            f.write(f"Emails encontrados ({len(emails)}):\n")
            f.write("\n".join(f"- {email}" for email in emails))

        print(f" Sucesso! Resultados salvos em: {arquivo_saida}")
    
    except IOError as e:
        print(f"❌ Erro ao salvar o arquivo: {e}")

if __name__ == "__main__":
    rodar_scanner()
