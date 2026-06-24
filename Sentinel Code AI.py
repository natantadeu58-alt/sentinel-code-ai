import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv("GROQ_API_KEY")
model = None
if chave:
    client = Groq(api_key=chave)
else:
    print("Erro: A chave GROQ_API_KEY não encontrada no arquivo .env")
    raise SystemExit(1)
def analisar(): 
    with open("test_code.py", "r", encoding="utf-8") as f:
        codigo = f.read()
        print(" Groq analisando código em tempo recorde...")
        try:
            chat_completions = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"Analise este código: \n\n{codigo}",
                    }
                ],
                model="llama-3.1-8b-instant"
            )
            print("\n--- SETINEL CODE AI: AUDITORIA DE SEGURANÇA ---\n")
            print(chat_completions.choices[0].message.content)
        except Exception as e:
            print(f"Erro ao processar: {e}")
if __name__ == "__main__":
    analisar()
