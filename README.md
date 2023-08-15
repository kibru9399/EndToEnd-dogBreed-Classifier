# END-TO-END DOG BREED CLASSIFICATION --PROJECT
## About the dataset
Tsinghua Dogbreed Dataset is a large-scale dataset of dog images that was created by researchers at Tsinghua University in China. The dataset contains over 70,000 images of 130 different dog breeds. The images were collected from a variety of sources, including social media, image search engines, and personal collections.
Here are some of the key features of the Tsinghua Dogbreed Dataset:

It contains over 70,000 images of 130 different dog breeds.
The images were collected from a variety of sources, including social media, image search engines, and personal collections.
The images are high-quality and well-labeled.
The dataset is publicly available for research purposes.https://cg.cs.tsinghua.edu.cn/ThuDogs/

## About the project and workflow
The main purpose of this project is to do end to end machine learning project by following best ML practices. 

This end-to-end machine learning project focuses on the detection of dog breed using a deep learning model. The project follows a CI/CD workflow with GitHub Actions and EC2 deployment.

The project gathers data from the web download it.The data is then cleaned and pre-processed, and a deep learning model is trained on the data. The model is then evaluated on a held-out test set, and the results are analyzed.

Once the model is trained and evaluated, it is deployed to a Docker container using GitHub Actions. The Docker container is then pushed to Amazon ECR. Next, the Docker image is pulled from Amazon ECR and deployed to an Amazon EC2 instance. The Amazon EC2 instance is then configured to run the Docker container. The Docker container is then made available to users through a web application. The web application allows users to upload images of dogs, and the model will predict the breed of the dog

The project is designed to be scalable and extensible.The project also demonstrates the use of CI/CD for machine learning projects, which can help to improve the reliability and reproducibility of machine learning models.

Here are some of the key features of the project:

* It uses a deep learning model to detect chicken diseases.
* It follows a CI/CD workflow with GitHub Actions and EC2 deployment.
* It is scalable and extensible.
* It demonstrates the use of CI/CD for machine learning projects.




## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/kibru9399/dogBreed-EndToEnd.git```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app



