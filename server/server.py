from flask import Flask
from entries import EntryDB

app = Flask(__name__)

def run():
    app.run(port=8080)

@app.route("/entries" , methods=["GET"])
def get_entries():
    db = EntryDB("entries.db")
    entries = db.get_entries()
    return entries, 200, {"Access-Control-Allow-Origin": "*"}

if __name__ == "__main__":
    run()