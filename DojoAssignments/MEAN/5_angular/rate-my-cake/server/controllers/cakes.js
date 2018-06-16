Cake = require('../models/cake.js').cake;
Comment = require('../models/cake.js').comment;

module.exports = {
  showAll: showAll,
  show: show,
  submitCake: submitCake,
  comment: comment,
  showAllComments: showAllComments,
  deleteCake: deleteCake,

}

function showAll(req, res) {
  Cake.find({}, function(err, result){
    if(err){
      console.log('err in finding all cakes')
    }
    console.log('got cakes:', result)
    res.json({cakes: result})
  })
}

function show(req, res) {
  Cake.find({_id: req.params.id}, function(err, result){
    if(err){
      console.log('err in finding all cakes')
    }
    console.log('got cakes:', result)
    res.json({cakes: result})
  })
}

function submitCake(req, res){
  Cake.create(req.body, function(err, result){
    if(err){
      console.log('Error in submitting cake', err);
      res.send(err);
    }
    console.log('successfully submitted cake', result);
    res.json({cake: result})
  });
}

function comment(req, res){
  Comment.create(req.body.comment, function(err, result){
    if(err){
      console.log('Error in commenting')
    }
    console.log('successfully commented on a cake', result)
    // add comment and average rating into cake
    Cake.findOneAndUpdate({_id: req.body.cakeId}, {$set: {avgRating: req.body.avgRating}, $push: {comments: req.body.comment}}, {new:true}, function(err, data){
      if(err){
        console.log('could not update cake with comment')
      }
      console.log('updated cake with new comment: ', data)
    })
    res.json({comment: result})
  })
}

function showAllComments(req, res) {
  Comment.find({}, function(err, result){
    if(err){
      console.log('err in finding all comments')
    }
    console.log('got comments:', result)
    res.json({cakes: result})
  })
}

function deleteCake(req, res){
  Cake.deleteOne({_id: req.params.id}, function(err, result){
    if(err){
      console.log('did not remove cake')
      res.send(err)
    }
    else {
      console.log('removed cake')
    }
  })
  // res.redirect('/')
}
