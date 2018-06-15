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
  newTask = {title: "", description: ""}

  constructor(private _httpService: HttpService){   // make it an attribute to the class
  }
  ngOnInit() {
    this.getTasksFromService();
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
  createTask(){
    console.log('entered createTask')
    let observable = this._httpService.createTask(this.newTask);
    observable.subscribe(data => {
      console.log('Created this task!: ', data);
      this.getTasksFromService();
      this.newTask = {title: "", description: ""}
    })
  }
  editTask(this.taskById){
    let observable = this._httpService.editTask(this.taskById);
    observable.subscribe(data => {
      console.log('edited this data: ', data);
      this.getTasksFromService();
      this.taskById = [];
    })
  }
  deleteTask(id){
    console.log('got into delete')
    let observable = this._httpService.deleteTask(id);
    observable.subscribe(response => {
      console.log(response);
    })
    this.getTasksFromService();
  }
}
