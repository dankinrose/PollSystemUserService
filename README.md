[Uploading README.md…]()
# 🗳️ Poll System – Backend (Microservices)

Backend system built with **FastAPI** using a **Microservices architecture**, including two independent services and two dedicated MySQL databases, fully orchestrated with **Docker Compose**.

This README explains **exactly how to run the system end-to-end**.

---

## 🧱 Architecture Overview

The system consists of **four containers**:

### User Service
- FastAPI application
- Manages users
- Runs on port **8000**
- Database: **MySQL (user-db)**

### Poll Service
- FastAPI application
- Manages polls, questions, and votes
- Communicates with User Service via HTTP
- Runs on port **8081**
- Database: **MySQL (poll-db)**

### Databases
- `user-db` – MySQL for User Service
- `poll-db` – MySQL for Poll Service

All components run on the same internal Docker network.

---

## 📁 Relevant Project Structure

```text
PollSystemUserService/
│
├── infra/
│   └── docker-compose.yml
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── ...
│
└── requirements.txt
```

```text
PollSystemPollService/
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── ...
│
└── requirements.txt
```

---

## ⚙️ Prerequisites

- Docker Desktop (with Docker Compose)
- Windows / Linux / macOS
- Free ports:
  - 8000
  - 8081
  - 3306
  - 3307

---

## ▶️ How to Run the System

### 1️⃣ Navigate to the infra directory
All commands **must be executed from the infra directory**:

```powershell
cd PollSystemUserService/infra
```

---

### 2️⃣ Clean previous runs (recommended)
```powershell
docker compose down -v --remove-orphans
```

---

### 3️⃣ Verify defined services
```powershell
docker compose config --services
```

Expected output:
```text
poll-db
poll-service
user-db
user-service
```

---

### 4️⃣ Start the databases
```powershell
docker compose up -d poll-db user-db
```

Wait until both databases are **healthy**:

```powershell
docker compose ps
```

---

### 5️⃣ Start the services
```powershell
docker compose up -d poll-service user-service
```

---

### 6️⃣ Verify running containers
```powershell
docker ps
```

You should see:
- infra-user-service-1
- infra-poll-service-1
- infra-user-db-1 (healthy)
- infra-poll-db-1 (healthy)

---

## 🌐 API Documentation

Swagger UI is available at:

- **User Service**  
  http://localhost:8000/docs

- **Poll Service**  
  http://localhost:8081/docs

If both pages load successfully, the system is running correctly.

---

## 🔗 Internal Service Communication

Inside Docker:
- Services communicate **by service name**
- `localhost` is **never used** for inter-service communication

Examples:
- Poll → User: `http://user-service:8000`
- User → Poll: `http://poll-service:8081`

---

## 🛠️ Important Notes

- Port mappings (3306 / 3307) are **only for host access**
- Between containers:
  - MySQL port is always **3306**
  - Hostname is the **service name**
- Docker Compose ensures correct startup order and networking

---

## 🧪 Troubleshooting

### Service fails on startup
```powershell
docker compose logs poll-service
docker compose logs user-service
```

### Database connection errors
Ensure configuration uses:
```text
MYSQL_HOST = poll-db / user-db
MYSQL_PORT = 3306
```

---

## ✅ Summary

✔ Full microservices architecture  
✔ Independent services and databases  
✔ Internal HTTP communication  
✔ Single-command Docker Compose deployment  

---

This project follows the architectural principles demonstrated in the course and extends them to a full Docker-based deployment.
