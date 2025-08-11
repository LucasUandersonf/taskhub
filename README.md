# 🚀 TaskHub — Gerenciador de Tarefas Pessoal

✨ Um gerenciador de tarefas moderno, seguro e intuitivo. Organize seu dia com eficiência e estilo usando o TaskHub.

---

## 📌 Sobre

TaskHub é uma aplicação web desenvolvida em Python com Flask, voltada para o gerenciamento pessoal de tarefas. Com arquitetura escalável, segurança robusta e interface responsiva baseada em Bootstrap 5, o TaskHub oferece uma solução completa para aumentar sua produtividade.

- 🧠 Arquitetura limpa com Application Factory  
- 🧩 Modularização com Blueprints  
- 🔐 Autenticação segura com Flask-Login  

---

## ⚙️ Funcionalidades

- 🔐 Registro, login e logout de usuários  
- 📝 CRUD completo de tarefas (criar, listar, editar, excluir)  
- 🎯 Filtros por prioridade, status e datas  
- 📱 Interface responsiva com Bootstrap 5  
- 💬 Feedback instantâneo via mensagens flash  
- 🔄 Migrações automáticas de banco com Flask-Migrate  
- ✅ Testes automatizados com pytest e medição de cobertura  
- ☁️ Deploy em ambiente cloud (Render)  

---

## 🧪 Tecnologias Utilizadas

| Frontend       | Backend                  | Banco de Dados           | Testes               | Deploy     |
|----------------|--------------------------|-------------------------|----------------------|------------|
| HTML5, CSS3    | Python 3.10+, Flask 2.3.2| SQLite (dev) / PostgreSQL (prod) | pytest, pytest-cov    | Render     |
| Bootstrap 5    | Flask-Login, Flask-WTF   | SQLAlchemy ORM          | Flask-Testing        |            |

---

## 🚀 Instalação e Configuração

### Pré-requisitos

- Python 3.10+  
- Git  

### Passos para rodar localmente

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

Relatório Final — Projeto TaskHub

Visão Geral:
TaskHub é um sistema web para gerenciamento de tarefas com autenticação, interface responsiva e arquitetura escalável, desenvolvido como projeto completo para portfólio aplicando boas práticas profissionais.

Objetivos:
	•	Aprender e aplicar Flask profissionalmente
	•	CRUD protegido por autenticação
	•	Padrões e arquitetura de mercado (App Factory, Blueprints, ORM, Migrations)
	•	MVP pronto para produção
	•	Testes automatizados para garantir qualidade

Principais Funcionalidades:
	•	Registro e login com Flask-Login
	•	CRUD completo de tarefas com controle de acesso por usuário
	•	Interface responsiva com Bootstrap
	•	Migrações automáticas com Flask-Migrate
	•	Deploy em Render
	•	Testes com pytest e cobertura

Arquitetura e Boas Práticas:
	•	App Factory para múltiplos ambientes
	•	Modularização com Blueprints
	•	ORM + Migrations para banco
	•	Camada de formulários separada (Flask-WTF)
	•	Segurança com hashing de senha
	•	Testes unitários e integração

Aprendizados e Resultados:
	•	Domínio de arquitetura Flask profissional
	•	Experiência com deploy e problemas de produção
	•	Uso de ORM e migrações reais
	•	Implementação de testes e métricas de qualidade
	•	Projeto pronto para portfólio e entrevistas

Próximos Passos:
	•	Sistema de prioridade para tarefas
	•	Filtros e busca avançada
	•	API REST para mobile
	•	Melhorias de design com componentes customizados


> 💙 Obrigado por conferir o **TaskHub**. Sua produtividade merece uma ferramenta à altura!
