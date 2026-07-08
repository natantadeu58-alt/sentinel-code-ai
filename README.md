# 🛡️ Sentinel Code AI - Cybersecurity Toolkit

Um kit completo de ferramentas em Python focado em Cibersegurança, Auditoria Automatizada de Código (SAST) com Inteligência Artificial, Engenharia de Privacidade (LGPD) e Inteligência de Ameaças.

## 🚀 Ferramentas Inclusas no Kit

- **🤖 Auditoria de Código com IA (`auditor_ia.py`):** Analisador estático que lê arquivos de código-fonte locais e utiliza os modelos LLM da API do **Groq** (`llama-3.1-8b-instant`) para identificar e diagnosticar vulnerabilidades críticas (como SQL Injection) em tempo recorde.
- **🔒 Scanner de Privacidade LGPD (`scanner_lgpd.py`):** Script automatizado que realiza a varredura estruturada de diretórios locais em lote, identifica o vazamento de dados sensíveis (PII) como CPFs e aplica máscaras de proteção (`123.***.***-12`) em conformidade com as diretrizes de privacidade.
- **🕵️ Detector de Phishing & Blacklist (`detector_phishing.py`):** Analisador preventivo de URLs que intercepta palavras-chave suspeitas utilizando expressões regulares (Regex) e realiza o cruzamento de dados com uma lista negra (Blacklist) local de endereços IP bloqueados.
- **📄 Extrator de Logs com Regex (`scanner_regex.py`):** Utilitário focado em extração de informações brutas que varre arquivos de texto em busca de padrões específicos de endereços IP e e-mails para relatórios de auditoria.

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Groq SDK** (IA aplicada à segurança ofensiva e análise de riscos)
- **Python-Dotenv** (Isolamento seguro de chaves confidenciais da API)
- **Expressões Regulares (`re`)** (Análise avançada e filtragem de strings)
- **Pathlib & Os** (Manipulação de arquivos do sistema e automação de diretórios em lote)

## 📈 Histórico de Evolução do Projeto (Jornada de Aprendizado)
*Como estudante de Engenharia de Software, a arquitetura deste repositório reflete minha evolução prática e amadurecimento lógico através do controle de versão (Git):*
- **Fase 1.0 (Lógica Inicial):** Desenvolvimento de buscas simples com strings e condicionais para detecção rudimentar de Phishing.
- **Fase 2.0 (Expressões Regulares):** Implementação de Regex avançadas para validação e criação de estruturas de dados locais para Blacklists de IPs.
- **Fase 3.0 (Engenharia de Privacidade):** Construção de algoritmos locais para mascaramento de dados (CPFs) baseados na LGPD via entradas manuais no terminal.
- **Fase 4.0 (Automação e IA):** Refatoração completa de toda a suíte de ferramentas, implementando leitura automatizada de diretórios inteiros e integração completa com Inteligência Artificial Generativa para auditoria estática.

## 🔧 Como Executar as Ferramentas

### 1. Pré-requisitos
Certifique-se de possuir o Python instalado e uma credencial de acesso no [Groq Console](https://groq.com).

### 2. Configurar as Dependências
Instale as bibliotecas necessárias declaradas no arquivo do projeto:
```bash
pip install -r requirements.txt
```

### 3. Configurar as Variáveis de Ambiente
Crie um arquivo chamado `.env` na raiz do repositório e insira seu token:
```env
GROQ_API_KEY=sua_chave_groq_aqui
```

### 4. Executar um Módulo
Basta chamar a ferramenta desejada diretamente pelo terminal:
```bash
python auditor_ia.py
```

---
💡 *Desenvolvido como projeto de portfólio prático integrado, demonstrando habilidades em Segurança da Informação, LGPD, Regex e Engenharia de Software.*


Responsável:

Natan

Estudante de Engenharia de Software
Futuro Especialista e Engenheiro de Segurança Cibernética.

