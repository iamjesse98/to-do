import sys
import os
import json
import datetime
import io
from bottle import run, route

page = str('''
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css?family=Quicksand');
</style> 
</head>
<body style = "padding: 0; Margin: 0; font-family: 'Quicksand', sans-serif;">
<h1>{}</h1>
<h2>Today</h2>
<ul>
{}
</ul>
<h2>Tomorrow</h2>
<ul>
{}
</ul>
</body>
</html>
''')

try:
    to_unicode = unicode
except NameError:
    to_unicode = str

os.chdir("data/") #this will change directory to db directory 

try:
	if( sys.argv[1] == 'create' ):
		if os.path.exists(sys.argv[2] + '.json'):
			print('Already exits!!!')
		else:
			data = os.open(sys.argv[2] + '.json', os.O_CREAT)
			open(sys.argv[2] + '.json', 'w').write('{}')
	
	elif( sys.argv[1] == 'add' ):
		if os.path.exists(sys.argv[3] + '.json'):
			#add an item
			print("{} added to {}".format(sys.argv[2], sys.argv[3]))
			with open(sys.argv[3] + '.json') as data_file:    
				item = json.load(data_file)
			if (sys.argv[2] not in item.keys()):
				item.update({sys.argv[2] : {'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'target': sys.argv[4] + ' ' + sys.argv[5], 'desc': ' '.join(sys.argv[6:])}})
			else:
				if sys.argv[4] != item[sys.argv[2]]['target'].split()[1] or sys.argv[5] != item[sys.argv[2]]['target'].split()[-1]:
					item.update({sys.argv[2] : {'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'target': sys.argv[4] + ' ' + sys.argv[5], 'desc': ' '.join(sys.argv[6:])}})
				else:
					print('The item cannot be updated')
			with io.open(sys.argv[3] + '.json', 'w', encoding='utf8') as outfile:
    				str_ = json.dumps(item, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
    				outfile.write(to_unicode(str_))
		else:
			print("Can't add {0} to {1}\nThe file {1} doesn't exists!!!".format(sys.argv[2], sys.argv[3]))
	
	elif( sys.argv[1] == 'list' ):
		if os.path.exists(sys.argv[2] + '.json'):
			with open(sys.argv[2] + '.json') as data_file:
				d = json.load(data_file)
			print(*d.keys())
		else:
			print("There is no such user!!!")
	
	elif( sys.argv[1] == 'delete' ):
		print('successfully deleted')
		os.remove(sys.argv[2] + '.json')
	elif( sys.argv[1] == 'remove' ):
		if os.path.exists(sys.argv[3] + '.json'):
			print('successfully removed {} from {}'.format(sys.argv[2], sys.argv[3]))
			with open(sys.argv[3] + '.json') as data_file:
					d = json.load(data_file)
			del d[sys.argv[2]]
			open(sys.argv[3] + '.json', 'w').write('')
			with io.open(sys.argv[3] + '.json', 'w', encoding='utf8') as outfile:
    				outfile.write(to_unicode(json.dumps(d, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)))
		else:
			print("There is no such user!!!")

	elif( sys.argv[1] == 'show' ):
		@route('/show/<name>')
		def show(name):
			if os.path.exists(sys.argv[2] + '.json'):
				name = sys.argv[2]
				with open(sys.argv[2] + '.json') as data_file:
					d = json.load(data_file)
				ites = ''.join(['<li>{}</li>'.format(i) for i in d.keys()])
				return page.format(sys.argv[2], ites, ites)
		run(reload = True, debug = True)

	else:
		print("Read the manual properly")
except IndexError:
	print( open('readme.txt', 'r').read() )
