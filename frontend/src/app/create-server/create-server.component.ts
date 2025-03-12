import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component, OnChanges, SimpleChanges } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ConfigService } from '../config.service';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-create-server',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, FormsModule],
  templateUrl: './create-server.component.html',
  styleUrl: './create-server.component.css',
})
export class CreateServerComponent implements OnChanges {
  public current_description: string = 'A minecraft server.';
  public current_adress: string = 'adress';
  public current_image: string =
    'https://i.pinimg.com/564x/4a/16/1d/4a161d4d6fa53f0cba2152411e2e2159.jpg';
  public game_version: string = '1.21.1';
  public server_version: string = 'Vanilla';
  public ram_min: string = '1024';
  public ram_max: string = '2048';

  createServer() {
    var url =
      this.config.buildUrl('create_server') +
      `?game_version=${this.game_version}&description=${this.current_description}&ram_max=${this.ram_max}&ram_min=${this.ram_min}&server_version=${this.server_version}`;

    this.http.get(url).subscribe((response: any) => {
      console.log(response.message);
    });
  }

  ngOnChanges(changes: SimpleChanges): void {
    console.log(changes);
  }

  constructor(private http: HttpClient, private config: ConfigService) {}
}
