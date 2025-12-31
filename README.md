# 📡 MT SureBet → Telegram Notifier

Sistema desenvolvido para enviar automaticamente notificações de um site para o Telegram utilizando Flask como backend.

O projeto recebe eventos do site e encaminha as informações diretamente para um canal ou grupo do Telegram através de um bot.

---

## 🚀 Funcionalidades

- Integração entre site e Telegram
- Envio automático de mensagens
- Backend simples e eficiente
- Configuração via variáveis de ambiente
- Estrutura limpa e objetiva

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Flask
- Telegram Bot API
- Requests
- Python Dotenv

---

## 📁 Estrutura do Projeto

```
mtsurebet-automation-bot/
├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── bot/
│   ├── __init__.py
│   └── telegram_bot.py
│
├── routes/
│   ├── __init__.py
│   └── api.py

```

---

## ⚙️ Configuração do Ambiente

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/mtsurebet-telegram-bot.git
cd mtsurebet-telegram-bot
```

---

### 2️⃣ Criar ambiente virtual (opcional)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar variáveis de ambiente

Crie um arquivo `.env` baseado no `.env.example`:

```env
TELEGRAM_BOT_TOKEN=SEU_TOKEN_AQUI
TELEGRAM_CHAT_ID=SEU_CHAT_ID_AQUI
```

---

## ▶️ Executando o Projeto

```bash
python app.py
```

O servidor Flask ficará ativo e pronto para receber requisições do site.

---

## 🔔 Funcionamento

1. O site envia uma requisição HTTP para o backend Flask
2. O Flask processa os dados recebidos
3. A mensagem é enviada automaticamente para o Telegram

---

## 🔐 Segurança

- Dados sensíveis não são versionados
- O arquivo `.env` está protegido no `.gitignore`
- Apenas o `.env.example` é versionado

---

## 📌 Observações Importantes

- O bot precisa estar no canal ou grupo
- Em canais, o bot deve ser administrador
- O Chat ID deve ser configurado corretamente

---

## 👤 Autor

**Karlos Sanchez**  
Estudante de Ciência da Computação  
Foco em automação, integração de sistemas e ciência de dados

---

## 📄 Licença

Projeto desenvolvido para fins educacionais e portfólio.
