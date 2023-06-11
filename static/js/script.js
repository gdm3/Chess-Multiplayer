var config = {
  draggable: true,
  position: 'start',
  onDrop
}
const boardd = Chessboard2('board', config)

function onDrop (source, target) {

  var cur_board = boardd.fen()
  // see if the move is legal
  console.log(source.target, source.source)
  
  axios.post('/', {
    source: source.source,
    target: source.target
  })
  .then(function (response) {
    console.log(response.data);
    if(response.data.processed == false){
      console.log(cur_board, boardd.fen())
      boardd.fen(cur_board)
    }
  })
  .catch(function (error) {
    console.log(error);
  });
}

