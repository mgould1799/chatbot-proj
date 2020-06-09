import {Component, OnInit} from '@angular/core';
import { ChatbotApiService } from 'services/chatbot.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'Slack Chatbot App';
  messages : any;
  inputMessage = '';

  constructor(private chatBotService: ChatbotApiService) {}
  async ngOnInit() {
    await this.listMessages();

  }

  async listMessages(){
    let messageList = await this.chatBotService.ListMessages();
    this.messages = messageList['response'];
  }
  async sendMessage(){
    console.log(this.inputMessage);
    await this.chatBotService.SendMessage(this.inputMessage);
    await this.listMessages();
  }
}
