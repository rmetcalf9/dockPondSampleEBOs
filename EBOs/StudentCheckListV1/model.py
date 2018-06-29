
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentCheckList/V1/StudentCheckListEBO:StudentCheckListEBOTypeV1':
      return flaskRestPlusAPI.model('StudentCheckListEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentCheckList/V1/StudentCheckListEBO:IdentificationTypeV1')),
        'PersonIdentifier': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonEBO:IdentificationTypeV1')),
        'Programme': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Programme/V1/ProgrammeRBO:ProgrammeReferenceTypeV1')),
        'Term': fields.Nested(flaskRestPlusAPI.model('InlineTermType', {
          'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
            'Code': fields.String(default='',description='Term Identifier'),
          })),
        })),
        #Element LastUpdated has a type that is not catered for (xsd:date) 0
        'CheckListStatus': fields.String(default='',description='What is current status of checklist item e.g recieved, pending This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StudentCheckList\V1\XXIC_CheckListStatus.dvm'),
        'CheckListItemType': fields.String(default='',description='This code depends on type of check list item e.g TFFF This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\StudentCheckList\V1\XXIC_CheckListItemType.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentCheckList/V1/StudentCheckListEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'Code': fields.String(default='',description='Code of the Student Checklist item will consist of CheckListItemType-PersonIdentifier-ProgrammeCode-TermCode'),

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
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('StudentCheckListEBOV1', {
    'StudentCheckListEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/StudentCheckList/V1/StudentCheckListEBO:StudentCheckListEBOTypeV1')),

  })

