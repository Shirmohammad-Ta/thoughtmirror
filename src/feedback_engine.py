"""
Generates cognitive-behavioral suggestions based on LLM analysis.
"""

def generate_feedback(analysis_results):
    feedback = []
    for result in analysis_results:
        feedback.append({
            "thought": result["original"],
            "suggestion": "Try reframing this thought positively."
        })
    return feedback
