from flask_restplus import fields

def getModel(flaskRestPlusAPI):
  return flaskRestPlusAPI.model('New', {
      'id': fields.String(default='',description='Unique guid for this thingy'),
      'text': fields.String(default='',description='User displayed text')
  })
