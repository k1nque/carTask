# carTask
## Запуск и настройка

##### docker-compose.yml:
 - В сервисе postgres укажите поля: 
 -- POSTGRES_DB
 -- POSTGRES_USER
 -- POSTGRES_PASSWORD
 -- Также можете изменить порты по умолчанию
---
#### Настройка переменный окружения (.env)
 - Переименуйте template.env в .env, а также укажите нужные поля, в зависимости от внесенных изменений ранее в docker-compose.yml

## Запуск

```bash
docker compose up
```