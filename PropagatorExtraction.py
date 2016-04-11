import pandas as pd
import os
#import glob
#from pandas import DataFrame
import xlsxwriter
import re
#import xlrd
import matplotlib.pyplot as plt

colFile=0
colMolecule=1
colFullPointGroup=2
colLargestAbelianSubgroup=3
colLargestConciseAbelianSubgroup=4
colCharge=5
colMultiplicity=6
colBasis=7
colOrbital=8
colHF=9
colOVGF_A=10
colOVGF_A_ps=11
colOVGF_B=12
colOVGF_B_ps=13
colOVGF_C=14
colOVGF_C_ps=15
colOVGF_Recommended=16
colOVGF_Recommended_ps=17
colP3=18
colP3_ps=19
colP3_plus=20
colP3_plus_ps=21
colD2=22
colD2_ps=23
colOVGF_A_HF=24
colOVGF_B_HF=25
colOVGF_C_HF=26
colOVGF_Recommended_HF=27
colP3_HF=28
colP3_plus_HF=29
colD2_HF=30



'''path to this file'''
path=os.path.dirname(os.path.realpath(__file__))
#/Users/Jared/Dropbox/Auburn/Research/Second_Research/Propagator

'''excel file name to open with path'''
excelFilePathName='/propagatorFilesExcel.xlsx'

'''folder containing the propagator files'''
propagatorFilesFolder='/Jared_Propa'

row=1

def writeDataToExcel(worksheet, row, fileInformation,orbital,hf,ovgf_a, ovgf_a_ps, ovgf_b,\
            ovgf_b_ps,ovgf_c, ovgf_c_ps,ovgf_recommend,ovgf_recommended_ps,\
            p3,p3_plus,d2, ovgf_a_hf,ovgf_b_hf,ovgf_c_hf,\
            ovgf_recommend_hf,p3_hf,p3_plus_hf,d2_hf,molecule,charge,multiplicity,\
            basis,fullPointGroup,largestAbelianSubgroup,largestConciseAbelianSubgroup,p3_ps,p3_plus_ps,d2_ps):
            
    
    worksheet.write(row, colFile, fileInformation)
    worksheet.write(row, colOrbital, orbital)
    worksheet.write(row, colHF, hf)
    worksheet.write(row, colOVGF_A, ovgf_a)
    worksheet.write(row, colOVGF_B, ovgf_b)
    worksheet.write(row, colOVGF_C, ovgf_c)
    worksheet.write(row, colOVGF_A_ps, ovgf_a_ps)
    worksheet.write(row, colOVGF_B_ps, ovgf_b_ps)
    worksheet.write(row, colOVGF_C_ps, ovgf_c_ps)
    worksheet.write(row, colOVGF_Recommended, ovgf_recommend)
    worksheet.write(row, colOVGF_Recommended_ps, ovgf_recommended_ps)
    worksheet.write(row, colP3, p3)
    worksheet.write(row, colP3_ps, p3_ps)
    worksheet.write(row, colP3_plus, p3_plus)
    worksheet.write(row, colP3_plus_ps, p3_plus_ps)
    worksheet.write(row, colD2, d2)
    worksheet.write(row, colD2_ps, d2_ps)
    worksheet.write(row, colOVGF_A_HF, ovgf_a_hf)
    worksheet.write(row, colOVGF_B_HF, ovgf_b_hf)
    worksheet.write(row, colOVGF_C_HF, ovgf_c_hf)
    worksheet.write(row, colOVGF_Recommended_HF, ovgf_recommend_hf)
    worksheet.write(row, colP3_HF,p3_hf)
    worksheet.write(row, colP3_plus_HF, p3_plus_hf)
    worksheet.write(row, colD2_HF, d2_hf)
    worksheet.write(row, colMolecule, molecule)
    worksheet.write(row, colCharge, charge)
    worksheet.write(row, colMultiplicity, multiplicity)
    worksheet.write(row, colBasis, basis)
    worksheet.write(row, colFullPointGroup, fullPointGroup)
    worksheet.write(row, colLargestAbelianSubgroup, largestAbelianSubgroup)
    worksheet.write(row, colLargestConciseAbelianSubgroup, largestConciseAbelianSubgroup)
    
