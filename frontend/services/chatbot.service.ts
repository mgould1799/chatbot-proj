import {Injectable} from '@angular/core';
import {HttpClient, HttpErrorResponse, HttpParams} from '@angular/common/http';
import 'rxjs/add/operator/catch';


@Injectable()
export class ChatbotApiService {

  constructor(private http: HttpClient) {}

  // GET method to send slack message
  async SendMessage(message) {
    let params = new HttpClient().set('message', message);
    return await this.http.get('', {params})
  }
}
