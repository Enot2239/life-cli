# ⚡ life-cli

> Your command-line productivity assistant — manage tasks, track habits, and generate passwords from one terminal interface.

---

## 🚀 Features

- ✅ Task Manager: add, list, complete and delete tasks
- 🔐 Password Generator: create secure passwords with optional symbols
- 📈 Habit Tracker: mark daily habits and view progress
- 📦 Lightweight: no web, no UI — pure Python CLI
- 🧠 Built with [Typer](https://typer.tiangolo.com/) & [Rich](https://rich.readthedocs.io/)

---

## 🧰 Installation

1. Clone the repository:

```bash
git clone https://github.com/Enot2239/life-cli.git
cd life-cli
Install dependencies:

bash
Копировать
Редактировать
pip install -r requirements.txt
Run the CLI:

bash
Копировать
Редактировать
python main.py --help
🖥️ CLI Help Output
General help
bash
Копировать
Редактировать
python main.py --help
Task commands
bash
Копировать
Редактировать
python main.py task add "Buy groceries"
python main.py task list
python main.py task done 1
python main.py task delete 1
Password generation
bash
Копировать
Редактировать
python main.py pass generate --length 16 --symbols
python main.py pass generate -l 20 --no-symbols
Habit tracker
bash
Копировать
Редактировать
python main.py habit track reading
python main.py habit history reading
python main.py habit list
📂 Project Structure
arduino
Копировать
Редактировать
life-cli/
├── app/
│   ├── config.py
│   ├── tasks.py
│   ├── passwords.py
│   └── habits.py
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
💡 To Do
 Add weather and quote modules

 Pomodoro timer

 Export stats to .md or .csv

 Add GitHub Actions test suite

📃 License
MIT License

Made with ❤️ by @Enot2239
