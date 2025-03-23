
![Desenho da Cabeça de um Robô](robo.png)
# Chatbot Especializado em Análise de Negócios

## 🎯 Objetivo do Chatbot

O objetivo deste chatbot é fornecer respostas especializadas sobre:

- Análise de negócios  
- Gestão empresarial  
- KPIs (Indicadores-chave de desempenho)  
- Modelagem de processos  
- Tomadas de decisão estratégicas  

Ele foi projetado para **responder a perguntas dentro desse contexto** e **finalizar a conversa educadamente após a terceira interação do usuário**, fornecendo um **resumo dos temas abordados**.

---

## 🧰 Tecnologias Utilizadas

- **Python**: Versão 3.12  
- **Groq**: API para interagir com o modelo de linguagem

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de que você tem os seguintes itens instalados:

- **Python 3.12**  
  [Clique aqui para baixar](https://www.python.org/downloads/)

- **Pip** (gerenciador de pacotes do Python)  
  Normalmente já vem instalado junto com o Python.

---

## 🚀 Passo a Passo para Rodar o Chatbot

### 📦 Passo 1: Instalar as Dependências

Abra o terminal ou prompt de comando, vá até o diretório onde o arquivo `app.py` está localizado e execute:

```bash
pip install -r requirements.txt
Certifique-se de que existe um arquivo requirements.txt com as bibliotecas necessárias.

🔑 Passo 2: Configurar a Chave de API do Groq
Você precisa configurar a variável de ambiente GROQ_API_KEY com sua chave de API do Groq.

No Windows (Prompt de Comando):
cmd
Copiar
Editar
set GROQ_API_KEY=sua_chave_de_api
No Linux ou macOS (Terminal):
bash
Copiar
Editar
export GROQ_API_KEY=sua_chave_de_api
Substitua sua_chave_de_api pela sua chave de API real.

▶️ Passo 3: Executar o Script
Ainda no terminal, execute o script app.py com o seguinte comando:

bash
Copiar
Editar
python app.py
🧠 Estrutura do Código
Uma visão geral do que o código faz:

Configuração da API do Groq

Inicialização do histórico de mensagens

Função para coletar mensagens e interagir com a IA

Início da interação com o usuário via terminal

✅ Conclusão
Seguindo esses passos, você conseguirá rodar o chatbot e interagir com ele através do terminal.

Certifique-se de ter todas as dependências instaladas

Verifique se a chave de API está corretamente configurada

Se tiver qualquer dúvida ou problema, revise os passos com atenção

📬 Dica: Mantenha o terminal aberto durante a interação e observe as mensagens retornadas. Isso facilitará testes e ajustes caso necessário.

