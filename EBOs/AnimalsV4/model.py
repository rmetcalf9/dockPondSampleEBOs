from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('Animal', {
      'name': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
      'type': fields.String(default='',description='What type of animal are they?'),
      'HatedByRobert': fields.Boolean(default=False,description='Does Robert hate this animal?'),
      'TestNestedStructure': fields.Nested(getTypeModel('ABC')),
      'TestListStructure': fields.list(fields.String(default='',description='list item')),
      'TestNestedListStructure': fields.list(fields.Nested(getTypeModel('DEF'))
  })

def getTypeModel(typeName):
  if typeName=='ABC':
    return flaskRestPlusAPI.model('ABC', {
        'Nname': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
        'Ttype': fields.String(default='',description='What type of animal are they?'),
        'HHatedByRobert': fields.Boolean(default=False,description='Does Robert hate this animal?')
    })
  if typeName=='DEF':
    return flaskRestPlusAPI.model('DEF', {
        'Nname': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
        'Nname2222': fields.String(default='',description='What is the name of this animal? (Must be unique)')
    })
  raise Exception('Searching for unknown type')