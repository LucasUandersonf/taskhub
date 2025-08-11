# TaskHub

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/LucasUandersonf/TaskHub)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3.2-lightgrey)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

TaskHub é uma aplicação web moderna para gerenciamento de tarefas pessoais, construída com Python e Flask seguindo boas práticas de arquitetura, modularidade e segurança. O sistema conta com autenticação de usuários, CRUD completo de tarefas, interface responsiva com Bootstrap e testes automatizados, visando escalabilidade e código limpo.

---

## Índice

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Arquitetura do Projeto](#arquitetura-do-projeto)
- [Instalação e Configuração](#instalação-e-configuração)
- [Como Usar](#como-usar)
- [Testes](#testes)
- [Contribuição](#contribuição)
- [Licença](#licença)

---

## Sobre

O TaskHub foi desenvolvido com o objetivo de oferecer uma ferramenta simples, eficiente e segura para organização pessoal de tarefas. O projeto utiliza uma arquitetura em camadas, com uso do padrão Application Factory do Flask para facilitar manutenção e escalabilidade. O foco principal é o desenvolvimento profissional de software, com atenção especial a testes, segurança e usabilidade.

---

## Funcionalidades

- Cadastro, login e logout de usuários com autenticação segura (Flask-Login)
- CRUD completo de tarefas (criar, visualizar, editar, excluir)
- Organização das tarefas com prioridade, status e datas
- Interface responsiva usando Bootstrap 5 para melhor experiência em desktop e mobile
- Mensagens flash para feedback ao usuário
- Estrutura modular com Blueprints para separação de funcionalidades
- Migrações de banco com Flask-Migrate e SQLAlchemy ORM
- Testes unitários e funcionais com pytest para garantir qualidade do código

---

## Tecnologias Utilizadas

- Python 3.10+
- Flask 2.3.2
- SQLAlchemy ORM
- Flask-Migrate (Alembic)
- Flask-Login
- Flask-WTF (forms seguros e validados)
- Bootstrap 5 (UI responsiva)
- pytest (testes automatizados)
- SQLite (banco de dados local para desenvolvimento)

---

## Arquitetura do Projeto

O TaskHub utiliza a arquitetura **Application Factory** do Flask, que permite criar a aplicação via função `create_app()`, facilitando configuração dinâmica e testes. O código está organizado em Blueprints para separar as responsabilidades:


taskhub
├── app/
│    ├── init.py         # Application factory, extensões, config
│    ├── models.py           # Modelos SQLAlchemy
│    ├── auth/               # Blueprint de autenticação (login, logout, registro)
│    ├── tasks/              # Blueprint de gerenciamento de tarefas (CRUD)
│    ├── templates/          # HTML com Jinja2
│    ├── static/             # CSS, JS, imagens
│    └── forms.py            # Flask-WTF forms
├── tests/                   # Testes unitários e funcionais com pytest
├── migrations/              # Scripts de migração do banco
├── config.py                # Configurações da aplicação (dev, prod, test)
├── requirements.txt         # Dependências
└── run.py                   # Script para rodar a aplicação



---

## Instalação e Configuração

Siga os passos abaixo para rodar o TaskHub localmente:

```bash
# Clone o repositório
git clone https://github.com/LucasUandersonf/TaskHub.git
cd TaskHub

# Crie e ative o ambiente virtual
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Configure variáveis de ambiente (exemplo para Linux/macOS)
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY='uma_chave_secreta_forte'

# Crie o banco e execute as migrações
flask db init
flask db migrate -m "Criação inicial do banco"
flask db upgrade

# Execute a aplicação
flask run
```

Acesse http://localhost:5000 no navegador para usar o sistema.

Como Usar
	•	Cadastre uma nova conta pelo formulário de registro
	•	Faça login para acessar sua dashboard pessoal
	•	Crie, edite, visualize e exclua tarefas facilmente
	•	Use a interface responsiva para acessar o TaskHub em dispositivos móveis
	•	Receba mensagens de feedback após ações realizadas (sucesso, erro)

⸻

Testes

Para garantir a qualidade do código, o TaskHub possui testes automatizados com pytest. Para rodá-los:

# Certifique-se que o ambiente virtual está ativado
pytest --cov=app tests/


Desenvolvido por Lucas Uanderson
LinkedIn | GitHub
