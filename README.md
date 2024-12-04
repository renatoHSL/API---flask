# API---flask

Este projeto é uma API RESTful para o gerenciamento de tarefas, desenvolvida com Python e Flask. O objetivo é
implementar uma API organizada, escalável e segura, que suporte operações CRUD (Create, Read, Update, Delete) para
entidades como usuários e tarefas.

Esse projeto está em construção, e as etapas iniciais envolvem a configuração da arquitetura do projeto, definição de
rotas e configuração do ambiente de desenvolvimento.

Objetivos do Projeto

Implementar uma estrutura de API RESTful escalável e organizada.
Criar endpoints para o gerenciamento de usuários e tarefas, com operações CRUD.
Incorporar boas práticas de segurança, validação de dados e autenticação com JWT.
Adicionar documentação automática dos endpoints usando Swagger ou OpenAPI (em fases posteriores).

Requisitos

Python 3.8+
Flask
SQLAlchemy (para conexão com o banco de dados)
python-dotenv (para gerenciamento de variáveis de ambiente)

Os endpoints planejados para o projeto incluem:

Usuários:

POST /users: Criar um novo usuário
GET /users: Listar todos os usuários
GET /users/{user_id}: Obter informações de um usuário específico
PUT /users/{user_id}: Atualizar dados de um usuário
DELETE /users/{user_id}: Excluir um usuário
Tarefas:

POST /tasks: Criar uma nova tarefa
GET /tasks: Listar todas as tarefas
GET /tasks/{task_id}: Obter detalhes de uma tarefa específica
PUT /tasks/{task_id}: Atualizar uma tarefa
DELETE /tasks/{task_id}: Excluir uma tarefa

Roadap:

# **Roadmap para Desenvolvimento da API RESTful**

## **Semana 1: Planejamento e Configuração Inicial**

### **Dia 1-2: Planejamento e Estruturação da Arquitetura**

- [X] Definir o objetivo principal da API e a entidade a ser gerenciada (ex.: usuários/tarefas ou produtos/pedidos).
- [X] Especificar rotas principais e endpoints (ex.: `/api/v1/users`, `/api/v1/tasks`).
- [X] Estruturar o projeto com diretórios organizados:
    - `/models` (modelos de dados)
    - `/routes` (definição das rotas)
    - `/services` (lógica de negócios)
    - `/config` (configurações sensíveis)
- [X] Configurar variáveis de ambiente (ex.: `env` para banco de dados e chaves secretas).

### **Dia 3-4: Configuração do Banco de Dados e Modelagem de Dados**

- [X] Escolher entre PostgreSQL ou MongoDB.
- [X] Criar o banco de dados e configurar a conexão.
- [X] Modelar as entidades principais:
    - **PostgreSQL**: Tabelas de `users` e `tasks` com relacionamento.
    - **MongoDB**: Coleções em MongoDB com `users` referenciando `tasks`.
- [ ] Implementar as migrações de banco de dados usando **Alembic** (se PostgreSQL).

---

## **Semana 2: Desenvolvimento CRUD e Validação**

### **Dia 5-8: Desenvolvimento dos Endpoints CRUD**

- [ ] Implementar rotas para operações básicas:
    - **Criar**: POST `/api/v1/users` ou `/api/v1/tasks`.
    - **Ler**: GET `/api/v1/users` (lista) e `/api/v1/users/{id}` (detalhe).
    - **Atualizar**: PUT `/api/v1/users/{id}`.
    - **Deletar**: DELETE `/api/v1/users/{id}`.
- [ ] Implementar validação de dados (com Pydantic ou Marshmallow).
- [ ] Adicionar tratamento de erros (ex.: dados inválidos ou recurso não encontrado).

### **Dia 9-10: Validação e Tratamento de Erros**

- [ ] Configurar middleware para capturar erros globais.
- [ ] Implementar mensagens personalizadas para erros:
    - **400**: Dados inválidos.
    - **401**: Não autorizado.
    - **404**: Recurso não encontrado.
    - **500**: Erro interno.
- [ ] Documentar como os erros são retornados para manter consistência.

---

## **Semana 3: Segurança e Documentação**

### **Dia 11-13: Autenticação e Autorização com JWT**

- [ ] Implementar geração de tokens JWT para autenticação.
- [ ] Criar rotas protegidas que exijam token válido (middleware de validação).
- [ ] Adicionar controle de autorização baseado em permissões.

### **Dia 14-15: Documentação da API com Swagger/OpenAPI**

- [ ] Configurar documentação automática:
    - **FastAPI**: Gerar documentação nativa.
    - **Flask**: Configurar com **Flask-Swagger** ou outro plugin.
- [ ] Adicionar descrições e exemplos detalhados para cada endpoint.
- [ ] Garantir que parâmetros de entrada e resposta estejam claros.

---

## **Semana 4: Testes e Deploy**

### **Dia 16-19: Testes Automatizados**

- [ ] Configurar ambiente de testes com **Pytest**.
- [ ] Escrever testes para todos os endpoints:
    - Cenários de sucesso (ex.: criação bem-sucedida de usuário).
    - Cenários de erro (ex.: tentativa de deletar recurso inexistente).
