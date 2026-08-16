subjects = [
    "politics", "latin",
    "dance", "architecture",
    "physics", "calculus",
    "poetry", "history",
    "computer science", "visual arts"]

full_gradebook = {
    "25_winter": {
        subjects[0] : 80,
        subjects[1] : 96,
        subjects[2] : 97,
        subjects[3] : 65,
    },
    "25_summer": {
        subjects[4] : 98,
        subjects[5] : 97,
        subjects[6] : 85,
        subjects[7] : 88,
    }
}

full_gradebook["25_summer"][subjects[8]] = 100
full_gradebook["25_summer"][subjects[9]] = 93

full_gradebook["25_summer"][subjects[9]] += 5

full_gradebook["25_summer"][subjects[6]] = "Pass"

print(full_gradebook)