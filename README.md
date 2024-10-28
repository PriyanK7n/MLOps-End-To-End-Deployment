# END TO END Data Science ML PROJECT for Student Performance Prediction


## AWS EC2 Deployment Steps:
- Step 1: Set Up Amazon ECR and IAM User
    1. Create Amazon Elastic Container Registry (ECR)
       * In the AWS Console, navigate to ECR and create a new repository.
       * Note down your repository URI, which will look like {AWS_ACCOUNT_ID}.dkr.ecr.{REGION}.amazonaws.com/{REPO_NAME}.
    2. Create an IAM User with Required Permissions
       * Go to the IAM Console and create a new user with programmatic access.
       * Attach the following policies to the user:
           * AmazonEC2ContainerRegistryFullAccess
           * AmazonEC2FullAccess
       * Generate Access Key and Secret Access Key for this user, which will be used for AWS CLI access.
- Step 2: Build and Push Docker Image Locally (Initial Setup)
    1. Log in to ECR: Use the AWS CLI to authenticate Docker to your ECR:
        ```aws ecr get-login-password --region <YOUR_REGION> | docker login --username AWS --password-stdin <YOUR_ECR_URI>```
    2. Build and Push Docker Image
        * Build the Docker image: 
        ```docker build -t <YOUR_ECR_URI>:latest .```
        * Push the image to ECR:
        ```docker push <YOUR_ECR_URI>:latest```
- Step 3: Launch and Configure AWS EC2 Instance
    1. Launch an EC2 Instance
          * Recommended configuration:
            * OS: Ubuntu
            * Instance Type: t2.medium
            * Login Method: Key pair
            * Security Group: Allow HTTPS traffic and a custom TCP rule on the port your app will use (e.g., 8080).
    2. Install Docker on EC2
          * SSH into your EC2 instance and run the following commands to install Docker
        
            ```bash
                sudo apt-get update -y
                sudo apt-get upgrade -y
                curl -fsSL https://get.docker.com -o get-docker.sh
                sudo sh get-docker.sh
                sudo usermod -aG docker ubuntu```
- Step 4: Set Up GitHub Actions Workflow for CI/CD
    1. Configure GitHub Secrets
       * In your GitHub repository, go to Settings > Secrets and variables > Actions and add the following secrets:
           * AWS_ACCESS_KEY_ID: Access key from your IAM user.
           * AWS_SECRET_ACCESS_KEY: Secret access key from your IAM user.
           * ECR_URI: ECR repository URI.
    2. Create a Workflow File
       * In your repository, create a .github/workflows directory and add a workflow file (e.g., deploy.yml). In my reposiotry I created a main.yaml workflow file for AWS ECR CI/CD Deployment.
- Step 5: Configure EC2 as a Self-Hosted Runner for GitHub Actions
    1. Run Self-Hosted Runner on EC2
        * Follow GitHub's instructions for setting up a self-hosted runner on the EC2 instance.
        * Run the following commands on the EC2 CLI to start the runner: ```# Replace with actual commands provided by GitHub for setting up the runner```
    2. Enable Continuous Deployment
       * After setting up the runner, your workflow will automatically trigger on a push to the main branch and deploy your app to Amazon EC2.




### Visual Representation


1. Push Change to GitHub Repo (main)
           |
           v
2. GitHub Actions CI/CD Workflow
           |
           v
3. Build Docker Image & Log in to AWS ECR
           |
           v
4. Push Docker Image to AWS ECR
           |
           v
5. Amazon EC2 ubuntu linux instance Pulls & Deploys Image
           |
           v
6. Updated App Live on Amazon EC2 instance 





## Azure Deployment Steps
- Step 1: Set Up Azure Container Registry (ACR) and Web App
    1. Create Azure Container Registry (ACR)
         * In the Azure Portal, navigate to Container Registries and create a new registry.
         * Enter the details:
             * Registry Server URL: {ACR}.azurecr.io
             * Login: your ACR 
         * Ensure your ACR allows for authentication and access to your Web App.
  
    2. Build and Push Docker Image Locally (Initial Setup)
        * Build Docker Image ```docker build -t testdockerpriyank.azurecr.io/student-performance:latest .```
        * Log in to ACR ```docker login testdockerpriyank.azurecr.io```
        * Push the Docker image``` docker push testdockerpriyank.azurecr.io/student-performance:latest```
- Step 2: Create Azure Web App and Configure GitHub Actions for CI/CD
    1. Create Azure Web App
             * In the Azure Portal, navigate to App Services and create a new Web App.
             * In the Container Settings section, select Azure Container Registry as the deployment source and choose your previously pushed image.
    2. Set Up GitHub Actions Workflow for CI/CD

    In your GitHub repository (PriyanK7n/MLOps-End-To-End-Deployment), create a .github/workflows directory and add a new workflow YAML file (deploy.yml). I Created the **main_student-performance.yml** file. 

        
    3. Set Up GitHub Secrets

CI/CD Pipeline Explanation
* **Push Trigger**: The workflow triggers on a push to the main branch.
* **Docker Image Build and Push**: The workflow logs into ACR, builds the Docker image, and pushes it to ACR.
* **Deployment to Azure Web App**: The Docker image is deployed from ACR to your Azure Web App.

### Visual Representation

1. Push Change to GitHub Repo (main)
           |
           v
2. GitHub Actions CI/CD Workflow
           |
           v
3. Build Docker Image & Log in to ACR
           |
           v
4. Push Docker Image to ACR
           |
           v
5. Azure Web App Pulls & Deploys Image
           |
           v
6. Updated App Live on Azure Web App


