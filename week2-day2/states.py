state = str(raw_input('Enter a state to look up its capitol: ')).capitalize()

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                      'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                      'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

print state_dictionary.get(state, 'Capitol unknown.')     
