import json


def load_candidates():
    """Возвращает список всех кандидатов"""

    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidate_by_id(candidate_id):
    """Возвращает одного кандидата по его id"""

    candidates = load_candidates()
    for candidate in candidates:
        if candidate["id"] is candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидата по имени"""
    candidates = load_candidates()
    candidates_matches = []
    candidate_name_lower = candidate_name.lower()

    for candidate in candidates:
        if candidate_name_lower in candidate["name"].lower():
            candidates_matches.append(candidate)

    return candidates_matches


def get_candidates_by_skill(skill_name):
    """Возвращает кандидата по навыку"""
    candidates = load_candidates()
    skilled_candidates = []
    skill_lower = skill_name.lower()

    for candidate in candidates:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates