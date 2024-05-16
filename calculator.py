import tkinter as tk
import speech_recognition as sr
import pyttsx3

def button_click(number):
    """Handles button clicks for numbers."""
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    """Clears the display."""
    display.delete(0, tk.END)

def button_operator(operator):
    """Handles button clicks for operators."""
    global first_number, operation
    first_number = float(display.get())
    operation = operator
    display.delete(0, tk.END)

def button_equals():
    """Calculates the result."""
    second_number = float(display.get())
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            result = "Error"
        else:
            result = first_number / second_number
    display.delete(0, tk.END)
    display.insert(0, result)
    speak(f"The answer is {result}")

def speak(text):
    """Speaks the given text."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_input():
    """Handles voice input and calculation."""
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak your calculation...")
            audio = r.listen(source)
        try:
            calculation = r.recognize_google(audio)
            print(f"You said: {calculation}")
            try:
                result = eval(calculation)
                display.delete(0, tk.END)
                display.insert(0, result)
                speak(f"The answer is {result}")
            except:
                display.delete(0, tk.END)
                display.insert(0, "Error")
                speak("Invalid input.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
            speak("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition; {e}")
            speak("Could not request results from Google Speech Recognition. Please try again.")
    except Exception as e:
        print(f"Error during voice input: {e}")
        speak("Error during voice input. Please try again.")

def switch_mode():
    """Switches between light and dark modes."""
    global current_mode
    if current_mode == "light":
        current_mode = "dark"
        window.configure(bg=dark_background_color)
        display.configure(bg=dark_display_color, fg=dark_text_color)
        for button in buttons:
            button.configure(bg=dark_button_color, fg=dark_text_color)
        mode_button.configure(text="Light Mode")
    else:
        current_mode = "light"
        window.configure(bg=light_background_color)
        display.configure(bg=light_display_color, fg=light_text_color)
        for button in buttons:
            button.configure(bg=light_button_color, fg=light_text_color)
        mode_button.configure(text="Dark Mode")

# Create main window
window = tk.Tk()
window.title("GUI with Voice Calculator")

# Define colors
light_background_color = "#f0f0f0"
light_button_color = "#e0e0e0"
light_operator_color = "#ff9933"
light_equal_color = "#00cc00"
light_display_color = "white"
light_text_color = "black"

dark_background_color = "#282c34"
dark_button_color = "#36393f"
dark_operator_color = "#ff9933"
dark_equal_color = "#00cc00"
dark_display_color = "#40444c"
dark_text_color = "white"

current_mode = "light"  # Start with light mode
window.configure(bg=light_background_color)

# Display for showing numbers and results
display = tk.Entry(window, width=25, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
display.configure(bg=light_display_color, fg=light_text_color, font=("Arial", 16))

# Define buttons
button_7 = tk.Button(window, text="7", width=5, command=lambda: button_click(7), bg=light_button_color)
button_8 = tk.Button(window, text="8", width=5, command=lambda: button_click(8), bg=light_button_color)
button_9 = tk.Button(window, text="9", width=5, command=lambda: button_click(9), bg=light_button_color)
button_add = tk.Button(window, text="+", width=5, command=lambda: button_operator("+"), bg=light_operator_color)

button_4 = tk.Button(window, text="4", width=5, command=lambda: button_click(4), bg=light_button_color)
button_5 = tk.Button(window, text="5", width=5, command=lambda: button_click(5), bg=light_button_color)
button_6 = tk.Button(window, text="6", width=5, command=lambda: button_click(6), bg=light_button_color)
button_subtract = tk.Button(window, text="-", width=5, command=lambda: button_operator("-"), bg=light_operator_color)

button_1 = tk.Button(window, text="1", width=5, command=lambda: button_click(1), bg=light_button_color)
button_2 = tk.Button(window, text="2", width=5, command=lambda: button_click(2), bg=light_button_color)
button_3 = tk.Button(window, text="3", width=5, command=lambda: button_click(3), bg=light_button_color)
button_multiply = tk.Button(window, text="*", width=5, command=lambda: button_operator("*"), bg=light_operator_color)

button_0 = tk.Button(window, text="0", width=5, command=lambda: button_click(0), bg=light_button_color)
button_clear = tk.Button(window, text="C", width=5, command=button_clear, bg=light_button_color)
button_equals = tk.Button(window, text="=", width=5, command=button_equals, bg=light_equal_color)
button_divide = tk.Button(window, text="/", width=5, command=lambda: button_operator("/"), bg=light_operator_color)

# Voice input button
button_voice = tk.Button(window, text="Voice Input", width=10, command=voice_input, bg="#66ccff")
button_voice.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

# Mode switch button
mode_button = tk.Button(window, text="Dark Mode", width=10, command=switch_mode, bg="#66ccff")
mode_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5)

# Place buttons on the grid
button_7.grid(row=1, column=0, padx=5, pady=5)
button_8.grid(row=1, column=1, padx=5, pady=5)
button_9.grid(row=1, column=2, padx=5, pady=5)
button_add.grid(row=1, column=3, padx=5, pady=5)

button_4.grid(row=2, column=0, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_subtract.grid(row=2, column=3, padx=5, pady=5)

button_1.grid(row=3, column=0, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_multiply.grid(row=3, column=3, padx=5, pady=5)

button_0.grid(row=4, column=0, padx=5, pady=5)
button_clear.grid(row=4, column=1, padx=5, pady=5)
button_equals.grid(row=4, column=2, padx=5, pady=5)
button_divide.grid(row=4, column=3, padx=5, pady=5)

# Keep track of all buttons
buttons = [
    button_7, button_8, button_9, button_add,
    button_4, button_5, button_6, button_subtract,
    button_1, button_2, button_3, button_multiply,
    button_0, button_clear, button_equals, button_divide,
    button_voice, mode_button
]

window.mainloop()