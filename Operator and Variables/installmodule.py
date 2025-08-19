import pyttsx3
print("pyttsx3 is installed and ready!")

engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("Nabihaa go outtt")
engine.runAndWait()