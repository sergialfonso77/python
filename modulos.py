import mensajes 

print(mensajes.messageFormatter("Error: Este mensaje es de error", "error"))
print()
print(mensajes.messageFormatter("Éxito: Este mensaje es de éxito", "success"))
print()
print(mensajes.messageFormatter("Advertencia: Este mensaje es una advertencia",
"warning"))
print()
print(mensajes.messageFormatter("Información: Este mensaje es informativo", "info"))
print()
print("Este mensaje es normal")