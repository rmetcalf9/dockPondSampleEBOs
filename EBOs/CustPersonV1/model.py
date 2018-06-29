
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'CID': fields.String(default='',description='College CID for the person'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:PersonNameTypeV1':
      return flaskRestPlusAPI.model('PersonNameTypeV1', {
        'FirstName': fields.String(default='',description='Person first name'),
        'MiddleName': fields.String(default='',description='Middle name could also be know as \'given name\''),
        'LastName': fields.String(default='',description='Person last name/Family Name/Surname'),
        'Prefix': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\Person\V1\XXIC_PersonTitle.dvm'),
        'PreferredName': fields.String(default='',description='This is the name the person prefers to be known as'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:CustPersonEBOTypeV1':
      return flaskRestPlusAPI.model('CustPersonEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:IdentificationTypeV1')),
        'Name': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:PersonNameTypeV1')),
        'PhysicalAddresses': fields.Nested(flaskRestPlusAPI.model('InlinePhysicalAddressesType', {
          'PhysicalAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1'))),
        })),
        'ElectronicAddresses': fields.Nested(flaskRestPlusAPI.model('InlineElectronicAddressesType', {
          'ElectronicAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1'))),
        })),
        'Status': fields.String(default='',description='Cust Person Status e.g Active, Inactive This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_PartyStatus.dvm'),
        'CustomerAccounts': fields.Nested(flaskRestPlusAPI.model('InlineCustomerAccountsType', {
          'CustomerAccount': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:CustomerAccountTypeV1'))),
        })),

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
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:CustomerAccountTypeV1':
      return flaskRestPlusAPI.model('CustomerAccountTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:IdentificationTypeV1')),
        'AccountName': fields.String(default='',description=''),
        'CustomerClassCode': fields.String(default='',description='The is the customer class code of the Customer e.g UKGOVT, British Council etc This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_CustomerClassCode.dvm'),
        'AccountStatus': fields.String(default='',description='Customer Account Status e.g Active, Inactive This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_AccountStatus.dvm'),
        'CustomerType': fields.String(default='',description='The is the account type of the Customer e.g External This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_CustomerType.dvm'),
        'ProfileClass': fields.String(default='',description='The is the profile class of the Customer e.g Registry - Sponsors, Accommodation This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_CustomerProfileClass.dvm'),
        'Contacts': fields.Nested(flaskRestPlusAPI.model('InlineContactsType', {
          'Contact': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:ContactTypeV1'))),
        })),
        'Sites': fields.Nested(flaskRestPlusAPI.model('InlineSitesType', {
          'Site': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:AcctSiteTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'AccountNumber': fields.String(default='',description='Customer Unique Identifier (Customer Account Number)'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:AcctSiteTypeV1':
      return flaskRestPlusAPI.model('AcctSiteTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'SiteNumber': fields.String(default='',description='Site Number for the Customer (Unique within the Customer Account)'),
        })),
        'SiteName': fields.String(default='',description='Party Site Name'),
        'SiteCategory': fields.String(default='',description='The is the site category of the Customer e.g Registry, Research - Non Medical, Corporate - Other This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_SiteCategory.dvm'),
        'SiteUsages': fields.Nested(flaskRestPlusAPI.model('InlineSiteUsagesType', {
          'SiteUsage': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:SiteUseTypeV1'))),
        })),
        #Element StudentSponsorFlag has a type that is not catered for (xsd:boolean) 0
        'OrgID': fields.String(default='',description='The is the Organization ID relating to the Original System Reference e.g 101 - Imperial College, 9515 - TB - Imperial College ThinkSpace Limited etc This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_Organizations.dvm'),
        'Status': fields.String(default='',description='Site Status for the Customer e.g Active, Inactive This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_SiteStatus.dvm'),
        'PhysicalAddresses': fields.Nested(flaskRestPlusAPI.model('InlinePhysicalAddressesType', {
          'PhysicalAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1'))),
        })),
        'ElectronicAddresses': fields.Nested(flaskRestPlusAPI.model('InlineElectronicAddressesType', {
          'ElectronicAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1'))),
        })),
        'Contacts': fields.Nested(flaskRestPlusAPI.model('InlineContactsType', {
          'Contact': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:ContactTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:SiteUseTypeV1':
      return flaskRestPlusAPI.model('SiteUseTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'SiteUseID': fields.String(default='',description='Site Usage ID for the Customer Site Usage Type'),
        })),
        'SiteUseCode': fields.String(default='',description='Business use purpose for the Site e.g BILL_TO. The DVM is from Ebiz (FND_LOOKUP Type - SITE_USE_CODE) and is also used by Contact Type This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_SiteUseCode.dvm'),
        'SiteUseLocation': fields.String(default='',description='Business purpose location reference for the Site'),
        'PrimaryFlag': fields.String(default='',description='Primary Flag Site Usage'),
        'Status': fields.String(default='',description='Site Status for the Customer e.g Active, Inactive This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_SiteStatus.dvm The DVM is from the same source as the DVM used by Account Site'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/Customer:ContactTypeV1':
      return flaskRestPlusAPI.model('ContactTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'ContactReferenceNum': fields.String(default='',description='Contact Role Reference for the Account (Unique across all CustomerAccounts)'),
        })),
        'Name': fields.String(default='',description='Contact Name for the Account'),
        'Type': fields.String(default='',description='Contact Type for the Customer e.g BILL_TO The DVM is from the same source as the DVM used by SiteUseCode (i.e. from Ebiz FND_LOOKUP Type - SITE_USE_CODE) This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_SiteUseCode.dvm'),
        'Status': fields.String(default='',description='Contact Status for the Customer e.g Active, Inactive This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_ContactStatus.dvm'),
        'ContactNumber': fields.String(default='',description='Contact Number for the Customer'),
        'EffectiveDates': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/EffectiveDateType:EffectiveDateTypeV1')),
        'PhysicalAddresses': fields.Nested(flaskRestPlusAPI.model('InlinePhysicalAddressesType', {
          'PhysicalAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/PhysicalAddress:PhysicalAddressTypeV1'))),
        })),
        'ElectronicAddresses': fields.Nested(flaskRestPlusAPI.model('InlineElectronicAddressesType', {
          'ElectronicAddress': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/ElectronicAddressType:ElectronicAddressTypeV1'))),
        })),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('CustPersonEBOV1', {
    'CustPersonEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/CustPerson/V1:CustPersonEBOTypeV1')),

  })

