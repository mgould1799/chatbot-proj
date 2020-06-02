import {Component, OnInit} from '@angular/core';
import { ChatbotApiService } from 'services/chatbot.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'frontend';
  messages = []

  constructor(private chatBotService: ChatbotApiService) {}
  ngOnInit(){
    let messageList = this.chatBotService.ListMessages();
    this.messages = messageList['result'];
    console.log(this.messages);
  }
}
