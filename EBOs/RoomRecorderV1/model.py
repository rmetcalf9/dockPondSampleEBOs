
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/RoomRecorder/V1/RoomRecorderEBO:RoomRecorderEBOTypeV1':
      return flaskRestPlusAPI.model('RoomRecorderEBOTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/RoomRecorder/V1/RoomRecorderEBO:IdentificationTypeV1')),
        'RoomID': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1')),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/RoomRecorder/V1/RoomRecorderEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'RecorderID': fields.String(default='',description='Cannonical Mashine Number identifier this needs to match one of the values from this dvm - AIAMetaData\AIAComponents\EnterpriseObjectLibrary\Core\IC_EBO\RoomRecorder\V1\XXIC_RoomRecorder.dvm'),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:SpaceReferenceTypeV1':
      return flaskRestPlusAPI.model('SpaceReferenceTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1')),
        'Name': fields.String(default='',description=''),
        'Description': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Space/V1/SpaceRBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'Code': fields.String(default='',description='Code of the Space will consist of BuildingCode-FloorCode-SpaceCode as SpaceCode itself is not unique by itself'),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('RoomRecorderEBOV1', {
    'RoomRecorderEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/RoomRecorder/V1/RoomRecorderEBO:RoomRecorderEBOTypeV1')),

  })

