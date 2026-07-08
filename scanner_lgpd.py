import re
import os
from datetime import datetime
def mascarar_cpf(cpf):
    return f"{cpf[:3]}***-***{cpf[-2:]}"
def processar_arquivos():
        pasta = "documentos_teste"
        if not os.path.exists(pasta):
            os.makedirs(pasta)
            print(f"Pasta '{pasta}' criada.")
            return
        print(f"--- '{pasta}' INICIANDO AUDITORIA DE PRIVACIDADE")
        print(f"Data e hora: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        for nome_arquivo in os.listdir(pasta):
            if nome_arquivo.endswith(".txt"):
                caminho = os.path.join(pasta, nome_arquivo)
                with open(caminho, "r", encoding="utf-8") as f:
                    texto = f.read()
                    cpfs = re.findall(r"\b\d{3}\.?[0-9]{3}\.?[0-9]{3}-?[0-9]{2}\b", texto)
                    if cpfs:
                        print(f"\n[!] ALERTA: Dados detectados no arquivo '{nome_arquivo}':")
                        for cpf in cpfs:
                            print(f"    - CPF: {mascarar_cpf(cpf)}")
                    else:
                        print(f"\n[✓] Arquivo seguro: {nome_arquivo}")
if __name__ == "__main__":
    processar_arquivos()
                       

