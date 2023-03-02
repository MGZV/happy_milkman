## Simple CRM for farmer

1. Install Docker and Docker Compose
2. Rename .env-example to .env
3. Run command
`docker-compose up web`
4. Create migrations
`alembic revision --autogenerate -m "initial"`

5. Migrate
`alembic upgrade head`    

Docs
http://0.0.0.0:8000/docs
