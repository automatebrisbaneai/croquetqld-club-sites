"""
Committee review runner — 5 AI committee members review a club website.
Usage: python run-committee-review.py <html_file> <round_number> <output_file>

Models (verified 2026-03-28):
  Barb/Denise: x-ai/grok-4.20-beta
  Kevin/Graham: google/gemini-3.1-pro-preview
  Sandra: minimax/minimax-m2.5:free
"""
import sys, json, re, urllib.request, concurrent.futures
from datetime import date

OPENROUTER_KEY = "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"
CLUB = "Headland-Buderim Croquet Club"
REFERENCE_URL = "https://tenbinlabs.xyz"
BRIEF = """We'd love something sophisticated and modern. Tenbinlabs has that dark, clean feel that seems premium and serious. Our club has been around a long time and we're proud of our competitive players. We want something that feels like we mean business, but still welcoming.

Submitter: Jan Whitfield (Secretary)
Reference site: https://tenbinlabs.xyz
Style description: Dark, clean, institutional minimalism. Deep black background, white type, lavender/purple accent colours. The site should feel premium and serious while still being welcoming to new players."""

COMMITTEE = [
    {
        "name": "Barb",
        "role": "President",
        "model": "x-ai/grok-4.20-beta",
        "temperature": 0.4,
        "system": f"""You are Barb, 62, President of {CLUB}. You pushed hard to get this website built. You submitted a link to {REFERENCE_URL} because you liked its dark, premium feel — it looks like a serious organisation, not a hobby club. You are direct, sometimes blunt, and you care about first impressions.

You review websites the way you'd walk into a venue: what do you see first, what do you see second, is the flow logical. You will always demand at least one structural change — a section moved, merged, or reordered. You are willing to say "start over" if the structure is fundamentally wrong.

The original submission brief was: {BRIEF}

Do not pad your feedback. If something works, say so and move on. If it doesn't, say exactly where and what to change. Be specific about locations (e.g. "the schedule section needs to move above the about section"). Score 1-10 at the end."""
    },
    {
        "name": "Kevin",
        "role": "Treasurer",
        "model": "google/gemini-3.1-pro-preview",
        "temperature": 0.5,
        "system": f"""You are Kevin, 55, Treasurer of {CLUB}. Former graphic designer (15 years). You have strong opinions about visual consistency.

The committee submitted {REFERENCE_URL} as the style they wanted. You will compare what was built against that reference. You notice colour weight, spacing inconsistency, font weight mismatches, and effects that weren't asked for. You believe restraint is sophistication.

The original submission brief was: {BRIEF}

Be precise: "the heading font weight is too heavy — the reference uses 400 weight Syne with tight letter spacing" not "the font feels off." Always demand at least one specific visual correction. If the CSS doesn't match what was extracted from the reference, say so explicitly. Score 1-10 at the end."""
    },
    {
        "name": "Denise",
        "role": "New Member",
        "model": "x-ai/grok-4.20-beta",
        "temperature": 0.5,
        "system": f"""You are Denise, 41, who joined {CLUB} 4 months ago. You use your phone for everything and you remember clearly what it felt like to be an outsider to croquet.

You look at this website on your phone first. Your one question: "If I knew nothing about croquet, would this tell me how to turn up and play?" You are sensitive to jargon. The call-to-action must be visible without scrolling on mobile.

The original submission brief was: {BRIEF}

Always demand at least one usability or copy change. If the phone number isn't clickable (must be a tel: link), say so. If "come and try" is buried, say so. If the first session being free isn't obvious from the hero, say so. Score 1-10 at the end."""
    },
    {
        "name": "Graham",
        "role": "Visitor from another club",
        "model": "google/gemini-3.1-pro-preview",
        "temperature": 0.4,
        "system": f"""You are Graham, 58, a competitive player from another club 40 minutes away. You're checking out {CLUB}'s new website to see if it's worth the drive for Tuesday games.

You need: when are the games, what croquet code (GC/AC/WC/Golf), visiting fee, who to call. You've seen 6 club websites this month and you can tell in 30 seconds if a site was built with care or knocked together. Missing photos of courts means you're suspicious. Hollow claims like "vibrant community" mean nothing without evidence.

The original submission brief was: {BRIEF}

Always demand at least one content addition — a missing practical detail, a hollow claim that needs backing, a photo that should be there. Score 1-10 at the end."""
    },
    {
        "name": "Sandra",
        "role": "Contrarian committee member",
        "model": "minimax/minimax-m2.5:free",
        "temperature": 0.7,
        "system": f"""You are Sandra, 67, on the {CLUB} committee for 11 years. You didn't want to redesign the website and you've been grudging about this whole process. You thought the old website was fine.

You are not hostile — you care about the club — but you're hard to satisfy. If everyone else will like something, you find fault. If the reference style was delivered perfectly, you're now not sure it was the right style to begin with.

The original submission brief was: {BRIEF}

From Round 2 onwards you must explicitly reference what other members said and disagree with at least one of them. You're the most likely to say "start over." Always demand at least one specific change. Score 1-10 at the end."""
    }
]


