from fastapi import FastAPI
import uvicorn


app = FastAPI()

search_history = []

request_id = 0

@app.post("/add_vitamins")
def add_vitamins(vitamins: str | None):
    vitamins_list = [vitamin.strip(",") for vitamin in vitamins.split()]
            
            # Исключаем пустые строки, если между запятыми были лишние пробелы
    vitamins_clean = [v for v in vitamins_list if v]
    for vitamin in vitamins_clean:
        if vitamin.isalpha():
            global request_id
            request_id += 1
            # Разбиваем строку по пробелам и очищаем каждый элемент от запятых по краям
            vitamins_list = [vitamin.strip(",") for vitamin in vitamins.split()]
            
            # Исключаем пустые строки, если между запятыми были лишние пробелы
            vitamins_clean = [v for v in vitamins_list if v]

            search_history.append({
                "number_of_request" : request_id,
                "request" : vitamins_clean
            })
            
            return {"result": vitamins_clean}
            
        
        else:
            return{"Error": "Не балуйся"}

@app.get("/history")
def get_history():
    return {"user_history": search_history}

# Этот блок сработает при прямом запуске файла: python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)