def numberOfBasisSets(logarray):
    '''returns a list of the split log arrays by basis set. length is number of basis sets'''
    commandLocation=[]
    logsToReturn=[]
    x=0
    while x < len(logarray):
        if logarray[x] =='corrections':
            commandLocation.append(x)
        x+=1
    commandLocation.append(len(logarray))
    x=0
    logsToReturn.append(logarray[:commandLocation[0]])
    #the first log in the array is from the start of the file to the first keyword
    while x< len(commandLocation)-1:
        b=logarray[commandLocation[x]:commandLocation[x+1]]
        logsToReturn.append(b)
        x+=1
    return logsToReturn

def dataExtract(path):
    workbook = xlsxwriter.Workbook(path + excelFilePathName)
    worksheet = workbook.add_worksheet('Propagator')
    
    bold = workbook.add_format({'bold': True})
    
    worksheet.write(0, colFile, 'File', bold)
    worksheet.write(0, colMolecule, 'Molecule', bold)
    worksheet.write(0, colFullPointGroup, 'Full Point Group', bold)
    worksheet.write(0, colLargestAbelianSubgroup, 'Largest Abelian Subgroup', bold)
    worksheet.write(0, colLargestConciseAbelianSubgroup, 'Largest Concise Abelian Subgroup', bold)
    worksheet.write(0, colCharge, 'Charge', bold)
    worksheet.write(0, colMultiplicity, 'Multiplicity', bold)
    worksheet.write(0, colBasis, 'Basis', bold)
    worksheet.write(0, colOrbital, 'Orbital', bold)
    worksheet.write(0, colHF, 'HF', bold)
    worksheet.write(0, colOVGF_A, 'OVGF A', bold)
    worksheet.write(0, colOVGF_A_ps, 'OVGF A PS', bold)
    worksheet.write(0, colOVGF_B, 'OVGF B', bold)
    worksheet.write(0, colOVGF_B_ps, 'OVGF B PS', bold)
    worksheet.write(0, colOVGF_C, 'OVGF C', bold)
    worksheet.write(0, colOVGF_C_ps, 'OVGF C PS', bold)
    worksheet.write(0, colOVGF_Recommended, 'OVGF Recommended', bold)
    worksheet.write(0, colOVGF_Recommended_ps, 'OVGF Recommended PS', bold)
    worksheet.write(0, colP3, 'P3', bold)
    worksheet.write(0, colP3_ps, 'P3 PS', bold)
    worksheet.write(0, colP3_plus, 'P3+', bold)
    worksheet.write(0, colP3_plus_ps, 'P3+ PS', bold)
    worksheet.write(0, colD2, 'D2', bold)
    worksheet.write(0, colD2_ps, 'D2 PS', bold)
    worksheet.write(0, colOVGF_A_HF, 'OVGF A-HF', bold)
    worksheet.write(0, colOVGF_B_HF, 'OVGF B-HF', bold)
    worksheet.write(0, colOVGF_C_HF, 'OVGF C-HF', bold)
    worksheet.write(0, colOVGF_Recommended_HF, 'OVGF-Recommended-HF', bold)
    worksheet.write(0, colP3_HF, 'P3-HF', bold)
    worksheet.write(0, colP3_plus_HF, 'P3+-HF', bold)
    worksheet.write(0, colD2_HF, 'D2-HF', bold)
    
    row=1
    
    logFiles=[]

    for path, subdirs, files in os.walk(path+propagatorFilesFolder):
        for name in files:
            if os.path.join(path, name)[len(os.path.join(path, name))-\
            4:len(os.path.join(path, name))]=='.txt':
                logFiles.append(os.path.join(path, name)) 
    
    for currentFile in logFiles: 
        log = open(currentFile, 'r').read()
        splitLog = re.split(r'[\\\s]\s*', log)
        
        #fileInformation needs to be added to excel
        fileInformation=currentFile
        
        firstSplitLog=numberOfBasisSets(splitLog)[0]
        x=0
        while x<len(firstSplitLog):
            if firstSplitLog[x]=='Stoichiometry':
                molecule=firstSplitLog[x+1]
            if firstSplitLog[x]=='Charge':
                charge=firstSplitLog[x+2]
            if firstSplitLog[x]=='Multiplicity':
                multiplicity=firstSplitLog[x+2]
            if firstSplitLog[x]=='Standard' and firstSplitLog[x+1]=='basis:':
                basis=firstSplitLog[x+2]
            if firstSplitLog[x]=='Full':
                fullPointGroup=firstSplitLog[x+3]
            if firstSplitLog[x]=='Largest' and firstSplitLog[x+1]=='Abelian':
                largestAbelianSubgroup=firstSplitLog[x+3]
            if firstSplitLog[x]=='concise':
                largestConciseAbelianSubgroup=firstSplitLog[x+3]
            
            
            x+=1
        
        for splitlog in numberOfBasisSets(splitLog)[1:]:
            #NUMBEROFSPLITS will return where in log file it needs to be split for basis sets
            #textFile(log)   #text file will return each log split by basis set because some aren't
            #print(splitlog)
            
            x=0
            while x<len(splitlog):
                
                if splitlog[x]=='Method' and splitlog[x+1]=='Orbital':

                    orbital=splitlog[x+6]
                    hf=float(splitlog[x+7])
                    ovgf_a=float(splitlog[x+8])
                    ovgf_a_ps=float(splitlog[x+9])
                    ovgf_b=float(splitlog[x+13])
                    ovgf_b_ps=float(splitlog[x+14])
                    ovgf_c=float(splitlog[x+18])
                    ovgf_c_ps=float(splitlog[x+19])
        
                if splitlog[x]=='recommended':
                    ovgf_recommend=float(splitlog[x+8])
                    ovgf_recommended_ps=float(splitlog[x+9])

  
                if splitlog[x]=='Converged' and splitlog[x+1]=='3rd' and splitlog[x+2]=='order':
                    p3=float(splitlog[x+7])
                    p3_ps=float(splitlog[x+9])
                    
                    try:
                        p3_plus=float(splitlog[x+17])
                        p3_plus_ps=float(splitlog[x+19])
                    except:
                        p3_plus=None
                        p3_plus_ps=None
                        
                if splitlog[x]=='Converged' and splitlog[x+1]=='second':
                    d2=float(splitlog[x+6])
                    d2_ps=float(splitlog[x+8])
                
                if x==len(splitlog)-1:
                    ovgf_a_hf = ovgf_a-hf
                    ovgf_b_hf=ovgf_b-hf
                    ovgf_c_hf=ovgf_c-hf
                    ovgf_recommend_hf=ovgf_recommend-hf
                    
                    p3_hf=p3-hf
                    if p3_plus!=None:
                        p3_plus_hf=p3_plus-hf
                    else:
                        p3_plus_hf=None
                    d2_hf=d2-hf
        
                x+=1
    
            writeDataToExcel(worksheet, row, fileInformation,orbital,hf,ovgf_a, ovgf_a_ps, ovgf_b,\
            ovgf_b_ps,ovgf_c, ovgf_c_ps,ovgf_recommend,ovgf_recommended_ps,\
            p3,p3_plus,d2, ovgf_a_hf,ovgf_b_hf,ovgf_c_hf,\
            ovgf_recommend_hf,p3_hf,p3_plus_hf,d2_hf,molecule,charge,multiplicity,basis,\
            fullPointGroup,largestAbelianSubgroup,largestConciseAbelianSubgroup,p3_ps,p3_plus_ps,d2_ps)
            row+=1
                
        
