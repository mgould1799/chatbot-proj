import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';

import { catchError } from 'rxjs/operators';



@Injectable()
export class ChatbotApiService {

  constructor(private http: HttpClient) {}

  // POST method to send slack message
  async SendMessage(message) {
    return await this.http.post('https://cors-anywhere.herokuapp.com/http://slack-api-dev.us-east-1.elasticbeanstalk.com/bot/message?message='+message, {}).
    toPromise().then(response => {
      return {response: response}
    });
  }

  async ListMessages() {
    return await this.http.get('https://cors-anywhere.herokuapp.com/http://slack-api-dev.us-east-1.elasticbeanstalk.com/bot/list/message').
    toPromise().then(response => {
      return {response: response}
    });
  }
}

