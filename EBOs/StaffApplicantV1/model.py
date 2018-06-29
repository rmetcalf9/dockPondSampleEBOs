
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:StaffApplicantEBOTypeV1':
      return flaskRestPlusAPI.model('StaffApplicantEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:IdentificationTypeV1')),
        #Element OfferLastUpdated has a type that is not catered for (xsd:dateTime) 0
        'Person': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeV1')),
        'AdditionalPersonInfo': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:AdditionalPersonInfoTypeV1')),
        'Job': fields.Nested(flaskRestPlusAPI.model('InlineJobType', {
          'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
            'JobNo': fields.String(default='',description=''),
          })),
          'JobTitle': fields.String(default='',description='Job Title e.g Assistant Bursary Payroll Manager'),
          #Element ProbationDuration has a type that is not catered for (xsd:decimal) 0
          'ProbationDurationUnit': fields.String(default='',description='The Probation period e.g Weeks, Days, Months,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_ProbationDurationUnit.dvm'),
          #Element WorkingHours has a type that is not catered for (xsd:decimal) 0
          'Frequency': fields.String(default='',description='The Work period e.g Week, Day,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_Frequency.dvm'),
        })),
        'HRAdvisor': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeV1')),
        'RecruitmentAdvisor': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:PersonEBOTypeV1')),
        'Application': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:ApplicationTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:ApplicationTypeV1':
      return flaskRestPlusAPI.model('ApplicationTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'ApplicationID': fields.String(default='',description=''),
        })),
        'Effectivedate': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),
        'PreviousEmployments': fields.Nested(flaskRestPlusAPI.model('InlinePreviousEmploymentsType', {
          'PreviousEmployment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:PreviousEmploymentTypeV1'))),
        })),
        'Qualifications': fields.Nested(flaskRestPlusAPI.model('InlineQualificationsType', {
          'Qualification': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:QualificationTypeV1'))),
        })),
        'Assignment': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:TalentlinkAssignmentTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'StaffApplicantCID': fields.String(default='',description=''),
        'JobNo': fields.String(default='',description='Talentlink Unique Application Identifier'),
        'OfferVersionNo': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:AdditionalPersonInfoTypeV1':
      return flaskRestPlusAPI.model('AdditionalPersonInfoTypeV1', {
        'EthnicOrigin': fields.String(default='',description='The cultural and ethnic origin,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_EthnicOrigin.dvm'),
        #Element LatestHireDate has a type that is not catered for (xsd:dateTime) 0
        'ReligionOrBelief': fields.String(default='',description='Religion or Belief IC HRMS Prot. Characteristics,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_ReligionOrBelief.dvm'),
        'GenderIdentity': fields.String(default='',description='Gender Identity IC HRMS Prot. Characteristics'),
        'PreferredGenderIdentity': fields.String(default='',description='Gender Identity IC HRMS Prot. Characteristics,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_PreferGenIdentity.dvm'),
        'SexualOrientation': fields.String(default='',description='Sexual orientation IC HRMS Prot. Characteristics,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_SexualOrientation.dvm'),
        'SpecialInformation': fields.Nested(flaskRestPlusAPI.model('InlineSpecialInformationType', {
          #Element ShareConsent has a type that is not catered for (xsd:boolean) 0
          'Disabled': fields.String(default='',description='The long-term disability, physical or mental impairment, this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_PersonDisability.dvm'),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:QualificationTypeV1':
      return flaskRestPlusAPI.model('QualificationTypeV1', {
        'Title': fields.String(default='',description='Qualification person holds'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:PreviousEmploymentTypeV1':
      return flaskRestPlusAPI.model('PreviousEmploymentTypeV1', {
        'Employer': fields.String(default='',description='Company Name of previous employment'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),
        'Job': fields.String(default='',description='Position Title of previous employment'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:TalentlinkAssignmentTypeV1':
      return flaskRestPlusAPI.model('TalentlinkAssignmentTypeV1', {
        'Department': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1')),
        'HROrganization': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1')),
        'AssignmentCategory': fields.String(default='',description='AssignmentCategory field in ICIS using Type of contract lookup,this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_ContractType.dvm'),
        'Effectivedate': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),
        'JobFamily': fields.String(default='',description='Job Family, this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StaffApplicant\V1\XXIC_JobFamily.dvm'),
        'JobLevel': fields.String(default='',description='Job Level,part of the Grade description'),
        #Element BaseSalary has a type that is not catered for (xsd:decimal) 0
        #Element SalaryValue has a type that is not catered for (xsd:decimal) 0
        #Element WorkingHours has a type that is not catered for (xsd:decimal) 0
        'Point': fields.String(default='',description='Spine point'),
        'Supervisor': fields.Nested(flaskRestPlusAPI.model('InlineSupervisorType', {
          'SupervisorCID': fields.String(default='',description='Line Manager CID'),
          'SupervisorAssignmentNumber': fields.String(default='',description='Line Manager CID'),
        })),

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
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:HROrganizationUnitReferenceTypeV1':
      return flaskRestPlusAPI.model('HROrganizationUnitReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/HROrganizationUnit/V1/HROrganizatinUnitRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'OrgCode': fields.String(default='',description=''),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('StaffApplicantEBOV1', {
    'StaffApplicantEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StaffApplicant/V1/StaffApplicantEBO:StaffApplicantEBOTypeV1')),

  })

