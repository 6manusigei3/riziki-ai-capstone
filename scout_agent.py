class ScoutAgent:
    def analyze_message(self, message):
        keywords = ["school fees", "loan shark", "debt"]

        for keyword in keywords:
            if keyword in message.lower():
                return {
                    "alert": True,
                    "reason": keyword
                }

        return {
            "alert": False,
            "reason": None
        }
