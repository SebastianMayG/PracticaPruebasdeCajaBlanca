from validador_credenciales import ValidadorCredenciales

class TestProcesarCredencialesCajaBlanca:
    
    def setup_method(self):
        self.procesador = ValidadorCredenciales()

    # =========================================================================
    # PRUEBAS PARA email_strength_test
    # =========================================================================

    def test_camino_1_correo_none(self):
        """Camino 1: correo = nulo """
        resultado, mensaje = self.procesador.email_strength_test("")
        assert resultado == False
        assert "nula" in mensaje

    def test_camino_2_correo_arroba(self):
        """Camino 2: correo = arroba """
        resultado, mensaje = self.procesador.email_strength_test("admin")
        assert resultado == False
        assert "@" in mensaje
    
    def test_camino_3_correo_menos_de_5_caracteres(self):
        """Camino 3: correo con el usuario menor a 5 caracteres"""
        resultado, mensaje = self.procesador.email_strength_test("admi@uacam.mx")
        assert resultado == False
        assert "usuario" in mensaje
    
    def test_camino_4_correo(self):
        """Camino 4: correo con dominio"""
        resultado, mensaje = self.procesador.email_strength_test("admi123@")
        assert resultado == False
        assert "dominio" in mensaje

        # =========================================================================
    # PRUEBAS PARA password_strength_test - V(G) = 8 (8 caminos basicos)
    # =========================================================================

    def test_camino_1_none(self):
        """Camino 1: contraseña = nula"""
        resultado, mensaje = self.procesador.password_strength_test(" ")
        assert resultado == False
        assert "nula" in mensaje

    def test_camino_2_menos_de_8_caracteres(self):
        """Camino 2: contraseña menor a 8 caracteres"""
        resultado, mensaje = self.procesador.password_strength_test("123456")
        assert resultado == False
        assert "8 caracteres" in mensaje

    def test_camino_3_sin_mayusculas(self):
        """Camino 3: sin letras mayusculas"""
        resultado, mensaje = self.procesador.password_strength_test("abc123@#")
        assert resultado == False
        assert "mayuscula" in mensaje

    def test_camino_4_sin_minusculas(self):
        """Camino 4: sin letras minusculas"""
        resultado, mensaje =self.procesador.password_strength_test("ABC123@#")
        assert resultado == False
        assert "minuscula" in mensaje

    def test_camino_5_sin_numeros(self):
        """Camino 5: sin numeros"""
        resultado, mensaje = self.procesador.password_strength_test("Abcdef@#")
        assert resultado == False
        assert "numero" in mensaje

    def test_camino_6_sin_caracter_especial(self):
        """Camino 6: sin caracter especial"""
        resultado, mensaje = self.procesador.password_strength_test("Abcdef12")
        assert resultado == False
        assert "especial" in mensaje

    def test_camino_7_valido(self):
        """Camino 7: contraseña valida"""
        resultado, mensaje = self.procesador.password_strength_test("Abcd123{]")
        assert resultado == True
        assert "valida" in mensaje

    def test_camino_8_usuario_en_contrasena(self):
        """Camino 8: contraseña con usuario"""
        self.procesador.email_strength_test("admin@uacam.mx")
        resultado, mensaje = self.procesador.password_strength_test("adminL1234{]")
        assert resultado == False
        assert "usuario" in mensaje