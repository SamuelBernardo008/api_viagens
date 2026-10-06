# API Viagens

![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![uv](https://img.shields.io/badge/uv-DE5B88?style=for-the-badge&logo=astral&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

![GitHub Repo Size](https://img.shields.io/github/repo-size/SamuelBernardo008/api_viagens)
![GitHub License](https://img.shields.io/github/license/SamuelBernardo008/api_viagens?color=blue)

API RESTful para gestão de viagens desenvolvida em **Python** utilizando **FastAPI** e gerenciada de forma rápida e moderna com o **`uv`**.

---

## Sobre o Projeto

A **API Viagens** é um serviço backend projetado para gerenciar rotas, destinos e dados de viagens. A aplicação adota uma arquitetura modular dividida em modelos, schemas de validação e rotas, com integração a um banco de dados MySQL e documentação interativa gerada automaticamente via Swagger UI.

---

## Funcionalidades

- [x] **Arquitetura Modular**: Organização em diretórios `models`, `schema` e `route`.
- [x] **Validação de Dados**: Schemas com validação rigorosa via Pydantic.
- [x] **Integração com Banco de Dados**: Conexão otimizada com MySQL (suporte a `cryptography` / SHA-256).
- [x] **Documentação Automática**: Swagger UI (`/docs`) e ReDoc (`/redoc`).
- [x] **Gerenciamento Moderno de Pacotes**: Uso do `uv` com `pyproject.toml` e `uv.lock`.
- [x] **Testes Rápidos de Requisição**: Arquivo `tests.http` configurado para testes diretos no editor.

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3.12+
- **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
- **Gerenciador de Dependências:** [uv](https://github.com/astral-sh/uv)
- **Banco de Dados:** MySQL
- **Driver / Criptografia:** PyMySQL e Cryptography

---

## Estrutura do Projeto

```text
api_viagens/
├── app/
│   ├── models/       # Modelos de dados e entidades ORM
│   ├── route/        # Controladores e definições de endpoints
│   ├── schema/       # Validações e serialização com Pydantic
│   ├── __init__.py
│   ├── database.py   # Configuração e inicialização da conexão com MySQL
│   └── main.py       # Ponto de entrada da aplicação FastAPI
├── .gitignore
├── .python-version
├── pyproject.toml    # Configuração e dependências do projeto
├── README.md
├── tests.http        # Testes de requisições HTTP
└── uv.lock           # Arquivo de trava das versões exatas do uv
```

---

## Como Executar o Projeto

### Pré-requisitos

Antes de iniciar, certifique-se de ter instalado:
- [Python 3.9 ou superior](https://www.python.org/) 
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Servidor **MySQL** em execução e configurado

---

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/SamuelBernardo008/api_viagens.git
   cd api_viagens
   ```

2. **Sincronizar o ambiente virtual e dependências:**
   O `uv` gerenciará a criação do ambiente e a instalação das versões exatas:
   ```bash
   uv sync
   ```

3. **Executar a API com Uvicorn:**
   ```bash
   uv run uvicorn app.main:app --reload
   ```

4. **Acessar a documentação no navegador:**
   - **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Testando os Endpoints

- **Swagger UI:** Acesse `http://127.0.0.1:8000/docs` para interagir visualmente com os endpoints.
- **VS Code (`tests.http`):** Com a extensão **REST Client** instalada, abra o arquivo `tests.http` e clique em **"Send Request"** sobre cada requisição para testar as respostas da API.

---

## Como Contribuir

1. Faça um **Fork** do repositório.
2. Crie uma **Branch** para a sua funcionalidade:
   ```bash
   git checkout -b feature/nova-funcionalidade
   ```
3. Faça os **Commits**:
   ```bash
   git commit -m 'feat: Adiciona novo endpoint de viagens'
   ```
4. Envie as alterações (**Push**):
   ```bash
   git push origin feature/nova-funcionalidade
   ```
5. Abra um **Pull Request**.

---

## Licença

Este projeto está sob a licença [MIT](LICENSE).

---

## Contato

Desenvolvido por **Samuel Bernardo** 

- **GitHub:** [@SamuelBernardo008](https://github.com/SamuelBernardo008)
- **LinkedIn:** [Samuel Bernardo Rodrigues](https://www.linkedin.com/in/samuelbernardo008/?isSelfProfile=true)
