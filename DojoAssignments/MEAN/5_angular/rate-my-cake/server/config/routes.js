const Handler = require('../controllers/cakes.js');

module.exports = function Routify(app){
  // get all cakes
  app.get('/cakes', function(req, res){
    Handler.showAll(req, res);
  });

  // get one cake by ID
  app.get('/cakes/:id', function(req, res){
    Handler.show(req,res);
  });

  // submit a cake
  app.post('/cakes', function(req, res){
    Handler.submitCake(req, res);
  })

  // rate a cake (comment)
  app.post('/comments', function(req, res){
    Handler.comment(req, res);
  })

  // update cake
  app.put('/cakes/:id', function(req, res){
    Handler.updateCake(req, res);
  })

  // delete cake
  app.delete('/cakes/:id', function(req, res){
    Handler.deleteCake(req, res);
  })

}
