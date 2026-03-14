import json
import sys
import os

valid_types = [
"MEDICINE","PROBLEM","PROCEDURE","TEST","VITAL_NAME",
"IMMUNIZATION","MEDICAL_DEVICE","MENTAL_STATUS",
"SDOH","SOCIAL_HISTORY"
]

valid_assertions = ["POSITIVE","NEGATIVE","UNCERTAIN"]

valid_temporality = [
"CURRENT","CLINICAL_HISTORY","UPCOMING","UNCERTAIN"
]

valid_subject = ["PATIENT","FAMILY_MEMBER"]


def evaluate(input_file, output_file):

    with open(input_file) as f:
        data = json.load(f)

    entities = data.get("entities", [])
    total = len(entities)

    entity_errors = 0
    assertion_errors = 0
    temporality_errors = 0
    subject_errors = 0
    date_correct = 0
    complete_entities = 0

    for e in entities:

        required = ["type","assertion","temporality","subject"]

        if all(attr in e for attr in required):
            complete_entities += 1

        if e.get("type") not in valid_types:
            entity_errors += 1

        if e.get("assertion") not in valid_assertions:
            assertion_errors += 1

        if e.get("temporality") not in valid_temporality:
            temporality_errors += 1

        if e.get("subject") not in valid_subject:
            subject_errors += 1

        if "date" in e and e["date"]:
            date_correct += 1


    result = {

        "file_name": os.path.basename(input_file),

        "entity_type_error_rate": entity_errors/total,

        "assertion_error_rate": assertion_errors/total,

        "temporality_error_rate": temporality_errors/total,

        "subject_error_rate": subject_errors/total,

        "event_date_accuracy": date_correct/total,

        "attribute_completeness": complete_entities/total
    }

    with open(output_file,"w") as f:
        json.dump(result,f,indent=4)


if __name__ == "__main__":

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    evaluate(input_file,output_file)
