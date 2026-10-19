import sqlite3
from sqlite3 import Error
from flask import Flask, render_template, request

app = Flask(__name__) #creates a flask website
DATABASE = "hsr.db" #defines the file path from the sqlite database

#connects the database and returns the connection object
def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Error as e:
        print(e)
        return None

@app.route("/")#Route from the homepage
def render_home():
    return render_template("index.html")

@app.route('/characters')#fetches characters info from the database
def render_characters():
    query = "SELECT Character, Path, Element, Version_released, Home_Planet, First_met, HP, ATK, DEF, SPD FROM Character"
    con = create_connection(DATABASE)#opens connection
    cur = con.cursor()
    cur.execute(query)
    character_list = cur.fetchall()
    con.close()
    print(character_list)
    return render_template("characters.html", characters=character_list)

@app.route("/search", methods=["GET", "POST"])#search feature
def render_search():
    search = request.form['search']
    query = "SELECT Character, Path, Element, Version_released, Home_Planet, First_met, HP, ATK, DEF, SPD FROM Character WHERE Character LIKE ? OR Path LIKE ? OR Element LIKE ? OR Version_released LIKE ? OR Home_Planet LIKE ? OR First_met LIKE ? OR HP LIKE ? OR ATK LIKE ? OR DEF LIKE ? OR SPD LIKE ?"
    con = create_connection(DATABASE)
    cur = con.cursor()
    cur.execute(query, (search,search,search,search,search,search,search,search,search,search))
    character_list = cur.fetchall()
    con.close()
    return render_template("characters.html", characters=character_list)
#runs flask
if __name__ == "__main__":
    app.run()
