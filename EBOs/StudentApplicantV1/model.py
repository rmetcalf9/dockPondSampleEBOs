
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:StudentApplicantEBOTypeV1':
      return flaskRestPlusAPI.model('StudentApplicantEBOTypeV1', {
        'Person': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeV1')),
        'EmergencyContacts': fields.Nested(flaskRestPlusAPI.model('InlineEmergencyContactsType', {
          'EmergencyContact': fields.Nested(flaskRestPlusAPI.model('InlineEmergencyContactType', {
            'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:IdentificationTypeV1')),
            'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonNameTypeV1')),
            'PhysicalAddresses': fields.Nested(flaskRestPlusAPI.model('InlinePhysicalAddressesType', {
              'PhysicalAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1'))),
            })),
            'ElectronicAddresses': fields.Nested(flaskRestPlusAPI.model('InlineElectronicAddressesType', {
              'ElectronicAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1'))),
            })),
            'RelationshipToPerson': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_RelationshipToPerson.dvm'),
          })),
        })),
        'ApplicantProgrammeVersions': fields.Nested(flaskRestPlusAPI.model('InlineApplicantProgrammeVersionsType', {
          'ApplicantProgrammeVersion': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:ApplicantProgrammeVersionTypeV1'))),
        })),
        'DisclosureAndBarringService': fields.Nested(flaskRestPlusAPI.model('InlineDisclosureAndBarringServiceType', {
          'Submitted': fields.String(default='',description='This will indicate either the disclosure was submitted or not'),
          'Number': fields.String(default='',description='The disclosure number e.g 001359416860'),
          #Element IssueDate has a type that is not catered for (xsd:dateTime) 0
        })),
        'VisaDetails': fields.Nested(flaskRestPlusAPI.model('InlineVisaDetailsType', {
          #Element Tier4StudentFlag has a type that is not catered for (xsd:boolean) 0
          'Indicator': fields.String(default='',description='Yes/No Tier5StudentIndicator - if Visa type is STUD'),
          #Element IssueDate has a type that is not catered for (xsd:dateTime) 0
          'VisaType': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_StudentVisaType.dvm'),
          #Element VisaExpiry has a type that is not catered for (xsd:date) 0
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:ApplicantProgrammeVersionTypeV1':
      return flaskRestPlusAPI.model('ApplicantProgrammeVersionTypeV1', {
        'Programme': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:ProgrammeTypeV1')),
        #Element StartDate has a type that is not catered for (xsd:dateTime) 0
        #Element EndDate has a type that is not catered for (xsd:dateTime) 0
        'Active': fields.String(default='',description='This indicates if the applicant is active or not'),
        'KeyProgramme': fields.String(default='',description=''),
        'ProgrammeAttemptStatus': fields.String(default='',description=''),
        #Element CurrentProgrammeYear has a type that is not catered for (xsd:integer) 0
        #Element ProgrammeYear has a type that is not catered for (xsd:integer) 0
        #Element AcademicYear has a type that is not catered for (xsd:integer) 0
        'Campus': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Campus:CampusCodeTypeV1')),
        'CurrentCohortYear': fields.String(default='',description='A class of student applicants e.g Class of 2004'),
        'OriginalCohortYear': fields.String(default='',description='A class of student applicants e.g Class of 2004'),
        'FullTimePartTime': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_StudentFullTimePartTime.dvm'),
        'International_Domestic_Status': fields.String(default='',description='FeeResidencyStatus - This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_StudentInternational_Domestic_Status.dvm'),
        'ApplicantEnrollmentCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_StudentEnrollmentCode.dvm'),
        #Element PrimaryIndicator has a type that is not catered for (xsd:boolean) 0
        #Element PlacementFlag has a type that is not catered for (xsd:boolean) 0
        'StudentType': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_StudentType.dvm'),
        'Decision': fields.Nested(flaskRestPlusAPI.model('InlineDecisionType', {
          'DecisionStatus': fields.String(default='',description=''),
          #Element DecisionDate has a type that is not catered for (xsd:dateTime) 0
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:ProgrammeTypeV1':
      return flaskRestPlusAPI.model('ProgrammeTypeV1', {
        'Programme': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:IdentificationTypeV1')),
        'Version': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:ProgrammeVersionReferenceTypeV1')),
        'Department': fields.Nested(flaskRestPlusAPI.model('InlineDepartmentType', {
          'Code': fields.String(default='',description='Department code of where the student applicant is affiliated'),
          'Name': fields.String(default='',description='Department name of where the student applicant is affiliated'),
        })),
        'Awards': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:AwardTypeV1')),
        'ProgrammeLength': fields.String(default='',description='Should this be here or under Programme EBO Length of the programme. Need to concatenate with " " and SKRPMOD_SSDT_CODE_UOMS where decoded to get Desciption (1 = Years; 2 = Months; 3 = Weeks; 4 = Days; 5 = Hours) to get for example "2 Years", "36 Months" etc.'),
        'ProgrammeLevel': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Student\V1\XXIC_ProgrammeLevel.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeIGNOREV1':
      return flaskRestPlusAPI.model('PersonEBOTypeIGNOREV1', {

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeV1':
      return flaskRestPlusAPI.model('PersonEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:IdentificationTypeV1')),
        'PersonName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonNameTypeV1')),
        #Element DateOfBirth has a type that is not catered for (xsd:dateTime) 0
        'Gender': fields.String(default='',description='This is Legal Sex of the person This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonGENDER.dvm'),
        'MaritalStatus': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonMaritalStatus.dvm'),
        'Nationality': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonNationality.dvm'),
        #Element DeceasedFlag has a type that is not catered for (xsd:boolean) 0
        #Element DeceasedDate has a type that is not catered for (xsd:dateTime) 0
        'EthnicOrigin': fields.String(default='',description='Person\'s Ethnic Origin - This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonEthnicOrigin.dvm'),
        'Domicile': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonDomicile.dvm'),
        'PhysicalAddresses': fields.Nested(flaskRestPlusAPI.model('InlinePhysicalAddressesType', {
          'PhysicalAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1'))),
        })),
        'ElectronicAddresses': fields.Nested(flaskRestPlusAPI.model('InlineElectronicAddressesType', {
          'ElectronicAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1'))),
        })),
        'SystemCredentials': fields.Nested(flaskRestPlusAPI.model('InlineSystemCredentialsType', {
          'SystemCredential': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:SystemCredentialTypeV1'))),
        })),
        'HESADisabilities': fields.Nested(flaskRestPlusAPI.model('InlineHESADisabilitiesType', {
          'HESADisability': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:HESADisabilityTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonTypeV1':
      return flaskRestPlusAPI.model('PersonTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:IdentificationTypeV1')),
        'PersonName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonNameTypeV1')),
        #Element DateOfBirth has a type that is not catered for (xsd:dateTime) 0
        'Gender': fields.String(default='',description='This is Legal Sex of the person This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonGENDER.dvm'),
        'MaritalStatus': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonMaritalStatus.dvm'),
        'Nationality': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonNationality.dvm'),
        #Element DeceasedFlag has a type that is not catered for (xsd:boolean) 0
        #Element DeceasedDate has a type that is not catered for (xsd:dateTime) 0
        'EthnicOrigin': fields.String(default='',description='Person\'s Ethnic Origin - This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonEthnicOrigin.dvm'),
        'Domicile': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonDomicile.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonNameTypeV1':
      return flaskRestPlusAPI.model('PersonNameTypeV1', {
        'FirstName': fields.String(default='',description='This is person first name'),
        'MiddleName': fields.String(default='',description='Middle name could also be know as \'given name\''),
        'LastName': fields.String(default='',description='This will be the person last name/ Family Name/Surname'),
        'Title': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonTitle.dvm'),
        'PreferredName': fields.String(default='',description='This indicate which name the person preferredto be known as'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:SystemCredentialTypeV1':
      return flaskRestPlusAPI.model('SystemCredentialTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'CredentialType': fields.String(default='',description='This will hold type of credential e.g SSO'),
          'CredentialValue': fields.String(default='',description='The actual value of the credntial use e.g osmith'),
        })),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:DeclaredDisabilityV1':
      return flaskRestPlusAPI.model('DeclaredDisabilityV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'Code': fields.String(default='',description='This will hold type of credential e.g SSO'),
          'Description': fields.String(default='',description='The actual value of the credntial use e.g osmith'),
        })),
        'UpdatedBy': fields.String(default='',description=''),
        #Element UpdatedDate has a type that is not catered for (xsd:date) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'CID': fields.String(default='',description='College CID for the person'),
        'UCASPERID': fields.String(default='',description='UCAS Personal ID for the person'),
        'EMBARKID': fields.String(default='',description='Embark Online Application ID for the student applicant'),
        'NINumber': fields.String(default='',description='National Insurance Number'),
        'HESAID': fields.String(default='',description='HESA Identifier'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:HESADisabilityTypeV1':
      return flaskRestPlusAPI.model('HESADisabilityTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'Code': fields.String(default='',description='Code of the HESA disability - This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_HESADisabilityCode.dvm'),
        })),
        'Description': fields.String(default='',description='Description of HESA disability'),
        #Element LastUpdateDate has a type that is not catered for (xsd:date) 0
        'LastUpdateBy': fields.String(default='',description='Who updated this information? - Is this system name or person name?'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'AddressNumber': fields.String(default='',description='Address Unique Identifier'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1':
      return flaskRestPlusAPI.model('PhysicalAddressTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:IdentificationTypeV1')),
        'AddressUsages': fields.Nested(flaskRestPlusAPI.model('InlineAddressUsagesType', {
          'AddressUsage': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/UsageType:UsageTypeV1'))),
        })),
        'Address1': fields.String(default='',description='The first Line of address'),
        'Address2': fields.String(default='',description='Second line of address'),
        'Address3': fields.String(default='',description='Third line of Address'),
        'Address4': fields.String(default='',description='Fourth Line of Address'),
        'Region': fields.String(default='',description='County/Region/District/Province/State'),
        'City': fields.String(default='',description='City or Town'),
        'PostalCode': fields.String(default='',description='Post Code of an address'),
        'Country': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_Country.dvm'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1':
      return flaskRestPlusAPI.model('EffectiveDateTypeV1', {
        #Element StartDateTime has a type that is not catered for (xsd:dateTime) 0
        #Element EndDateTime has a type that is not catered for (xsd:dateTime) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/UsageType:UsageTypeV1':
      return flaskRestPlusAPI.model('UsageTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'UsageID': fields.String(default='',description='The usage identifier'),
        })),
        'UsageCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_UsageCode.dvm'),
        'PreferredIndicator': fields.String(default='',description='Indicates if this is the preferred usage'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1':
      return flaskRestPlusAPI.model('ElectronicAddressTypeV1', {
        'Identification': fields.String(default='',description='Unique identifier'),
        'ElectronicAddrTypeCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_ElectronicAddrTypeCode.dvm'),
        'Address': fields.String(default='',description='this is the actual electronic address and this could be Email(someone@everyone.com) etc'),
        'AddressUsages': fields.Nested(flaskRestPlusAPI.model('InlineAddressUsagesType', {
          'AddressUsage': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/UsageType:UsageTypeV1'))),
        })),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Campus:CampusCodeTypeV1':
      return flaskRestPlusAPI.model('CampusCodeTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'CampusCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_CampusCode.dvm'),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:ProgrammeReferenceTypeV1':
      return flaskRestPlusAPI.model('ProgrammeReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:IdentificationTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:AwardTypeV1':
      return flaskRestPlusAPI.model('AwardTypeV1', {
        'Award': fields.List(fields.String(default='',description='')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:ProgrammeVersionReferenceTypeV1':
      return flaskRestPlusAPI.model('ProgrammeVersionReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:VersionIdentificationTypeV1')),
        'Description': fields.String(default='',description='This is Programme/Course description or Title e.g Bachelor of Nursing'),
        'Faculty': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Faculty:FacultyCodeTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'ProgrammeCode': fields.String(default='',description='This is Programme/Course unique identifier e.g MED101'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:VersionIdentificationTypeV1':
      return flaskRestPlusAPI.model('VersionIdentificationTypeV1', {
        #Element Version has a type that is not catered for (xsd:integer) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Faculty:FacultyCodeTypeV1':
      return flaskRestPlusAPI.model('FacultyCodeTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'FacultyCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_FacultyCode.dvm'),
        })),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('StudentApplicantEBOV1', {
    'StudentApplicantEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentApplicant/V1/StudentApplicantEBO:StudentApplicantEBOTypeV1')),

  })

