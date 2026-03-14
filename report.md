# Clinical AI Evaluation

This project evaluates the reliability of a clinical NLP pipeline that extracts entities from OCR-based medical charts.

## Metrics

- Entity Type Error Rate
- Assertion Error Rate
- Temporality Error Rate
- Subject Error Rate
- Event Date Accuracy
- Attribute Completeness

## Observations

Common issues observed:

- Some entities missing attributes
- Temporality classification inconsistent
- Family history occasionally attributed to patient

## Improvements

Possible reliability guardrails:

- Schema validation
- Temporal consistency checks
- LLM verification layer
