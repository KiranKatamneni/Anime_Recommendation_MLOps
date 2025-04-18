# 🎥 Anime Recommendation System with MLOps

This project implements an end-to-end Anime Recommendation System, integrating robust MLOps practices. It includes data versioning, model training pipelines, CI/CD workflows, containerization, deployment strategies, and experiment tracking with **Comet ML**.

---

## 🚀 Features

- **Data Versioning**: Uses DVC to track datasets and model artifacts.
- **Model Training**: Modular scripts for clean and configurable training workflows.
- **Experiment Tracking**: Integrated with **Comet ML** for logging metrics, visualizations, and model comparisons.
- **CI/CD Pipelines**: Automated pipelines with Jenkins for continuous integration and deployment.
- **Containerization**: Docker ensures consistency across environments.
- **Deployment**: Kubernetes manifests for scalable orchestration.
- **Web Interface**: Flask-powered frontend for anime recommendations.

---

## 📁 Project Structure

  ```bash
├── .dvc/                 # DVC configuration files
├── artifacts/            # Stored artifacts like models and datasets
├── build/lib/            # Build outputs
├── config/               # YAML configs for training, DVC, Comet, etc.
├── custom_jenkins/       # Jenkins pipeline scripts
├── logs/                 # Application and training logs
├── notebook/             # Jupyter notebooks for EDA & prototyping
├── pipeline/             # ML pipeline scripts
├── src/                  # Core source code
├── static/               # Web static files
├── templates/            # Flask HTML templates
├── utils/                # Utility functions
├── .dvcignore            # Ignore patterns for DVC
├── .gitignore            # Ignore patterns for Git
├── Dockerfile            # Container specification
├── Jenkinsfile           # CI/CD configuration
├── application.py        # Flask entrypoint
├── deployment.yaml       # Kubernetes deployment config
├── requirements.txt      # Python dependencies
├── setup.py              # Project setup config
├── tester.py             # Test runner script

```
---

## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- Git
- Docker
- DVC
- Jenkins
- Kubernetes
- Comet ML account

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/KiranKatamneni/Anime_Recommendation_MLOps.git
cd Anime_Recommendation_MLOps
```
### 🔧 Setup Instructions

#### 1. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. Initialize and Pull Data using DVC

```bash
dvc init
dvc pull
```

2. **Run the Flask app**

```bash
docker build -t anime-recommender .
docker run -p 5000:5000 anime-recommender
```
## 📊 Experiment Tracking with Comet ML

Use **Comet ML** to:

- Track training and validation metrics  
- Compare experiment runs  
- Visualize model performance, hyperparameters, and logs  
- Share reproducible experiment results

💡 *Comet ML logging is automatically activated during training if your API key is configured properly.*

---

## ⚙️ CI/CD Pipeline

The project uses **Jenkins** for continuous integration and deployment.

- The `Jenkinsfile` defines automated stages for:
  - Testing the codebase
  - Training and versioning models
  - Building Docker images
  - Deploying the application to the target environment

## 🧪 Testing

To run tests locally:

```bash
python tester.py
```

## 🤝 Contributing

Contributions are welcome!

1. **Fork** the repository  
2. **Create a branch** (`feature/your-feature`)  
3. **Commit** your changes  
4. **Push** to the branch  
5. **Open a Pull Request**
