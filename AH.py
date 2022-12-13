#Author:Ang Xie,Iza Lumpio,Yushu Li

#This is a class for doctors
class Doctor:
    
    def __init__(self):
        pass
        
    def formatDrInfo(self,doctor_list):
        #Formats each doctor’s information (properties) in the same format used in the .txt file 
        format_doctor=''
        for doctor in doctor_list:
            doctor=doctor[0]+'_'+doctor[1]+'_'+doctor[2]+'_'+doctor[3]+'_'+doctor[4]+'_'+doctor[5]+'\n'
            format_doctor+=doctor
        return format_doctor
        
    def readDoctorsFile(self):
        #Reads from “doctors.txt” file and fills the doctor objects in a list
        doctor_list=[]
        with open ('doctors.txt','r') as rf:
            for row in rf:
                row = row.rstrip('\n')
                row=row.split('_')
                doctor_list.append(row)
        return doctor_list
    
    def addDrToFile(self,doctor_list):
        # Writes new doctors to the doctors list.
        self.id=input('Enter the doctor’s ID:\n')
        self.name=input('Enter the doctor’s name:\n')
        self.speciality=input('Enter the doctor’s specility:\n')
        self.timing=input('Enter the doctor’s timing (e.g., 7am-10pm):\n')
        self.qualification=input('Enter the doctor’s qualification:\n')
        self.room_number=input('Enter the doctor’s room number:\n')
        new_doctor=[self.id,self.name,self.speciality,self.timing,self.qualification,self.room_number]
        doctor_list.append(new_doctor)
        return doctor_list
    
    def writeListOfDoctorsToFile(self,format_doctor):
        # Writes the list of doctors to the doctors.txt file after formatting it correctly
        with open('doctors.txt','w') as wf:
            wf.write(format_doctor)
        pass
    
    
    def searchDoctorById(self,doctor_list):
        #Searches whether the doctor is in the list of doctors/file using the doctor ID that the user enters
        id= input('\nEnter the doctor’s ID:\n')
        for doctor in doctor_list:
            if id == doctor[0]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("\nCan't find the doctor with the same ID on the system")
        return False
    
    def searchDoctorByName(self,doctor_list):
        #Searches whether the doctor is in the list of doctors/file using the doctor name that the user enters
        name=input('\nEnter the doctor’s name:\n\n')
        for doctor in doctor_list:
            if name == doctor[1]:
                print('\nId'.ljust(15),'Name'.ljust(15),'Speciality'.ljust(15),'Timing'.ljust(15),'Qualification'.ljust(15),'Room Number\n'.ljust(15))
                print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
                return doctor
        print("\nCan't find the doctor with the same name on the system\n")
        return False
        
    def editDoctorInfo(self,doctor_list):
        #Asks the user to enter the ID of the doctor to change their information, and then the user can enter the new doctor information
        id= input('\nPlease enter the id of the doctor that you want to edit their information:\n\n')
        for doctor in doctor_list:
            if id == doctor[0]:
                doctor[1]=input('Enter new Name: \n')
                doctor[2]=input('Enter new Specilist in:\n')
                doctor[3]=input('Enter new Timing: (e.g., 7am-10pm):\n')
                doctor[4]=input('Enter new Qualification: \n')
                doctor[5]=input('Enter new Room number: \n')
                index=doctor_list.index(doctor)
                doctor_list[index]=doctor
                return doctor_list
        print("Can't find the doctor with the same ID on the system")
        pass
    
    def displayDoctorsList(self,doctor_list):
        #Displays doctor information on different lines
        for doctor in doctor_list:
            print(doctor[0].ljust(15),doctor[1].ljust(15),doctor[2].ljust(15),doctor[3].ljust(15),doctor[4].ljust(15),doctor[5].ljust(15))
        pass
        

class facility():
    def __init__(self):
        self.txt=[]
        with open("facilities.txt", "r") as file:
            lines=file.readlines()
            for line in lines:
                self.txt.append(line.split("\n")[0])

    def addFacility(self,name):
        #Adds and writes the facility name to the list
        self.txt.append(name)


    def displayFacilities(self):
        #Displays the list of facilities
        for name in self.txt:
            print(name)
        print('\nBack to the prevoius Menu\n')    
            

    def writeListOffacilitiesToFile(self):
        #Writes the facilities list to facilities.txt
        with open("facilities.txt", "w") as file:
            for name in self.txt:
                file.write(name+"\n")

