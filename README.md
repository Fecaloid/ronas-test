### How to prepare project and run docker compose
1) Create .env file.
    ```
    cp .env_example .env
    ```
2) Create and start containers
    ```
    docker-compose build
    docker-compose up -d
   
3) Run migrations
    ```
    docker exec ronas_ronas_web_1 python3 manage.py migrate
    ```
   
4) Run tests
    ```
   docker exec ronas_ronas_web_1 python3 manage.py test
   ```
5) Read the docs
   ```
   http://127.0.0.1:8002/swagger/ # swagger view
   http://127.0.0.1:8002/redoc/ # redoc view
   ```