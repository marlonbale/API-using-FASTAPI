# API-using-FASTAPI
Creating API using FASTAPI and testing using POSTMAN

# Introduction & Goals
In this project goal is to create a simple customer and invoices API using FastAPI in Python and test the endpoints using POSTMAN.

## Table of Contents
1. [Introduction](#Introduction)
2. [Project Overview](#Project-overview)
3. [Dependencies and Tools](#Dependencies-and-tools)
4. [Using Postman](#Using-Postman)
6. [Conclusion](#Conclusion)

## Project Overview
The Python script creates a FastAPI application that serves as the backend for the API project. It functions for managing customers and invoices, providing endpoints to handle different types of requests. The main features of the project include:

**Adding a Customer**: 
The API allows users to add new customers to the system by sending a POST request to the /customers/ endpoint with customer details provided in JSON format.

**Getting a Customer by Customer ID**: Users can retrieve specific customer data by sending a GET request to the /customers/{customer_id} endpoint, where {customer_id} represents the unique identifier of the customer.

**Creating a New Invoice**: The API supports the creation of new invoices for a particular customer. Users can send a POST request to the /invoices/ endpoint with invoice details provided in JSON format.

**Getting All Invoices for a Customer**: Users can fetch all invoices associated with a specific customer by sending a GET request to the /invoices/{customer_id} endpoint, where {customer_id} is the unique identifier of the customer.

## Dependencies and Tools:

- FastAPI: Framework for building APIs with Python. It simplifies the process of defining API routes and data models.
- Pydantic: Python library used to define data models for customer and invoice entities.
- PostMan: Testing tool

## Using Postman:

[Link to API project Postman Collection](API_project.postman_collection.json)

## Conclusion:
This script was written in Python to get an understanding of APIs with Python. By employing FastAPI it showcases how to build a beginner-friendly API project with essential CRUD operations for managing customer and invoice data. The inclusion of Postman testing allowed me to gain hands on exploration and validation of the API's functionalities. In conclusion, the project helped me to understand API development practically.








