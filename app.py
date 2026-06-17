from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json.get("message", "").lower()

    if "who made you" in user_message:
        reply = "I am an AI assistant created by Mr. Dhanraj Singh from Pratapgarh."

    elif "hello" in user_message or "hi" in user_message:
        reply = "Hello! How can I help you today?"

    elif "how are you" in user_message:
        reply = "I am doing great."

    elif "your name" in user_message:
        reply = "My name is Dhanraj AI."

    elif "india" in user_message:
        reply = "India is a country in South Asia."

    elif "ai" in user_message:
        reply = "AI means Artificial Intelligence."

    elif "joke" in user_message:
        reply = "Why did the computer go to the doctor? Because it had a virus."

    else:
        reply = "Sorry, I don't know that yet."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)