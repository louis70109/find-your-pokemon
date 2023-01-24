import requests
def find_CN_by_EN_name(request_json, name='Fire Punch') -> list:
  return_data = []
  data = request_json['data']
  for da in data:
    if da['nameEn'] == name:
      return_data = da
      break
  return return_data
