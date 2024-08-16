# LoginSite

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-green)
![MongoDB](https://img.shields.io/badge/MongoDB-4.x-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-red)

![login](https://github.com/user-attachments/assets/9ecfeea2-1d72-496a-ab32-6758951350bb)


Este é um simples site de login desenvolvido para autenticação de usuários. O objetivo deste projeto é fornecer uma base para a criação de um sistema de login seguro e funcional, que pode ser facilmente integrado em projetos web maiores.

## Funcionalidades

- Login de usuários com email e senha.
- Sistema de hash para armazenamento seguro de senhas.
- Mensagens de erro para falhas de autenticação.
- Design responsivo, adaptado para dispositivos móveis.

## Tecnologias Utilizadas

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript (Vanilla)

- **Backend:**
  - Python
  - Flask
  - MongoDB (ou outro banco de dados à sua escolha)

- **Autenticação:**
  - JWT (JSON Web Tokens)
  - Bcrypt para hashing de senhas

## Instalação

Siga os passos abaixo para executar o projeto localmente:

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/nomedorepositorio.git
    ```

2. Navegue até o diretório do projeto:

    ```bash
    cd nomedorepositorio
    ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

4. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

5. Crie um arquivo `.env` na raiz do projeto e adicione as variáveis de ambiente necessárias:

    ```
    FLASK_APP=src/app.py
    FLASK_ENV=development
    MONGO_URI=sua_url_do_mongodb
    JWT_SECRET=sua_chave_secreta
    ```

6. Inicie o servidor Flask:

    ```bash
    flask run
    ```

7. Acesse o site no navegador:

    ```
    http://localhost:5000
    ```

## Estrutura de Pastas

```plaintext
├── public/
│   ├── css/
│   ├── js/
│   └── index.html
├── src/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   └── app.py
├── venv/
├── .env
├── requirements.txt
└── README.md
