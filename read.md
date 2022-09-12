<b>Appication:</b>

1. Create project(Project name snippet).
2. Creating the project app (app name is textdata).
3. Using requirement.txt file we can install all the packages.
    syntax :
        pip install -r requirements.txt

Application work flow:

1. user want to register.

    api: http://127.0.0.1:8000/api/register/
2. User want to login and token will generate in response

    api: http://127.0.0.1:8000/api/token/login
3. Refresh token:

    api:http://127.0.0.1:8000/api/token/refresh/
4. Overview API (total count, listing)
    api:http://127.0.0.1:8000/api/totalCountList/
5. Create API
    api:http://127.0.0.1:8000/api/addingSnippet/
6. Detail API
   api:http://127.0.0.1:8000/api/viewListOfSnippet/
7. Update API
    api: http://127.0.0.1:8000/api/updateSnippet/{id}
8. Delete API
    api: http://127.0.0.1:8000/api/deleteSnippet/{id}
9. Tag list API
    api:http://127.0.0.1:8000/api/listTag/
10. Tag Detail API
    api:http://127.0.0.1:8000/api/tagDetails/