from fastapi import FastAPI, HTTPException, Request
from fastapi import FastAPI

app = FastAPI()


@app.get("/products")
async def get_products(search_query: str = None):
	"""Get a list of products.

	Args:
		search_query: A search term.

	Returns:
		A list of product objects matching the search query.
	"""

	products = ["shoes", "electronics", "clothing",
             "running shoes", "mobile phones", "sports shoes"]
	# Filter products based on search_query if provided
	if search_query:
		products = [product for product in products if search_query in product]

	return {"products": products}

app = FastAPI()


@app.get("/products")
async def get_products(search_query: str = None):
	"""Get a list of products.

	Args:
		search_query: A search term.

	Returns:
		A list of product objects matching the search query.
	"""

	products = ["shoes", "electronics", "clothing",
             "running shoes", "mobile phones", "sports shoes"]
	# Filter products based on search_query if provided
	if search_query:
		products = [product for product in products if search_query in product]

	return {"products": products}


"""
	Endpoint to submit user data using a POST request in FastAPI.

	Parameters:
	- request: FastAPI Request object containing information 
				about the HTTP request.

	Returns:
	A simple confirmation message with the submitted user data.
"""


@app.post("/submit_data")
async def submit_data(request: Request):
	try:
		# Extracting user data from the request body
		data = await request.json()

		# Validate the presence of required fields
		if "username" not in data or "age" not in data:
			raise HTTPException(
				status_code=422, detail="Incomplete data provided")

		# Extracting username and age from the request JSON body
		username = data["username"]
		age = data["age"]

		# Returning a confirmation message
		return {"message": "User data submitted successfully!",
                    "user_data": {"username": username, "age": age}}

	except HTTPException as e:
		# Re-raise HTTPException to return the specified
		# status code and detail
		raise e
	except Exception as e:
		# Handle other unexpected exceptions and return a
		# 500 Internal Server Error
		raise HTTPException(
			status_code=500, detail=f"An error occurred: {str(e)}")

if __name__ == "__main__":
	import uvicorn
	# Run the FastAPI application using uvicorn
	uvicorn.run(app, host="127.0.0.1", port=8000)
