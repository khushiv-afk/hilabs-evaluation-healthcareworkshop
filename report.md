# HiLabs Clinical AI Evaluation Report

## Project Overview

This project evaluates the reliability of a clinical AI pipeline that extracts medical entities from OCR-processed clinical charts.

The evaluation framework measures error rates across multiple reasoning dimensions.

---

## Dataset

The dataset contains 30 medical charts.

Each chart includes:

- OCR text (.md)
- Extracted clinical entities (.json)

---

## Evaluation Metrics

The following metrics were computed:

- Entity type error rate
- Assertion error rate
- Temporality error rate
- Subject attribution error rate
- Event date accuracy
- Attribute completeness

---

## Observed Weaknesses

During analysis several weaknesses were observed:

- Vital signs sometimes misclassified as tests
- Family history occasionally attributed to patient
- Past procedures sometimes labeled as current events
- Missing attributes in some entities

---

## Error Heatmap

| Error Type | Severity |
|------------|---------|
| Entity Type | Medium |
| Assertion | Low |
| Temporality | High |
| Subject | Medium |

---

## Proposed Guardrails

To improve reliability:

1. Add rule-based validation layer
2. Implement temporal consistency checks
3. Use LLM verification layer
4. Apply strict schema validation

---

## Conclusion

Evaluation frameworks like this are critical for improving the reliability and safety of clinical AI systems before deployment.
