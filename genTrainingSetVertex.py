# genTrainingSet.py
from datatypes import LifestyleQuestionare, LifestyleQuestionareFromDataset, formatInputPrompt

f = open("dataset/dementia_patients_health_data.csv","r")
o = open("dataset/genOut.jsonl","w")



line = f.readline()
line = f.readline()

while line != "":
    content = line.split(",")

    ## original dataset parsing
    Diabetic = 'true' if (content[0] == '1') else 'false'
    AlcoholLevel = content[1]
    HeartRate = content[2]
    BloodOxygenLevel = content[3]
    BodyTemperature = content[4]
    Weight = content[5]
    MRI_Delay = content[6]
    Presecription = content[7]
    if Presecription == "" : Presecription = "None"
    DosageMg = content[8]
    if DosageMg == '' : DosageMg = '0'
    Age = content[9]
    EducationLevel = content[10]
    DominantHand = content[11]
    Gender = content[12]
    FamilyHistory = 'true' if (content[13] == 'Yes') else 'false'
    SmokingStatus = content[14]
    APOE_e19 = 'true' if (content[0] == 'Positive') else 'false'
    PhysicalActivity = content[16]
    DepressionStatus = 'true' if (content[17] == 'Yes') else 'false'
    MedicationHistory = 'true' if (content[19] == 'Yes') else 'false'
    NutritionDiet = content[20]
    SleepQuality = content[21]
    ChronicHealthConditions = content[22]

    Dementia = content[-1].strip()
    contentStr = "Diabetic:"+Diabetic+",AlcoholLevel:"+AlcoholLevel+", HeartRate:"+HeartRate+", BloodOxygenLevel:"+BloodOxygenLevel+", BodyTemperature:"+BodyTemperature+", Weight:"+Weight+", MRI_Delay:"+MRI_Delay+", Presecription:"+Presecription+", DosageMg:"+DosageMg+", Age:"+Age+", EducationLevel:"+EducationLevel+", DominantHand:"+DominantHand+", Gender:"+Gender+", FamilyHistory:"+FamilyHistory+", SmokingStatus:"+SmokingStatus+", APOE_e19:"+APOE_e19+", PhysicalActivity:"+PhysicalActivity+", DepressionStatus:"+DepressionStatus+", MedicationHistory:"+MedicationHistory+", NutritionDiet:"+NutritionDiet+", SleepQuality:"+SleepQuality+", ChronicHealthConditions"+ChronicHealthConditions
    ## original end



    x = LifestyleQuestionareFromDataset(content)
    contentStr2 = formatInputPrompt(x)

    if contentStr != contentStr2 : raise ValueError()
    if Dementia != x.Dementia : raise ValueError()

    outLine = '{"contents":[{"role":"user","parts":[{"text":"'+contentStr+'"}]},{"role":"model","parts":[{"text":"'+Dementia+'"}]}]}\n'
    o.write(outLine)

    line = f.readline()


f.close()
o.close()