"""
Patient class with properties:
- pid: patient id
- name: patient's name
- disease: patient's disease
- gender: paatient's gender
- age: patient's age
Patient class' methods:
- formatPatientInfo: formats patient's information to be added to the file
- enterPatientInfo: Asks user to enter the patient info
- readPatientsFile: reads from file patients.txt
- searchPatientById: Searches for a patient using their id
- displayPatientInfo:Displays patient info
- editPatientInfo:asks the user to edit patient information
- displayPatientsList: displays the list of patients
- writeListOfPatientsToFile: writes a list of patients into the patients.txt file
- addPatientToFile: Adds a new patient to the file
"""
class Patient:
    def __init__(self,pid,name,disease,gender,age):
        self.pid =pid
        self.name=name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    def formatPatientInfo(self): 
        return "%s_%s_%s_%s_%s"%(self.pid,self.name,self.disease,self.gender,self.age)
    
    def enterPatientInfo(self): 
        self.pid = input("Enter the patient ID: \n")
        self.name = input("Enter the patient's name: \n")
        self.disease = input("Enter the patient's disease: \n")
        self.gender = input("Enter the patient's gender: \n")
        self.age = input("Enter the patient's age: \n")
    
    def readPatientsFile(self): 
        file = open("patients.txt","r")
        patient_file = file.readlines() #a list of strings
        for i in patient_file:
            patient_file[patient_file.index(i)] = i.strip("\n")
        file.close()
        return patient_file
    
    # use substrings for searching the id
    def searchPatientById(self): 
        search_id = input("Enter the patient id you want to search: \n")
        patientsInfo_list = self.readPatientsFile()
        #counter for how much is found
        found = 0
        # a list for patients info found
        patients_found = []
        for each_string in patientsInfo_list:
            if search_id == each_string[:len(search_id)]:
                found += 1
                patients_found.append(each_string)
        
        if found <1:
            print("The patient ID entered is not found.")
        else:
            print("The following patient(s) are/is found:")
            for each_item in patients_found:
                print(each_item.replace("_","\t"))

          
    def displayPatientInfo(self):
            print(self.formatPatientInfo.replace("_","\t"))
    
    def editPatientInfo(self):
        search_id = input("Please enter the id of the patient that you want to edit their information: \n")
        patient_list = self.readPatientsFile()
        list_of_patient_list = []
        for each_string in patient_list:
            if search_id ==each_string[:len(search_id)]:
                sublist = each_string.split("_")
                sublist[1] = input("Enter the patient's new name: \n")
                sublist[2]= input("Enter the patient's new disease: \n")
                sublist[3]= input("Enter the patient's new gender: \n")
                sublist[4]= input("Enter the patient's new age: \n")
                list_of_patient_list.append(sublist)
            else:
                sublist = each_string.split("_")
                list_of_patient_list.append(sublist)
        
        #make new file with new info
        file = open("patients.txt","w")
        for each_sublist in list_of_patient_list:
            file = open("patients.txt","a")
            file.write("%s_%s_%s_%s_%s"%(each_sublist[0],each_sublist[1],each_sublist[2],each_sublist[3],each_sublist[4]) + "\n")
            file.close()
    
    def displayPatientsList(self):
        patient_file = self.readPatientsFile()
        for each_list in patient_file:
            print(each_list.replace("_","\t"))
    
    def writeListOfPatientsToFile(self,list_of_patients):
        file = open("patients.txt","a")
        for each_patient in list_of_patients:
            file.write("\n" + each_patient.formatPatientInfo())
            each_patient.formatPatientInfo()
    
    def addPatientToFile(self):
        self.enterPatientInfo()
        file = open("patients.txt","a")
        file.write("\n"+self.formatPatientInfo())
        file.close


