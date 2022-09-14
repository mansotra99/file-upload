##project 

**Upload to cloud Storage (GCP in mycase)**
Using presigned Url


## Technology:

	Language : Python
  
	Framework :  FastApi
  
	Database : Mysql
  
	Cloud Storage : GCP




### **Fast-api-Boilerplate**
https://github.com/mansotra99/Fast-api-Boilerplate

FastAPI framework, high performance, easy to learn, fast to code, ready for production

## ENVIRONMENT
For each Type of environment Create a respective file and pass those variables in **start.sh** file 

**Key** : ENVIRONMENT

**Value** : [PRODUCTION,STAGING,DEVELOPMENT]  (Any One)

**File** : [.env.production, .env.staging, .env.development] (Respective to Value)



## Database Connection

Add db_host, db_password, db_user, db_name , db_port in env file.

Although using SQLAlchemy but that is just to create connection, Can implement models with respect to your needs.


## TO RUN PROJECT

To run just use command "**bash start.sh**"  on linux need to configure for other OS.

Created Reponse, Logging Common Structure
Added request_id(Can also be passed from Nginx Server) which can be helpful for debugging

## SWAGGER DOCS
on web browser run localhost:[port]/docs
  
Example: localhost:8000/docs


## Project Docs

https://docs.google.com/document/d/1fe5VOP0DrrzZzt4_PuuMBBOxWoj75SzGSZxJXrhw7B4/edit?usp=sharing



## CONTRIBUTION
Still Learning,

So feel free, Anything You wanna contirubute.



