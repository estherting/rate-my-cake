import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';  // 2. import HttpClientModule so we can make http requests
import { HttpService } from './http.service'; // 1. register the service
import { FormsModule } from '@angular/forms'; // import formsmodule for ngModel

import { AppComponent } from './app.component';
import { TaskComponent } from './task/task.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,          // 2. import HttpClientModule
    FormsModule,
  ],
  providers: [HttpService],   // 1. register the service
  bootstrap: [AppComponent]
})
export class AppModule { }
