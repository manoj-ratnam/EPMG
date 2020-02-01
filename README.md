# EPMG
Assignment Code for EPMG submitted by candidate **Manoj Jayarathinam.

This repo has code/solutions for 3 challenges posted: 

>Challenge #1

> A 3 tier environment is a common setup. Use a tool of your choosing/familiarity create these resources. Please remember we will not be judged on the outcome but more focusing on the approach, style and reproducibility.
Challenge #2

## SOLUTION:

The subdirectory in this repo contain "3-tier-aws-application" that has a terraform solution to establish a 3-tire aws environment. 
Below are the steps to launch run the terraform and launch the web-application (in this sample, we are hosting a sample flask project):

    Requirements
      Terraform >= 0.11.1
      AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables exported.
    
    Usage
      Clone this repository and run the following:
      
      To Initialize Terrraform remote backend:
        terraform init -backend-config=terraform.remote
      
      Terraform plan:
         terraform plan
      
      Terraform apply:
         terraform apply

The above will create an ec2 instance with 3-tire architecture and will necessary security groups, vpcs, networking rules to deploy and run a sample web application. After it completes, you should be abl to connect to (http://EC2_INSTANCE_IP/app1) and (http://EC2_INSTANCE_IP/app2) from your browser.
