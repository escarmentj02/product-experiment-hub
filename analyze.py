import argparse
import math


def analyze(control_conversions, control_visitors, treatment_conversions, treatment_visitors):
    p1 = control_conversions / control_visitors
    p2 = treatment_conversions / treatment_visitors
    pooled = (control_conversions + treatment_conversions) / (control_visitors + treatment_visitors)
    standard_error = math.sqrt(pooled * (1 - pooled) * (1 / control_visitors + 1 / treatment_visitors))
    z_score = (p2 - p1) / standard_error if standard_error else 0
    return {"control_rate": round(p1, 4), "treatment_rate": round(p2, 4), "absolute_lift": round(p2 - p1, 4), "relative_lift": round((p2 - p1) / p1, 4), "z_score": round(z_score, 3), "decision_hint": "investigate further" if abs(z_score) < 1.96 else "statistically distinguishable"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--control-conversions", type=int, required=True)
    parser.add_argument("--control-visitors", type=int, required=True)
    parser.add_argument("--treatment-conversions", type=int, required=True)
    parser.add_argument("--treatment-visitors", type=int, required=True)
    args = parser.parse_args()
    print(analyze(**vars(args)))
