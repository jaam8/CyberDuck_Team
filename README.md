Certainly! Here is a detailed and well-structured README for your project, taking into account the provided project structure and requirements.

---

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

3. **Запуск Docker контейнеров:**

   ```bash
   docker-compose up --build
   ```

### Проверка работы

После успешного запуска, сервис будет доступен по адресу [http://localhost:8000](http://localhost:8000).

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

## Стек технологий

- **Python:** Высокая производительность и большое сообщество разработчиков.
- **Django:** Быстрая разработка и безопасность.
- **PostgreSQL:** Надежная и мощная СУБД.
- **Docker:** Облегчает развертывание и масштабирование приложения.

## О команде

Наша команда состоит из шести участников, каждый из которых вносит уникальный вклад в проект:

1. **Имя Участника 1**
   - Роль: Backend Developer
   - Опыт: 5 лет в разработке на Python и Django.
   - Вклад: Реализация основной логики приложения и работа с базой данных.

2. **Имя Участника 2**
   - Роль: Frontend Developer
   - Опыт: 4 года в разработке интерфейсов.
   - Вклад: Создание интуитивно понятного и функционального интерфейса.

3. **Имя Участника 3**
   - Роль: DevOps Engineer
   - Опыт: 6 лет в DevOps.
   - Вклад: Настройка CI/CD и работа с Docker.

4. **Имя Участника 4**
   - Роль: Legal Advisor
   - Опыт: 10 лет в юридической практике.
   - Вклад: Обеспечение юридической значимости решения.

5. **Имя Участника 5**
   - Роль: Project Manager
   - Опыт: 8 лет в управлении проектами.
   - Вклад: Координация работы команды и контроль сроков.

6. **Имя Участника 6**
   - Роль: QA Engineer
   - Опыт: 7 лет в тестировании ПО.
   - Вклад: Обеспечение качества и стабильности работы приложения.

## Лицензия

Этот проект лицензируется под MIT License. Подробности см. в файле [LICENSE](LICENSE).
