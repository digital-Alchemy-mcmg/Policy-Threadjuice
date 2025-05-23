
import random
import uuid
import json

governance_ideologies = {
    "Free-Market Capitalism": "Market Libertarian",
    "Mixed Economy": "Centrist Pragmatist",
    "Social Market Economy": "Social Democrat",
    "State Capitalism": "Strategic Authoritarian",
    "Command Economy": "Centralized Planner",
    "Islamic Economic System": "Faith-Based Economist",
    "Developmental State Model": "Growth Technocrat",
    "Balanced Progress Economy": "AI-Governed Optimizer",
    "Regional Resource Governance Economy": "Guild Regionalist",
    "Authoritarian Resource-Hoarding Monarchy": "Extraction Monarchist"
}

phases = ["The Pragmatist", "The Idealist", "The Operator", "The Loyalist", "The Maverick"]
risk_flags = ["Burnout risk", "Ambition overreach", "Susceptible to coercion", "Ideological rigidity", "None"]
career_highlights = [
    "Former Position: WTO Deputy Director",
    "Academic Background: Economics PhD",
    "Published author on renewable economies",
    "Served in high-conflict negotiation zones",
    "Led trade reforms during crisis period",
    "Architect of post-conflict reconstruction policy"
]

def generate_attributes(performance):
    base = {"low": 3, "modest": 5, "high": 7}[performance]
    return {
        "Diplomatic Prowess": round(random.uniform(base, base + 2), 1),
        "Economic Strategy": round(random.uniform(base, base + 2), 1),
        "Policy Implementation": round(random.uniform(base - 1, base + 1.5), 1),
        "Crisis Management": round(random.uniform(base - 2, base + 1), 1),
        "Trade Negotiation": round(random.uniform(base, base + 3), 1)
    }

def generate_candidate(governance_type, risk_level="low", performance="modest"):
    ideology = governance_ideologies[governance_type]
    return {
        "agent_id": str(uuid.uuid4()),
        "name": f"Dr. {random.choice(['Amara', 'Kenji', 'Luis', 'Fatima', 'Elena'])} {random.choice(['Chen', 'Singh', 'Martinez', 'Okoro', 'Ivanov'])}",
        "phase_name": random.choice(phases),
        "age": random.randint(38, 63),
        "gender": random.choice(["F", "M"]),
        "background": random.choice(["East Asian", "African Diaspora", "North American", "Mixed Heritage"]),
        "ideology": ideology,
        "governance_alignment": governance_type,
        "attribute_ratings": generate_attributes(performance),
        "risk_flags": random.choices(risk_flags[:-1], k=1 if risk_level == "high" else 0),
        "career_notes": random.sample(career_highlights, 2),
        "position_compatibility_score": round(random.uniform(6.5, 9.5), 1) if performance != "low" else round(random.uniform(4.5, 6.5), 1),
        "learning_rate": round(random.uniform(0.6, 1.0) if performance == "high" else random.uniform(0.3, 0.7), 2)
    }

def generate_batch(governance_type, count=10, risk_level="low", performance="modest"):
    return [generate_candidate(governance_type, risk_level, performance) for _ in range(count)]

if __name__ == "__main__":
    candidates = []
    for gov in governance_ideologies.keys():
        candidates.extend(generate_batch(gov, count=15, risk_level="low", performance="modest"))
        candidates.extend(generate_batch(gov, count=3, risk_level="high", performance="high"))

    with open("agent_candidates_full.json", "w") as f:
        json.dump(candidates, f, indent=2)
