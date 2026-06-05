class GuardianAgent:
    def evaluate_loan(self, amount):
        if amount <= 15000:
            return {
                "status": "approved"
            }

        return {
            "status": "escalate"
        }
