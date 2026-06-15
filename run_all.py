"""
run_all.py

Purpose:
    Run the full evaluation pipeline from scratch in correct order.
    This script exists to prove reproducibility — every result in the
    research memo can be regenerated from raw prompts and API calls.

Rationale:
    A research pipeline is only credible if someone else can run it.
    This script is the single entry point for the entire project.

Usage:
    python run_all.py

Order:
    1. Pipeline: call Claude + GPT on all 40 prompts
    2. Analysis: compute safety/empathy/scope statistics
    3. LLM judge: auto-score all responses
    4. Reliability: compute Cohen's Kappa
    5. Matched pairs: language effect analysis
    6. Multi-turn: escalating conversation pilot

Note:
    Running this script will make API calls and incur costs.
    Estimated cost: ~$0.50 USD at current API rates.
"""

import subprocess
import sys
import os

def run_script(script_name, description):
    """
    Run a single script and report success or failure.
    Rationale: isolate each step so failures are easy to diagnose.
    """
    print(f"\n{'='*60}")
    print(f"Running: {script_name}")
    print(f"Purpose: {description}")
    print(f"{'='*60}")

    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True
    )

    if result.returncode == 0:
        print(f"SUCCESS: {script_name}")
        if result.stdout:
            print(result.stdout[-500:])  # last 500 chars to avoid flooding
    else:
        print(f"FAILED: {script_name}")
        print(result.stderr[-500:])
        return False

    return True


def main():
    print("="*60)
    print("CAI Mental Health Evaluation — Full Pipeline")
    print("Repository: github.com/doctorparksparks/cai-mental-health-eval")
    print("="*60)

    # Check .env exists
    if not os.path.exists(".env"):
        print("\nERROR: .env file not found.")
        print("Copy .env.example to .env and add your API keys.")
        print("  cp .env.example .env")
        sys.exit(1)

    steps = [
        ("day08_pipeline_2models.py",
         "Call Claude + GPT on all 40 prompts → day08_responses_2models.csv"),

        ("day08_analysis.py",
         "Compute safety/empathy/scope statistics → charts/"),

        ("day08_llm_judge.py",
         "Auto-score all responses using LLM-as-judge → day08_llm_judge.csv"),

        ("day08_reliability.py",
         "Compute Cohen's Kappa inter-rater reliability"),

        ("day08_matched_pair_analysis.py",
         "Analyse language effects via matched pairs → day08_matched_pairs.csv"),

        ("day09_failure_extractor.py",
         "Extract and summarise clinical failure cases"),

        ("day10_multiturn_pilot.py",
         "Run multi-turn escalation scenarios → day10_multiturn_results.csv"),
    ]

    results = []
    for script, description in steps:
        success = run_script(script, description)
        results.append((script, success))

    # Summary
    print(f"\n{'='*60}")
    print("PIPELINE SUMMARY")
    print(f"{'='*60}")
    for script, success in results:
        status = "✓" if success else "✗"
        print(f"  {status} {script}")

    passed = sum(1 for _, s in results if s)
    print(f"\n{passed}/{len(steps)} steps completed successfully.")

    if passed == len(steps):
        print("\nAll steps passed. Results are reproducible.")
    else:
        print("\nSome steps failed. Check error messages above.")


if __name__ == "__main__":
    main()