class HunterAgent:
    def prepare_briefing(self, applicant):
        return f"""
RIZIKI AI BRIEFING

Applicant: {applicant['name']}
Occupation: {applicant['occupation']}
Amount Requested: KES {applicant['amount']}

Recommendation:
Human review required.
"""
