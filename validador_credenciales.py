import re

class ValidadorCredenciales:

        def __init__(self):
                self.usuario = ""

        def email_strength_test(self, email):
                if not email or email.strip() == "":
                        return False, "El correo no puede ser nula o vacia"
                if not "@" in email:
                        return False, "El correo debe de tener @"
        
                usuario, dominio = email.split("@")
                
                if len(usuario) < 5:
                        return False, "El usuario debe contener al menos 5 caracteres"
                if len(dominio.strip()) == 0:
                        return False, "El correo debe de contener un dominio"
                
                self.usuario = usuario
                return True, "El correo es valido"


        def password_strength_test(self, password):
                if not password or password.strip() == "":
                        return False, "La contraseña no puede ser nula o vacia"
                if len(password) < 8:
                        return False, "La contraseña debe tener al menos 8 caracteres"
                if not re.search(r"[a-z]", password):
                        return False, "La contraseña debe contener al menos una letra minuscula"
                if not re.search(r"[A-Z]", password):
                        return False, "La contraseña debe contener al menos una letra mayuscula"
                if not re.search(r"\d", password):
                        return False, "La contraseña debe contener al menos un numero"
                if not re.search(r"[^a-zA-Z0-9]", password):
                        return False, "La contraseña debe contener al menos un caracter especial"
                if self.usuario and self.usuario.lower() in password.lower():
                        return False, "La contraseña no debe de contener el usuario"
                return True, "La contraseña es valida"
