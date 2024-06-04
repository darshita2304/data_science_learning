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
