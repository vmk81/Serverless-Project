# Project to invoke CRUD operations on DynamoDB using Lambda Functions and API Gateway
## Summary:
This project is to demonstrate how we can invoke CRUD (Create,Read,Update,Delete) operations on a DynamoDB database using a Lambda Function. The user invokes the operation through a POST API that resides on an API Gateway.  
![Arch-1](https://github.com/vmk81/Serverless-Project/assets/157844406/b190c973-87ed-4e60-bc78-ff9d5141aa5d)  

## Lambda Function Details
Line 7 assigns the boto3 resource for dynamodb.  
Line 8 assigns the table name which will be created in dynamodb.  
Line 11 assigns the the kind of CRUD operation user is performing  
Line 12 assigns the details of the operation  
Line 15 performs the 'create' operation on the dynamodb table using the details from Line 12  
Line 19 performs the 'read' operation on the dynamodb table  
Line 27 performs the 'update' operation on the dynamodb table  
Line 32 performs the 'delete' operation on the dynamodb table  
![Lambda Function](https://github.com/vmk81/Serverless-Project/assets/157844406/f93e311a-2932-4ea3-bd4b-01b610fc511f)  

## This project will involve 5 sections.

Section 1: Create an IAM role for Lambda to perform actions on DynamoDB.  
Section 2: Create a Lambda Function to perform CRUD operations on DynamoDB.  
Section 3: Create a DynamoDB Table.  
Section 4: Create the API Gateway that will invoke the Lambda Function.  
Section 5: Test the Output.  
