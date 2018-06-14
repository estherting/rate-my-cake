import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';    // 3. dependency injection


@Injectable({
  providedIn: 'root'
})
export class HttpService {
  constructor(private _http: HttpClient) {    // make it an attribute in the class..._http is going to be a type of HttpClient
    // this.getTasks();
    this.getTaskById();
  }

  getTasks(){
      return this._http.get('/tasks'); // return the observable
   }
   postToServer(){
      return this._http.post('/tasks', task);
   }

   getTaskById(id: String){
     console.log("###################", id)
     return this._http.get('/tasks/'+id);
   }
}
