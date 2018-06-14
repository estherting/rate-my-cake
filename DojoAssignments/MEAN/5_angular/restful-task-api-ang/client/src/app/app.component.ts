import { Component, OnInit } from '@angular/core';
import { HttpService } from './http.service';   // dependency injection

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'MEAN';
  tasks =[];
  taskById = [];
  constructor(private _httpService: HttpService){   // make it an attribute to the class
  }
  ngOnInit() {
    // this.getTasksFromService();
  }
  getTasksFromService(){
    let observable = this._httpService.getTasks()
    observable.subscribe(data => {
      console.log('Got our data!', data);
      this.tasks = data['tasks'];   // save data in an attribute
    })
  }
  getTaskById(id){
    let observable = this._httpService.getTaskById(id: String);
    console.log('ID: ', id)
    observable.subscribe(data => {
      console.log('Got one task by ID!', data);
      this.taskById = data['task'];   // save data in an attribute
    })
  }
}
