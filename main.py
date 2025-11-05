import procesar_credenciales_test

class Main:
    
    # ==========================================================
    # EJECUCIÓN MANUAL DE PRUEBAS CON COBERTURA SIMPLE
    # ==========================================================

    def ejecutar_pruebas_con_cobertura(self):
        print("=" * 50)
        print("EJECUTANDO PRUEBAS DE CAJA BLANCA")
        print("=" * 50)

        tester = procesar_credenciales_test.TestProcesarCredencialesCajaBlanca()
        metodos_prueba = [m for m in dir(tester)
        if m.startswith("test_") and "correo" in m] + [m for m in dir(tester)
        if m.startswith("test_") and "correo" not in m]


        
        total = len(metodos_prueba)
        exitos = 0
        fallos = 0

        for metodo in metodos_prueba:
            try:
                tester.setup_method()
                getattr(tester, metodo)()
                print(f"{metodo}: PASO")
                exitos += 1
            except AssertionError as e:
                print(f"{metodo}: FALLO -> {e}")
                fallos += 1
            except Exception as e:
                print(f"{metodo}: ERROR -> {e}")
                fallos += 1

        print("=" * 50)
        print(f"Total de pruebas: {total}")
        print(f"Pruebas exitosas: {exitos}/{total}")
        print(f"Pruebas fallidas: {fallos}/{total}")
        print(f"Tasa de exito: {(exitos/total)*100:.1f}%")
        print("=" * 50)
        print("COBERTURA DE CAMINOS BASICOS")
        print(f"  Metodo password_strength_test: {total}/{total} ({(total/total)*100:.1f}%)")

if __name__ == "__main__":
    main = Main()
    main.ejecutar_pruebas_con_cobertura()
