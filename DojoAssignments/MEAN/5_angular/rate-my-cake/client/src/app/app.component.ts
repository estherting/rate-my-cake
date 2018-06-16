import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'app';
  cakes = [];
  newCake = {baker: "", imgUrl: ""};
  newComment = {comment: "", stars: 5}
  selectedCake: any;

  constructor(private _httpService: HttpService){
  }
  ngOnInit(){
    this.getAllCakes();
  }

  getAllCakes(){
    let observable = this._httpService.getAllCakes();
    observable.subscribe(data => {
      console.log('got cakes back!', data);
      this.cakes = data['cakes']
    })
  }

  submitCake(){
    let observable = this._httpService.submitCake(this.newCake);
    observable.subscribe(data => {
      console.log('got submitted cake back', data);
      this.cake = data['cake']
      this.getAllCakes();
    })
    this.newCake = {baker: "", imgUrl: ""}
  }

  rate(cakeId){
    // re-calculate average rating
    let observable = this._httpService.getOneCake(cakeId);
    observable.subscribe(data => {
      let totalStars: number = Number(this.newComment.stars);
      for (let comment of data['cakes'][0]['comments']){
        totalStars += comment.stars;
      }
      let avgRating= Math.round((totalStars / (data['cakes'][0]['comments'].length+1))*10)/10;
      let observable = this._httpService.rate({avgRating: avgRating, comment: this.newComment, cakeId:cakeId});
      observable.subscribe(data => {
        console.log('got comment back after submitting', data);
        this.newComment = {comment: "", stars: 5};
        this.getAllCakes();
      })
    })
  }

  cakeToShow(cake){
    this.selectedCake = cake;
  }
}
