
import glob
import os

down_path = r"c:\Users\bocek\OneDrive - QCM, s.r.o\codes\python_projects\SUKL_UI_Tests\src\resources\downloads"
jsons = sorted(glob.glob(f"{down_path}\\*.json"), key=os.path.getctime)
[print(x) for x in jsons]