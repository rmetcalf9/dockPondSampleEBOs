
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/User/V1/UserEBO:UserEBOTypeV1':
      return flaskRestPlusAPI.model('UserEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/User/V1/UserEBO:IdentificationTypeV1')),
        'CID': fields.String(default='',description='College CID'),
        'Status': fields.String(default='',description='Status of the User'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/User/V1/UserEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'UserName': fields.String(default='',description='Cannonical User identifier'),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('UserEBOV1', {
    'UserEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/User/V1/UserEBO:UserEBOTypeV1')),

  })

