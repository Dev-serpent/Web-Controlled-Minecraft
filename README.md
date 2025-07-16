# 🧱 Minecraft Web Remote Control (Phase 1)

Control Minecraft redstone from a dynamic Flask web interface — powered by custom right-clickable blocks and a live command panel.

Built with:

* 🛠️ Python (Flask)
* 🎮 Minecraft + NeoForge mod
* 🧠 Real-time Minecraft ↔ Web syncing

---

## 🚀 Setup Instructions

### 1️⃣ Upload the Mod

Place the provided `.jar` mod file into your Minecraft `mods` folder.

```
.minecraft/mods/
```

> Ensure you're using the **NeoForge** loader with a compatible Minecraft version.

---

### 2️⃣ Run the Python Server

Open `app.py` in your terminal or IDE and run it:

```bash
python app.py
```

---

### 3️⃣ Visit the Control Site

Click the link Flask shows (usually something like):

```
 * Running on http://127.0.0.1:5000/
```

Or open this in your browser:

```
http://127.0.0.1:5000
```

---

### 4️⃣ Open Minecraft World

* Open any single-player world
* Make sure **cheats are enabled**
* Launch the world before proceeding

---

### 5️⃣ Click the “Connect” Button

On the website, click the **“Connect to Minecraft”** button.
This verifies that Minecraft is running and ready.

---

### 6️⃣ Right-Click a Custom Block

In the game:

* Locate one of your **custom blocks** (e.g. `red_signal_off`)
* Right-click it

✅ This will:

* Run `/lamp x y z` in Minecraft
* Add a button to your control panel

---

### 7️⃣ Reload the Web Page

Visit `/control` (or just reload the site)

You’ll now see a button labeled like `button1`.

🟠 Clicking this button will:

* Send `/lamp x y z` to Minecraft
* Toggle redstone (or custom behavior) remotely!

---

## 🎉 Done — You're Controlling Minecraft Remotely

Welcome to the future of redstone.

You can:

* 📂 Rename buttons
* 🗑 Delete unused toggles
* 🔁 Create more by right-clicking more blocks
* 🧠 Control your world from your browser!

---

## 🛠 Developer Notes

* Flask runs on port `5000`
* Minecraft listens on mod-injected HTTP handler at port `5001`
* Communication is handled via `/command` and `/add_button` endpoints

---

## 📆 Coming Next: Phase 2

> 🎤 Voice-controlled mobs & spoken AI commands inside Minecraft...

Stay tuned for more 👀
