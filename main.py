

from fastapi import FastAPI
import uvicorn

app = FastAPI()

search_history = []
request_id = 0

@app.post("/add_vitamins")
def add_vitamins(vitamins: str | None = None):
    # 1. Проверяем, передана ли вообще строка
    if not vitamins:
        return {"Error": "Строка с витаминами пуста"}
        
    global request_id

    # 2. Очищаем и собираем список витаминов
    vitamins_list = [vitamin.strip(",") for vitamin in vitamins.split()]
    vitamins_clean = [v for v in vitamins_list if v]

    # 3. Валидация: проверяем КАЖДЫЙ витамин в списке
    for vitamin in vitamins_clean:
        if not vitamin.isalpha():
            # Если хотя бы ОДИН элемент содержит цифры или знаки, сразу прерываемся
            return {"Error": "Не балуйся"}

    # 4. Если всё успешно прошли, увеличиваем счетчик и пишем в историю
    request_id += 1
    search_history.append({
        "number_of_request": request_id,
        "request": vitamins_clean
    })
    
    return {"result": vitamins_clean}

@app.get("/history")
def get_history():
    return {"user_history": search_history}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
