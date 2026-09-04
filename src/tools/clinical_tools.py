from src.database.database import ClinicalDatabase


def get_patient_information(patient_id: int):
    """
    Tool to retrieve basic information about a patient.
    Uses synthetic demo data only.
    """

    database = ClinicalDatabase()
    database.initialize()

    patient = database.get_patient_by_id(patient_id)

    if not patient:
        return {
            "status": "not_found",
            "message": "Patient not found."
        }

    return {
        "status": "success",
        "patient_id": patient[0],
        "age": patient[1],
        "sex": patient[2]
    }


def get_patient_lab_results(patient_id: int):
    """
    Tool to retrieve laboratory results for a patient.
    Uses synthetic demo data only.
    """

    database = ClinicalDatabase()
    database.initialize()

    results = database.get_recent_lab_results(patient_id)

    return {
        "status": "success",
        "patient_id": patient_id,
        "results": [
            {
                "test_name": result[0],
                "value": result[1],
                "unit": result[2],
                "date": result[3]
            }
            for result in results
        ]
    }