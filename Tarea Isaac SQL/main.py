import pyodbc
import os
import datetime
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
SERVER = 'DESKTOP-8U16EUU'
DATABASE = 'Escuela'

try:
    connection = pyodbc.connect(f'DRIVER={{ODBC Driver 17 for SQL SERVER}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
    print("Conexion exitosa")
    cursor = connection.cursor()   
    while True:
        r=int(input("¿Que desea hacer? \n1-Agregar una clase \n2-Actualizar clase \n3-Mostrar clases \n4-Buscar clase\n5-Eliminar clase\n6-Salir\n"))
        match r:
            case 1:
                clear()
                while True:
                    cursor = connection.cursor()  
                    try:
                        A = int(input("---Numero del Aula---\n"))
                        break
                    except ValueError:
                        print("Dato Erroneo")

                while True:
                    try:
                        HI = int(input("---Hora de Inicio(Formato 24 horas)---\n")) 
                        while True:
                            if HI>24 or HI<1:
                                clear()
                                print("Dato erroneo, vuelva a introducirlo")
                                HI = int(input("---Hora de Inicio(Formato 24 horas)---\n")) 
                            else:
                                break 
                        while True:
                            HIM = int(input("---Minutos de Inicio---\n")) 
                            if HIM>59 or HIM<0:
                                clear()
                                print("Dato erroneo, vuelva a introducirlo")
                                HIM = int(input("---Minutos de Inicio---\n")) 
                            else:
                                break       
                        break
                    except ValueError:
                        print("Dato Erroneo")

                while True:
                    try:
                        HF = int(input("---Hora de Fin(Formato 24 horas)---\n"))                                 
                        while True:
                            if HF>24 or HF<1:
                                clear()
                                print("Dato erroneo, vuelva a introducirlo")
                                HF = int(input("---Hora de Fin(Formato 24 horas)---\n")) 
                            else:
                                break 
                        
                        HIF = int(input("---Minutos de Fin---\n")) 
                        while True:
                            if HIF>59 or HIF<0:
                                clear()
                                print("Dato erroneo, vuelva a introducirlo")
                                HIF = int(input("---Minutos de Fin---\n")) 
                            else:
                                break       
                        break
                    except ValueError:
                        print("Dato Erroneo")

                query = 'INSERT INTO Clases VALUES(?, ?, ?, ?, 1)'
                tVHI = datetime.time(HI, HIM, 00)
                tSHI = tVHI.strftime('%H:%M:%S')
                tVHF = datetime.time(HF, HIF, 00)
                tSHF = tVHF.strftime('%H:%M:%S')
                clear()

                cursor.execute("SELECT MAX(ClaseID) FROM Clases")
                UI = cursor.fetchone()[0]
                c = (UI or 0) + 1

                clase={
                    'ClaseID':c,
                    'Aula':A,
                    'HoraInicio':tSHI,
                    'HoraFin':tSHF
                }

                cursor.execute(query,clase["ClaseID"], clase["Aula"],clase["HoraInicio"], clase["HoraFin"])
                cursor.commit()
                cursor.close()
                input("¡Se ingreso la clase a la base de datos!")
                clear()
            case 2:
                try:
                    clear()
                    cursor = connection.cursor()   
                    ID=int(input("---Ingrese ID---\n"))
                    cursor.execute(f"SELECT * FROM Clases WHERE ClaseID = {ID}")
                    r = cursor.fetchone()
                    clear()
                    print(f"ID: {ID}\nAula: {r[1]}\nHora de Inicio: {r[2]}\nHora de finalizacion {r[3]}")
                    while True:
                        opc= int(input("¿Cual desea actualizar?\n1-Aula\n2-Hora de Inicio\n3-Hora de finalizacion\n4-Salir\n"))
                        clear()
                        match opc:
                            case 1:
                                clear()
                                cursor = connection.cursor()
                                A = input('---Ingrese nueva Aula---\n ')
                                cursor.execute(f'UPDATE Clases SET Aula={A} WHERE ClaseID = {ID}')
                                cursor.commit()
                                cursor.close()
                                input("¡Se actualizo el Aula!")
                                clear()
                            case 2:
                                try:
                                    cursor = connection.cursor()
                                    HI = int(input("---Hora de Inicio(Formato 24 horas)---\n")) 
                                    while True:
                                        if HI>24 or HI<1:
                                            clear()
                                            print("Dato erroneo, vuelva a introducirlo")
                                            HI = int(input("---Hora de Inicio(Formato 24 horas)---\n")) 
                                        else:
                                            break 
                                    while True:
                                        HIM = int(input("---Minutos de Inicio---\n")) 
                                        if HIM>59 or HIM<0:
                                            clear()
                                            print("Dato erroneo, vuelva a introducirlo")
                                            HIM = int(input("---Minutos de Inicio---\n")) 
                                        else:
                                            break    
                                    tVHI = datetime.time(HI, HIM, 00)
                                    tSHI = tVHI.strftime('%H:%M:%S')
                                    cursor.execute(f"UPDATE Clases SET HoraInicio = '{tSHI}' WHERE ClaseID = {ID}")
                                    cursor.commit()
                                    cursor.close()
                                    input("¡Se actualizo la hora inicial!")      
                                    clear()                              
                                except:
                                    input("Dato erroneo")
                            case 3:
                                try:
                                    cursor = connection.cursor()
                                    HF = int(input("---Hora de Fin(Formato 24 horas)---\n"))                                 
                                    while True:
                                        if HF>24 or HF<1:
                                            clear()
                                            print("Dato erroneo, vuelva a introducirlo")
                                            HF = int(input("---Hora de Fin(Formato 24 horas)---\n")) 
                                        else:
                                            break 

                                    HIF = int(input("---Minutos de Fin---\n")) 
                                    while True:
                                        if HIF>59 or HIF<0:
                                            clear()
                                            print("Dato erroneo, vuelva a introducirlo")
                                            HIF = int(input("---Minutos de Fin---\n")) 
                                        else:
                                            break                                      
                                    tVHF = datetime.time(HF, HIF, 00)
                                    tSHF = tVHF.strftime('%H:%M:%S')
                                    cursor.execute(f"UPDATE Clases SET HoraFin = '{tSHF}' WHERE ClaseID = {ID}")
                                    cursor.commit()
                                    cursor.close()
                                    input("¡Se actualizo la hora final!")
                                    clear()
                                except:
                                    input("Dato Erroneo")
                            case 4: 
                                break
                except:
                    input("Dato erroneo")
            case 3:
                try:
                    clear()
                    cursor = connection.cursor()   
                    cursor.execute("SELECT * From Clases")
                    m=cursor.fetchall()
                    for m in m:
                        input(f'ID:{m[0]}\nAula:{m[1]}\nHora Inicial:{m[2]}\nHora Final:{m[3]}')
                    clear()
                except:
                    input("Dato erroneo")
                    clear()
            case 4:
                try:
                    clear()
                    ID=int(input("---Ingrese ID de la clase---\n"))
                    cursor = connection.cursor()   
                    cursor.execute(f'SELECT * From Clases WHERE ClaseID = {ID}')
                    BC= cursor.fetchone()
                    input(f'ID:{ID}\nAula:{BC[1]}\nHora Inicial:{BC[2]}\nHora Final:{BC[3]}')
                    clear()
                except:
                    input("Dato erroneo")
                    clear()
            case 5:
                clear()
                try:
                    ID=int(input("---Ingrese ID de la clase---\n"))
                    cursor = connection.cursor()   
                    cursor.execute(f'SELECT * From Clases WHERE ClaseID={ID}')
                    BC= cursor.fetchone()
                    print(f'ID:{ID}\nAula:{BC[1]}\nHora Inicial:{BC[2]}\nHora Final:{BC[3]}')
                    YN=int(input("¿Estas seguro de querer eliminar esta clase? (1:Si||2:No)\n"))
                    if YN==1:
                        cursor.execute(f'DELETE FROM Clases WHERE ClaseID={ID}')
                        cursor.commit()
                        cursor.close()
                    else:
                        break
                except: 
                    input("Dato erroneo")
                clear()
            case 6:
                break
except Exception as ex:
    print(ex)