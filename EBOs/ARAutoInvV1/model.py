
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ARAutoInvEBOTypeV1':
      return flaskRestPlusAPI.model('ARAutoInvEBOTypeV1', {
        #Element ORG_ID has a type that is not catered for (xsd:decimal) 0
        'BATCH_SOURCE_NAME': fields.String(default='',description=''),
        'Lookups': fields.Nested(flaskRestPlusAPI.model('InlineLookupsType', {
          'INTERFACE_LINE': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ATTTYPEV1')),
          'REF_LINE': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ATTTYPEV1')),
          'HDR': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ATTTYPEV1')),
        })),
        'ORIG_SYS_BATCH_NAME': fields.String(default='',description=''),
        'LINES_TBL': fields.Nested(flaskRestPlusAPI.model('InlineLINES_TBLType', {
          'Line': fields.List(fields.Nested(flaskRestPlusAPI.model('InlineLineType', {
            #Element INTERFACE_LINE_CONTEXT has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT1 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT2 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT3 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT4 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT5 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT6 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT7 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT8 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT9 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT10 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT11 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT12 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT13 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT14 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT15 has a type that is not catered for () 0
            #Element SET_OF_BOOKS_ID has a type that is not catered for (xsd:decimal) 0
            #Element LINE_TYPE has a type that is not catered for () 0
            #Element DESC has a type that is not catered for () 0
            #Element CURRENCY_CODE has a type that is not catered for () 0
            #Element AMOUNT has a type that is not catered for (xsd:decimal) 0
            #Element CUST_TRX_TYPE_NAME has a type that is not catered for () 0
            #Element TERM_NAME has a type that is not catered for () 0
            #Element ORIG_SYS_BILL_CUST_ID has a type that is not catered for (xsd:decimal) 0
            #Element ORIG_SYS_BILL_ADDRESS_ID has a type that is not catered for (xsd:decimal) 0
            #Element ORIG_SYS_BILL_CONTACT_ID has a type that is not catered for (xsd:decimal) 0
            #Element CONVERSION_TYPE has a type that is not catered for () 0
            #Element CONVERSION_DATE has a type that is not catered for (xsd:dateTime) 0
            #Element CONVERSION_RATE has a type that is not catered for (xsd:decimal) 0
            #Element TRX_DATE has a type that is not catered for (xsd:dateTime) 0
            #Element GL_DATE has a type that is not catered for (xsd:dateTime) 0
            #Element TRX_NUM has a type that is not catered for () 0
            #Element QTY has a type that is not catered for (xsd:decimal) 0
            #Element QTY_ORDERED has a type that is not catered for (xsd:decimal) 0
            #Element UNIT_SELLING_PRICE has a type that is not catered for (xsd:decimal) 0
            #Element UNIT_STANDARD_PRICE has a type that is not catered for (xsd:decimal) 0
            #Element PRINTING_OPTION has a type that is not catered for () 0
            #Element REASON_CODE has a type that is not catered for () 0
            #Element TAX_CODE has a type that is not catered for () 0
            #Element PRIMARY_SALESREP_NUM has a type that is not catered for () 0
            #Element PURCHASE_ORDER has a type that is not catered for () 0
            #Element REF_LINE_CONTEXT has a type that is not catered for () 0
            #Element REF_LINE_ATT1 has a type that is not catered for () 0
            #Element REF_LINE_ATT2 has a type that is not catered for () 0
            #Element REF_LINE_ATT3 has a type that is not catered for () 0
            #Element REF_LINE_ATT4 has a type that is not catered for () 0
            #Element REF_LINE_ATT5 has a type that is not catered for () 0
            #Element REF_LINE_ATT6 has a type that is not catered for () 0
            #Element REF_LINE_ATT7 has a type that is not catered for () 0
            #Element REF_LINE_ATT8 has a type that is not catered for () 0
            #Element REF_LINE_ATT9 has a type that is not catered for () 0
            #Element REF_LINE_ATT10 has a type that is not catered for () 0
            #Element REF_LINE_ATT11 has a type that is not catered for () 0
            #Element REF_LINE_ATT12 has a type that is not catered for () 0
            #Element REF_LINE_ATT13 has a type that is not catered for () 0
            #Element REF_LINE_ATT14 has a type that is not catered for () 0
            #Element REF_LINE_ATT15 has a type that is not catered for () 0
            #Element ATT_CAT has a type that is not catered for () 0
            #Element ATT1 has a type that is not catered for () 0
            #Element ATT2 has a type that is not catered for () 0
            #Element ATT3 has a type that is not catered for () 0
            #Element ATT4 has a type that is not catered for () 0
            #Element ATT5 has a type that is not catered for () 0
            #Element ATT6 has a type that is not catered for () 0
            #Element ATT7 has a type that is not catered for () 0
            #Element ATT8 has a type that is not catered for () 0
            #Element ATT9 has a type that is not catered for () 0
            #Element ATT10 has a type that is not catered for () 0
            #Element ATT11 has a type that is not catered for () 0
            #Element ATT12 has a type that is not catered for () 0
            #Element ATT13 has a type that is not catered for () 0
            #Element ATT14 has a type that is not catered for () 0
            #Element ATT15 has a type that is not catered for () 0
            #Element HDR_ATT_CAT has a type that is not catered for () 0
            #Element HDR_ATT1 has a type that is not catered for () 0
            #Element HDR_ATT2 has a type that is not catered for () 0
            #Element HDR_ATT3 has a type that is not catered for () 0
            #Element HDR_ATT4 has a type that is not catered for () 0
            #Element HDR_ATT5 has a type that is not catered for () 0
            #Element HDR_ATT6 has a type that is not catered for () 0
            #Element HDR_ATT7 has a type that is not catered for () 0
            #Element HDR_ATT8 has a type that is not catered for () 0
            #Element HDR_ATT9 has a type that is not catered for () 0
            #Element HDR_ATT10 has a type that is not catered for () 0
            #Element HDR_ATT11 has a type that is not catered for () 0
            #Element HDR_ATT12 has a type that is not catered for () 0
            #Element HDR_ATT13 has a type that is not catered for () 0
            #Element HDR_ATT14 has a type that is not catered for () 0
            #Element HDR_ATT15 has a type that is not catered for () 0
            #Element COMMENTS has a type that is not catered for () 0
            #Element INTERNAL_NOTES has a type that is not catered for () 0
            #Element UOM_NAME has a type that is not catered for () 0
            #Element CREDIT_METHOD_FOR_INSTALLMENTS has a type that is not catered for () 0
            #Element INTERFACE_LINE_ID has a type that is not catered for (xsd:decimal) 0
            #Element INTERFACE_STATUS has a type that is not catered for () 0
            #Element CUST_TRX_ID has a type that is not catered for (xsd:decimal) 0
          }))),
        })),
        'DIST_TBL': fields.Nested(flaskRestPlusAPI.model('InlineDIST_TBLType', {
          'Dist': fields.List(fields.Nested(flaskRestPlusAPI.model('InlineDistType', {
            #Element INTERFACE_LINE_CONTEXT has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT1 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT2 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT3 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT4 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT5 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT6 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT7 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT8 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT9 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT10 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT11 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT12 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT13 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT14 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT15 has a type that is not catered for () 0
            #Element ACCOUNT_CLASS has a type that is not catered for () 0
            #Element AMOUNT has a type that is not catered for (xsd:decimal) 0
            #Element PERCENT has a type that is not catered for (xsd:decimal) 0
            #Element COMMENTS has a type that is not catered for () 0
            #Element SEG1 has a type that is not catered for () 0
            #Element SEG2 has a type that is not catered for () 0
            #Element SEG3 has a type that is not catered for () 0
            #Element SEG4 has a type that is not catered for () 0
            #Element SEG5 has a type that is not catered for () 0
            #Element SEG6 has a type that is not catered for () 0
            #Element SEG7 has a type that is not catered for () 0
            #Element SEG8 has a type that is not catered for () 0
            #Element SEG9 has a type that is not catered for () 0
            #Element SEG10 has a type that is not catered for () 0
            #Element SEG11 has a type that is not catered for () 0
            #Element SEG12 has a type that is not catered for () 0
            #Element SEG13 has a type that is not catered for () 0
            #Element SEG14 has a type that is not catered for () 0
            #Element SEG15 has a type that is not catered for () 0
            #Element SEG16 has a type that is not catered for () 0
            #Element SEG17 has a type that is not catered for () 0
            #Element SEG18 has a type that is not catered for () 0
            #Element SEG19 has a type that is not catered for () 0
            #Element SEG20 has a type that is not catered for () 0
            #Element SEG21 has a type that is not catered for () 0
            #Element SEG22 has a type that is not catered for () 0
            #Element SEG23 has a type that is not catered for () 0
            #Element SEG24 has a type that is not catered for () 0
            #Element SEG25 has a type that is not catered for () 0
            #Element SEG26 has a type that is not catered for () 0
            #Element SEG27 has a type that is not catered for () 0
            #Element SEG28 has a type that is not catered for () 0
            #Element SEG29 has a type that is not catered for () 0
            #Element SEG30 has a type that is not catered for () 0
          }))),
        })),
        'CREDITS_TBL': fields.Nested(flaskRestPlusAPI.model('InlineCREDITS_TBLType', {
          'Credit': fields.List(fields.Nested(flaskRestPlusAPI.model('InlineCreditType', {
            #Element INTERFACE_LINE_CONTEXT has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT1 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT2 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT3 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT4 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT5 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT6 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT7 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT8 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT9 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT10 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT11 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT12 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT13 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT14 has a type that is not catered for () 0
            #Element INTERFACE_LINE_ATT15 has a type that is not catered for () 0
            #Element SALESREP_NUM has a type that is not catered for () 0
            #Element SALES_CREDIT_TYPE_NAME has a type that is not catered for () 0
            #Element SALES_CREDIT_AMOUNT_SPLIT has a type that is not catered for (xsd:decimal) 0
            #Element SALES_CREDIT_PERCENT_SPLIT has a type that is not catered for (xsd:decimal) 0
          }))),
        })),
        'Response': fields.Nested(flaskRestPlusAPI.model('InlineResponseType', {
          #Element BATCHFAIL has a type that is not catered for (xsd:decimal) 0
          'BATCHFAILMSG': fields.String(default='',description=''),
          #Element AI_REQUEST_ID has a type that is not catered for (xsd:decimal) 0
          #Element Loaded_CREDITS_RECCNT has a type that is not catered for (xsd:decimal) 0
          #Element Loaded_CREDITS_SUMAMNT has a type that is not catered for (xsd:decimal) 0
        })),
        'ERRORS_RSP_TBL': fields.Nested(flaskRestPlusAPI.model('InlineERRORS_RSP_TBLType', {
          'ErrorRsp': fields.List(fields.Nested(flaskRestPlusAPI.model('InlineErrorRspType', {
            #Element INTERFACE_LINE_ID has a type that is not catered for (xsd:decimal) 0
            #Element MSG_TEXT has a type that is not catered for () 0
            #Element INVALID_VALUE has a type that is not catered for () 0
          }))),
        })),
        'CHECKSUM': fields.Nested(flaskRestPlusAPI.model('InlineCHECKSUMType', {
          #Element LINES_RECCNT has a type that is not catered for (xsd:decimal) 0
          #Element CREDITS_RECCNT has a type that is not catered for (xsd:decimal) 0
          #Element DISTRIB_RECCNT has a type that is not catered for (xsd:decimal) 0
          #Element LINES_SUMAMNT has a type that is not catered for (xsd:decimal) 0
          #Element CREDITS_SUMAMNTSP has a type that is not catered for (xsd:decimal) 0
          #Element DISTRIB_SUMAMNT has a type that is not catered for (xsd:decimal) 0
          #Element ERRORS_RECCNT has a type that is not catered for (xsd:decimal) 0
          #Element LINES_ERRCNT has a type that is not catered for (xsd:decimal) 0
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ATTTYPEV1':
      return flaskRestPlusAPI.model('ATTTYPEV1', {
        #Element ATT1 has a type that is not catered for () 0
        #Element ATT2 has a type that is not catered for () 0
        #Element ATT3 has a type that is not catered for () 0
        #Element ATT4 has a type that is not catered for () 0
        #Element ATT5 has a type that is not catered for () 0
        #Element ATT6 has a type that is not catered for () 0
        #Element ATT7 has a type that is not catered for () 0
        #Element ATT8 has a type that is not catered for () 0
        #Element ATT9 has a type that is not catered for () 0
        #Element ATT10 has a type that is not catered for () 0
        #Element ATT11 has a type that is not catered for () 0
        #Element ATT12 has a type that is not catered for () 0
        #Element ATT13 has a type that is not catered for () 0
        #Element ATT14 has a type that is not catered for () 0
        #Element ATT15 has a type that is not catered for () 0

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('ARAutoInvEBOV1', {
    'ARAutoInvEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/ARAutoInv/V1:ARAutoInvEBOTypeV1')),

  })

