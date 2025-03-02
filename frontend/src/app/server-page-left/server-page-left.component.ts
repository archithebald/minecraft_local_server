import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ConfigService } from '../config.service';
import { HttpClient, HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-server-page-left',
  standalone: true,
  imports: [CommonModule, HttpClientModule],
  templateUrl: './server-page-left.component.html',
  styleUrl: './server-page-left.component.css',
})
export class ServerPageLeftComponent implements OnInit {
  protected serverId: string | null = null;
  protected endpoint: string | null = null;
  private server: any = {};

  ngOnInit(): void {
    this.serverId = this.route.snapshot.paramMap.get('id');
    this.endpoint = `/server/${this.serverId}`;
    var url = this.config.buildUrl('get_server') + `?id=${this.serverId}`;
    this.http.get(url).subscribe((response: any) => {
      this.server = JSON.parse(response?.data ?? response);
      console.log('Fetched Server:', this.server);
    });
  }

  redirectToServer() {
    this.router.navigate([`/server/${this.serverId}`], {
      state: { server: this.server },
    });
  }

  redirectToOptions() {
    this.router.navigate([`/server/${this.serverId}/options`], {
      state: { server: this.server },
    });
  }

  redirectToConsole() {
    this.router.navigate([`/server/${this.serverId}/console`], {
      state: { server: this.server },
    });
  }

  redirectToFiles() {
    this.router.navigate([`/server/${this.serverId}/files`], {
      state: { server: this.server },
    });
  }

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private config: ConfigService,
    private http: HttpClient
  ) {}
}
