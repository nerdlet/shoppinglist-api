
from flask import Flask, jsonify, abort, make_response, request, url_for


app = Flask(__name__)


shoppinglist = [{
		'id':1,
		'name': u'fashion',
		'date_created': u'22/4/2017',
		
		},
		{
		'id':2,
		'name': u'groceries',
		'date_created': u'22/4/2017',
		
		}]


'''get a particular shoppinglist'''
@app.route('/dashboard/<int:shoppinglist_id>', methods = ['GET'])
def get_shopping_list(id):
	shoppinglist = filter(lambda t: t['id'] == shoppinglist_id, shoppinglists)
	if len(shoppinglist) == 0:
		abort(404)
	return jsonify({ 'shoppinglist' : shoppinglist[0] })



'''
Update of new shoppinglist
'''
@app.route('/dashboard/<int:shoppinglist_id>', methods = ['PUT'])

def update_shopping_list(id):
	ahoppinglist = filter(lambda t:t['id'] == shoppinglist_id, shoppinglists)
	if len(shoppinglist) == 0:
		abort(400)
	if not request.json:
		abort(400)
	if 'name' in request.json != unicode:
		abort(400)
	

	shoppinglist[0]['name'] = request.json.get('name', shoppinglist[0]['name'])
	shoppinglist[0]['date_created'] = request.json.get('date_created', shoppinglist[0]['date_created'])
	return jsonify({ 'shoppinglist' : shoppinglist[0] })

'''
deleting an existing shoppinglist
'''
@app.route('/dashboard/savelistitem/<int:shoppinglist_id>', methods = ['DELETE'])

def delete_shoppinglist(shoppinglist_id):
	shoppinglist = filter(lambda t: t['id'] == shoppinglist_id, shoppinglists)
	if len(shoppinglist) == 0:
		abort(400)
	shoppinglist.remove(shoppinglist[0])
	return jsonify({ 'result': True })
	
'''
create new shoppinglist
'''
@app.route('/dashboard/add/addnewitem', methods = ['POST'])
def create_shoppinglist():
	if not request.json or not 'name' in request.json:
		abort(400)
	shoppinglist = {
	'id': shoppinglist[-1]['id']+1,
	'name': request.json['name'],
	'date_created': request.json.get('date_created', ""),
	
	}
	shoppinglist.append(shoppinglist)
	return jsonify({ 'shoppinglist' : shoppinglist }),201



'''
get list of all  in shoppinglists
'''
@app.route('/dashboard/shopppinglist', methods = ['GET'])
def get_shoppinglists():
	return jsonify({ 'shoppinglist' : map(make_public_shoppinglist, shoppinglist) })


if __name__ == '__main__':
	app.run(debug = True)

