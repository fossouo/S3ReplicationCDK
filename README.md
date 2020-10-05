# Welcome to your CDK Python project!

This is a project that contains two artefacts : the first artefact provide the capability to create S3 buckets and IAM Policies, the second part of the project provides capability to create replication rule. 

## Steps to follow in other to launch the project 

 * `source activate condaenv`          activate your virtual python environment 
 * `pip install -r requirements.txt`       install all needed librairies
 * `cdk synth`      emits the synthesized CloudFormation template
 * `cdk deploy first-stack`        deploy the first artefact stack to your default AWS account/region
 * `cdk deploy second-stack`        deploy the second artefact to your default AWS account/region