def call_reviewer(member, html, round_num, prior_feedback=None):
    url = "https://openrouter.ai/api/v1/chat/completions"

    user_content = f"Here is the {CLUB} website (Round {round_num} review):\n\n{html}\n\n"
    if prior_feedback and round_num > 1:
        user_content += f"Last round feedback summary from the committee:\n{prior_feedback}\n\n"
    user_content += "Please review and rate 1-10. What works? What specifically needs changing? State your demands clearly."

    payload = json.dumps({
        "model": member["model"],
        "temperature": member["temperature"],
        "messages": [
            {"role": "system", "content": member["system"]},
            {"role": "user", "content": user_content}
        ],
        "max_tokens": 1500
    }).encode()

    req = urllib.request.Request(url, data=payload, method='POST')
    req.add_header('Authorization', f'Bearer {OPENROUTER_KEY}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('HTTP-Referer', 'https://croquetclaude.com')
    req.add_header('X-Title', 'CroquetClaude Committee Review')

    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read())

    return data['choices'][0]['message']['content']


def extract_score(text):
    # Look for patterns like "7/10", "Score: 8", "Rating: 9/10"
    patterns = [
        r'(?:score|rating|rate|i.?d give it|give this)[:\s]+(\d+)\s*(?:/\s*10)?',
        r'\b(\d+)\s*/\s*10\b',
        r'\b(\d+)\s*out of\s*10\b',
    ]
    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            score = int(matches[-1])  # Take last score mentioned
            if 1 <= score <= 10:
                return score
    return None


def main():
    html_file = sys.argv[1] if len(sys.argv) > 1 else r"C:\croquet-os\apps\club-sites\example3\index.html"
    round_num = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    output_file = sys.argv[3] if len(sys.argv) > 3 else fr"C:\croquet-os\apps\club-sites\example3\review-round{round_num}.md"
    prior_file = sys.argv[4] if len(sys.argv) > 4 else None

    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    prior_feedback = None
    if prior_file:
        with open(prior_file, 'r', encoding='utf-8') as f:
            prior_feedback = f.read()

    print(f"Running Round {round_num} committee review ({len(COMMITTEE)} members)...")
    print(f"HTML: {len(html)} chars")
    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = {
            executor.submit(call_reviewer, m, html, round_num, prior_feedback): m["name"]
            for m in COMMITTEE
        }
        for future in concurrent.futures.as_completed(futures):
            name = futures[future]
            try:
                results[name] = future.result()
                score = extract_score(results[name])
                print(f"  OK {name}: {score}/10" if score else f"  OK {name}: (no score found)")
            except Exception as e:
                results[name] = f"ERROR: {e}"
                print(f"  FAIL {name}: {e}")

    today = date.today().isoformat()
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"""---
author: ai
type: resource
status: active
created: {today}
description: "Committee review Round {round_num} — example3 ({CLUB}, ref: tenbinlabs.xyz)"
---

# Committee Review — Round {round_num}

**Club:** {CLUB}
**Reference:** {REFERENCE_URL}
**Date:** {today}

---

""")
        scores = {}
        for m in COMMITTEE:
            name = m["name"]
            role = m["role"]
            text = results.get(name, "No response")
            score = extract_score(text)
            scores[name] = score
            f.write(f"## {name} ({role})\n\n")
            f.write(text + "\n\n---\n\n")

        # Score summary
        valid_scores = [s for s in scores.values() if s is not None]
        avg = sum(valid_scores) / len(valid_scores) if valid_scores else 0
        f.write("## Score Summary\n\n")
        for m in COMMITTEE:
            name = m["name"]
            s = scores.get(name)
            f.write(f"- **{name}** ({m['role']}): {s}/10\n" if s else f"- **{name}** ({m['role']}): ?\n")
        f.write(f"\n**Average: {avg:.1f}/10**\n")
        all_8_plus = all(s is not None and s >= 8 for s in scores.values())
        f.write(f"\n**Pass (all 8+):** {'YES' if all_8_plus else 'NO'}\n")

    print(f"\nSaved to: {output_file}")
    print("\n--- SCORE SUMMARY ---")
    for m in COMMITTEE:
        name = m["name"]
        s = scores.get(name)
        print(f"  {name}: {s}/10" if s else f"  {name}: ?")
    if valid_scores:
        print(f"  Average: {avg:.1f}/10")
        print(f"  Pass: {'YES' if all_8_plus else 'NO'}")


if __name__ == "__main__":
    main()
