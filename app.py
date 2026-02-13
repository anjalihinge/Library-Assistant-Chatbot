from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ---------------- LIBRARY DATA ---------------- #
books = [
    # Database
    {"title": "DBMS", "author": "Korth", "subject": "Database", "copies": 3},
    {"title": "Database System Concepts", "author": "Silberschatz", "subject": "Database", "copies": 2},
    {"title": "NoSQL Distilled", "author": "Pramod Sadalage", "subject": "Database", "copies": 1},

    # Operating Systems
    {"title": "Operating System", "author": "Silberschatz", "subject": "Operating Systems", "copies": 2},
    {"title": "Modern Operating Systems", "author": "Tanenbaum", "subject": "Operating Systems", "copies": 1},

    # Networks
    {"title": "Computer Networks", "author": "Tanenbaum", "subject": "Networks", "copies": 0},
    {"title": "Data Communications", "author": "Forouzan", "subject": "Networks", "copies": 2},

    # Programming
    {"title": "Java: The Complete Reference", "author": "Herbert Schildt", "subject": "Programming", "copies": 4},
    {"title": "Python Crash Course", "author": "Eric Matthes", "subject": "Programming", "copies": 3},

    # Algorithms
    {"title": "Introduction to Algorithms", "author": "CLRS", "subject": "Algorithms", "copies": 1},
]


# ---------------- ROUTES ---------------- #
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"].lower()

    # get all subjects dynamically
    subjects = set(b["subject"].lower() for b in books)

    # -------- SUBJECT SPECIFIC QUESTIONS -------- #
    for subject in subjects:
        if subject in user_msg:
            subject_books = [b for b in books if b["subject"].lower() == subject]

            if subject_books:
                reply = f"📚 <b>{subject.title()} Books:</b><br>"
                for b in subject_books:
                    reply += f"- {b['title']} ({b['copies']} copies)<br>"
            else:
                reply = f"❌ No books available for {subject.title()}."

            return jsonify({"reply": reply})

    # -------- ALL BOOKS -------- #
    if "book" in user_msg:
        reply = "📚 <b>Books by Section:</b><br><br>"
        sections = {}

        for b in books:
            sections.setdefault(b["subject"], []).append(b)

        for section, items in sections.items():
            reply += f"<b>{section}</b><br>"
            for book in items:
                reply += f"- {book['title']} ({book['copies']} copies)<br>"
            reply += "<br>"

    # -------- AUTHORS -------- #
    elif "author" in user_msg:
        authors = sorted(set(b["author"] for b in books))
        reply = "✍️ <b>Authors in Library:</b><br>"
        for a in authors:
            reply += f"- {a}<br>"

    # -------- AVAILABILITY -------- #
    elif "availability" in user_msg or "available" in user_msg:
        reply = "📦 <b>Book Availability:</b><br>"
        for b in books:
            status = "Available" if b["copies"] > 0 else "Not Available"
            reply += f"- {b['title']} : {status}<br>"

    # -------- BORROW RULES -------- #
    elif "borrow" in user_msg or "return" in user_msg:
        reply = (
            "📄 <b>Borrowing Rules:</b><br>"
            "• Maximum 14 days<br>"
            "• Fine ₹2/day after due date<br>"
            "• Max 2 books at a time"
        )

    # -------- DEFAULT -------- #
    else:
        reply = "👋 Hello! Ask me about books, authors, availability, or borrow rules."

    return jsonify({"reply": reply})


# ---------------- RUN ---------------- #
if __name__ == "__main__":
    app.run(debug=True)
