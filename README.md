# CyberDuck Team - Legal Entity Rights Verification Service

## Описание проекта

Проект создан для автоматизации процесса проверки прав юридического лица на подписание документов. Основная цель - упростить процесс проверки доверенности и права представления в юридических отношениях через использование современных цифровых технологий. Наше решение позволяет компаниям быстро и надежно удостоверяться в легитимности представителей, сокращая время и ресурсы, затрачиваемые на ручную проверку.

## Как запустить

### Настройка окружения

1. **Клонирование репозитория:**

   ```bash
   git clone https://github.com/jaam8/CyberDuck_Team.git
   cd CyberDuck_Team
   ```

2. **Заполнение `.env` файлов:**

   - Скопируйте файлы `.env.example` в `.env` в директории `.docker` и `backend`.
   - Заполните необходимые параметры в файлах `.env`.

   Пример:

   ```env
   # .docker/.env
   POSTGRES_USER=your_db_user
   POSTGRES_PASSWORD=your_db_password
   POSTGRES_DB=your_db_name
   ```

   ```env
   # backend/.env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DATABASE_URL=postgres://your_db_user:your_db_password@postgres/your_db_name
   ```

3. **Настройка SSL сертификатов для Nginx:**

   - Создайте директорию для хранения сертификатов:

     ```bash
     mkdir -p .docker/nginx/certs
     ```

   - Поместите ваши SSL сертификаты и ключи в `.docker/nginx/certs`:

     - `fullchain.pem` - ваш полный цепной сертификат
     - `privkey.pem` - ваш закрытый ключ

   - Обновите конфигурацию Nginx в `.docker/nginx/nginx.conf` для использования SSL:

     ```nginx
     server {
         listen 80;
         listen [::]:80;
         server_name your_domain.com;
         return 301 https://$host$request_uri;
     }

     server {
         listen 443 ssl;
         listen [::]:443 ssl;
         server_name your_domain.com;

         ssl_certificate /etc/nginx/certs/fullchain.pem;
         ssl_certificate_key /etc/nginx/certs/privkey.pem;
         ssl_protocols TLSv1.2 TLSv1.3;
         ssl_prefer_server_ciphers on;

         location / {
             proxy_pass http://backend:8000;
             proxy_set_header Host $host;
             proxy_set_header X-Real-IP $remote_addr;
             proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
             proxy_set_header X-Forwarded-Proto $scheme;
         }
     }
     ```

4. **Запуск Docker контейнеров:**

   ```bash
   docker-compose up --build
   ```

### Проверка работы

После успешного запуска, сервис будет доступен по адресу [https://your_domain.com](https://your_domain.com).

## Описание решения

### Преимущества

- **Автоматизация:** Сокращение времени на проверку доверенности и прав представления.
- **Безопасность:** Использование электронных подписей и иных способов легитимации, что гарантирует юридическую значимость.
- **Удобство:** Предоставление шаблонов авторизационных писем в электронном виде, что упрощает процесс взаимодействия с клиентами.
- **Снижение затрат:** Уменьшение необходимости ручной проверки, что экономит ресурсы компании.

### Архитектура

Наше решение построено на микросервисной архитектуре с использованием Docker для контейнеризации. Основные компоненты включают:

- **Backend:** Реализован на Python с использованием фреймворка Django. Отвечает за логику приложения и работу с базой данных.
- **Frontend:** Отвечает за взаимодействие с пользователем и предоставление интуитивно понятного интерфейса.
- **Database:** PostgreSQL используется для хранения всех необходимых данных.
- **Nginx:** Используется как обратный прокси-сервер для управления входящими запросами и распределения нагрузки.

### Модульность

Проект организован таким образом, чтобы облегчить его расширение и поддержку. Каждая часть системы (backend, frontend, database) изолирована и может быть обновлена или заменена независимо от других.

### Безопасность

Особое внимание уделено безопасности данных и взаимодействий:
- Все данные передаются по защищенным каналам (SSL).
- Используются современные методы аутентификации и авторизации.
- Регулярные обновления и патчи для всех используемых библиотек и компонентов.

## Стек технологий

- **Python:** Высокая производительность и большое сообщество разработчиков.
- **Django:** Быстрая разработка и безопасность.
- **PostgreSQL:** Надежная и мощная СУБД.
- **Docker:** Облегчает развертывание и масштабирование приложения.
- **Nginx:** Эффективный и надежный веб-сервер.

## Лицензия

Этот проект лицензируется под MIT License. Подробности см. в файле LICENSE.
