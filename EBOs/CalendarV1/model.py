
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Calendar/V1/CalendarEBO:CalendarsTypeV1':
      return flaskRestPlusAPI.model('CalendarsTypeV1', {
        'Identification': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Calendar/V1/CalendarEBO:IdentificationTypeV1')),
        'Description': fields.String(default='',description=''),
        #Element StartDate has a type that is not catered for (xsd:dateTime) 0
        #Element EndDate has a type that is not catered for (xsd:dateTime) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/Calendar/V1/CalendarEBO:IdentificationTypeV1':
      return flaskRestPlusAPI.model('IdentificationTypeV1', {
        'CalendarCode': fields.String(default='',description=''),
        'CalendarSeqNumber': fields.String(default='',description=''),

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('V1', {

  })

