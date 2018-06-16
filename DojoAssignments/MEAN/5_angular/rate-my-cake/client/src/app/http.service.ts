import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class HttpService {

  constructor(private _http: HttpClient) { }
  getAllCakes(){
    return this._http.get('/cakes');
  }
  getOneCake(cakeId){
    return this._http.get('/cakes/'+cakeId)
  }
  submitCake(newCake){
    return this._http.post('/cakes', newCake)
  }
  rate(object){
    return this._http.post('/comments', object)
  }
}
