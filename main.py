from flask import Flask, render_template, request, jsonify
from chess import Board

app = Flask(__name__)

board = Board()


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html', chess_board=board)
  else:
    data = request.get_json()
    target = data['target']
    source = data['source']
    target_letter = target[0]
    target_number = target[1]
    source_letter = source[0]
    source_number = source[1]

    results = {'processed': board.validate_move((source_letter, int(source_number)), (target_letter, int(target_number)))}
    return jsonify(results)

@app.route('/<id>')
def game(id):
  return "hello" + id
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
