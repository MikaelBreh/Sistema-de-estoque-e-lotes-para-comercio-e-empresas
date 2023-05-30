from datetime import datetime

def validar_data(data_str):
    try:
        data = datetime.strptime(data_str, '%d/%m/%Y')
        return data.strftime('%d/%m/%Y') == data_str
    except ValueError:
        return False
