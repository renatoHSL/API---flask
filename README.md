# **API RESTful para Gerenciamento de Tarefas**

![Python](https://img.shields.io/badge/python-v3.11-blue)
![Flask](https://img.shields.io/badge/flask-v3.0.3-lightblue)
![PostgreSQL](https://img.shields.io/badge/postgresql-v12-green)
![Docker](https://img.shields.io/badge/docker-ready-important)

## **Descrição**

Esta API foi desenvolvida para gerenciar tarefas e usuários de forma eficiente, seguindo boas práticas de arquitetura e
segurança. A aplicação oferece funcionalidades completas de **CRUD** para **usuários** e **tarefas**, além de
autenticação segura com **JWT**.

---

## **Principais Recursos**

- **CRUD Completo:**
    - Usuários e tarefas com rotas específicas.
- **Autenticação JWT:**
    - Login seguro e geração de tokens.
- **Banco de Dados Relacional:**
    - Integração com PostgreSQL usando SQLAlchemy.
- **Validação de Dados:**
    - Marshmallow para validação e serialização de entrada/saída.
- **Documentação Automática:**
    - Gerada automaticamente com Flasgger.
- **Testes Automatizados:**
    - Pytest para validação de funcionalidades principais.
- **Ambiente Contêinerizado:**
    - Configuração pronta com Docker e Docker Compose.

---

## **Principais Endpoints**

### **1. Usuários**

- **Criar Usuário**:  
  `POST /users`  
  **Descrição**: Cria um novo usuário.  
  **Exemplo de Payload**:
  ```json
  {
    "name": "João Silva",
    "email": "joao@email.com",
    "password": "senha123"
  }
  ```

- **Listar Usuários**:
  `GET /users`
  **Descrição**: Retorna todos os usuários cadastrados.

- **Buscar Usuário por ID**:
  `GET /users/{user_id}`
  **Descrição**: Descrição: Retorna as informações de um usuário específico.

- **Atualizar Usuário**:
  `PATCH /users/{user_id}`
  **Descrição**: Atualiza os dados de um usuário.

- **Excluir Usuário**:
  `DELETE /users/{user_id}`
  **Descrição**: Descrição: Remove um usuário do sistema.

### **2. Tarefas**

- **Criar Tarefa**:  
  `POST /tasks`  
  **Descrição**: Cria uma nova tarefa.  
  **Exemplo de Payload**:
  ```json
  {
    "title": "Finalizar relatório",
    "description": "Concluir o relatório mensal até sexta-feira",
    "user_id": 1
  }
  ```

- **Listar Tarefas**:
  `GET /id/tasks`
  **Descrição**: Retorna todas as tarefas cadastradas.

- **Buscar Tarefa por ID**:
  `GET /tasks/id/{task_id}`
  **Descrição**: Descrição: Retorna os detalhes de uma tarefa específica.

- **Atualizar Tarefa**:
  `PATCH /tasks/id/{task_id}`
  **Descrição**: Atualiza as informações de uma tarefa.

- **Excluir Tarefa**:
  `DELETE /tasks/id/{task_id}`
  **Descrição**: Descrição: Remove uma tarefa do sistema.

- **Buscar Tarefa por ID do Usuário**:
  `GET /tasks/user_id/{user_id}`
  **Descrição**: Descrição: Retorna os detalhes de todas as tarefas de um usuário específico.

- **Atualizar Tarefa de um Usuário**:
  `PATCH /tasks/user_id/{user_id}`
  **Descrição**: Atualiza as informações de uma tarefa de um usuário específico.

- **Excluir Tarefa de um Usuário**:
  `DELETE /tasks/user_id/{user_id}`
  **Descrição**: Descrição: Remove uma tarefa do sistema de um usuário específico.

### **3. Autenticação**

## Login

**Endpoint:**  
`POST /login`

**Descrição:**  
Valida as credenciais do usuário e retorna um token JWT.

**Exemplo de Payload:**

  ```json
  {
  "email": "joao@email.com",
  "password": "senha123"
}
  ```

## **4. Testes Automatizados**

Este projeto inclui testes automatizados utilizando **Pytest** para garantir a funcionalidade e a confiabilidade da API.
Os testes cobrem cenários principais, como:

- Operações CRUD para usuários e tarefas.
- Validação de autenticação com JWT.
- Tratamento de erros comuns (400, 404, 500).

### **5. Funcionalidades Extras**

## Validação de Dados

Os dados de entrada são validados utilizando **Marshmallow**.

## Tratamento de Erros

Respostas claras para erros comuns, como:

- **400:** Requisição inválida.
- **404:** Recurso não encontrado.
- **500:** Erro interno no servidor.

## Documentação da API

Disponível em `/apidocs` para facilitar a exploração dos endpoints.