import azure.functions as func
import json
from ml_model import load_model, predict

model = load_model()

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        data = req.get_json()
        predictions = predict(model, data)
        return func.HttpResponse(json.dumps(predictions), status_code=200)
    except Exception as e:
        return func.HttpResponse(str(e), status_code=500)
