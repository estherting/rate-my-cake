var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/cake');

const CommentSchema = new mongoose.Schema({
  comment: {type: String},
  stars: {type: Number, required: true}
}, {timestamps: true})

const CakeSchema = new mongoose.Schema({
  baker: {type: String, required: true},
  imgUrl: {type: String, required: true},
  avgRating: {type: Number, default: 0},
  comments: [CommentSchema],
}, {timestamps: true})

// mongoose.Promise = global.Promise;

module.exports = {
  cake: mongoose.model('Cake', CakeSchema),
  comment: mongoose.model('Comment', CommentSchema),
}
