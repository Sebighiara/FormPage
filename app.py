from dotenv import load_dotenv
import os
from supabase import create_client
from flask import Flask, render_template, request, redirect

#load env vars
load_dotenv()
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")

#setup supabase client
supabase = create_client(url, key)

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST":
        #get data from user
        req = request.form
        name = req.get("name")
        last_name = req.get("last_name")

        #insert the data from the user to supabase table
        data = supabase.table("names").insert({"name": name, "last_name": last_name}).execute()

        return redirect(request.url)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

