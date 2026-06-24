import re
def escaneador_dados_sensíveis(texto):
    padrao_cpf = r'\d{3}\.\d{3}\.\d{3}-\d{2}'
    padrao_email = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    cpfs = re.findall(padrao_cpf, texto)
    emails = re.findall(padrao_email, texto)
    return cpfs, emails
def gerar_relatorio(cpfs, emails):
    print("\n" + "="*40)
    print("RELATÓRIO DE EXPOSIÇÃO DE DADOS")
    print("="*40)
    total = len(cpfs) + len(emails)
    if total > 0:
        print(f"RISCO DETECTADO! Encontrados {total} itens sensíveis:")
        if cpfs:
            print(f"\nCPFs Detectados ({len(cpfs)}):")
            for cpf in cpfs:
                print(f"- {cpf[:3]}.***.***-{cpf[-2:]}")
        if emails:
            print(f"\nE-mails Detectados ({len(emails)}):")
            for email in emails:
                print(f"- {email}") 
    print("\n" + "-" * 40)
    print("Status: Analise Concluida.")
    
print("DATA PRIVACY SCANNER v1.0 (LGPD Focused)")
print("Cole o conteúdo para análise (digite 'SAIR' em uma nova linha para finalizar):")
linhas = []
while True:
    linha = input()
    if linha.upper() == "SAIR":
        break
    linhas.append(linha)
texto_completo = "\n".join(linhas)

if texto_completo.strip():
    cpfs, emails = escaneador_dados_sensíveis(texto_completo)
    gerar_relatorio(cpfs, emails)
else:
    print("Nenhum texto inserido.")
