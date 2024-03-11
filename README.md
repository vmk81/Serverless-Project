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

This project will involve 5 sections.  

Section 1: Create an IAM role for Lambda to perform actions on DynamoDB.  
Section 2: Create a Lambda Function to perform CRUD operations on DynamoDB.  
Section 3: Create a DynamoDB Table.  
Section 4: Create the API Gateway that will invoke the Lambda Function.  
Section 5: Test the Output.  

## Detailed Procedure

### Section 1: Create an IAM role for Lambda to perform actions on DynamoDB.
1. Navigate to the IAM Dashboard and click on Roles on the left side(Red Arrow in the screenshot below).Click the 'Create role' button.Choose the Lambda use case to allow the role to be attached to a Lambda function(Black Arrow).
![1-IAM role 1](https://github.com/vmk81/Serverless-Project/assets/157844406/2a4aab3c-8555-4a80-ae30-fadd01477a02)

2. On the Add permissions page copy/paste AmazonDynamoDBFullAccess on the search bar, select it and click on Next.Give the role a name and click on 'Create role' button.
![2-IAM role 2](https://github.com/vmk81/Serverless-Project/assets/157844406/1e4838b7-4e93-459d-84f0-14452b2e81d1)

### Section 2: Create a Lambda Function to perform CRUD operations on DynamoDB
3. Navigate to Lambda service and click on 'Create function'. Choose 'Author from scratch'. Give a Function name and choose the Runtime as Python 3.12 . Then click on 'Create function' button.
![3-Create Lambda](https://github.com/vmk81/Serverless-Project/assets/157844406/c827ab4d-b16c-4276-974d-60219e615bba)

4. On the next page inside the code section(Red Arrow in the screenshot below) and copy/paste the Lambda Function code that will perform the CRUD operation on the DynamoDB database.
![4-Create Lambda Add Code](https://github.com/vmk81/Serverless-Project/assets/157844406/a4b25612-845c-4eb9-bcfa-20e8abdf5d70)

### Section 3: Create the DynamoDB table that the Lambda function operations.
5. Open the DynamoDB console. On the left side of the console, choose Dashboard(Red Arrow in the screenshot below) and navigate to the Dashboard. Then click on Tables below the Dashboard option on the left.   
![5-DynamoDB](https://github.com/vmk81/Serverless-Project/assets/157844406/b8dfff00-0ffc-47fa-9970-abed3c7b2161)

6. Inside the table details page,give a name for Table name which is my-serverless-table in this case and give 'id' inside Parition key with 'String'. Click on 'Create table' button at the bottom.
![6-DynamoDB-Table](https://github.com/vmk81/Serverless-Project/assets/157844406/86b2f4e5-b624-4779-bc2f-8fb44d16a0b6)

### Section 4: Create an API that will invoke the Lambda Function

7. Go to the API Gateway console and click on 'Create API' button.Scroll to the REST API section and click on 'Build'. Give a name to the API which is Dynamo-API in this case and click on 'Create API' button.
![7-Create Rest API](https://github.com/vmk81/Serverless-Project/assets/157844406/dfda5b6c-d360-4964-9dcf-6e93f954f26e)
 
8. Navigate inside the API and click on 'Create resource' button (Red Arrow in the screenshot below).Inside the Create resource page,give a name inside 'Resource name' and click on 'Create resource' button. The 'Resource path' will automatically get populated once its get created.  
![8-Create Rest API Resource](https://github.com/vmk81/Serverless-Project/assets/157844406/0a3f5855-52d8-47a2-bed7-d753fa9dab9c)

9. Inside the Resources page,click on 'Create method' button(Red Arrow in the screenshot below).Inside the Create method page,select POST as the method type(Black Arrow) and 'Integration type' as Lambda . Under 'Lambda function',select the Lambda arn for the Lambda we created in step 3. And then click on 'Create method'.  
![9-Create Rest API Method](https://github.com/vmk81/Serverless-Project/assets/157844406/d0fe1505-f065-40cc-bb4b-84b1e3db7a77)

10. Now we are ready to deploy the API. Click on the 'Deploy API' button. Inside the Deploy API page select 'New Stage' and give the 'Stage name' as Test.And then click on 'Deploy' button. On the Stages page collapse the Test stage(Red Arrow in the screenshot below) to POST. And then invoke URL and copy(Black Arrow).  
![10-Create Rest API Deploy](https://github.com/vmk81/Serverless-Project/assets/157844406/107d912e-cd37-48df-9d8b-e8e0f8aa5240)

### Section 5: Test the Output

11. Open Postman from your Desktop and copy/paste the url copied from step 10 and paste it on the url box . Select POST as the protocol from the left. Go to 'Body' tab (Red Arrow in the screenshot below) and paste the JSON from Sample.JSON attached to this page. Make sure the operation variable is 'create' (Black Arrow) and click on 'Send'button. If you recieved status code 200, then it was successful. Navigate to the DynamoDb table we created earlier and click on 'View table details' tab . You can see the new table entry(Blue Arrow).Hence the 'Create' test succeeded.
![11-Test for Update](https://github.com/vmk81/Serverless-Project/assets/157844406/ab947c39-db8e-49ec-a31b-34d7b8a36917)

13. Go back to Postman and repeat the same step for 'Read' operation . Change the operation parmeter on JSON to 'read' (Red Arrow in the screenshot below). and click on 'Send' button. You recieved status code 200 . Hence the 'Read' test succeeded. Repeat the same steps for 'Update' and 'Delete' by making the similar changes in the operation parameter.
![12-Test for Read](https://github.com/vmk81/Serverless-Project/assets/157844406/dfb7f21b-ab42-4e68-bac9-d92289d78d3b)

