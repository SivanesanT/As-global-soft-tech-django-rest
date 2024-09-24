from django.urls import include, path
from .views import *

urlpatterns = [
    path('member/', MymemberView.as_view()),
    path('member/<int:pk>/', MymemberView.as_view()),
    path('register/',registerUser.as_view()),    
    path('login/', LoginUser.as_view()),
]





# token 42be20f4c097e0e7204229029f6c668fcda33dbe sri sri@123
# Postman: -> POST: http://127.0.01:8000/register/ { "username":"name", "email":"email@email.com", "password": "password@123" }

# -> POST: http://127.0.0.1:8000/login/ { "username":"name", "password": "password@123" } #it will give ressponse at token take it .

# ------------------------------------------CRUD--------------------------------

# ->GET: http://127.0.0.1:8000/member/ //include the header as token "it given token" and Aurthorization it now send request to get all datas

# ->POST: http://127.0.0.1:8000/member/ //include the headers as token { "name":"yourname", "age":20, "description":"just test" }

# ->PUT: http://127.0.0.1:8000/member/(give a id)/ //include the headers as token { "name":"updatedname", "age":23, "description":"just updatetest" }

# ->PATCH: http://127.0.0.1:8000/member/(give a id)/ //include the headers as token { "description":"just updatetest1" }

# ->DELETE: http://127.0.0.1:8000/member/(give a id)/ //include the headers as token