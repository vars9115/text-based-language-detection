from flask import Flask, render_template, request
from langdetect import detect, LangDetectException

app = Flask(__name__)

language_names = {
    "en": "English",
    "te": "Telugu",
    "ta": "Tamil",
    "hi": "Hindi",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "pt": "Portuguese",
    "ru": "Russian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh-cn": "Chinese",
    "ar": "Arabic"
}

@app.route("/", methods=["GET", "POST"])
def home():
    language = ""
    text = ""
    error = ""

    if request.method == "POST":
        text = request.form.get("text", "").strip()

        if text:
            try:
                code = detect(text)
                language = language_names.get(code, code)
            except LangDetectException:
                error = "Unable to detect the language."
        else:
            error = "Please enter some text."

    return render_template(
        "index.html",
        language=language,
        text=text,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)