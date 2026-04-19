from services.link_checker import check_links
def analyze_email(email: str):
    email = email.lower()
    suspicious_keywords = ["urgent", "win", "free", "click here", "password", "bank", "verify"]
    score = 0
    reasons = []

    for word in suspicious_keywords:
        if word in email:
            score += 1
            reasons.append(f"contains '{word}'")

    link_data=check_links(email)

    if link_data["total_links"]>0:
        score+=1
        reasons.append("contains link ")

    if len(link_data["suspicious_links"])>0:
        score+=2
        reasons.append("suspicious link detected")

    if score>=3:
        result="phishing "
    else:
        result="safe"


    return {
        "result": result,
        "score": score,
        "reasons": reasons,
        "links": link_data
    }

