# 🚀 TaskHub — Gerenciador de Tarefas Pessoal

[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/LucasUandersonf/TaskHub)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-2.3.2-lightgrey)](https://flask.palletsprojects.com/)
[![Testes](https://img.shields.io/badge/testes-pytest-green)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

> ✨ Um gerenciador de tarefas moderno, seguro e intuitivo. Organize seu dia com eficiência e estilo usando o **TaskHub**.

---

![TaskHub Demo](https://user-images.githubusercontent.com/SEU_USUARIO/taskhub-demo.gif)

---

## 📚 Índice

- [📌 Sobre](#sobre)
- [⚙️ Funcionalidades](#funcionalidades)
- [🧪 Tecnologias Utilizadas](#tecnologias-utilizadas)
- [🚀 Instalação e Configuração](#instalação-e-configuração)
- [🧭 Como Usar](#como-usar)
- [🧪 Testes](#testes)
- [🎥 Demonstração](#demonstração)
- [🖼️ Screenshots](#screenshots)
- [🗺️ Roadmap](#roadmap)
- [❓ FAQ](#faq)
- [🤝 Contribuição](#contribuição)
- [📄 Licença](#licença)
- [📬 Contato](#contato)

---

## 📌 Sobre

**TaskHub** é uma aplicação web desenvolvida com **Python + Flask**, voltada para o gerenciamento pessoal de tarefas. Com arquitetura escalável, segurança robusta e uma interface responsiva baseada em **Bootstrap 5**, o TaskHub é ideal para quem busca produtividade sem complicações.

> 🧠 Arquitetura limpa com Application Factory  
> 🧩 Modularização com Blueprints  
> 🔐 Autenticação segura com Flask-Login

---

## ⚙️ Funcionalidades

- 🔐 Autenticação completa (cadastro, login, logout)
- 📝 CRUD de tarefas com prioridade, status e datas
- 🎯 Filtros inteligentes para organização eficiente
- 📱 Interface responsiva e moderna com Bootstrap 5
- 💬 Feedback em tempo real via mensagens flash
- 🧩 Estrutura modular para fácil manutenção
- 🔄 Migrações com Flask-Migrate e SQLAlchemy
- ✅ Testes automatizados com Pytest

---

## 🧪 Tecnologias Utilizadas

| 💻 Frontend     | 🧠 Backend      | 🗄️ Banco de Dados | 🧪 Testes        |
|----------------|----------------|-------------------|------------------|
| Bootstrap 5    | Python 3.10+   | SQLite            | Pytest           |
| HTML5, CSS3    | Flask 2.3.2    | SQLAlchemy ORM    | Flask-Testing    |

---

## 🚀 Instalação e Configuração

### 🔧 Pré-requisitos

- Python 3.10+
- Git

### 📦 Passos para rodar localmente

```bash
# Clonar o repositório
git clone https://github.com/LucasUandersonf/TaskHub.git
cd TaskHub

# Criar e ativar ambiente virtual
python -m venv venv

# Linux/macOS
source venv/bin/activate

# Windows
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Configurar variáveis de ambiente
export FLASK_APP=run.py
export FLASK_ENV=development
export SECRET_KEY='sua_chave_secreta_forte_aqui'

# Inicializar banco de dados
flask db init
flask db migrate -m "Criação inicial do banco"
flask db upgrade

# Executar aplicação
flask run
```

---

## 🧭 Como Usar

1. 📝 Acesse a página de registro e crie sua conta  
2. 🔐 Faça login com seu usuário e senha  
3. 📋 Crie, edite, visualize e exclua suas tarefas  
4. 🎯 Use filtros por prioridade e status para melhor organização  
5. 💬 Receba feedback instantâneo através das mensagens flash  
6. 📱 Acesse de qualquer dispositivo com a interface responsiva

---

## 🧪 Testes

Para executar os testes automatizados com cobertura, utilize:

```bash
pytest --cov=app tests/
```

---

## 🎥 Demonstração

Veja o TaskHub em ação:  
📽️ *[GIF de demonstração acima]*

---

## 🖼️ Screenshots

> Em breve: galeria com capturas da interface responsiva e funcionalidades em destaque.

---

## 🗺️ Roadmap

✨ Funcionalidades planejadas:

- 🗂️ Sistema de categorias para tarefas  
- 📧 Notificações por email e push  
- 📅 Integração com calendários externos (Google Calendar, Outlook)  
- 📱 Aplicativo mobile dedicado (React Native / Flutter)  
- 🌙 Modo escuro (dark mode)  
- 🎨 Melhorias na UI/UX baseadas no feedback dos usuários  
- ☁️ Deploy em ambiente cloud com CI/CD

> 💡 Contribuições são muito bem-vindas para acelerar esse roadmap!

---

## ❓ FAQ

**TaskHub é gratuito?**  
✅ Sim, é um projeto open source e gratuito para uso pessoal e educacional.

**Posso contribuir?**  
🛠️ Claro! Veja a seção [Contribuição](#contribuição) para saber como.

**Preciso de um banco de dados externo para rodar?**  
🗄️ Não, por padrão o projeto usa SQLite, que é embutido e simples para desenvolvimento local.

---

## 🤝 Contribuição

Contribuições são muito bem-vindas! Para contribuir com o projeto:

1. 🍴 Faça um fork deste repositório  
2. 🌿 Crie uma branch com sua feature: `git checkout -b minha-feature`  
3. 💬 Faça commits claros e objetivos  
4. 📥 Envie um pull request explicando as suas mudanças

---

## 📄 Licença

Este projeto está licenciado sob a licença **MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📬 Contato

**Lucas Uanderson** — Engenheiro de Software  
🔗 [LinkedIn](https://www.linkedin.com/in/SEU_USUARIO) | [GitHub](https://github.com/LucasUandersonf)  
📧 Email: lucasuandersonfs@outlook.com

---

> 💙 Obrigado por conferir o **TaskHub**. Sua produtividade merece uma ferramenta à altura!
