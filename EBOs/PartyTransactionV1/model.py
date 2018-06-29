
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:PartyTransactionEBOTypeV1':
      return flaskRestPlusAPI.model('PartyTransactionEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:IdentificationTypeV1')),
        'UserType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:CodeMeaningTypeV1')),
        'SystemType': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:CodeMeaningTypeV1')),
        #Element TrxDate has a type that is not catered for (xsd:dateTime) 0
        'InternalNotes': fields.String(default='',description=''),
        'SpecialInstructions': fields.String(default='',description=''),
        'Comments': fields.String(default='',description=''),
        #Element Status has a type that is not catered for (StatusType) 0
        'BatchSource': fields.String(default='',description=''),
        'BatchName': fields.String(default='',description=''),
        'BatchReference': fields.String(default='',description=''),
        'PONumber': fields.String(default='',description=''),
        'Terms': fields.String(default='',description=''),
        'BillTo': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:UsageTypeV1')),
        'ShipTo': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:UsageTypeV1')),
        'SoldTo': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:UsageTypeV1')),
        'RemitTo': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:UsageTypeV1')),
        'PartyTransactionRefs': fields.Nested(flaskRestPlusAPI.model('InlinePartyTransactionRefsType', {
          'PartyTransactionRef': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:PartyTransactionRefTypeV1'))),
        })),
        'ScheduledPayments': fields.Nested(flaskRestPlusAPI.model('InlineScheduledPaymentsType', {
          'ScheduledPayment': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:ScheduledPaymentTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:ScheduledPaymentTypeV1':
      return flaskRestPlusAPI.model('ScheduledPaymentTypeV1', {
        #Element TermNumber has a type that is not catered for (xsd:integer) 0
        'Type': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:CodeMeaningTypeV1')),
        #Element DueDate has a type that is not catered for (xsd:dateTime) 0
        #Element ActualDateClosed has a type that is not catered for (xsd:dateTime) 0
        'CurrencyCode': fields.String(default='',description=''),
        #Element Status has a type that is not catered for (StatusType) 0
        #Element AcctAmountDueRemaining has a type that is not catered for (xsd:decimal) 0
        #Element AmountDueOriginal has a type that is not catered for (xsd:decimal) 0
        #Element AmountDueRemaining has a type that is not catered for (xsd:decimal) 0
        #Element FreightOriginal has a type that is not catered for (xsd:decimal) 0
        #Element FreightRemaining has a type that is not catered for (xsd:decimal) 0
        #Element TaxOriginal has a type that is not catered for (xsd:decimal) 0
        #Element TaxRemaining has a type that is not catered for (xsd:decimal) 0
        #Element AmountApplied has a type that is not catered for (xsd:decimal) 0
        #Element AmountAdjusted has a type that is not catered for (xsd:decimal) 0
        #Element AmountInDispute has a type that is not catered for (xsd:decimal) 0
        #Element AmountCredited has a type that is not catered for (xsd:decimal) 0
        'ExchangeRateType': fields.String(default='',description=''),
        #Element ExchangeDate has a type that is not catered for (xsd:dateTime) 0
        #Element ExchangeRate has a type that is not catered for (xsd:decimal) 0
        'Comments': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:UsageTypeV1':
      return flaskRestPlusAPI.model('UsageTypeV1', {
        'PartyAccountRef': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyAccount/V1/PartyAccountRBO:PartyAccountRefTypeV1')),
        'PhysicalAddress': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CommonEBO/V1/PhysicalAddress:PhysicalAddressTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:CodeMeaningTypeV1':
      return flaskRestPlusAPI.model('CodeMeaningTypeV1', {
        'Code': fields.String(default='',description=''),
        'Meaning': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:PrimaryKeyTypeV1':
      return flaskRestPlusAPI.model('PrimaryKeyTypeV1', {
        'TrxID': fields.String(default='',description=''),
        #Element SubLedgerType has a type that is not catered for (SubLedgerType) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:FirstAlternateKeyTypeV1':
      return flaskRestPlusAPI.model('FirstAlternateKeyTypeV1', {
        'TrxNumber': fields.String(default='',description=''),
        'AccountNumber': fields.String(default='',description=''),
        'AddressNumber': fields.String(default='',description=''),
        'OrgID': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:SecondAlternateKeyTypeV1':
      return flaskRestPlusAPI.model('SecondAlternateKeyTypeV1', {
        'VoucherNumber': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'PrimaryKey': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:PrimaryKeyTypeV1')),
        'FirstAlternateKey': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:FirstAlternateKeyTypeV1')),
        'SecondAlternateKey': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:SecondAlternateKeyTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:PartyTransactionRefTypeV1':
      return flaskRestPlusAPI.model('PartyTransactionRefTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionRBO:IdentificationTypeV1')),
        'SystemTypeCode': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyAccount/V1/PartyAccountRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'AccountNumber': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyAccount/V1/PartyAccountRBO:PartyAccountRefTypeV1':
      return flaskRestPlusAPI.model('PartyAccountRefTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyAccount/V1/PartyAccountRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CommonEBO/V1/PhysicalAddress:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'AddressNumber': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CommonEBO/V1/PhysicalAddress:PhysicalAddressTypeV1':
      return flaskRestPlusAPI.model('PhysicalAddressTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_CommonEBO/V1/PhysicalAddress:IdentificationTypeV1')),
        'Address1': fields.String(default='',description=''),
        'Address2': fields.String(default='',description=''),
        'Address3': fields.String(default='',description=''),
        'Address4': fields.String(default='',description=''),
        'Country': fields.String(default='',description=''),
        'City': fields.String(default='',description=''),
        'PostalCode': fields.String(default='',description=''),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('PartyTransactionEBOV1', {
    'PartyTransactionEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/PartyTransaction/V1/PartyTransactionEBO:PartyTransactionEBOTypeV1')),

  })

