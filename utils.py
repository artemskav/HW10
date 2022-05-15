import json

def load_candidates():
    with open("candidates.json", "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data

def code_html_main_page():
    list_candidate = ""
    candidates = load_candidates()
    for candidate in candidates:
        name_candidate = candidate["name"]
        position_candidate = candidate["position"]
        skills_candidate = candidate["skills"]
        list_candidate += f"\n{name_candidate}\n"
        list_candidate += f"{position_candidate}\n"
        list_candidate += f"{skills_candidate}\n"
    return "<pre>" + list_candidate + "</pre>"

def code_html_one_candidate(pk):
    list_candidate = ""
    candidates = load_candidates()
    for candidate in candidates:
        if pk == candidate["id"]:
            name_candidate = candidate["name"]
            position_candidate = candidate["position"]
            skills_candidate = candidate["skills"]
            picture_candidate = candidate["picture"]
            list_candidate += f"\n{name_candidate}\n"
            list_candidate += f"{position_candidate}\n"
            list_candidate += f"{skills_candidate}\n"
    return f"<img src={picture_candidate}>" + "\n<pre>" + list_candidate + "</pre>"

def code_html_skills(skill):
    list_candidate = ""
    candidates = load_candidates()
    for candidate in candidates:
        skills = candidate["skills"].lower()
        if skill in skills:
            name_candidate = candidate["name"]
            position_candidate = candidate["position"]
            skills_candidate = candidate["skills"]
            list_candidate += f"\n{name_candidate}\n"
            list_candidate += f"{position_candidate}\n"
            list_candidate += f"{skills_candidate}\n"
    return "<pre>" + list_candidate + "</pre>"

#print(code_html_main_page())