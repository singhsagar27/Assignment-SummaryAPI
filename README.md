# 🚀 Summary & Bullet Points API  

A Django REST API that generates **summaries and bullet points** using Groq's LLM.  

## 📌 Features  
✅ Generate **text summaries** using AI  
✅ Convert text into **bullet points**  
✅ **JWT authentication** for security  
✅ Stores results in a **database**  
✅ **Swagger UI** for API documentation  

---

## 🔧 **Setup & Installation**  

### 1️⃣ Clone the Repository  
```sh
git clone https://github.com/singhsagar27/Assignment-SummaryAPI.git
cd Assignment-SummaryAPI
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
```sh
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=llama-3.3-70b-versatile
```

### 3️⃣ Apply Migrations & Create a Superuser
```sh
cd summary_api
python manage.py makemigrations summarizer
python manage.py migrate
python manage.py createsuperuser
```

### 6️⃣ Start the Server
```sh
python manage.py runserver
```

# 📜 API Endpoints  
## 🔑 Authentication (JWT)  

### **1️⃣ Generate Access & Refresh Tokens**  
```sh
curl --location 'http://127.0.0.1:8000/api/token/' \
--header 'Content-Type: application/json' \
--data '{
           "username": "sagar",
           "password": "Yureka10"
         }'
```

`
## 1️⃣ Generate Summary  

### 📌 Request:  
```sh
curl -X POST http://127.0.0.1:8000/api/generate-summary/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": "Artificial Intelligence (AI) is transforming industries."}'
```

### 📌 Response:  
```sh
{
  "refresh": "your_refresh_token_here",
  "access": "your_access_token_here"
}
```

## 1️⃣ Refresh Expired Access Token

```sh
curl --location 'http://127.0.0.1:8000/api/token/refresh/' \
--header 'Content-Type: application/json' \
--data '{
           "refresh": "your_refresh_token_here"
         }'
```

### 📌 Response:  
```sh
{
  "access": "your_new_access_token_here"
}
```

## 2️⃣ Generate Bullet Points 

### 📌 Request:  
```sh
curl -X POST http://127.0.0.1:8000/api/generate-bullet-points/ \
     -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"text": "Electric vehicles reduce pollution and lower fuel costs."}'
```

### 📌 Response:  
```sh
{
  "id": 2,
  "original_text": "Electric vehicles reduce pollution and lower fuel costs.",
  "summary": null,
  "bullet_points": [
    "- EVs help in reducing pollution.",
    "- They have lower fuel costs compared to gasoline vehicles."
  ],
  "created_at": "2025-02-09T12:11:11.376995Z"
}
```

## 🌐 Interactive API Documentation (Swagger UI)  
For full API documentation, visit:  
🔗 [Swagger UI](http://127.0.0.1:8000/swagger/)  

Run the server:  
```sh
python manage.py runserver
```

## 🧪 Running Unit Tests & Coverage
 
### 1️⃣ Run All Tests 
```sh
python manage.py test summarizer
```

### 2️⃣ Run a Specific Test
```sh
python manage.py test summarizer.tests.SummaryAPITest.test_generate_summary_valid_text
```

### 3️⃣⃣ Check Test Coverage
```sh
coverage run --source=summarizer manage.py test summarizer
coverage report -m
```

### 4️⃣ Generate HTML Coverage Report
```sh
coverage html
start htmlcov/index.html  # Windows
open htmlcov/index.html   # macOS/Linux
```

## 📖 Assumptions & Notes  
- Uses **Groq's LLM** for text processing.  
- **JWT authentication** is required for all API requests.  
- Only **authenticated users** can access API endpoints.  
- `summary` and `bullet_points` fields are **mutually exclusive**.  
- **Mocks are used in tests** to avoid real API calls.  

---

## ✅ Contributing  
1. **Fork the repository**  
2. **Create a new branch**  
3. **Make changes & push**  
4. **Submit a pull request**  

---

## 📃 License  
This project is licensed under the **MIT License**.  
