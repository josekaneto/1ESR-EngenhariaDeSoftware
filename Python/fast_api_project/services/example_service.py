def get_data():
    return {"message": "Data fetched successfully!"}

def save_data(payload: dict):
    payload["processed"] = True
    return payload