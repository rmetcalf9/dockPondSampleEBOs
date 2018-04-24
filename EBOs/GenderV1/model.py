from flask_restplus import fields

def getModel(appObj):
  return appObj.flastRestPlusAPIObject.model('AnimalGender', {
      'id': fields.String(default='',description='Unique guid for this gender'),
      'text': fields.String(default='',description='User displayed text')
  })
