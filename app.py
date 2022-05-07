from fastapi import FastAPI, Request
import uvicorn
import logging
import subprocess
# import os

# print(os.getcwd())
subprocess.call(['sh', './download.sh'], shell=True)

from autocorrection.correct import AutoCorrection
from config.config import get_config

config_app = get_config()

logging.basicConfig(filename=config_app['log']['app'],
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

description = """
# Vietnamese Spelling Correction
"""

app = FastAPI(
    title="Spell Correction",
    description=description,
    version="0.0.1"
)

autocorrection = AutoCorrection()


# def run_setup():
    


@app.post("/correct")
async def correct_sentence(request: Request):
    data = await request.json()
    data = dict(data)
    sent = data["text"]
    corrected = autocorrection.correction(sent)
    try:
        corrected = autocorrection.correction(sent)
    except Exception as e:
        corrected = sent
        logging.warning(e)
        
    return {
        "result": {
            "text": corrected,
        }
    }

if __name__ == "__main__":
    # run_setup()
    uvicorn.run(app, host="0.0.0.0", port=8000)
# if __name__ == "__main__":  
    # uvicorn.run(
    #     app, 
    #     host=config_app['server']['ip_address'], 
    #     port=config_app['server']['port']
    # )
    # uvicorn.run(app, host="0.0.0.0", port=8080)