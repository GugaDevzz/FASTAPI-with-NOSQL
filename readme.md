# FastAPI with NoSQL / JSON 🚀

\[pt-br\] | [en](#-english-version)

## 🇧🇷 Versão em Português

O **FASTAPI-with-NOSQL** é uma API RESTful assíncrona desenvolvida em Python com **FastAPI**, projetada para gerenciar cadastros e persistir dados utilizando uma estrutura NoSQL / banco em arquivo JSON (`armazenar.json`).

Este projeto evolui a lógica de cadastro tradicional para um serviço web moderno, fornecendo documentação automática (Swagger/ReDoc), validação de esquema e respostas estruturadas em JSON.

---

### 📌 Sumário

* [Funcionalidades](#-funcionalidades)
* [Estrutura do Projeto](#-estrutura-do-projeto)
* [Pré-requisitos](#-pré-requisitos)
* [Como Executar](#-como-executar)
* [Documentação da API](#-documentação-da-api)
* [Descrição dos Módulos](#-descrição-dos-módulos)
* [Licença](#-licença)

---

### ✨ Funcionalidades

* **API RESTful de Alta Performance:** Construída com FastAPI e executada via Uvicorn.
* **Persistência de Dados em JSON (NoSQL):** Operações CRUD integradas a um banco em documento JSON local (`armazenar.json`).
* **Documentação Automática:** Interface interativa Swagger UI e ReDoc geradas automaticamente.
* **Separação de Responsabilidades:** Módulos isolados para conexões, checkout e rotas principais.

---

### 📂 Estrutura do Projeto

```
FASTAPI-with-NOSQL-main/
├── API cadastro/
│   ├── armazenar.json       # Ficheiro/banco de dados NoSQL local
│   ├── chekout.py           # Regras e fluxo de checkout
│   ├── conectar_json.py     # Gerenciador de conexão e leitura/escrita do JSON
│   └── main.py              # Ponto de entrada da API e definição das rotas FastAPI
└── .gitattributes           # Configurações do Git
```

---

### 🛠️ Pré-requisitos

Certifique-se de ter o **Python 3.8+** instalado em sua máquina.

```bash
python --version
```

Instale as dependências necessárias (FastAPI e Uvicorn):

```bash
pip install fastapi uvicorn
```

---

### 🚀 Como Executar

1. Navegue até o diretório da API:

   ```bash
   cd "FASTAPI-with-NOSQL-main/API cadastro"
   ```

2. Inicie o servidor da API com **Uvicorn**:

   ```bash
   uvicorn main:app --reload
   ```

3. O servidor estará rodando em: `http://127.0.0.1:8000`

---

### 📖 Documentação da API

Após iniciar o servidor, você pode testar todos os endpoints diretamente no navegador:

* **Swagger UI (Interativo):** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 🧩 Descrição dos Módulos

* **`main.py`**: Arquivo principal contendo a instância da aplicação `FastAPI`, rotas e middleware.
* **`conectar_json.py`**: Responsável por ler, gravar e atualizar dados em tempo real no arquivo `armazenar.json`.
* **`chekout.py`**: Lógica de negócios voltada ao encerramento de cadastros ou processos de compra/registro.
* **`armazenar.json`**: Base de dados local em formato de documento NoSQL.

---

## 🇺🇸 English Version

**FASTAPI-with-NOSQL** is an asynchronous RESTful API built with Python and **FastAPI**, designed for managing registrations and persisting data using a NoSQL / JSON-file storage backend (`armazenar.json`).

This project transitions standard registration scripts into a modern web service with automated OpenAPI docs, schema validation, and JSON responses.

---

### 📌 Table of Contents

* [Features](#-features-1)
* [Project Structure](#-project-structure-1)
* [Prerequisites](#-prerequisites-1)
* [How to Run](#-how-to-run-1)
* [API Documentation](#-api-documentation)
* [Module Breakdown](#-module-breakdown-1)
* [License](#-license-1)

---

### ✨ Features

* **High-Performance REST API:** Built using FastAPI and served via Uvicorn.
* **JSON Document Storage (NoSQL style):** Direct CRUD operations on `armazenar.json`.
* **Automated Documentation:** Instant Swagger UI and ReDoc interface generation.
* **Modular Architecture:** Isolated modules for database connection, checkout procedures, and API endpoints.

---

### 📂 Project Structure

```
FASTAPI-with-NOSQL-main/
├── API cadastro/
│   ├── armazenar.json       # Local NoSQL JSON database
│   ├── chekout.py           # Checkout/completion business logic
│   ├── conectar_json.py     # JSON read/write helper functions
│   └── main.py              # FastAPI app entry point and endpoints
└── .gitattributes           # Git repository configuration
```

---

### 🛠️ Prerequisites

Ensure you have **Python 3.8+** installed.

```bash
python --version
```

Install required dependencies:

```bash
pip install fastapi uvicorn
```

---

### 🚀 How to Run

1. Navigate to the API folder:

   ```bash
   cd "FASTAPI-with-NOSQL-main/API cadastro"
   ```

2. Start the API server using **Uvicorn**:

   ```bash
   uvicorn main:app --reload
   ```

3. Access the application at: `http://127.0.0.1:8000`

---

### 📖 API Documentation

Once the server is running, explore and test the endpoints:

* **Interactive Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc Documentation:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 🧩 Module Breakdown

* **`main.py`**: Central script defining `FastAPI()` application routes and endpoints.
* **`conectar_json.py`**: Database utility for parsing and serializing JSON records in `armazenar.json`.
* **`chekout.py`**: Checkout process validation and business logic handler.
* **`armazenar.json`**: Primary data storage structured as a NoSQL JSON document.

---

## 📄 Licença / License

Este projeto está sob a licença MIT / This project is licensed under the MIT License.