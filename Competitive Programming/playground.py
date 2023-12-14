def maskPII(s: str) -> str:
    if "@" in s:
        email = s.split("@")

        email[0] = email[0].lower()
        email[1] = email[1].lower()

        email[0] = email[0][0] + "*****" + email[0][-1]

        email = "@".join(email)

        return email
    else:
        separationChars = ["+", "-", "(", ")", " "]
        phone = s

        for char in separationChars:
            phone = phone.replace(char, "")

        phone = (
            f"***-***-{phone[6:]}"
            if len(phone) == 10
            else f"+*-***-***-{phone[7:]}"
            if len(phone) == 11
            else f"+**-***-***-{phone[8:]}"
            if len(phone) == 12
            else f"+***-***-***-{phone[9:]}"
        )

        return phone


words = ["+1(234)567-890", "+38(068)00-77-147", "+132(758)61-73-222"]

for word in words:
    res = maskPII(word)
    print(f"{res}\n")
