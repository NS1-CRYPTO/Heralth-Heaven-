# Minimal FastAPI server for ClinicAssist demo
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import uvicorn
from agent import ClinicAgent

app = FastAPI(title="ClinicAssist (gpt-oss local demo)")
agent = ClinicAgent()

class TextCase(BaseModel):
    patient_age: int
    patient_sex: str
    presenting_complaint: str
    vitals: dict = {}

@app.post('/triage/text')
async def triage_text(case: TextCase):
    result = agent.triage_from_text(case.dict())
    return {"result": result}

@app.post('/triage/photo')
async def triage_photo(patient_age: int, patient_sex: str, presenting_complaint: str, photo: UploadFile = File(...)):
    image_bytes = await photo.read()
    result = agent.triage_with_image({
        "patient_age": patient_age,
        "patient_sex": patient_sex,
        "presenting_complaint": presenting_complaint,
        "image_bytes": image_bytes
    })
    return {"result": result}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
