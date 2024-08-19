# Project
Welcome to the Cybersecurity Attack Detection project for MLOps Zoomcamp! This repository contains an end-to-end machine learning MLOps solution designed to detect cybersecurity attacks. This project leverages the InSDN dataset https://www.kaggle.com/datasets/badcodebuilder/insdn-dataset and employs a range of technologies to ensure robust, scalable, and efficient cybersecurity solutions. Below is a comprehensive guide to understanding and using this project.
# Problem Description
In the realm of cybersecurity, detecting and responding to attacks in real time is crucial. This project addresses the challenge of identifying potential security breaches by analyzing network traffic data. The primary goal is to build a machine learning model that can accurately classify network events as either benign or indicative of an attack. The project utilizes the inSDN dataset from Kaggle, which provides a rich set of data for training and testing the model.
# Architecture
The architecture of this project is designed to be modular and scalable. Here's an overview of the key components and technologies used:

Dataset
Dataset: inSDN Dataset on Kaggle
The dataset includes network traffic data used for training and evaluating the machine learning models.
Technologies and Tools
Cloud: Saturn Cloud

Saturn Cloud is used to provide scalable computing resources for model training and experimentation.
Experiment Tracking: MLFlow

MLFlow is used to track experiments, log metrics, and manage model versions.
Workflow Orchestration: Mage

Mage is utilized for orchestrating and managing data workflows and pipeline execution.
Monitoring: Evidently

Evidently is employed to monitor the model’s performance and generate insights.
CI/CD: GitHub Actions

GitHub Actions is used for continuous integration and deployment, automating the testing and deployment process.
Infrastructure as Code (IaC): Terraform

Terraform is used to define and provision the cloud infrastructure in a scalable and repeatable manner.

# Getting Started

Start locally with docker compose by running 
    ./scripts/start.sh
Access Services:
Mage Platform: http://localhost:6789
MLFlow: http://localhost:5000
Adminer: http://localhost:8080
Grafana: http://localhost:3000

Deploying the Project with Terraform
If you prefer to deploy the project using Terraform in Saturn Cloud for instance, follow these steps:

Set Up Terraform Configuration: Ensure that your Terraform configuration files are properly set up to provision the required cloud resources.

Initialize Terraform:


    terraform init
Apply Terraform Configuration:
    apply

Deploy the Project: Follow your cloud provider's specific instructions for deploying and managing services.