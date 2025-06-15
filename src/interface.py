"""
Simple CLI interface to run the full pipeline.
"""

from input_simulator import get_thought_input, save_thoughts
from llm_analyzer import analyze_thoughts
from feedback_engine import generate_feedback

def main():
    thoughts = get_thought_input()
    save_thoughts(thoughts)

    analysis = analyze_thoughts(thoughts)
    feedback = generate_feedback(analysis)

    print("\n--- Analysis Results ---")
    for item in analysis:
        print(item)

    print("\n--- Feedback Suggestions ---")
    for item in feedback:
        print(item)

if __name__ == "__main__":
    main()
