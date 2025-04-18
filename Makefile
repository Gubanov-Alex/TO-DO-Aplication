.PHONY=run
run:
	python src/manage.py runserver

.PHONY=revision
revision:
	python src/manage.py makemigrations

.PHONY=migrate
migrate:
	python src/manage.py migrate


#====================================
#Reqests
#====================================


.PHONY=john_create
john_create:
	curl -X POST -H "Content-Type: application/json" --location http://localhost:8000/users/ --data '{"email": "john@email.com", "name": "john", "password": "Sasha666"}'


.PHONY=john_token
john_token:
	curl -X POST -H "Content-Type: application/json" --location http://localhost:8000/auth/token/ -d '{"email": "john@email.com", "password": "Sasha666"}'



.PHONY=john_get
john_get:
	curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0OTk3NDk3LCJpYXQiOjE3NDQ5OTcxOTcsImp0aSI6IjgxNTRhOWJmMTdlYzQ3NmZiNGZhOGQ2YWJhOTJmZTE3IiwidXNlcl9pZCI6Mn0.izzsFmq7zhh_DIeTuTCI0-dOwAFWFamllQQaNvRSiPc" --location http://localhost:8000/users/ | jq


.PHONY=task_create
task_create:
	curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDAyNDUyLCJpYXQiOjE3NDUwMDIxNTIsImp0aSI6ImU2Zjc0MDM0ZjhmYTQ2NDNhOWE3Y2RjNTdkZGZmYTU0IiwidXNlcl9pZCI6Mn0.5grDYL_VHrOiUgxySChUIxP02LvvnZG8-7oE_VPhtEw" --location http://localhost:8000/tasks/ -d '{"title": "bread", "description": "buy 2kg"}'

.PHONY=task_get
task_get:
	curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDAyNDUyLCJpYXQiOjE3NDUwMDIxNTIsImp0aSI6ImU2Zjc0MDM0ZjhmYTQ2NDNhOWE3Y2RjNTdkZGZmYTU0IiwidXNlcl9pZCI6Mn0.5grDYL_VHrOiUgxySChUIxP02LvvnZG8-7oE_VPhtEw" --location http://localhost:8000/tasks/ | jq


.PHONY=file
file:
	curl -X POST \
	-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDA0MzcyLCJpYXQiOjE3NDUwMDQwNzIsImp0aSI6IjIyMzc2ZTliOWQxNTRmM2Q5Zjc0NzcyOTk0Mzc3ZTFiIiwidXNlcl9pZCI6Mn0.KW0hV7dwhwL5-J6LMJT1zzBImIVPaLk5a7QrW9xaLOY" \
	-F "attachment=@/home/oleksandr/PycharmProjects/TO-DO-Aplication/file.txt" \
	http://localhost:8000/tasks/2/attachment/ | jq


.PHONY=toggle
toggle:
	curl -X POST \
	-H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1MDA1MDY5LCJpYXQiOjE3NDUwMDQ3NjksImp0aSI6ImNmM2ZmMjhkMTYzYTQ5MzQ5OGMwNDBhNzRmYjhkYTIxIiwidXNlcl9pZCI6Mn0.cJctJ1G3HUGQND6nrRL1mwoCOiUMptIIXzlEivMMbKc" \
	http://localhost:8000/tasks/2/toggle/ | jq