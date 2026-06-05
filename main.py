from scout_agent import ScoutAgent
from guardian_agent import GuardianAgent
from hunter_agent import HunterAgent

scout = ScoutAgent()
guardian = GuardianAgent()
hunter = HunterAgent()

message = "I need money for school fees"

applicant = {
    "name": "Grace",
    "occupation": "Market Vendor",
    "amount": 28000
}

scout_result = scout.analyze_message(message)

print("Scout Result:")
print(scout_result)

guardian_result = guardian.evaluate_loan(
    applicant["amount"]
)

print("\nGuardian Result:")
print(guardian_result)

if guardian_result["status"] == "escalate":
    print("\nHunter Briefing:")
    print(hunter.prepare_briefing(applicant))
