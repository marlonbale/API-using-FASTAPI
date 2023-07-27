# API-using-FASTAPI
Creating API using FASTAPI and testing using POSTMAN

# 1.Introduction & Goals
In this project goal is to create a simple customer and invoices API using FastAPI in Python and test the endpoints using POSTMAN.

## Table of Contents
1. [Introduction](#Introduction)
2. [Project Overview](#Project-overview)
3. [Dependencies and Tools](#Dependencies-and-tools)
4. [Using Postman](#Using-Postman)
6. [Conclusion](#conclusion)

## 2.Project Overview
The Python script creates a FastAPI application that serves as the backend for the API project. It functions for managing customers and invoices, providing endpoints to handle different types of requests. The main features of the project include:

**Adding a Customer**: 
The API allows users to add new customers to the system by sending a POST request to the /customers/ endpoint with customer details provided in JSON format.

**Getting a Customer by Customer ID**: Users can retrieve specific customer data by sending a GET request to the /customers/{customer_id} endpoint, where {customer_id} represents the unique identifier of the customer.

**Creating a New Invoice**: The API supports the creation of new invoices for a particular customer. Users can send a POST request to the /invoices/ endpoint with invoice details provided in JSON format.

**Getting All Invoices for a Customer**: Users can fetch all invoices associated with a specific customer by sending a GET request to the /invoices/{customer_id} endpoint, where {customer_id} is the unique identifier of the customer.

## 3.Dependencies and Tools:

- FastAPI: Framework for building APIs with Python. It simplifies the process of defining API routes and data models.
- Pydantic: Python library used to define data models for customer and invoice entities.
- PostMan: Testing tool

## 4.Using Postman:

By using "POST" method we add a new customer, in the request body JSON data for the new customer was added.
http://127.0.0.1:8000/customers/

{
	"info": {
		"_postman_id": "ece04d3c-bd35-4b82-aa47-24115743e7b1",
		"name": "API project",
		"description": "Testing API endpoints that was created using POSTMAN. POSTMAN acts as a client to interact with the local server (here in this case) by sending HTTP requests and receiving responses.",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "28681012",
		"_collection_link": "https://www.postman.com/flight-cosmonaut-19955813/workspace/my-workspace/collection/28681012-ece04d3c-bd35-4b82-aa47-24115743e7b1?action=share&creator=28681012&source=collection_link"
	},
	"item": [
		{
			"name": "POST Add a New Customer",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"customer_id\": 101,\n    \"name\": \"Messi\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/customers/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"customers",
						""
					]
				},
				"description": "By using \"POST\" method we add a new customer, in the request body JSON data for the new customer was added."
			},
			"response": [
				{
					"name": "POST Add a New Customer",
					"originalRequest": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n    \"customer_id\": 101,\n    \"name\": \"Messi\"\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/customers/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"customers",
								""
							]
						}
					},
					"status": "OK",
					"code": 200,
					"_postman_previewlanguage": "json",
					"header": [
						{
							"key": "date",
							"value": "Fri, 21 Jul 2023 19:18:50 GMT"
						},
						{
							"key": "server",
							"value": "uvicorn"
						},
						{
							"key": "content-length",
							"value": "34"
						},
						{
							"key": "content-type",
							"value": "application/json"
						}
					],
					"cookie": [],
					"body": "{\n    \"customer_id\": 101,\n    \"name\": \"Messi\"\n}"
				}
			]
		},
		{
			"name": "Get a Customer by Customer ID",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/customers/123",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"customers",
						"123"
					]
				},
				"description": "\"GET\" method is used to get a customer by the customer id."
			},
			"response": [
				{
					"name": "Get a Customer by Customer ID",
					"originalRequest": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/customers/123",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"customers",
								"123"
							]
						}
					},
					"status": "OK",
					"code": 200,
					"_postman_previewlanguage": "json",
					"header": [
						{
							"key": "date",
							"value": "Fri, 21 Jul 2023 18:45:32 GMT"
						},
						{
							"key": "server",
							"value": "uvicorn"
						},
						{
							"key": "content-length",
							"value": "35"
						},
						{
							"key": "content-type",
							"value": "application/json"
						}
					],
					"cookie": [],
					"body": "{\n    \"customer_id\": 123,\n    \"name\": \"Marlon\"\n}"
				}
			]
		},
		{
			"name": "Create a new invoice",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"Invoice_no\": 3,\n  \"Invoice_Date\":\"2023-07-21\",\n  \"customer_id\": 101\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/invoices/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"invoices",
						""
					]
				},
				"description": "by using \"POST\" method in the drop down we create a new invoice with the relevant data required for the each field."
			},
			"response": [
				{
					"name": "Create a new invoice",
					"originalRequest": {
						"method": "POST",
						"header": [],
						"body": {
							"mode": "raw",
							"raw": "{\n  \"Invoice_no\": 3,\n  \"Invoice_Date\":\"2023-07-21\",\n  \"customer_id\": 101\n}",
							"options": {
								"raw": {
									"language": "json"
								}
							}
						},
						"url": {
							"raw": "http://127.0.0.1:8000/invoices/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"invoices",
								""
							]
						}
					},
					"status": "OK",
					"code": 200,
					"_postman_previewlanguage": "json",
					"header": [
						{
							"key": "date",
							"value": "Fri, 21 Jul 2023 19:19:51 GMT"
						},
						{
							"key": "server",
							"value": "uvicorn"
						},
						{
							"key": "content-length",
							"value": "62"
						},
						{
							"key": "content-type",
							"value": "application/json"
						}
					],
					"cookie": [],
					"body": "{\n    \"Invoice_no\": 3,\n    \"Invoice_Date\": \"2023-07-21\",\n    \"customer_id\": 101\n}"
				}
			]
		},
		{
			"name": "Get All Invoices",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/invoices/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"invoices",
						""
					]
				},
				"description": "Getting all the invoices that are being added using \"GET\" method."
			},
			"response": [
				{
					"name": "Get All Invoices",
					"originalRequest": {
						"method": "GET",
						"header": [],
						"url": {
							"raw": "http://127.0.0.1:8000/invoices/",
							"protocol": "http",
							"host": [
								"127",
								"0",
								"0",
								"1"
							],
							"port": "8000",
							"path": [
								"invoices",
								""
							]
						}
					},
					"status": "OK",
					"code": 200,
					"_postman_previewlanguage": "json",
					"header": [
						{
							"key": "date",
							"value": "Fri, 21 Jul 2023 19:20:02 GMT"
						},
						{
							"key": "server",
							"value": "uvicorn"
						},
						{
							"key": "content-length",
							"value": "190"
						},
						{
							"key": "content-type",
							"value": "application/json"
						}
					],
					"cookie": [],
					"body": "[\n    {\n        \"Invoice_no\": 1,\n        \"Invoice_Date\": \"2023-07-21\",\n        \"customer_id\": 123\n    },\n    {\n        \"Invoice_no\": 2,\n        \"Invoice_Date\": \"2023-07-21\",\n        \"customer_id\": 100\n    },\n    {\n        \"Invoice_no\": 3,\n        \"Invoice_Date\": \"2023-07-21\",\n        \"customer_id\": 101\n    }\n]"
				}
			]
		},
		{
			"name": "Getting a Specific Invoice",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/invoices/1",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"invoices",
						"1"
					]
				},
				"description": "By adding an invoice number we can get the specific invoice requested."
			},
			"response": []
		}
	]
}

  












