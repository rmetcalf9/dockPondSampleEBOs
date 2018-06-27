from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('Animal', {
      'name': fields.String(default='',description='What is the name of this animal? (Must be unique)'),
      'type': fields.String(default='',description='What type of animal are they?'),
      'HatedByRobert': fields.Boolean(default=False,description='Does Robert hate this animal?')
  })
