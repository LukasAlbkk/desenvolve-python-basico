import datetime

data = datetime.datetime.now().date()
print(f"Data: {data}")
hora = datetime.datetime.now().time()
hora_minutos = f"{hora.hour}:{hora.minute}"
print(f"Hora: {hora_minutos}")