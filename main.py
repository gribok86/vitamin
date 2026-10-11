from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

search_history = []
request_id = 0
valid_vitamins = ["Vitamin A (Витамин A) — A", "Retinol (Ретинол) — A", "Beta-carotene (Бета-каротин) — BC", "Vitamin B1 (Витамин B1) — B1", "Thiamine (Тиамин) — B1", "Vitamin B2 (Витамин B2) — B2", "Riboflavin (Рибофлавин) — B2", "Vitamin B3 (Витамин B3) — B3", "Niacin (Ниацин) — B3", "Nicotinamide (Никотинамид) — B3", "Vitamin B5 (Витамин B5) — B5", "Pantothenic acid (Пантотеновая кислота) — B5", "Vitamin B6 (Витамин B6) — B6", "Pyridoxine (Пиридоксин) — B6", "Vitamin B7 (Витамин B7) — B7", "Biotin (Биотин) — B7", "Vitamin B9 (Витамин B9) — B9", "Folic acid (Фолиевая кислота) — B9", "Vitamin B12 (Витамин B12) — B12", "Cobalamin (Кобаламин) — B12", "Vitamin C (Витамин C) — C", "Ascorbic acid (Аскорбиновая кислота) — C", "Vitamin D2 (Витамин D2) — D2", "Ergocalciferol (Эргокальциферол) — D2", "Vitamin D3 (Витамин D3) — D3", "Cholecalciferol (Холекальциферол) — D3", "Vitamin E (Витамин E) — E", "Tocopherol (Токоферол) — E", "Vitamin K1 (Витамин K1) — K1", "Phylloquinone (Филлохинон) — K1", "Vitamin K2 (Витамин K2) — K2", "Menaquinone (Менахинон) — K2", "Vitamin F (Витамин F) — F", "Vitamin P (Витамин P) — P", "Bioflavonoids (Биофлавоноиды) — P", "Vitamin U (Витамин U) — U", "S-methylmethionine (S-метилметионин) — SMM", "Vitamin H (Витамин H) — H", "Vitamin B4 (Витамин B4) — B4", "Adenine (Аденин) — B4", "Vitamin B8 (Витамин B8) — B8", "Inositol (Инозитол) — B8", "Vitamin B10 (Витамин B10) — B10", "PABA (ПАБК) — PABA", "Vitamin B13 (Витамин B13) — B13", "Orotic acid (Оротовая кислота) — B13", "Vitamin B15 (Витамин B15) — B15", "Pangamic acid (Пангамовая кислота) — B15", "Vitamin B17 (Витамин B17) — B17", "Amygdalin (Амигдалин) — B17", "Vitamin T (Витамин T) — T", "Vitamin N (Витамин N) — N", "Lipoic acid (Липоевая кислота) — LA", "Choline (Холин) — Ch", "Calcium (Кальций) — Ca", "Phosphorus (Фосфор) — P", "Magnesium (Магний) — Mg", "Sodium (Натрий) — Na", "Potassium (Калий) — K", "Chloride (Хлорид) — Cl", "Sulfur (Сера) — S", "Iron (Железо) — Fe", "Zinc (Цинк) — Zn", "Copper (Медь) — Cu", "Manganese (Марганец) — Mn", "Iodine (Йод) — I", "Selenium (Селен) — Se", "Chromium (Хром) — Cr", "Molybdenum (Молибден) — Mo", "Cobalt (Кобальт) — Co", "Boron (Бор) — B", "Silicon (Кремний) — Si", "Vanadium (Ванадий) — V", "Nickel (Никель) — Ni", "Lithium (Литий) — Li", "Strontium (Стронций) — Sr", "Tin (Олово) — Sn", "Germanium (Германий) — Ge", "Rubidium (Рубидий) — Rb", "Omega-3 (Омега-3) — ω-3", "Alpha-linolenic acid (Альфа-линоленовая кислота) — ALA", "Eicosapentaenoic acid (Эйкозапентаеновая кислота) — EPA", "Docosahexaenoic acid (Докозагексаеновая кислота) — DHA", "Docosapentaenoic acid (Докозапентаеновая кислота) — DPA", "Omega-6 (Омега-6) — ω-6", "Linoleic acid (Линолевая кислота) — LA", "Gamma-linolenic acid (Гамма-линоленовая кислота) — GLA", "Arachidonic acid (Арахидоновая кислота) — AA", "Omega-9 (Омега-9) — ω-9", "Oleic acid (Олеиновая кислота) — OA", "Conjugated linoleic acid (Конъюгированная линолевая кислота) — CLA", "Medium-chain triglycerides (Среднецепочечные триглицериды) — MCT", "Histidine (Гистидин) — His", "Isoleucine (Изолейцин) — Ile", "Leucine (Лейцин) — Leu", "Lysine (Лизин) — Lys", "Methionine (Метионин) — Met", "Phenylalanine (Фенилаланин) — Phe", "Threonine (Треонин) — Thr", "Tryptophan (Триптофан) — Trp", "Valine (Валин) — Val", "Arginine (Аргинин) — Arg", "Cysteine (Цистеин) — Cys", "Glutamine (Глутамин) — Gln", "Tyrosine (Тирозин) — Tyr", "Glycine (Глицин) — Gly", "Proline (Пролин) — Pro", "Serine (Серин) — Ser", "Asparagine (Аспарагин) — Asn", "Alanine (Аланин) — Ala", "Aspartic acid (Аспарагиновая кислота) — Asp", "Glutamic acid (Глутаминовая кислота) — Glu", "Ornithine (Орнитин) — Orn", "Citrulline (Цитруллин) — Cit", "Taurine (Таурин) — Tau", "Carnitine (Карнитин) — Car", "Creatine (Креатин) — Cre", "HMB (HMB) — HMB", "GABA (ГАМК) — GABA", "5-HTP (5-HTP) — 5-HTP", "SAMe (SAMe) — SAMe", "N-acetylcysteine (N-ацетилцистеин) — NAC", "Glutathione (Глутатион) — GSH", "Lactobacillus (Лактобактерии) — Lacto", "Bifidobacterium (Бифидобактерии) — Bifido", "Saccharomyces boulardii (Saccharomyces boulardii) — S. boulardii", "Bacillus coagulans (Bacillus coagulans) — B. coagulans", "Inulin (Инулин) — Inulin", "Fructooligosaccharides (Фруктоолигосахариды) — FOS", "Galactooligosaccharides (Галактоолигосахариды) — GOS", "Xylooligosaccharides (Ксилоолигосахариды) — XOS", "Resistant starch (Резистентный крахмал) — RS", "Psyllium (Псиллиум) — Psyllium", "Pectin (Пектин) — Pectin", "Beta-glucan (Бета-глюкан) — β-glucan", "Coenzyme Q10 (Коэнзим Q10) — CoQ10", "Alpha-lipoic acid (Альфа-липоевая кислота) — ALA", "Acetyl-L-carnitine (Ацетил-L-карнитин) — ALCAR", "Methylsulfonylmethane (Метилсульфонилметан) — MSM", "Glucosamine (Глюкозамин) — GlcN", "Chondroitin (Хондроитин) — CS", "Collagen (Коллаген) — Coll", "Hyaluronic acid (Гиалуроновая кислота) — HA", "Resveratrol (Ресвератрол) — Res", "Curcumin (Куркумин) — Cur", "Quercetin (Кверцетин) — Quer", "Rutin (Рутин) — Rut", "Hesperidin (Гесперидин) — Hesp", "Lutein (Лютеин) — Lut", "Zeaxanthin (Зеаксантин) — Zea", "Astaxanthin (Астаксантин) — Asta", "Lycopene (Ликопин) — Lyc", "Chlorophyll (Хлорофилл) — Chl", "Spirulina (Спирулина) — Spir", "Chlorella (Хлорелла) — Chlore", "Melatonin (Мелатонин) — Mel", "DHEA (ДГЭА) — DHEA", "Pregnenolone (Прегненолон) — Preg", "Ashwagandha (Ашваганда) — Ash", "Rhodiola (Родиола) — Rhod", "Ginseng (Женьшень) — Gins", "Ginkgo (Гинкго) — Gink", "Milk thistle (Расторопша) — MT", "Berberine (Берберин) — Berb", "Cinnamon (Корица) — Cinn", "Chromium picolinate (Пиколинат хрома) — CrPic", "Digestive enzymes (Пищеварительные ферменты) — DE", "Betaine HCl (Бетаин HCl) — BetHCl", "Bile salts (Соли желчных кислот) — BS", "Fiber (Клетчатка) — Fib", "Phosphatidylserine (Фосфатидилсерин) — PS", "Phosphatidylcholine (Фосфатидилхолин) — PC", "DMAE (ДМАЭ) — DMAE"]
@app.post("/add_vitamins")
def add_vitamins(vitamins: str | None = None):
    if len(vitamins) > 35:
        return{"Error": "Вы передали больше 35 символов"}
    # 1. Проверяем, передана ли вообще строка
    if not vitamins or not vitamins.strip() :
        return {"Error": "Строка с витаминами пуста"}
    
    global request_id

    # 2. Очищаем и собираем список витаминов
    vitamins_list = [vitamin.strip(",") for vitamin in vitamins.split()]
    vitamins_clean = [v.lower() for v in vitamins_list if v]

    if len(vitamins_clean) > 10:
        return{"Error": "Вы ввели больше 10 витаминов за раз"}

    if vitamins_clean == []:
        raise HTTPException(404, "Вы ввели не витамины")
    for vitamin in vitamins_clean:
        if str(vitamin).lower() not in str(valid_vitamins).lower():
            raise HTTPException(
                status_code=404,
                detail=f"Ошибка: '{vitamin}' не является допустимым витамином."
            )
    

    # 3. Новая валидация: разрешаем только буквы, цифры и дефис
    for vitamin in vitamins_clean:
        # Проверяем каждый символ в названии витамина
        # c.isalnum() проверяет, является ли символ буквой или цифрой
        # c == "-" проверяет, является ли символ тире
        is_valid = all(c.isalnum() or c == "-" for c in vitamin)
        
        if not is_valid:
            # Если нашли запрещенный символ (например, $, @, +, =), возвращаем ошибку
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