"""
Laboratory Class with properties:
lab_name and lab_cost

Methods:
addLabtoFile - adds a Laboratory object into te lab txt file
writeListOfLabsToFile - writes a list of lab objects to the lab file
displayLabsList - displays the list of lab names in lab file
formatDrInfo - formats the current lab object attributes
enterLaboratoryInfo - asks user to enter lab name and cost
readLaboratoriesFile - reads the lab txt file and uses its 
creates a lab object with each corresdponding attribute and put in a list
"""
class Laboratory:
    def __init__(self,name,cost):
        self.lab_name = name
        self.lab_cost = cost

    def addLabToFile(self):
        self.enterLaboratoryInfo()
        lab_file = open("laboratories.txt","a")
        lab_file.write(self.formatLabInfo()+"\n")
        lab_file.close()

    def writeListOfLabsToFile(self,list_of_labs):
        lab_file = open("laboratories.txt","a")
        for each_lab in list_of_labs:
            lab_file.write("\n" + each_lab.formatLabInfo())
            

    def displayLabsList(self):
        lab_file = open("laboratories.txt","r")
        lab_list = []

        for each_line in lab_file:
            new_list = each_line.split("_")
            lab_list.append([new_list[0],new_list[1].strip()])
        lab_file.close()
        
        for i in lab_list:
            print("%s\t\t%s"%(i[0],i[1]))
    
    def formatLabInfo(self):
        lab_info = "%s_%s"%(self.lab_name,self.lab_cost)
        return lab_info
    
    def enterLaboratoryInfo(self):
        self.lab_name = input("Enter the name of the Laboratory:\n")
        self.lab_cost = input("Enter the cost of the Laboratory:\n")
    
    def readLaboratoriesFile(self):
        lab_file = open("laboratories.txt","r")

        #create a list of laboratory objects with the file's contents as its attribute values
        lab_obj_list = []
        
        for each_line in lab_file:
            line_list = each_line.split("_")
            new_lab = Laboratory(line_list[0],line_list[1])
            lab_obj_list.append(new_lab)
        
#The management process of doctor
def doctors():
    while True:
        dt=Doctor()
        doctor_list=dt.readDoctorsFile()
        nav2=input('\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n')
        if nav2=='1':
            dt.displayDoctorsList(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='2':
            dt.searchDoctorById(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='3':
            dt.searchDoctorByName(doctor_list)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='4':
            new_doctorList=dt.addDrToFile(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='5':
            new_doctorList=dt.editDoctorInfo(doctor_list)
            format_doctor=dt.formatDrInfo(new_doctorList)
            dt.writeListOfDoctorsToFile(format_doctor)
            print('\nBack to the prevoius Menu\n')
        elif nav2=='6':
            print('\nBack to the prevoius Menu\n')
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the prevoius Menu\n')
            break

#The management process of facilitys
def facilitys():
    op=facility()
    while True:
        print("\nFacilities Menu:")
        print("1 - Display Facilities list")
        print("2 - Add Facility")
        print("3 - Back to the Main Menu\n")            
        choose2 = input()
        if choose2 == "1":
            op.displayFacilities()
        elif choose2 == "2":
            name = input("Enter Facility name:\n")
            op.addFacility(name)
            op.writeListOffacilitiesToFile()
            print('\nBack to the prevoius Menu\n')
        elif choose2 == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the prevoius Menu\n')
            break
        
#The management process of laboratories
def laboratories():
    lab=Laboratory("name",0)
    while True:
        print("\nLaboratories Menu:")
        print("1 - Display laboratories list")
        print("2 - Add laboratory")
        print("3 - Back to the Main Menu\n")            
        choose3 = input()
        if choose3 == "1":
            lab.displayLabsList()
        elif choose3 == "2":
            lab.addLabToFile()
        elif choose3 == "3":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu\n')
            break


#The management process of patients
def patients():
    pat = Patient(00,"PatientX","Cold","","22")
    while True:
        print("\nPatients Menu:")
        print("1 - Display patients list")
        print("2 - Search patient by ID")
        print("3 - Add patient")
        print("4 - Edit patient info")
        print("5 - Back to the Main Menu\n")
        choose4 = input()
        if choose4 =="1":
            pat.displayPatientsList()
        elif choose4 =="2":
            pat.searchPatientById()
        elif choose4 == "3":
            pat.addPatientToFile()
        elif choose4 == "4":
            pat.editPatientInfo()
        elif choose4 == "5":
            break
        else:
            print('\nYou input a wrong number. Please try it again.\n')
            print('\nBack to the previous Menu\n')
            break
        
        
#Running main program
if __name__ == '__main__':
    while True:
        print('\nWelcome to Alberta Hospital (AH) Managment system\n')
        nav1=input("Select from the following options, or select 0 to stop: \n1 - 	Doctors \n2 - 	Facilities \n3 - 	Laboratories \n4 - 	Patients\n")
        if nav1=='1':
            doctors()
        elif nav1=='2':
            facilitys()
        elif nav1=='3':
            laboratories()
        elif nav1=='4':
            patients()
        elif nav1=='0':
            break