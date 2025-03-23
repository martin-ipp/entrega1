import random
import sys

# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    ("// Esto es un comentario", "/* Esto es un comentario */", "-- Esto es un comentario", "# Esto es un comentario"),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta
correct_answers_index = [1, 2, 0, 3, 1]

# Combinar preguntas, respuestas y respuestas correctas en una lista de tuplas
question_bank = list(zip(questions, answers, correct_answers_index))

# Seleccionar 3 preguntas aleatorias sin repetirse
questions_to_ask = random.sample(question_bank, k=3)

# Inicializar puntaje
score = 0

# Iterar sobre las preguntas seleccionadas
for question, answer_choices, correct_index in questions_to_ask:
    print(question)
    
    # Mostrar opciones de respuesta
    for i, answer in enumerate(answer_choices):
        print(f"{i + 1}. {answer}")

    # El usuario tiene 2 intentos para responder correctamente
    for _ in range(2):
        user_input = input("Respuesta: ")

        # Verificar si la entrada es un número entero
        if not user_input.isdigit():
            print("Respuesta no válida")
            sys.exit(1)

        user_answer = int(user_input) - 1

        # Verificar si la respuesta está dentro del rango válido
        if user_answer < 0 or user_answer >= len(answer_choices):
            print("Respuesta no válida")
            sys.exit(1)

        # Se verifica si la respuesta es correcta
        if user_answer == correct_index:
            print("¡Correcto!")
            score += 1  # Suma 1 punto por acierto
            break
        else:
            print("Incorrecto, intenta nuevamente.")
            score -= 0.5  # Descuenta 0.5 puntos por intento fallido
    else:
        # Si el usuario no responde correctamente después de 2 intentos, mostrar la respuesta correcta
        print(f"Incorrecto. La respuesta correcta es: {answer_choices[correct_index]}")

    # Espaciado entre preguntas
    print()

# Mostrar el puntaje final
score =0 if score<0 else score
print(f"Tu puntaje final es: {score:.1f} puntos")
