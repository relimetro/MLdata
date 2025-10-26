# Datatypes.py

class LifestyleQuestionare:
    def __init__(self,*,Diabetic,AlcoholLevel,HeartRate,BloodOxygenLevel,BodyTemperature,Weight,MRI_Delay,Presecription,DosageMg,Age,EducationLevel,DominantHand,Gender,FamilyHistory,SmokingStatus,APOE_e19,PhysicalActivity,DepressionStatus,MedicationHistory,NutritionDiet,SleepQuality,ChronicHealthConditions,Dementia):
        ## TODO, perform input validation / store as not string

        # all store as string for now
        self.Diabetic = Diabetic # true/flase
        self.AlcoholLevel = AlcoholLevel # float
        self.HeartRate = HeartRate # int
        self.BloodOxygenLevel = BloodOxygenLevel # float
        self.BodyTemperature = BodyTemperature # float
        self.Weight = Weight # float
        self.MRI_Delay = MRI_Delay # float
        self.Presecription = Presecription # string | "None"
        self.DosageMg = DosageMg # int | 0
        self.Age = Age # int
        self.EducationLevel = EducationLevel  # No School,Primary School,Secondary School,Deploma/Degree
        self.DominantHand = DominantHand  # Left,Right
        self.Gender = Gender # Male,Female
        self.FamilyHistory = FamilyHistory # true/false
        self.SmokingStatus = SmokingStatus # Current Smoker,Former Smoker,Never Smoked
        self.APOE_e19 = APOE_e19 # true/false
        self.PhysicalActivity = PhysicalActivity # Sedentary,Moderate Activity,Mild Activity
        self.DepressionStatus = DepressionStatus # true/false
        self.MedicationHistory = MedicationHistory # true/false
        self.NutritionDiet = NutritionDiet # Low-Carb Diet,Mediterranean Diet,Balanced Diet
        self.SleepQuality = SleepQuality # Poor,Good
        self.ChronicHealthConditions = ChronicHealthConditions # Diabetes,Hearth Disease,Hypertension,None
        self.Dementia = Dementia # 1|0

def LifestyleQuestionareFromDataset(content):
    ret = LifestyleQuestionare(
        Diabetic = 'true' if (content[0] == '1') else 'false',
        AlcoholLevel = content[1],
        HeartRate = content[2],
        BloodOxygenLevel = content[3],
        BodyTemperature = content[4],
        Weight = content[5],
        MRI_Delay = content[6],
        Presecription = "None" if content[7] == "" else content[7],
        DosageMg = "0" if content[8] == "" else content[8],
        Age = content[9],
        EducationLevel = content[10],
        DominantHand = content[11],
        Gender = content[12],
        FamilyHistory = 'true' if (content[13] == 'Yes') else 'false',
        SmokingStatus = content[14],
        APOE_e19 = 'true' if (content[0] == 'Positive') else 'false',
        PhysicalActivity = content[16],
        DepressionStatus = 'true' if (content[17] == 'Yes') else 'false',
        MedicationHistory = 'true' if (content[19] == 'Yes') else 'false',
        NutritionDiet = content[20],
        SleepQuality = content[21],
        ChronicHealthConditions = content[22],
        Dementia = content[-1].strip()
    )
    return ret



def formatInputPrompt(x:LifestyleQuestionare) -> str:
    return "Diabetic:"+x.Diabetic+",AlcoholLevel:"+x.AlcoholLevel+", HeartRate:"+x.HeartRate+", BloodOxygenLevel:"+x.BloodOxygenLevel+", BodyTemperature:"+x.BodyTemperature+", Weight:"+x.Weight+", MRI_Delay:"+x.MRI_Delay+", Presecription:"+x.Presecription+", DosageMg:"+x.DosageMg+", Age:"+x.Age+", EducationLevel:"+x.EducationLevel+", DominantHand:"+x.DominantHand+", Gender:"+x.Gender+", FamilyHistory:"+x.FamilyHistory+", SmokingStatus:"+x.SmokingStatus+", APOE_e19:"+x.APOE_e19+", PhysicalActivity:"+x.PhysicalActivity+", DepressionStatus:"+x.DepressionStatus+", MedicationHistory:"+x.MedicationHistory+", NutritionDiet:"+x.NutritionDiet+", SleepQuality:"+x.SleepQuality+", ChronicHealthConditions"+x.ChronicHealthConditions



