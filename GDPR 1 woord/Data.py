# -*- coding: utf-8 -*-
# 4 classes of training data


def GetTrainingData():
    training_data = []

    trainingDataRaw = []
    with open("TrainingData.txt") as f:
        trainingDataRaw = f.readlines()
    trainingDataRaw = [x.strip("\n") for x in trainingDataRaw]

    

    for line in trainingDataRaw:
        line = line.split(':',1)
        training_data.append({"class":line[0], "sentence":line[1]})

    for line in training_data:
        line['sentence'] = line['sentence'].strip().decode("ascii", "ignore").encode("ascii")
        if line['sentence'] == "":continue
    
    return training_data


GetTrainingData()
def GetAnswer(number):
    if number == "1": return GetAnswer1()
    elif number == "2": return GetAnswer2()
    elif number == "3": return GetAnswer3()
    elif number == "4": return GetAnswer4()
    elif number == "5": return GetAnswer5()
    elif number == "6": return GetAnswer6()
    elif number == "7": return GetAnswer7()
    elif number == "8": return GetAnswer8()
    elif number == "9": return GetAnswer9()
    elif number == "10": return GetAnswer10()
    return ""

#antwoord op de vraag, What is GDPR?
def GetAnswer1():   
    return """GDPR stands for General Data Protection Regulation and is the new European
Union Regulation set to replace the Data Protection Directive (DPD) and
The UK Data Protection Act 1998. After many years of debate it was approved
by the EU Parliament on April 14th 2016 and involves the protection of
personal data and the rights of individuals. Its aim is to ease the flow
of personal data across the 28 EU member states."""


#antwoord op de vraag, When will the GDPR come into effect?
def GetAnswer2():
    return """The Regulation will come into effect on the 25th May 2018 and will bring in
significant changes to current data protection laws as we know them. Any
company deemed non-compliant will face hefty fines."""


#antwoord op de vraag, Who does GDPR apply to?
def GetAnswer3():
    return """Any organisation which processes and holds the personal data of data subjects
residing in the EU will be obliged to abide by the laws set out by GDPR. This
applies to every organisation, regardless of whether or not they themselves
reside in one of the 28 EU member states."""


#antwoord op de vraag, What responsibilities will companies have under this new regulation?
def GetAnswer4():
    return """Rules for obtaining valid consent to use personal information will become much
tougher when the GDPR comes into force. Therefore, companies must ensure that
consent is clear, affirmative, and in plain language. Companies must also make
it easy for data subjects to withdraw consent if they wish to do so."""

        
#antwoord op de vraag, What kind of information does the GDPR apply to?
def GetAnswer5():
    return """Much like the Data Protection Act 1998, GDPR applies to personal data. The current
Data Protection Directive defines personal data as; "any information relating to an
identified or identifiable natural person ("data subject"); an identifiable person
is one who can be identified, directly or indirectly, in particular by  top frequently
asked questions about GDPRreference to an identification number or to one or more
factors specific to his physical, physiological, mental, economic, cultural or social
identity."
However, although this definition will mostly remain unchanged, it will be slightly
more detailed in that it will make clear that online identifiers, such as an IP address,
will also be classed as personal data.
Sensitive personal data - The GDPR refers to sensitive personal data as "special
categories of personal data which uniqely identify a person." This will include genetic
data and biometric data."""
        

#antwoord op de vraag, Are there any specific rules businesses should be following in order to ensure compliance?
def GetAnswer6():
    return """Article 5 of the EU GDPR states that personal data must be:
     - Processed lawfully, fairly and in a transparent manner
     - Collected only for specified, explicit and legitimate purposes
     - Adequate, relevant and limited to what is necessary
     - Accurate and kept up to date
     - Held only for the absolute time necessary and no longer
     - Processed in a manner that ensures appropriate security of the personal data"""

        
#antwoord op de vraag, What will the penalites be for failing to comply with GDPR?
def GetAnswer7():
    return """The GDPR have introduced a tiered approach to fines, meaning that the severity of the
breach will determine the fine imposed.
The maximum fine a company can face is 4% of their annual global turnover, or €20 million,
whichever is the highest.
Less serious violations, such as having improper records, or failing to notify of
any breaches, can be fined a maximum of 2% of their annual global turnover,
or €10 million."""
        
#antwoord op de vraag, What effect, if any, does Brexit have on GDPR?
def GetAnswer8():
    return """Even though UK Prime Minister, Theresa May, has now announced a definitive date
(29th March 2017) to begin the process of leaving the European Union, Brexit
is still expected to take at least two years to take full effect, therefore,
UK businesses still need to become GDPR ready by 25th May 2018."""

        
#antwoord op de vraag, Do all organisations now have to appoint a Data Protection Officer (DPO)?
def GetAnswer9():
    return """It is not necessarily compulsory for all organisations to appoint a DPO as this will
be dependent upon a number of factors.  According to the ICO, a company should
appoint a DPO if they:
    - are a public authority (with the exception of courts acting in their judicial capacity)
    - carry out large scale systematic monitoring of individuals, such as, online behaviour tracking; or
    - carry out large scale processing of special categories of data or data relating to ciminal convictions and offences
Any organisation is able to appoint a DPO if they wish to do so. However, even if a company chooses not to appoint a DPO because the above doesn't apply to them, they must still ensure that they have sufficient staff and skills in place to be able to carry out their obligations under the GDPR."""


#antwoord op de vraag, What rights will individuals have under GDPR?
def GetAnswer10():
    return """There are 8 fundamental rights of individuals under GDPR. These are:
    - The right to be informed - Organisations must be completely transparent
in how they are using personal data.
    - The right of access - Individuals will have the right to know exactly what
information is held about them and how it is processed.
    - The right of rectification - Individuals will be entitled to have personal
data rectified if it is inaccurate or incomplete.
    - The right to erasure - Also known as 'the right to be forgotten', this refers
to an individual's right to having their personal data deleted or removed without
the need for a specific reason as to why they wish to discontinue. 
    - The right to restrict processing - Refers to an individual's right to block or
supress processing of their personal data.
    - The right to data portability - This allows individuals to retain and reuse their
personal data for their own purpose.
    - The right to object - In certain circumstances, individuals are entitled to object
to their personal data being used. This includes, if a company uses personal data
for the purpose of direct marketing, scientific and historical research, or for
the performance of a task in the public interest.
    - Rights of automated decision making and profiling - The GDPR has put in place
safeguards to protect individuals against the risk that a potentially damaging
decision is made without human intervention. For example, individuals can choose
not to be the subject of a decision where the consequence has a legal bearing on
them, or is based on automated processing."""
        
