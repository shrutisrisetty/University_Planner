from datetime import datetime, timedelta

# -----------------------------
# DATA MODELS
# -----------------------------

class ClassSession:
    def __init__(self, day, start, end):
        self.day = day            # 0=Mon ... 6=Sun
        self.start = start
        self.end = end


class Subject:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.sessions = []        # multiple days


class Assignment:
    def __init__(self, subject_code, title, due_date):
        self.subject_code = subject_code
        self.title = title
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")


# -----------------------------
# DASHBOARD FUNCTION
# -----------------------------

def show_dashboard(subjects, assignments):
    today = datetime.today().weekday()
    now = datetime.now()
    next_week = now + timedelta(days=7)

    print("\n========== DASHBOARD ==========")

    # Today's Classes
    print("\n📅 TODAY'S CLASSES")
    today_classes = []

    for subject in subjects:
        for session in subject.sessions:
            if session.day == today:
                today_classes.append((subject, session))

    if not today_classes:
        print("No classes today.")
    else:
        today_classes.sort(key=lambda x: x[1].start)
        for s, c in today_classes:
            print(f"{c.start}-{c.end} | {s.name} ({s.code})")

    # Upcoming Assignments
    print("\n📝 UPCOMING ASSIGNMENTS (Next 7 Days)")
    upcoming = [
        a for a in assignments
        if now <= a.due_date <= next_week
    ]

    if not upcoming:
        print("No upcoming assignments.")
    else:
        upcoming.sort(key=lambda x: x.due_date)
        for a in upcoming:
            print(f"{a.title} [{a.subject_code}] - Due {a.due_date.date()}")

    print("\n===============================\n")


# -----------------------------
# MAIN (USER INPUT)
# -----------------------------

def main():
    subjects = []
    assignments = []

    print("Add Subjects and Classes")
    while True:
        name = input("Subject name (or 'done'): ")
        if name.lower() == "done":
            break

        code = input("Subject code: ")
        subject = Subject(name, code)

        while True:
            print("Day: 0=Mon 1=Tue 2=Wed 3=Thu 4=Fri 5=Sat 6=Sun")
            day = int(input("Class day: "))
            start = input("Start time (HH:MM): ")
            end = input("End time (HH:MM): ")
            subject.sessions.append(ClassSession(day, start, end))

            more = input("Add another day for this subject? (y/n): ")
            if more.lower() != "y":
                break

        subjects.append(subject)

    print("\nAdd Assignments")
    while True:
        title = input("Assignment title (or 'done'): ")
        if title.lower() == "done":
            break

        code = input("Subject code: ")
        due = input("Due date (YYYY-MM-DD): ")
        assignments.append(Assignment(code, title, due))

    # SHOW DASHBOARD
    show_dashboard(subjects, assignments)


if __name__ == "__main__":
    main()
