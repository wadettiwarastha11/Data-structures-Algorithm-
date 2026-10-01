# Google Calendar Application using Greedy Strategy
# Problem: Select maximum number of non-overlapping events

def select_events(events):
    # Sort events according to ending time
    events.sort(key=lambda event: event["end"])

    selected_events = []
    last_end_time = -1

    for event in events:
        if event["start"] >= last_end_time:
            selected_events.append(event)
            last_end_time = event["end"]

    return selected_events


# Calendar events
events = [
    {"name": "Team Meeting", "start": 9, "end": 10},
    {"name": "Project Discussion", "start": 10, "end": 11},
    {"name": "Lunch", "start": 11, "end": 12},
    {"name": "Client Meeting", "start": 9, "end": 11},
    {"name": "Coding Session", "start": 12, "end": 2},
    {"name": "Presentation", "start": 1, "end": 3}
]

selected = select_events(events)

print("Selected Calendar Events:")
for event in selected:
    print(
        event["name"],
        "->",
        event["start"],
        "to",
        event["end"]
    )
    