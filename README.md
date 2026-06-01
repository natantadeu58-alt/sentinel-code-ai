# 🛡️ Código-Sentinel-AI 

Um ecossistema modular avançado desenvolvido em **Python** voltado para cibersegurança, auditoria automatizada de redes e análise inteligente de vulnerabilidades. O projeto integra scripts especializados de varredura (scanners) e utiliza modelos de Inteligência Artificial para correlacionar dados coletados e avaliar riscos de segurança em tempo real.

O **Sentinel-AI** foi projetado para atuar como uma solução centralizada de DevSecOps, permitindo que administradores e engenheiros de segurança identifiquem brechas estruturais antes que sejam exploradas por agentes maliciosos.

---

## 📂 Estrutura de Módulos e Funcionalidades 

O ecossistema é composto por ferramentas complementares que cobrem diferentes camadas da segurança da informação:

* **`Sentinel Code AI.py` (Módulo Central)** O "cérebro" do ecossistema. Consome as APIs de Inteligência Artificial para receber relatórios de texto dos scanners técnicos e traduzi-los em análises de risco de alto nível com recomendações de correção (*remediation*).*

* **`Cyber_eye.py` (Scanner de Reconhecimento)** Atua na fase de *Footprinting*. Analisa portas lógicas abertas, identifica banners de serviços ativos (versões de sistemas) e mapeia a superfície de ataque exposta.

* * **`sentinel_btc.py` (Módulo de Monitorização de Ativos)** Script focado na análise de dados e integridade de transações/endereços, demonstrando a versatilidade do ecossistema no tratamento de protocolos criptográficos específicos.
  
  * * **`scanner_v1.py` ao `scanner_v5.py` (Suíte Evolutiva de Auditoria)** * **Scanner de Senhas & Autenticação:** Módulos dedicados a testar a robustez de credenciais corporativas e validação de políticas de segurança contra ataques de força bruta controlado.
    
    * **Scanner de Vulnerabilidades Web:** Análise automatizada de cabeçalhos HTTP, validação de certificados SSL/TLS e deteção de falhas comuns listadas no OWASP Top 10.

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.x
* **Bibliotecas de Rede:** `socket`, `requests`, `urllib3`
* **Inteligência Artificial:** Integração de Large Language Models (LLMs) via chamadas de API assíncronas para automação de triagem.
* **Segurança de Credenciais:** Gestão de variáveis de ambiente com `python-dotenv`.


---

### 🛡️ Boas Práticas de Segurança (DevSecOps)

* **Proteção de Segredos:** As chaves de API e tokens privados **nunca** são injetados diretamente no código-fonte. O projeto utiliza um arquivo `.env` local mapeado no `.gitignore` para blindagem de segredos.
* **Resiliência do Sistema:** Todas as varreduras web possuem tratamento de exceções robusto para evitar negação de serviço ou interrupções inesperadas durante a execução.

---

### 🚀 Próximos Passos do Roadmap

- [ ] Migrar a arquitetura dos scripts para uma estrutura modular de pacotes dentro de um diretório específico.
- [ ] Desenvolver relatórios automáticos exportáveis nos formatos JSON e PDF.

        
       ---

> [!WARNING]
> **Aviso:** Este ecossistema foi desenvolvido estritamente para fins educativos, auditorias de segurança autorizadas e testes de intrusão consentidos. O uso indevido dessas ferramentas para atividades maliciosas é de total responsabilidade do usuário.

