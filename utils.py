def err(brand,model,price):
    errors = dict()
    if not brand or not brand.strip():
        errors["brand"] = 'An brand is required'        
    if not model or not model.strip():
        errors["model"] = 'A model is required'
    if not price:
        errors["price"] = 'A price is required'
    return errors