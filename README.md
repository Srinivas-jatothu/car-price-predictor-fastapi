
# 🚗 Car Price Predictor API

A production-ready Machine Learning API built with FastAPI that predicts used car selling prices based on vehicle characteristics. The system features JWT authentication, Redis caching, and comprehensive monitoring with Prometheus and Grafana.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Redis](https://img.shields.io/badge/Redis-Caching-DC382D.svg?style=flat&logo=redis&logoColor=white)](https://redis.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://claude.ai/chat/LICENSE)

## 📋 Table of Contents

* [Features](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-features)
* [Architecture](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-architecture)
* [Model Input Features](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-model-input-features)
* [Getting Started](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-getting-started)
  * [Prerequisites](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#prerequisites)
  * [Local Development](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#local-development)
  * [Docker Deployment](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#docker-deployment)
* [API Documentation](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-api-documentation)
* [Authentication](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-authentication)
* [Monitoring &amp; Observability](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-monitoring--observability)
* [Deployment](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-deployment)
  * [Deploy to Render](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#deploy-to-render)
* [Project Structure](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-project-structure)
* [Environment Variables](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-environment-variables)
* [Contributing](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-contributing)
* [License](https://claude.ai/chat/1790d41e-ddef-40b9-bcc8-ecbc5fda1146#-license)

## ✨ Features

* **🤖 ML-Powered Predictions** : Scikit-learn model trained on real-world used car data
* **🔐 Dual Authentication** : JWT token-based auth and API key validation
* **⚡ Redis Caching** : Intelligent caching layer to optimize response times
* **📊 Monitoring Stack** : Pre-configured Prometheus metrics and Grafana dashboards
* **🐳 Containerized** : Full Docker and Docker Compose setup for seamless deployment
* **📚 Auto-Generated Docs** : Interactive API documentation via Swagger UI
* **☁️ Cloud-Ready** : One-click deployment configuration for Render
* **🔄 Async Support** : Built on ASGI for high-performance async operations

## 🧠 Model Input Features

The ML model requires the following input parameters for prediction:

| Feature           | Type    | Description                | Example                                |
| ----------------- | ------- | -------------------------- | -------------------------------------- |
| `company`       | string  | Car manufacturer/brand     | `"Maruti"`,`"Hyundai"`,`"Honda"` |
| `year`          | integer | Year of manufacture        | `2015`,`2018`                      |
| `owner`         | string  | Ownership history          | `"First"`,`"Second"`,`"Third"`   |
| `fuel`          | string  | Fuel type                  | `"Petrol"`,`"Diesel"`,`"CNG"`    |
| `seller_type`   | string  | Seller category            | `"Individual"`,`"Dealer"`          |
| `transmission`  | string  | Transmission type          | `"Manual"`,`"Automatic"`           |
| `km_driven`     | integer | Total kilometers driven    | `45000`,`120000`                   |
| `mileage_mpg`   | float   | Fuel efficiency (mpg)      | `18.5`,`22.3`                      |
| `engine_cc`     | integer | Engine displacement (cc)   | `1200`,`1500`                      |
| `max_power_bhp` | float   | Maximum power output (BHP) | `88.5`,`120.0`                     |
| `torque_nm`     | float   | Engine torque (Nm)         | `115.0`,`200.0`                    |
| `seats`         | integer | Seating capacity           | `5`,`7`                            |

### Sample Request Payload

```json
{
  "company": "Maruti",
  "year": 2015,
  "owner": "Second",
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual",
  "km_driven": 70000,
  "mileage_mpg": 20.5,
  "engine_cc": 1197,
  "max_power_bhp": 88.5,
  "torque_nm": 115.0,
  "seats": 5
}
```

## 🚀 Getting Started

### Prerequisites

* **Docker** and **Docker Compose** (recommended)
* **Python 3.11+** (for local development)
* **Redis** (for caching)

### Local Development

1. **Clone the repository**

```bash
git clone https://github.com/Srinivas-jatothu/car-price-predictor-fastapi.git
cd car-price-predictor-fastapi
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:

```env
API_KEY=your-secure-api-key
JWT_SECRET_KEY=your-jwt-secret-key
REDIS_URL=redis_URL
MODEL_PATH=app/models/model.joblib
```

5. **Run the application**

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Docker Deployment

1. **Build and start all services**

```bash
docker-compose up --build
```

2. **Run in detached mode**

```bash
docker-compose up -d
```

3. **View logs**

```bash
docker-compose logs -f api
```

4. **Stop services**

```bash
docker-compose down
```

## 📚 API Documentation

Once the application is running, access the interactive API documentation:

* **Swagger UI** : [http://localhost:8000/docs](http://localhost:8000/docs)
* **ReDoc** : [http://localhost:8000/redoc](http://localhost:8000/redoc)
* **OpenAPI Schema** : [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json)

### Core Endpoints

| Method   | Endpoint               | Description              | Auth Required |
| -------- | ---------------------- | ------------------------ | ------------- |
| `POST` | `/api/v1/predict`    | Get car price prediction | ✅ Yes        |
| `POST` | `/api/v1/auth/token` | Generate JWT token       | ❌ No         |
| `GET`  | `/health`            | Health check endpoint    | ❌ No         |
| `GET`  | `/metrics`           | Prometheus metrics       | ❌ No         |

## 🔐 Authentication

The API supports two authentication methods:

### 1. API Key Authentication

Include the API key in request headers:

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"company": "Maruti", "year": 2015, ...}'
```

### 2. JWT Token Authentication

First, obtain a token:

```bash
curl -X POST "http://localhost:8000/api/v1/auth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=demo&password=demo123"
```

Then use the token in subsequent requests:

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"company": "Maruti", "year": 2015, ...}'
```

## 📊 Monitoring & Observability

### Prometheus Metrics

Access real-time metrics at [http://localhost:9090](http://localhost:9090/)

Key metrics tracked:

* Request count and latency
* Prediction cache hit/miss rates
* Model inference time
* HTTP status code distribution

### Grafana Dashboards

Access visualization dashboards at [http://localhost:3000](http://localhost:3000/)

 **Default credentials** : `admin` / `admin`

Pre-configured dashboards include:

* API request throughput
* Response time percentiles
* Cache performance
* Error rates

### Custom Metrics Endpoint

Raw metrics available at: [http://localhost:8000/metrics](http://localhost:8000/metrics)

## 🌐 Deployment

### Deploy to Render

This project includes a `render.yaml` configuration for one-click deployment.

1. **Push your code to GitHub**

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Connect to Render**
   * Go to [Render Dashboard](https://dashboard.render.com/)
   * Click "New +" → "Blueprint"
   * Connect your GitHub repository
   * Render will automatically detect `render.yaml`
3. **Configure environment variables** in Render Dashboard:

```env
MODEL_PATH=app/models/model.joblib
API_KEY=your-production-api-key
JWT_SECRET_KEY=your-production-secret
```

4. **Deploy** - Render will automatically build and deploy your application

 **Live URL** : `https://your-app-name.onrender.com`

### Deploy to Other Platforms

<details>
<summary><b>AWS ECS / Fargate</b></summary>
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com
docker build -t car-price-api .
docker tag car-price-api:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/car-price-api:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/car-price-api:latest
```

</details>
<details>
<summary><b>Google Cloud Run</b></summary>
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/car-price-api
gcloud run deploy --image gcr.io/PROJECT-ID/car-price-api --platform managed
```

</details>
<details>
<summary><b>Heroku</b></summary>
```bash
heroku create your-app-name
heroku stack:set container
git push heroku main
```

</details>
## 📁 Project Structure

```
car-price-predictor-fastapi/
│
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── api/
│   │   ├── routes/             # API route handlers
│   │   └── dependencies.py     # Dependency injection
│   ├── models/
│   │   └── model.joblib        # Trained ML model
│   ├── schemas/                # Pydantic models
│   ├── services/               # Business logic
│   └── core/
│       ├── config.py           # Configuration management
│       └── security.py         # Authentication logic
│
├── tests/                      # Unit and integration tests
├── docker-compose.yml          # Multi-container orchestration
├── Dockerfile                  # Container image definition
├── prometheus.yml              # Prometheus configuration
├── render.yaml                 # Render deployment config
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## ⚙️ Environment Variables

| Variable           | Description                     | Default                     | Required |
| ------------------ | ------------------------------- | --------------------------- | -------- |
| `API_KEY`        | API key for authentication      | -                           | ✅ Yes   |
| `JWT_SECRET_KEY` | Secret key for JWT signing      | -                           | ✅ Yes   |
| `REDIS_URL`      | Redis connection URL            | `redis://localhost:6379`  | ✅ Yes   |
| `MODEL_PATH`     | Path to trained model file      | `app/models/model.joblib` | ✅ Yes   |
| `LOG_LEVEL`      | Logging verbosity               | `INFO`                    | ❌ No    |
| `CACHE_TTL`      | Cache expiration time (seconds) | `3600`                    | ❌ No    |

## 🧪 Testing

Run the test suite:

```bash
# Unit tests
pytest tests/unit

# Integration tests
pytest tests/integration

# Coverage report
pytest --cov=app tests/
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

Please ensure your code:

* Follows PEP 8 style guidelines
* Includes appropriate tests
* Updates documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://claude.ai/chat/LICENSE) file for details.

## 👨‍💻 Author

**Srinivas Jatothu**

* GitHub: [@Srinivas-jatothu](https://github.com/Srinivas-jatothu)

## 🙏 Acknowledgments

* Built with [FastAPI](https://fastapi.tiangolo.com/)
* ML powered by [scikit-learn](https://scikit-learn.org/)
* Monitoring via [Prometheus](https://prometheus.io/) & [Grafana](https://grafana.com/)
* Caching by [Redis](https://redis.io/)

---

<div align="center">
**⭐ Star this repo if you find it helpful!**

[Report Bug](https://github.com/Srinivas-jatothu/car-price-predictor-fastapi/issues) • [Request Feature](https://github.com/Srinivas-jatothu/car-price-predictor-fastapi/issues)

</div>
