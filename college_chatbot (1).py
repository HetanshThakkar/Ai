"""
College Enquiry Chatbot (Rule-Based)
------------------------------------
A simple chatbot that answers common college-related questions
using Python if-elif-else conditions and keyword matching.

Topic  : College
Group  : <Student 1 Name> (Enrollment No.) and <Student 2 Name> (Enrollment No.)
"""


def get_response(user_input):
    """Return the chatbot's reply for the given user input."""
    text = user_input.lower().strip()

    # ---------- Greetings ----------
    if text in ("hi", "hello", "hey") or "good morning" in text \
            or "good afternoon" in text or "good evening" in text:
        return "Hello! Welcome to the College Help Desk. How can I help you today?"

    elif "how are you" in text:
        return "I'm doing great, thank you! How can I assist you with college information?"

    # ---------- Admission ----------
    elif "admission" in text and ("last date" in text or "deadline" in text):
        return "The last date for admission applications is 30th June. Please apply before the deadline."

    elif "admission" in text or "apply" in text or "enroll" in text:
        return ("Admissions are open for all courses. You can apply online through the "
                "college website or visit the admission office with your documents.")

    elif "document" in text:
        return ("Documents required: 10th and 12th marksheets, leaving certificate, "
                "ID proof, passport-size photographs and a caste certificate (if applicable).")

    # ---------- Courses ----------
    elif "course" in text or "branch" in text or "program" in text:
        return ("We offer B.Tech (Computer, IT, Mechanical, Civil, Electrical), "
                "BCA, MCA, BBA and MBA programs.")

    elif "duration" in text:
        return "B.Tech is 4 years, BCA and BBA are 3 years, and MCA and MBA are 2 years."

    elif "eligibility" in text or "eligible" in text:
        return ("For B.Tech, you need 12th pass with Physics, Chemistry and Maths. "
                "For BCA/BBA, 12th pass in any stream. For MCA/MBA, a bachelor's degree.")

    # ---------- Fees & Scholarship ----------
    elif "fee" in text or "fees" in text or "cost" in text:
        return ("Approximate annual fees: B.Tech Rs. 90,000, BCA/BBA Rs. 50,000, "
                "MCA/MBA Rs. 70,000. Please contact the accounts office for exact details.")

    elif "scholarship" in text:
        return ("Scholarships are available for meritorious and economically weaker "
                "students. Apply through the state scholarship portal after admission.")

    # ---------- Placement ----------
    elif "placement" in text or "job" in text or "package" in text:
        return ("Our placement cell has a record of 85% placements. The average package "
                "is 4.5 LPA and the highest package is 18 LPA. Top recruiters include TCS, "
                "Infosys, Wipro and Accenture.")

    # ---------- Facilities ----------
    elif "library" in text:
        return "The library is open from 9 AM to 6 PM, Monday to Saturday, with over 20,000 books."

    elif "hostel" in text:
        return ("Separate hostels for boys and girls are available with Wi-Fi, mess and "
                "24x7 security. Hostel fees are about Rs. 60,000 per year.")

    elif "canteen" in text or "food" in text or "mess" in text:
        return "The canteen serves breakfast, lunch and snacks from 8 AM to 5 PM at student-friendly prices."

    elif "transport" in text or "bus" in text:
        return "College buses run from all major city points. Bus pass costs about Rs. 12,000 per year."

    elif "sports" in text or "ground" in text:
        return ("We have grounds for cricket, football and volleyball, along with indoor "
                "games, a gym and a yearly sports fest.")

    elif "wifi" in text or "wi-fi" in text or "internet" in text:
        return "Free high-speed Wi-Fi is available throughout the campus."

    # ---------- Exams & Timings ----------
    elif "exam" in text or "result" in text:
        return ("Semester exams are held twice a year, in November and April. "
                "Results are published on the college portal within 30 days.")

    elif "timing" in text or "time" in text or "hours" in text:
        return "College timings are 9:00 AM to 4:30 PM, Monday to Saturday. Sunday is a holiday."

    elif "holiday" in text or "vacation" in text:
        return "Summer vacation is in May-June and Diwali vacation is in November."

    # ---------- Contact ----------
    elif "contact" in text or "phone" in text or "email" in text or "number" in text:
        return "You can reach us at 0281-1234567 or email info@democollege.edu.in."

    elif "address" in text or "location" in text or "where" in text:
        return "Our campus is located on the Rajkot-Morbi Highway, Rajkot, Gujarat."

    # ---------- Thanks ----------
    elif "thank" in text:
        return "You're welcome! Feel free to ask if you have more questions."

    # ---------- Default ----------
    else:
        return ("Sorry, I did not understand that. You can ask me about admission, courses, "
                "fees, scholarships, placements, library, hostel, exams or contact details.")


TOPICS = [
    "Admission (how to apply, last date, documents required)",
    "Courses (courses offered, duration, eligibility)",
    "Fees and scholarships",
    "Placements (packages, recruiters)",
    "Facilities (library, hostel, canteen, transport, sports, Wi-Fi)",
    "Exams and results",
    "College timings and holidays",
    "Contact details and address",
]


def show_topics():
    """Print the list of topics the user can ask about."""
    print("You can ask me about:")
    for number, topic in enumerate(TOPICS, start=1):
        print(f"  {number}. {topic}")
    print()


def main():
    print("=" * 60)
    print("        COLLEGE ENQUIRY CHATBOT")
    print("=" * 60)
    show_topics()
    print("Type your question below. Type 'bye' or 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower().strip() in ("bye", "exit", "quit"):
            print("Bot: Goodbye! Have a great day.")
            break

        if user_input.strip() == "":
            print("Bot: Please type something so I can help you.")
            continue

        print("Bot:", get_response(user_input))
        print()


if __name__ == "__main__":
    main()
