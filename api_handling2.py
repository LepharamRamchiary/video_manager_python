import requests

def fetch_random_product_from_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    res = requests.get(url)
    data = res.json()
    
    
    if data["success"] and "data" in data:
        product_data = data["data"]
        title = product_data["title"]
        desc = product_data["description"]
        price = product_data["price"]
        image = product_data["images"][0]
        return title, desc, price, image
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        title, desc, price, image = fetch_random_product_from_freeapi()
        print(f"Title: {title} \nDesc: {desc} \nPrice: {price}")
        print("\n")
        print(image)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

# fetch_random_product_from_freeapi()