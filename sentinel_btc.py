import requests 
import time
from datetime import datetime
from groq import Groq
client = Groq(api_key="GROQ_API_KEY")
def obter_preço_btc():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"
    response = requests.get(url)
    data = response.json()
    preco = data['bitcoin']['usd']
    variacao = data['bitcoin']['usd_24h_change']
    return preco, variacao
def salvar_log(mensagem):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sentinel_btc_logs.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{timestamp}]{mensagem}\n")


def executar_sentinel():
    print("SENTINEL BITCOIN - Monitoramento Ativo...")
    salvar_log("Sistema iniciado e manitorando mercado.")
    while True:
        try:
            preco, variacao = obter_preço_btc()
            cor_variacao = "+" if variacao >= 0 else ""
            print(f"\n Check: BTC a $ {float(preco):,.2f} ({cor_variacao} {float(variacao):.2f}%)")
            if abs(variacao) > 0.1:
                prompt = (f"0 Bitcoin está custando ${preco} com variação de {variacao:.2f}%")
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                insight = chat_completion.choices[0].message.content
                print(f" IA INSIGHT: {insight}")
                salvar_log(f"BTC: ${preco} | Var: {variacao:.2f}% | IA: {insight}")
                time.sleep(60)
        except Exception as e:
            erro_msg = f"Erro na execução: {e}"
            print(f" {erro_msg}")
            salvar_log(f"Erro: {erro_msg}")
            time.sleep(10)


if __name__ == "__main__":
    executar_sentinel()
                    

                              
                              
                                  



