from fastapi import FastAPI,HTTPException

app = FastAPI() #creating an instance of FastAPI;

#creating a datamodel using pydantic to represent a customer and Invoice
from pydantic import BaseModel

class Customer(BaseModel):             
    customer_id: int   
    name : str  

class Invoice(BaseModel):
    Invoice_no: int
    Invoice_Date: str
    customer_id: int

 #creating  temporary data storage

CUSTOMERS = []
INVOICES  =[]

#implementing the API

#base url
@app.get("/")
async def root():
    return{"message":"Hello World!"}


#1. add a customer
@app.post("/customers/", response_model= Customer)
async def add_customer(customer: Customer):
    #checking if the customer exist
    for existing_customer in CUSTOMERS:
        if existing_customer.customer_id == customer.customer_id:
            raise HTTPException(status_code = 400, detail= "This Customer already exist")

    #adding the customer
    CUSTOMERS.append(customer)
    return customer

#2.Get a customer by customer_id

@app.get("/customers/{customer_id}", response_model= Customer)
async def get_customer(customer_id: int):
    #finding customer by id
    for customer in CUSTOMERS:
        if customer.customer_id == customer_id:
            return customer
        

#3.create new invoice
@app.post("/invoices", response_model=Invoice) 
async def create_invoice(invoice:Invoice):
# customer exist check
    customer_exists =  any(customer.customer_id == invoice.customer_id for customer in CUSTOMERS)
    if not customer_exists:
        raise HTTPException(status_code=404, detail="Customer not found")

#check if the invoice already exist
    for existing_invoice in INVOICES:
        if existing_invoice.customer_id == invoice.customer_id and existing_invoice.invoice_number == invoice.invoice_number:
            raise HTTPException(status_code=404, detail="Invoice already exists")
        
#add  the new invoice to the list
    INVOICES.append(invoice)
    return invoice
        

#4. Get all the invoices
@app.get("/invoices", response_model=INVOICES)
async def get_all_invoices():
    return INVOICES
      






























