import { Component, OnInit } from '@angular/core';
import { MatIcon } from '@angular/material/icon';
import {
  Router,
  RouterLink,
  RouterLinkActive,
  RouterOutlet,
  Routes,
} from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { ConfigService } from '../config.service';
import { CommonModule, NgFor } from '@angular/common';

@Component({
  selector: 'app-servers-list',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, CommonModule, MatIcon, CommonModule, NgFor],
  templateUrl: './servers-list.component.html',
  styleUrl: './servers-list.component.css',
})
export class ServersListComponent implements OnInit {
  public servers: any[] = [];

  ngOnInit(): void {
    this.fetchAllServers();
  }

  deleteServer(id: string) {
    var div = document.getElementById(id) as HTMLDivElement;

    var url =
      this.config.getApiBaseUrl() +
      this.config.getEndpoint('delete') +
      `?id=${id}`;
    this.http.get(url).subscribe((response: any) => {
      div.style.display = 'none';
    });
  }

  fetchAllServers() {
    var url =
      this.config.getApiBaseUrl() + this.config.getEndpoint('get_all_servers');
    this.http.get(url).subscribe((response: any) => {
      this.servers = JSON.parse(response.data);
    });
  }

  redirectToServer(server_id: string) {
    this.router.navigate(['/server', server_id]);
  }

  redirectToCreate() {
    this.router.navigate(['/create']);
  }

  constructor(
    private http: HttpClient,
    private config: ConfigService,
    private router: Router
  ) {}
}
