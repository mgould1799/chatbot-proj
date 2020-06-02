import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import { catchError } from 'rxjs/operators';



@Injectable()
export class ChatbotApiService {

  constructor(private http: HttpClient) {}

  // POST method to send slack message
  async SendMessage(message) {
    return await this.http.post('http://localhost:5000/bot/message', {params: message}).
    toPromise().then(response => {
      return {response: response}
    });
  }

  async ListMessages() {
    return await this.http.get('http://localhost:5000/bot/list/message').
    toPromise().then(response => {
      return {response: response}
    });
  }
}

