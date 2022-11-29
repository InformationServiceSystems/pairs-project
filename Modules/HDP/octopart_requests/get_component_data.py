from six.moves import urllib
import json


class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headername = None

    def execute(self, query, variables):
        return self._send(query, variables)


    def inject_token(self, token, headername='token'):
        self.token = token
        self.headername = headername

    def _send(self, query, variables):
        
        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers[self.headername] = '{}'.format(self.token)

        req = urllib.request.Request(self.endpoint, json.dumps(data).encode('utf-8'), headers)
 
        try:
            response = urllib.request.urlopen(req)
            return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print((e.read()))
            print('')
            raise e

    def search_part(client, query, limit):
        
        query_string = '''
       query ($q: String! $l: Int!){
      supSearch(q: $q limit: $l) {
        results {
          part {
            mpn
            manufacturer {
              displayFlag
              name
            }
            sellers() {
                company {
                    name
                }
            }
            medianPrice1000 {
                price
            }
            totalAvail
            category {
                name
            }
            estimatedFactoryLeadDays
          }
        }
      }
    }
        '''

        resp = client.execute(query_string, {'q': query, 'l': limit})
        return resp