- [ ] Usar banco de dados de teste para evitar impacto no ambiente real.
- [ ] Configurar CI/CD com **GitHub Actions** para executar testes automaticamente.

### **Dia 20-22: Configuração de Docker para Deploy**

- [ ] Criar o `Dockerfile` para containerizar a API.
- [ ] Configurar `docker-compose.yml` para incluir banco de dados e API.
- [ ] Testar ambiente com containers para verificar integridade.
- [ ] Usar `.dockerignore` para evitar envio de arquivos desnecessários.

---

## **Semana 5: Finalização e Publicação**

### **Dia 23-24: Publicação e Divulgação**

- [ ] Atualizar o README do GitHub com:
    - Visão geral do projeto.
    - Passo a passo de instalação e execução.
    - Exemplos de chamadas de API.
    - Sugestões de melhorias futuras.
- [ ] Publicar um post no LinkedIn:
    - Explicar o objetivo da API e tecnologias usadas.
    - Destacar aprendizados e desafios enfrentados.
    - Incluir link para o repositório.

---

## **Checkpoints Importantes**

1. Configuração inicial do projeto e banco de dados funcionando.
2. CRUD completo com validação e mensagens de erro.
3. Implementação de autenticação e autorização com JWT.
4. Documentação acessível via Swagger/OpenAPI.
5. Testes automatizados cobrindo todos os endpoints.
6. API funcionando com containers Docker.

---

**Duração total estimada:** 20-24 dias (dedicação de 4-6 horas por dia).

# Extras Desejáveis para o Projeto

## 1. Funcionalidades Avançadas

- [ ] **Autenticação e Autorização**
    - Implementar autenticação com JWT para proteger rotas.
    - Criar permissões específicas (ex.: apenas criadores podem excluir tarefas).

- [ ] **Filtros e Paginação**
    - Adicionar filtros em rotas de listagem (ex.: `/tasks?status=done`).
    - Implementar paginação para grandes volumes de dados (ex.: `/users?page=2&limit=10`).

- [ ] **Rotas Relacionadas**
    - Criar rotas para associar/desassociar usuários e tarefas.
        - Ex.: `POST /tasks/{task_id}/users` para adicionar um usuário a uma tarefa.
    - Adicionar uma rota para listar as tarefas de um usuário:
        - Ex.: `GET /users/{user_id}/tasks`.

## 2. Validação e Segurança

- [ ] **Validação de Dados**
    - Usar bibliotecas como `Marshmallow` ou `Pydantic` para validar inputs.
    - Adicionar mensagens de erro claras para entradas inválidas.

- [ ] **Segurança Avançada**
    - Implementar CORS para limitar acesso a domínios específicos.
    - Adicionar limite de requisições por IP (Rate Limiting) para proteger contra abusos.

- [ ] **Hash de Senhas**
    - Usar bibliotecas como `bcrypt` para salvar senhas de forma segura.
    - Garantir que o fluxo de autenticação lide corretamente com hashes.

## 3. Experiência do Usuário e Recursos Úteis

- [ ] **Conexão com frontend**
    - Adicionar integração com algum frontend (ainda nao decidi como).

- [ ] **Busca Avançada**
    - Adicionar capacidade de busca por texto nas tarefas (ex.: `/tasks?search=nome`).

- [ ] **Notificações**
    - Enviar e-mails ou notificações em eventos importantes (ex.: quando uma tarefa for atribuída).

- [ ] **Logs e Auditoria**
    - Registrar logs de ações (ex.: quem criou/deletou uma tarefa).
    - Criar uma tabela de auditoria para rastrear alterações em dados.

## 4. Documentação e Testes

- [ ] **Documentação Automática**
    - Usar `Flask-Swagger` ou `Flasgger` para gerar documentação automática dos endpoints.

- [ ] **Testes Automatizados**
    - Configurar testes unitários com `Pytest`.
    - Testar rotas e cenários de erro (ex.: criação de usuário com dados incompletos).

## 5. Deploy e Infraestrutura

- [ ] **Deploy com Docker**
    - Criar um `Dockerfile` para a API e configurar `docker-compose` para rodar junto com o banco de dados.

- [ ] **Configuração CI/CD**
    - Configurar GitHub Actions para rodar testes e realizar deploy automático.

## 6. Melhorias de Performance

- [ ] **Cache**
    - Implementar cache para rotas frequentes (ex.: listagem de tarefas).

- [ ] **Websockets**
    - Usar Websockets para notificações em tempo real (ex.: atualização de status de tarefas).

## 7. Internacionalização (Opcional)

- [ ] **Suporte a Múltiplos Idiomas**
    - Adicionar suporte para diferentes idiomas (ex.: mensagens de erro em inglês e português).

## 8. Monitoramento e Observabilidade

- [ ] **Monitoramento**
    - Usar ferramentas como `Flask-Monitoring-Dashboard` para acompanhar desempenho e métricas.

- [ ] **Health Checks**
    - Adicionar uma rota simples para verificar o status do serviço (ex.: `/health`).

