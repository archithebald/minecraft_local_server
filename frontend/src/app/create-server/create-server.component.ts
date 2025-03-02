import { HttpClient, HttpClientModule } from '@angular/common/http';
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ConfigService } from '../config.service';

@Component({
  selector: 'app-create-server',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule],
  templateUrl: './create-server.component.html',
  styleUrl: './create-server.component.css'
})
export class CreateServerComponent {
  createServer(game_version: string, description: string, ram_max: string, ram_min: string, server_version: string) {
    var url = this.config.buildUrl("create_server") + `?game_version=${game_version}&description=${description}&ram_max=${ram_max}&ram_min=${ram_min}&server_version=${server_version}`

    this.http.get(url).subscribe((response: any) => {
      console.log(response.message);
    });
  }

  constructor(private http: HttpClient, private config: ConfigService) {}
}
