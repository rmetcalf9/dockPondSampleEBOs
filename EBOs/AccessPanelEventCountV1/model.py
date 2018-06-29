
from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  #Function must be declared inside getModel function as this is the only part that is imported by dockPond
  def getTypeModel(flaskRestPlusAPI, typeName):
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:AccessPanelEventCountEBOTypeV1':
      return flaskRestPlusAPI.model('AccessPanelEventCountEBOTypeV1', {
        'Rows': fields.Nested(flaskRestPlusAPI.model('InlineRowsType', {
          'Row': fields.List(fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:RowTypeV1'))),
        })),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:RowTypeV1':
      return flaskRestPlusAPI.model('RowTypeV1', {
        'SystemName': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:MachineTypeV1')),
        'Period': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:PeriodTypeV1')),
        #Element Count has a type that is not catered for (xsd:integer) 0

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:MachineTypeV1':
      return flaskRestPlusAPI.model('MachineTypeV1', {
        'Identifier': fields.String(default='',description=''),

      })
    if typeName=='http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:PeriodTypeV1':
      return flaskRestPlusAPI.model('PeriodTypeV1', {
        #Element Start has a type that is not catered for (xsd:dateTime) 0
        #Element End has a type that is not catered for (xsd:dateTime) 0

      })
    raise Exception('Searching for unknown type')


  return flaskRestPlusAPI.model('AccessPanelEventCountEBOV1', {
    'AccessPanelEventCountEBO': fields.Nested(getTypeModel(flaskRestPlusAPI, 'http://ic.ac.uk/AIAMetaData/AIAComponents/EnterpriseObjectLibrary/Core/IC_EBO/AccessPanelEventCount/V1:AccessPanelEventCountEBOTypeV1')),

  })

