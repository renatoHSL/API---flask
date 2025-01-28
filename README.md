# **Projeto: API RESTful para Gerenciamento de Tarefas**

## **Objetivos do Projeto**

- Construir uma API RESTful organizada, escalável e segura.
- Implementar operações CRUD (Create, Read, Update, Delete) para usuários e tarefas.
- Incorporar práticas de segurança e validação de dados.

---

## **Requisitos**

### **1. Configuração Inicial e Arquitetura do Projeto**

- [x] Estruturar o projeto com diretórios organizados:
    - `/models`: Modelos de dados.
    - `/routes`: Definição das rotas.
    - `/services`: Lógica de negócios.
    - `/config`: Configurações sensíveis.
- [x] Configurar variáveis de ambiente (ex.: banco de dados, chaves secretas).
- [x] Configurar conexão com banco de dados PostgreSQL.
- [x] Criar tabelas de `users` e `tasks` com relacionamento usando SQLAlchemy.
- [x] Implementar migrações com Alembic.

---

### **2. Desenvolvimento CRUD**

- [x] Criar rotas para operações básicas:
    - **Usuários**
        - `POST /users`: Criar um novo usuário.
        - `GET /users`: Listar todos os usuários.
        - `GET /users/{user_id}`: Obter informações de um usuário específico.
        - `PUT /users/{user_id}`: Atualizar dados de um usuário.
        - `DELETE /users/{user_id}`: Excluir um usuário.
    - **Tarefas**
        - `POST /tasks`: Criar uma nova tarefa.
        - `GET /tasks`: Listar todas as tarefas.
        - `GET /tasks/{task_id}`: Obter detalhes de uma tarefa específica.
        - `PUT /tasks/{task_id}`: Atualizar uma tarefa.
        - `DELETE /tasks/{task_id}`: Excluir uma tarefa.
- [x] Implementar validação de dados usando Marshmallow.

---

### **3. Login, Validação, Tratamento de Erros e Segurança**

- [x] Adicionar tratamento de erros para casos comuns:
    - **400**: Dados inválidos.
    - **404**: Recurso não encontrado.
    - **500**: Erro interno.
- [X] Adicionar um fluxo de login para autenticação do usuário:
    - Criar um endpoint `POST /login` para autenticar o usuário.
    - Validar as credenciais (e-mail e senha) contra o banco de dados.
- [X] Implementar autenticação básica com JWT:
    - Retornar um token JWT se as credenciais forem válidas.
    - Gerar tokens JWT para autenticação.

---

### **4. Documentação da API**

- [X] Adicionar documentação automática usando Flasgger.
- [X] Garantir descrições claras e exemplos de entradas e saídas para cada endpoint.

---

### **5. Testes Automatizados**

- [X] Configurar ambiente de testes com Pytest.
- [X] Criar testes para validar cenários principais:
- [X] Usar banco de dados de teste para evitar impacto no ambiente real.

---

### **6. Deploy e Deployability**

- [X] Criar um `Dockerfile` para containerizar a aplicação.
- [X] Configurar `docker-compose.yml` para rodar API e banco de dados localmente.
- [X] Usar `.dockerignore` para evitar envio de arquivos desnecessários.
