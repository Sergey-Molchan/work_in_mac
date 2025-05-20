import logging
logging.basicConfig(level=logging.INFO)

def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except FileNotFoundError:
        logging.error(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        logging.error(f"Ошибка декодирования JSON в файле {file_path}")
        return []
