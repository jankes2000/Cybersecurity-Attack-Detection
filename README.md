Project

Welcome to the **Cybersecurity Attack Detection** project for MLOps Zoomcamp! This repository contains an end-to-end machine learning MLOps solution designed to detect cybersecurity attacks. This project leverages the [InSDN dataset](https://www.kaggle.com/datasets/badcodebuilder/insdn-dataset) and employs a range of technologies to ensure robust, scalable, and efficient cybersecurity solutions. Below is a comprehensive guide to understanding and using this project.

## Problem Description

In the realm of cybersecurity, detecting and responding to attacks in real-time is crucial. This project addresses the challenge of identifying potential security breaches by analyzing network traffic data. The primary goal is to build a machine learning model that can accurately classify network events as either benign or indicative of an attack. The project utilizes the inSDN dataset from Kaggle, which provides a rich set of data for training and testing the model.

### Problem

In modern IT systems, detecting and mitigating cyberattacks is a critical and challenging task. Cyberattacks are becoming increasingly sophisticated, with evolving patterns and tactics that can bypass traditional security measures. The primary issues faced are:

- **Volume and Complexity of Data**: IT systems generate vast amounts of data from various sources, including logs, network traffic, and user activity. Analyzing this data manually is impractical due to its sheer volume and complexity.
  
- **Evolving Threat Landscape**: Cyber threats continuously evolve, making it difficult for static security measures to keep up. New types of attacks and techniques can compromise systems if the detection mechanisms are not adaptive.
  
- **Real-Time Detection Needs**: Effective cyberattack detection requires real-time analysis to promptly identify and respond to potential threats before they cause significant damage.
  
- **Maintaining Model Accuracy**: As new data and attack vectors emerge, machine learning models used for detection need regular updates to maintain their accuracy and effectiveness.

### Solution

The project addresses these problems through a comprehensive machine learning-based cyberattack detection system, implemented using Mage AI pipelines. 

The project solves the problem of cyberattack detection by leveraging advanced machine learning techniques and automated processes. It effectively handles the complexities of large-scale data, adapts to evolving threats, and provides timely detection of potential cyberattacks. By integrating data preparation, model training, real-time prediction, and automatic retraining, the solution offers a comprehensive and adaptive approach to securing IT systems against sophisticated cyber threats.

## Implementation Architecture

The architecture of this project is designed to be modular and scalable. Here's an overview of the key components and technologies used:

### Dataset

- **Dataset**: [inSDN Dataset on Kaggle](https://www.kaggle.com/datasets/badcodebuilder/insdn-dataset)
  - The dataset includes network traffic data used for training and evaluating the machine learning models.

### Technologies and Tools

- **Cloud**: AWS
  - AWS is used to provide scalable computing resources for model training and experimentation.
  
- **Experiment Tracking**: MLFlow
  - MLFlow is used to track experiments, log metrics, and manage model versions.
  
- **Workflow Orchestration**: Mage AI
  - Mage is utilized for orchestrating and managing data workflows and pipeline execution.
  
- **Monitoring**: Evidently and MLFlow
  - Evidently and MLFlow are employed to monitor the model’s performance and generate insights.
  
- **CI/CD**: GitHub Actions
  - GitHub Actions is used for continuous integration and deployment, automating the testing and deployment process.
  
- **Infrastructure as Code (IaC)**: Terraform
  - Terraform is used to define and provision the cloud infrastructure in a scalable and repeatable manner.

### Pipelines

The cyberattack detection solution operates through a structured workflow involving several key pipelines:

1. **Data Preparation**
   - **Objective**: Collect and preprocess data to create useful features for training.
   - **Process**: This pipeline gathers data from various sources related to IT systems and cyber activity. It performs feature engineering to transform raw data into a structured format suitable for machine learning models.

2. **XGBoost Training**
   - **Objective**: Train a machine learning model using the XGBoost algorithm.
   - **Process**: XGBoost (Extreme Gradient Boosting) is used to train a model for detecting cyberattacks. This algorithm applies gradient boosting techniques to create a powerful ensemble model for accurate predictions.

3. **Predict**
   - **Objective**: Perform real-time predictions on incoming data.
   - **Process**: This pipeline makes online, real-time predictions using the trained XGBoost model to identify potential cyber threats or anomalies.

4. **Automatic Retraining**
   - **Objective**: Maintain and enhance model performance over time.
   - **Process**: Continuously gathers new training data and periodically retrains the model to adapt to emerging threats and maintain prediction accuracy.

5. **Deploying to Production**
   - **Objective**: Deploy the trained model to a production environment.
   - **Process**: Handles the deployment of the model and the associated infrastructure for real-time predictions.

### Summary

The solution integrates several key processes:
- **Data Preparation**: Ensures data quality and relevance for model training.
- **XGBoost Training**: Utilizes a powerful machine learning technique for building a predictive model.
- **Predict**: Provides real-time detection capabilities to identify cyber threats.
- **Automatic Retraining**: Keeps the model updated and effective over time.
- **Deploying to Production**: Manages the deployment and operational aspects of the model.

Together, these components form a robust system for detecting cyberattacks, continuously improving its performance, and adapting to new threats as they arise.

## Getting Started

Start locally with Docker Compose by running:
```bash
./scripts/start.sh
```

Access Services:
* Mage Platform: http://localhost:6789
* MLFlow: http://localhost:5000
* Adminer: http://localhost:8080
* Grafana: http://localhost:3000

Deploying the Project with Terraform
If you prefer to deploy the project using Terraform in AWS for instance, follow these steps.

The deployment process for Docker Compose using Mage on AWS, as outlined in the deploying_to_production pipeline within Mage AI, involves several key steps:

* Setting Up AWS Permissions:
Create IAM policies for deploying and destroying resources on AWS using Terraform.
Create an IAM user (MageDeployer) and attach the policies TerraformApplyDeployMage and TerraformDestroyDeleteResources to manage the deployment process. Generate access keys for this user to be used in the command-line interface (CLI).

* Configuring Terraform:
Install and set up Terraform on your local machine.
Customize the Terraform configurations by updating the variables.tf and env_vars.json files with the appropriate Docker image, application name, AWS region, and availability zones.

* Deploying to AWS:

Navigate to the Terraform directory and run the terraform init and terraform apply commands to deploy the application to AWS.

* Version Control and CI/CD:
Set up continuous integration and continuous deployment (CI/CD) using GitHub Actions.
If the Terraform templates from Mage are used, a GitHub Action YAML file will be generated automatically, containing the necessary configurations for building and deploying the application to AWS Elastic Container Service (ECS).
Create an IAM user (MageContinuousIntegrationDeployer) with the necessary policies for managing the CI/CD process. Add the generated access keys as secrets in your GitHub repository.
This process is thoroughly detailed and implemented within the deploying_to_production pipeline in Mage AI, guiding users through each step required for successful deployment.


# Mage AI Projct structure


This structure supports a modular approach to managing machine learning operations and integration with the Mage AI framework, facilitating development, deployment, and maintenance.

The project is organized into several directories and files, forming a comprehensive MLOps solution for cybersecurity attack detection. Below is a detailed description of the project structure:

## `mlops` Directory

- **`design.yaml`**: YAML configuration file for the overall design of the project.

## `detection_orchestration` directory in `mlops` directory

This directory contains the core modules and components responsible for orchestrating the detection process. It is divided into several subdirectories:


### `custom`

This folder contains custom scripts related to various aspects of the MLOps pipeline, including CI/CD, deployment, and model management and inference:


### `data_exporters`

Scripts in this folder are responsible for exporting data, including:

### `data_loaders`

This directory contains scripts for loading data into the system:

### `global_data_products.yaml`

YAML configuration file for global data products.

### `interactions`

Contains configuration files for defining interactions within the project:


### `io_config.yaml`


### `markdowns`

Documentation files providing guidance and instructions:

### `metadata.yaml`

YAML configuration file for metadata used throughout the project.

### `pipelines`

Contains modules and configurations for different pipeline stages:

- **`automatic_retraining`**: Pipeline for automatic model retraining.
- **`data_preparation`**: Pipeline for preparing data.
- **`deploying_to_production`**: Pipeline for deploying models to production.

- **`predict`**: Pipeline for making predictions.
  n.
- **`xgboost_training`**: Pipeline for training XGBoost models.
 ### `scratchpads`

### `sensors`

Contains scripts for detecting new data:

Includes scripts for transforming data and tuning hyperparameters:

- **`hyperparameter_tuning`**: Contains scripts for hyperparameters searching.




Certainly! Here’s how you can add a section to your README.md to explain how to access the Mage panel and perform an inference API request:

markdown
Skopiuj kod
# Accessing Mage Panel and Performing Inference

## Accessing the Mage Panel

To view the Mage project panel, navigate to the following URL in your web browser:

- **Local Development**: [http://localhost:6789](http://localhost:6789)
- **Remote Server**: [http://<your_mage_server_address>:6789](http://<your_mage_server_address>:6789)

Replace `<your_mage_server_address>` with the address of your Mage server if you are not running it locally.


![alt text](inference_pipeline.jpg "Inference pipeline")

![alt text](retraining_pipeline.jpg "Retraining pipeline")

![alt text](data_preparation_pipeline.jpg "Data preparation pipeline")


## Performing Inference via API

To perform an inference request using the Mage API, you can use the following `curl` command. Ensure you replace the `Authorization` token with your own API token.

```bash
curl --location 'http://localhost:6789/api/runs' \
--header 'Authorization: Bearer ef46ef6d89f44853b3d31ef771991bc5' \
--header 'Content-Type: application/json' \
--header 'Cookie: lng=en' \
--data '{
    "run": {
        "pipeline_uuid": "predict",
        "block_uuid": "inference",
        "variables": {
            "inputs": [
                {
                    "Protocol": 6,
                    "FIN Flag Cnt": 0,
                    "Init Bwd Win Byts": -1,
                    "SYN Flag Cnt": 0,
                    "Down/Up Ratio": 0,
                    "Src Port": 80,
                    "Dst Port": 443,
                    "ACK Flag Cnt": 1,
                    "Bwd Header Len": 64,
                    "Fwd Pkt Len Min": 0,
                    "Flow ID": "192.168.20.133-205.196.120.6-55200-443-6",
                    "Src IP": "205.196.120.6",
                    "Dst IP": "192.168.20.133",
                    "Timestamp": "5/2/2020 12:33"
                },
                {
                    "Protocol": 6,
                    "FIN Flag Cnt": 1,
                    "Init Bwd Win Byts": 63,
                    "SYN Flag Cnt": 0,
                    "Down/Up Ratio": 0,
                    "Src Port": 80,
                    "Dst Port": 43678,
                    "ACK Flag Cnt": 1,
                    "Bwd Header Len": 64,
                    "Fwd Pkt Len Min": 0,
                    "Flow ID": "192.168.3.130-200.175.2.130-80-43678-6",
                    "Src IP": "192.168.3.130",
                    "Dst IP": "200.175.2.130",
                    "Timestamp": "9/1/2020 16:33"
                }
            ]
        }
    }
}'