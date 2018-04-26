from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('AnimalGender', {
      'id': fields.String(default='',description='Unique guid for this gender'),
      'text': fields.String(default='',description='User displayed text')
  })
