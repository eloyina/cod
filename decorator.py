import logging
import functools
import time

def audit_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Registro de entrada al método
        entry_log = f"Inicio de ejecución: {func.__name__}"

        # Llamada al método original
        result = func(*args, **kwargs)

        # Registro de la 2lida del método
        exit_log = f"Fin de ejecución: {func.__name__}"

        # Registro de auditoría
        audit_log = {
            "function_name": func.__name__,
            "entry_log": entry_log,
            "exit_log": exit_log
        }

        return result, audit_log

    return wrapper

def calculate_sum(a, b):
    result = a + b
    return result

def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() with {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'TRACE: {func.__name__}() returned {original_result!r}')
        return original_result
    return wrapper

def argsykwargs(name, line):
    return f'{name}: {line}'

def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Configurar el logger
        logger = logging.getLogger(func.__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Registrar información antes de la ejecución
        logger.info('Iniciando ejecución de la función')

        # Ejecutar la función
        result = func(*args, **kwargs)

        # Registrar información después de la ejecución
        logger.info('Finalizando ejecución de la función')

        return result

    return wrapper

def ejemplo_funcion(parametro):
    print('La función ha sido ejecutada con el parámetro:', parametro)

def cache(func):
    memo = {}

    @functools.wraps(func)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result

    return wrapper

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def rate_limit(max_calls, period=60):
    def decorator(func):
        last_reset_time = time.time()
        call_count = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal last_reset_time
            nonlocal call_count

            current_time = time.time()

            if current_time - last_reset_time > period:
                # Han pasado más de "period" segundos, reiniciar el contador de llamadas
                call_count = 0
                last_reset_time = current_time

            if call_count >= max_calls:
                raise Exception("Rate limit exceeded. Try again later.")

            call_count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def access_control(required_permission):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Verificar si el usuario tiene el permiso requerido
            if current_user.get('permission') == required_permission:
                return func(*args, **kwargs)
            else:
                raise Exception("Acceso denegado.")

        return wrapper

    return decorator

# Configurar el logger
logging.basicConfig(level=logging.INFO)

# Usuario simulado
current_user = {'username': 'user1', 'permission': 'admin'}

while True:
    print("Seleccione una función:")
    print("1. calculate_sum")
    print("2. argsykwargs")
    print("3. ejemplo_funcion")
    print("4. factorial")
    print("5. my_function (rate_limit)")
    print("6. fibonacci")
    print("7. protected_function (access_control)")
    print("0. Salir")

    option = input("Ingrese el número de la función que desea ejecutar (0 para salir): ")

    if option == '0':
        break
    elif option == '1':
        result, audit = audit_log(calculate_sum)(5, 3)
        print(result)
        print(audit)
    elif option == '2':
        a = input('enter name: ')
        b = input('enter greet: ')
        print(trace(argsykwargs)(a, b))
    elif option == '3':
        parametro = input('Ingrese el parámetro para ejemplo_funcion: ')
        log_decorator(ejemplo_funcion)(parametro)
    elif option == '4':
        num = int(input('Ingrese el número para factorial: '))
        print(cache(factorial)(num))
    elif option == '5':
        max_calls = int(input('Ingrese el número máximo de llamadas para my_function: '))
        period = int(input('Ingrese el periodo de tiempo en segundos para rate_limit: '))
        limited_function = rate_limit(max_calls, period)(my_function)
        limited_function()
        def my_function():
            print('Executing my_function')
        limited_function = rate_limit(max_calls, period)(my_function)
        limited_function()
    elif option == '6':
        n = int(input('Ingrese el número para fibonacci: '))
        print(fibonacci(n))
    elif option == '7':
        protected_function = access_control('admin')(protected_function)
        try:
            protected_function()
            print("Acceso concedido.")
        except Exception as e:
            print(e)
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
