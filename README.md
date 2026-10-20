# **Sentinel Code AI**

Kit de ferramentas em Python para cibersegurança: auditoria automatizada de código (SAST) com inteligência artificial, engenharia de privacidade (LGPD) e inteligência de ameaças.

---

## **Ferramentas incluídas**

| Ferramenta | Arquivo | O que faz |
|---|---|---|
| **Auditoria de código com IA** | `auditor_ia.py` | Analisador estático que lê arquivos de código-fonte locais e usa um modelo LLM da API da Groq (`llama-3.1-8b-instant`) para identificar e diagnosticar vulnerabilidades críticas, como SQL Injection. |
| **Scanner de privacidade (LGPD)** | `scanner_lgpd.py` | Varre diretórios locais em lote, identifica dados pessoais sensíveis (PII), como CPFs, e aplica máscara de proteção (por exemplo, `123.***.***-12`). |
| **Detector de phishing e blacklist** | `detector_phishing.py` | Analisa URLs de forma preventiva, procurando palavras-chave suspeitas com expressões regulares e cruzando com uma lista local de endereços IP bloqueados. |
| **Extrator de logs com Regex** | `scanner_regex.py` | Varre arquivos de texto em busca de padrões de endereços IP e e-mails, para uso em relatórios de auditoria. |

---

## **Tecnologias utilizadas**

* Python 3.x
* Groq SDK (IA aplicada à análise de riscos em código)
* python-dotenv (isolamento da chave da API em variável de ambiente)
* Expressões Regulares (`re`)
* `pathlib` e `os` (manipulação de arquivos e pastas em lote)

---

## **Estrutura do projeto**

```
sentinel-code-ai/
├── auditor_ia.py
├── scanner_lgpd.py
├── detector_phishing.py
├── scanner_regex.py
├── requirements.txt
└── README.md
```

---

## **Como usar**

```bash
pip install -r requirements.txt
```

Crie um arquivo `.env` na raiz do projeto com a sua chave da Groq (o nome da variável deve ser o mesmo usado em `auditor_ia.py`):

```
GROQ_API_KEY=sua_chave_aqui
```

Execute a ferramenta desejada a partir da pasta do projeto:

```bash
python auditor_ia.py
python scanner_lgpd.py
python detector_phishing.py
python scanner_regex.py
```



---

## **Histórico de evolução do projeto**

Como estudante de Engenharia de Software, a evolução deste repositório reflete o meu aprendizado prático, documentado no controle de versão (Git):

* **Fase 1.0 (lógica inicial):** buscas simples com strings e condicionais para detecção rudimentar de phishing.
* **Fase 2.0 (expressões regulares):** Regex avançadas para validação e criação de estruturas de dados locais, como listas de IPs bloqueados.
* **Fase 3.0 (engenharia de privacidade):** algoritmos locais de mascaramento de CPFs, baseados na LGPD, com entrada manual pelo terminal.
* **Fase 4.0 (automação e IA):** refatoração completa da suíte, com leitura automática de diretórios inteiros e integração com IA generativa para auditoria estática de código.

---

## **Aviso**

Projeto desenvolvido para fins educacionais. Use as ferramentas apenas em código e em arquivos que você tem autorização para analisar.

---

## **Autor**

**Natan Tadeu dos Santos Coelho**
Estudante de Engenharia de Software e Cybersecurity | Futuro Engenheiro de Segurança Cibernética
