# pip install gql 
# pip install RequestsHTTPTransport

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

_transport = RequestsHTTPTransport(
    url='Your URL',  # like https://graphql-pokemon.now.sh/
    use_json=True,
)


client = Client(
    transport=_transport,
    fetch_schema_from_transport=True,
)

#input your query done in graphql below =)

query = gql(""" 
{

    pokemon(name: "Pikachu") {
        attacks {
            special {
                name
            }
        }
    }
}
""")
#Execute your query Graphql
print(client.execute(query)) 