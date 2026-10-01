# Google Calendar Application using Greedy Strategy
# Problem: Select maximum number of non-overlapping events
# Algorithm: Activity Selection

def time_to_minutes(time):
    """Convert HH:MM time into minutes."""
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def select_events(events):
    # Sort events according to their ending time
    events.sort(key=lambda event: time_to_minutes(event["end"]))

    selected_events = []
    last_end_time = 0

    for event in events:
        start_time = time_to_minutes(event["start"])

        # Select event if it does not overlap
        if start_time >= last_end_time:
            selected_events.append(event)
            last_end_time = time_to_minutes(event["end"])

    return selected_events


# Calendar events
events = [
    {"name": "Team Meeting", "start": "09:00", "end": "10:00"},
    {"name": "Project Discussion", "start": "10:00", "end": "11:00"},
    {"name": "Lunch", "start": "12:00", "end": "13:00"},
    {"name": "Client Meeting", "start": "09:30", "end": "11:30"},
    {"name": "Coding Session", "start": "13:00", "end": "14:30"},
    {"name": "Presentation", "start": "14:00", "end": "15:00"},
    {"name": "Project Review", "start": "15:00", "end": "16:00"}
]

# Select maximum number of non-overlapping events
selected_events = select_events(events)

# Display selected events
print("Selected Calendar Events:")
print("-------------------------")

for event in selected_events:
    print(
        event["name"],
        "->",
        event["start"],
        "to",
        event["end"]
    )