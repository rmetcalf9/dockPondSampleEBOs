
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'TransactionNumber': fields.String(default='',description='Unique identifier for transaction'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SettlementDetailTypeV1':
      return flaskRestPlusAPI.model('SettlementDetailTypeV1', {
        'PaymentTerms': fields.String(default='',description='Payment Terms e.g Sponser Full, 30 Days This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_PaymentTerms.dvm'),
        #Element PaymentDueDate has a type that is not catered for (xsd:date) 0
        'TransactionCurrency': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CurrencyType:CurrencyTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:ARBillingEBOTypeV1':
      return flaskRestPlusAPI.model('ARBillingEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:IdentificationTypeV1')),
        'BatchSourceName': fields.String(default='',description='Batch source name - where is this data coming from. This name defines how this data will be processed - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_BatchSourceName.dvm'),
        'RelatedCustomerTransaction': fields.Nested(flaskRestPlusAPI.model('InlineRelatedCustomerTransactionType', {
          'InterfaceHeaderAttributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceHeaderAttributeTypeV1')),
        })),
        'TransactionClass': fields.String(default='',description='Transaction Class e.g Deposit, Invoice This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_TransactionClass.dvm'),
        'TransactionStatus': fields.String(default='',description='Transaction Status e.g Open, Close, Pending or Void This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_TransactionStatus.dvm'),
        'TransactionType': fields.Nested(flaskRestPlusAPI.model('InlineTransactionTypeType', {
          'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
            'Code': fields.String(default='',description='Transaction Type e.g AAC, ZC, This is decided not to be DVM and there is long list of values and values depends on Transaction Class. We should not apply any logic in here and hence it is decided to leave transaction type as RBO'),
          })),
          'Description': fields.String(default='',description='this is description of transaction type'),
        })),
        'LegalEntity': fields.Nested(flaskRestPlusAPI.model('InlineLegalEntityType', {
          'OrgID': fields.String(default='',description='Org ID for legal entity derived using value in LegalEntity/LegalEntity and mapped to Org ID - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_LegalEntity.dvm'),
          'LegalEntity': fields.String(default='',description='This is operation unit/name of the org'),
        })),
        #Element TransactionDate has a type that is not catered for (xsd:date) 0
        #Element GLDate has a type that is not catered for (xsd:date) 0
        #Element IsTransactionComplete has a type that is not catered for (xsd:boolean) 0
        'Bill_To': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CustomerSite:CustomerSiteReferenceTypeV1')),
        'SalesRep': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonRBO:PersonReferenceTypeV1')),
        'Reference': fields.String(default='',description='What is the reference for this Billing'),
        'SettlementDetail': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SettlementDetailTypeV1')),
        'Comments': fields.String(default='',description='Comment about the transaction'),
        'InternalNotes': fields.String(default='',description='stores special instructions'),
        'Attributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:HeaderAttributeTypeV1')),
        'InterfaceHeaderAttributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceHeaderAttributeTypeV1')),
        'TransactionLines': fields.Nested(flaskRestPlusAPI.model('InlineTransactionLinesType', {
          'TransactionLine': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:TransactionLineTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SalesCreditsLineTypeV1':
      return flaskRestPlusAPI.model('SalesCreditsLineTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'SalesCreditID': fields.String(default='',description='Unique identifier for SalesCreditsLineType'),
        })),
        'SalesCreditTypeName': fields.String(default='',description='Sales Credit Type name e.g Quota Sales Credit and Non-quota Sales Credit This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_SalesCreditTypeName.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:HeaderAttributeTypeV1':
      return flaskRestPlusAPI.model('HeaderAttributeTypeV1', {
        'SourceSystemSpecificAttribute1': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute2': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute3': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute4': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute5': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute6': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute7': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute8': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute9': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:LineAttributeTypeV1':
      return flaskRestPlusAPI.model('LineAttributeTypeV1', {
        'SourceSystemSpecificAttribute1': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute2': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute3': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute4': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute5': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute6': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute7': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute8': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute9': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceHeaderAttributeTypeV1':
      return flaskRestPlusAPI.model('InterfaceHeaderAttributeTypeV1', {
        'SourceSystemHeaderReference': fields.String(default='',description='Transaction Header ID - so it can be linked between header and lines This Value maps to Interface_Header_Attribute1 in ICIS transaction header'),
        'SourceSystemSpecificAttribute1': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute2': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute3': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute4': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute5': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute6': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute7': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute8': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceLineAttributeTypeV1':
      return flaskRestPlusAPI.model('InterfaceLineAttributeTypeV1', {
        'SourceSystemHeaderReference': fields.String(default='',description='Transaction Header ID - so it can be linked between header and lines - This Value maps to Interface_Line_Attribute1 in ICIS transaction line'),
        'SourceSystemLineReference': fields.String(default='',description='Transaction line ID - so it can be linked between header and lines - This Value maps to Interface_Line_Attribute15 in ICIS transaction line'),
        'SourceSystemSpecificAttribute1': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute2': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute3': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute4': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute5': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute6': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute7': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),
        'SourceSystemSpecificAttribute8': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SourceSystemSpecificAttributeTypeV1':
      return flaskRestPlusAPI.model('SourceSystemSpecificAttributeTypeV1', {
        'Type': fields.String(default='',description='This is used to define what is this attribute e.g. Banner Internal Identification'),
        'Value': fields.String(default='',description='This is the value of above type e.g. 001'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:DistributionLineTypeV1':
      return flaskRestPlusAPI.model('DistributionLineTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'DistributionID': fields.String(default='',description='Identifier for the Distribution record.'),
        })),
        'AccountClass': fields.String(default='',description='Account Class for this distribution e.g. Freight, Receivable, Revenue. This needs to be one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_AccountClass.dvm'),
        #Element Amount has a type that is not catered for (xsd:decimal) 0
        'AcctdAmount': fields.String(default='',description='Amount of this record in the functional currency - is this GBP?'),
        'Percent': fields.String(default='',description='Percent of the line amount represented by this record'),
        'GLCodeCombination': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/GLCodeCombinationSegment:GLCodeCombinationSegmentCodeTypeV1')),
        'Comments': fields.String(default='',description='Comment about the revenue distribution.'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:TransactionLineTypeV1':
      return flaskRestPlusAPI.model('TransactionLineTypeV1', {
        'Identification': fields.Nested(flaskRestPlusAPI.model('InlineIdentificationType', {
          'LineID': fields.String(default='',description='Unique identifier for TransactionLineType'),
        })),
        #Element LinkToTrxLineId has a type that is not catered for (xsd:int) 0
        #Element LineNumber has a type that is not catered for (xsd:int) 0
        'RelatedCustomerTransactionLine': fields.Nested(flaskRestPlusAPI.model('InlineRelatedCustomerTransactionLineType', {
          'InterfaceLineAttributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceLineAttributeTypeV1')),
        })),
        'LineType': fields.String(default='',description='What is this and what are the possible values? This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_LineType.dvm'),
        'Description': fields.String(default='',description='Line description'),
        'TransactionReasonCode': fields.String(default='',description='TransactionReasonCode e.g Credit and Rebill, ZC This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\ARBilling\V1\XXIC_TransactionReasonCode.dvm'),
        #Element QuantityInvoiced has a type that is not catered for (xsd:int) 0
        #Element UnitSellingPrice has a type that is not catered for (xsd:decimal) 0
        #Element Amount has a type that is not catered for (xsd:int) 0
        'Attributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:LineAttributeTypeV1')),
        'InterfaceLineAttributes': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:InterfaceLineAttributeTypeV1')),
        'DistributionLines': fields.Nested(flaskRestPlusAPI.model('InlineDistributionLinesType', {
          'DistributionLine': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:DistributionLineTypeV1'))),
        })),
        'SalesCreditsLines': fields.Nested(flaskRestPlusAPI.model('InlineSalesCreditsLinesType', {
          'SalesCreditsLine': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:SalesCreditsLineTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CurrencyType:CurrencyTypeV1':
      return flaskRestPlusAPI.model('CurrencyTypeV1', {
        'CurrencyCode': fields.String(default='',description='This needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_CBO\V1\XXIC_CurrencyCode.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CustomerSite:CustomerSiteReferenceTypeV1':
      return flaskRestPlusAPI.model('CustomerSiteReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CustomerSite:IdentificationTypeV1')),
        'SiteID': fields.String(default='',description='This is unique identifier for customer address location'),
        'UniqueBill_ToLocationCriteria': fields.String(default='',description='If Site ID is missing unique bill to location criteria can be used to find address in ICIS. e.g. Location Creteria "Registry" will use customer\'s address with site Location defined as Registry'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/CustomerSite:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'CID': fields.String(default='',description='Unique customer identifier'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CBO/V1/GLCodeCombinationSegment:GLCodeCombinationSegmentCodeTypeV1':
      return flaskRestPlusAPI.model('GLCodeCombinationSegmentCodeTypeV1', {
        #Element Company has a type that is not catered for () 0
        #Element CostCentre has a type that is not catered for () 0
        #Element ProjectActivity has a type that is not catered for () 0
        #Element Analysis has a type that is not catered for () 0
        #Element Indicator has a type that is not catered for () 0
        #Element Sub1 has a type that is not catered for () 0
        #Element Sub2 has a type that is not catered for () 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonRBO:PersonReferenceTypeV1':
      return flaskRestPlusAPI.model('PersonReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonRBO:IdentificationTypeV1')),
        'FirstName': fields.String(default='',description='This is person first name'),
        'LastName': fields.String(default='',description='This will be the person last name/ Family Name/Surname'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Person/V1/PersonRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'CID': fields.String(default='',description='College CID for the person'),
        'UCASPERID': fields.String(default='',description='UCAS Personal ID for the person'),
        'EMBARKID': fields.String(default='',description='Embark Online Application ID for the student applicant'),
        'NINumber': fields.String(default='',description='National Insurance Number'),
        'HESAID': fields.String(default='',description='HESA Identifier'),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('ARBillingEBOV1', {
    'ARBillingEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARBilling/V1/ARBillingEBO:ARBillingEBOTypeV1')),

  })

