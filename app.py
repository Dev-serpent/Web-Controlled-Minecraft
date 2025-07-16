from flask import Flask, request, redirect, url_for, render_template, session
import requests

app = Flask(__name__)
app.secret_key = "minecraft-remote-secret"

buttons = []
button_counter = 1

@app.route("/")
def home():
    return render_template("check.html")

@app.route("/check", methods=["GET"])
def check():
    try:
        r = requests.post("http://localhost:5001/command", json={"cmd": "/say Checking connection..."})
        return redirect("/control")
    except Exception:
        return "<h2>❌ Minecraft is not active on port 5001</h2><a href='/'>Try again</a>"
@app.route("/delete_button", methods=["POST"])
def delete_button():
    try:
        id = int(request.form["id"])
        global buttons
        buttons = [b for b in buttons if b["id"] != id]
    except Exception as e:
        session["error"] = f"❌ Delete failed: {e}"
    return redirect("/control")

@app.route("/control")
def control():
    return render_template("control.html", buttons=buttons)

@app.route("/add_button", methods=["POST"])
def add_button():
    global button_counter
    try:
        raw = request.get_data(as_text=True).strip()
        print(f"[add_button] Received raw: {raw}")

        if not raw.startswith("/lamp "):
            return "Invalid command", 400

        parts = raw.split()
        if len(parts) != 4:
            return "Invalid format", 400

        _, x, y, z = parts
        new_button = {
            "id": button_counter,
            "name": f"button{button_counter}",
            "x": int(x),
            "y": int(y),
            "z": int(z)
        }
        buttons.append(new_button)
        button_counter += 1

        print(f"[add_button] Added: {new_button}")
        return "OK"
    except Exception as e:
        print(f"[add_button] ❌ Error: {e}")
        return f"Error: {e}", 500
@app.route("/rename", methods=["POST"])
def rename_button():
    try:
        bid = int(request.form.get("id"))
        new_name = request.form.get("new_name")
        for b in buttons:
            if b["id"] == bid:
                b["name"] = new_name
                break
    except Exception as e:
        session["error"] = f"❌ Rename failed: {e}"
    return redirect("/control")

@app.route("/command", methods=["POST"])
def send_command():
    command = request.form.get("cmd")
    try:
        r = requests.post("http://localhost:5001/command", json={"cmd": command})
        return redirect("/control")
    except Exception as e:
        session["error"] = f"❌ {type(e).__name__}: {e}"
        return redirect("/control")

if __name__ == "__main__":
    app.run(port=5000)
