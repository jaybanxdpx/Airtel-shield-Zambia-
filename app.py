Airtel Shield Zambia - Anti-Fraud AI Bot
Protects Zambians from Airtel/MTN mobile money fraud

import re

def detect_fraud(message):
    """Detect fake Airtel/MTN fraud SMS"""
    scam_patterns = [
        r"you received.*K\d+",
        r"claim.*money.*link",
        r"airtel.*money.*blocked",
        r"verify.*pin.*now",
        r"http.*bit\.ly.*airtel"
    ]
    
    message_lower = message.lower()
    for pattern in scam_patterns:
        if re.search(pattern, message_lower):
            return {"status": "SCAM", "confidence": 95, "advice": "Do NOT click! Delete & block."}
    
    return {"status": "SAFE", "confidence": 90, "advice": "Message looks legit."}

Example usage
test_sms = "You received K5000 from Airtel Money. Click http://bit.ly/airtel-claim to collect"
result = detect_fraud(test_sms)
print(f"Result: {result}")

WhatsApp integration with Meta Llama 3 AI (coming next)
TODO: Connect to WhatsApp Business API
