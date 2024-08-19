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
Cloud: AWS

Azure is used to provide scalable computing resources for model training and experimentation.
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
If you prefer to deploy the project using Terraform in AWS for instance, follow these steps.

The deployment process for Docker Compose using Mage on AWS, as outlined in the deploying_to_production pipeline within Mage AI, involves several key steps:

Setting Up AWS Permissions:

Create IAM policies for deploying and destroying resources on AWS using Terraform.
Create an IAM user (MageDeployer) and attach the policies TerraformApplyDeployMage and TerraformDestroyDeleteResources to manage the deployment process. Generate access keys for this user to be used in the command-line interface (CLI).
Configuring Terraform:

Install and set up Terraform on your local machine.
Customize the Terraform configurations by updating the variables.tf and env_vars.json files with the appropriate Docker image, application name, AWS region, and availability zones.
Deploying to AWS:

Navigate to the Terraform directory and run the terraform init and terraform apply commands to deploy the application to AWS.
Version Control and CI/CD:

Set up continuous integration and continuous deployment (CI/CD) using GitHub Actions.
If the Terraform templates from Mage are used, a GitHub Action YAML file will be generated automatically, containing the necessary configurations for building and deploying the application to AWS Elastic Container Service (ECS).
Create an IAM user (MageContinuousIntegrationDeployer) with the necessary policies for managing the CI/CD process. Add the generated access keys as secrets in your GitHub repository.
This process is thoroughly detailed and implemented within the deploying_to_production pipeline in Mage AI, guiding users through each step required for successful deployment.






