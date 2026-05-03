from flask import Flask, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/health")
def health():
    return "OK"

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()

        # Validate input
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' in request"}), 400

        prompt = data["prompt"]

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract response text
        ai_response = response.choices[0].message.content

        return jsonify({
            "response": ai_response
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)