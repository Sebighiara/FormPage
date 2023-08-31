from dotenv import load_dotenv
import os
from supabase import create_client
from flask import Flask, render_template

#load env vars
load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

#setup supabase client
supabase = create_client(url, key)

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()

