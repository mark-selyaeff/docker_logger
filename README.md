# Docker logger
**Инструкция:**
1. `make build`
2. `make start`
3. Через `nc localhost 65432` посылаем какие-нибудь запросы
4. `make stop` чтобы остановить контейнер
5. `make clean` чтобы удалить контейнер, образ и созданный volume
