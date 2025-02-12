from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Replace with your Gemini API Key
GEMINI_API_KEY = "AIzaSyCdPw0kiJnQhxPbANaT7kU35zUpve3rDU0"
genai.configure(api_key=GEMINI_API_KEY)

@app.route("/", methods=["GET"])
def generate_response():
    prompt = request.args.get("prompt")
    
    if not prompt:
        return jsonify({"response": "❌ No prompt provided."})

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})  # Returns AI-generated response
    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
