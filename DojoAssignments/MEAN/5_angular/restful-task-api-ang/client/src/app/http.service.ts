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
   createTask(newtask){
      return this._http.post('/tasks', newtask);
   }

   getTaskById(id: String){
     console.log("###################", id)
     return this._http.get('/tasks/'+id);
   }
   editTask(task){
     return this._http.put('/tasks/'+task[0]._id, task[0]);
   }
   deleteTask(id){
     console.log('got into delete in service. ID: ', id)
     return this._http.delete('/tasks/'+id);
   }
}
