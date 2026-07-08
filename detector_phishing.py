import re

def analisar_link(url):
    pontos_suspeitos = 0
    motivos = []
    
    if re.search(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', url):
        pontos_suspeitos += 1
        motivos.append("O link contém um endereço IP em vez de um domínio.")
        
    return pontos_suspeitos, motivos

if __name__ == "__main__":
    print("\n" + "=" * 30)
    print("Detector de Phishing v1.0")
    print("=" * 30 + "\n")
    
    url = input("Digite ou cole a URL para análise: ")
    print(f"Analisando o link: {url}")
    
    pontos, motivos = analisar_link(url)
    
    if pontos >= 1:
        print("\nLink perigoso: forte indício de phishing")
        for m in motivos:
            print(f"- {m}")
    else:
        print("\nLink parece seguro")
