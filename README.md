# 🏥 Sinan Core

## 📌 O que é o Sinan?

O **SINAN (Sistema de Informação de Agravos de Notificação)** é um
sistema utilizado no Brasil para coletar, transmitir e disseminar dados
sobre doenças e agravos de notificação compulsória.

Essas informações são fundamentais para: - Monitoramento da saúde
pública - Planejamento de ações epidemiológicas - Controle de surtos e
doenças

------------------------------------------------------------------------

## 🛠️ Tecnologias utilizadas

-   Python\
-   Django\
-   PostgreSQL\
-   Docker\
-   Docker Compose\
-   pgAdmin

------------------------------------------------------------------------

## ⚙️ Como configurar o ambiente de desenvolvimento (Python)

### 1. Clone o repositório

    git clone <URL_DO_REPOSITORIO>
    cd sinan-core

### 2. Crie o ambiente virtual

    python -m venv venv

### 3. Ative o ambiente virtual

**Git Bash / Linux / macOS:**

    source venv/Scripts/activate

**Windows (PowerShell):**

    venv\Scripts\Activate.ps1

**Windows (CMD):**

    venv\Scripts\activate.bat

### 4. Instale as dependências

    pip install -r requirements.txt

### 5. Suba o banco de dados com Docker

    docker-compose up -d

### 6. Execute as migrations

    python manage.py migrate

### 7. Crie um superusuário

    python manage.py createsuperuser

### 8. Inicie o servidor

    python manage.py runserver

Acesse: - http://127.0.0.1:8000/ - http://127.0.0.1:8000/admin/

------------------------------------------------------------------------

## 📂 Estrutura do projeto

    sinan-core/
    ├── config/
    ├── apps/
    ├── venv/
    ├── docker-compose.yml
    ├── requirements.txt

------------------------------------------------------------------------

## 🚀 Observações

-   Certifique-se de que o Docker esteja em execução\
-   O banco PostgreSQL roda em `localhost:5432`\
-   As credenciais estão no `docker-compose.yml`
